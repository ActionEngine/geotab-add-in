import { useEffect, useRef, useState } from "react";
import MapLibre, { MapRef, Marker } from "react-map-gl/maplibre";
import { useFetch } from "@/hooks/useFetch";
import VehicleIcon from "@/image/vehicle-icon";
import { VehicleStatusInfo } from "@/types/shemas/geotab";
import { callAsync } from "@/utils/geotabApi";
import "maplibre-gl/dist/maplibre-gl.css";

interface GeotabMapProps {
  api: GeotabApi;
}

const getVehicleId = (vehicle: VehicleStatusInfo) => vehicle.device.id;

const lerp = (from: number, to: number, t: number) => from + (to - from) * t;

const lerpAngle = (from: number, to: number, t: number) => {
  const diff = ((to - from + 540) % 360) - 180;
  return from + diff * t;
};

const GeotabMap = ({ api }: GeotabMapProps) => {
  const mapRef = useRef<MapRef>(null);
  const [animatedVehicles, setAnimatedVehicles] = useState<VehicleStatusInfo[]>(
    [],
  );
  const targetByIdRef = useRef<globalThis.Map<string, VehicleStatusInfo>>(
    new globalThis.Map(),
  );
  const lastFrameTimeRef = useRef<number | null>(null);

  const data = useFetch<VehicleStatusInfo[]>({
    fn: () => callAsync(api, "Get", { typeName: "DeviceStatusInfo" }),
    key: "all-vehicle-status-info",
    refetchInterval: 2 * 1000,
  });

  useEffect(() => {
    const incoming = data.data ?? [];

    targetByIdRef.current = new globalThis.Map(
      incoming.map((vehicle) => [getVehicleId(vehicle), vehicle]),
    );

    setAnimatedVehicles((prev) => {
      if (prev.length === 0) return incoming;

      const prevById = new globalThis.Map(
        prev.map((vehicle) => [getVehicleId(vehicle), vehicle]),
      );

      return incoming.map((vehicle) => {
        const previous = prevById.get(getVehicleId(vehicle));
        if (!previous) return vehicle;

        return {
          ...vehicle,
          latitude: previous.latitude,
          longitude: previous.longitude,
          bearing: previous.bearing,
        };
      });
    });
  }, [data.data]);

  useEffect(() => {
    let animationFrameId = 0;

    const tick = (timestamp: number) => {
      if (lastFrameTimeRef.current === null) {
        lastFrameTimeRef.current = timestamp;
      }

      const delta = timestamp - lastFrameTimeRef.current;
      lastFrameTimeRef.current = timestamp;

      const t = Math.min(1, 1 - Math.exp(-delta / 700));

      setAnimatedVehicles((prev) =>
        prev.map((vehicle) => {
          const target = targetByIdRef.current.get(getVehicleId(vehicle));
          if (!target) return vehicle;

          return {
            ...vehicle,
            latitude: lerp(vehicle.latitude, target.latitude, t),
            longitude: lerp(vehicle.longitude, target.longitude, t),
            bearing: lerpAngle(vehicle.bearing, target.bearing, t),
          };
        }),
      );

      animationFrameId = requestAnimationFrame(tick);
    };

    animationFrameId = requestAnimationFrame(tick);

    return () => {
      cancelAnimationFrame(animationFrameId);
      lastFrameTimeRef.current = null;
    };
  }, []);

  return (
    <MapLibre
      ref={mapRef}
      initialViewState={{
        latitude: 43.740825,
        longitude: -79.377625,
        zoom: 11,
      }}
      {...{
        aroundCenter: false,
      }} /* Not documented feature for better interaction experience */
      mapStyle="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
    >
      {animatedVehicles.map((vehicle, idx) => (
        <Marker
          key={vehicle.device.id || idx}
          longitude={vehicle.longitude}
          latitude={vehicle.latitude}
          rotation={vehicle.bearing}
        >
          <VehicleIcon />
        </Marker>
      ))}
    </MapLibre>
  );
};

export default GeotabMap;
