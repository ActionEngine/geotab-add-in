import { useEffect, useRef, useState } from "react";
import MapLibre, { MapRef, Marker } from "react-map-gl/maplibre";
import { useFetch } from "@/hooks/useFetch";
import VehicleIcon from "@/image/vehicle-icon";
import { VehicleStatusInfo } from "@/types/shemas/geotab";
import { VehicleValidation } from "@/types/shemas/validaton";
import { callAsync } from "@/utils/geotabApi";
import { getThresholdClassName } from "@/utils/threshold";
import "maplibre-gl/dist/maplibre-gl.css";

const PADDING_PX = 80;
const BBOX_PADDING_FACTOR = 0.1;
const MIN_BBOX_PADDING_DEGREES = 0.002;

const getVehicleId = (vehicle: VehicleStatusInfo) => vehicle.device.id;

const lerp = (from: number, to: number, t: number) => from + (to - from) * t;

const lerpAngle = (from: number, to: number, t: number) => {
  const diff = ((to - from + 540) % 360) - 180;
  return from + diff * t;
};

const getVehiclesBbox = (vehicles: VehicleStatusInfo[]) => {
  if (!vehicles.length) return null;

  let xmin = vehicles[0].longitude;
  let xmax = vehicles[0].longitude;
  let ymin = vehicles[0].latitude;
  let ymax = vehicles[0].latitude;

  for (const vehicle of vehicles) {
    if (vehicle.longitude < xmin) xmin = vehicle.longitude;
    if (vehicle.longitude > xmax) xmax = vehicle.longitude;
    if (vehicle.latitude < ymin) ymin = vehicle.latitude;
    if (vehicle.latitude > ymax) ymax = vehicle.latitude;
  }

  const width = xmax - xmin;
  const height = ymax - ymin;
  const xPadding = Math.max(
    width * BBOX_PADDING_FACTOR,
    MIN_BBOX_PADDING_DEGREES,
  );
  const yPadding = Math.max(
    height * BBOX_PADDING_FACTOR,
    MIN_BBOX_PADDING_DEGREES,
  );

  return [
    xmin - xPadding,
    ymin - yPadding,
    xmax + xPadding,
    ymax + yPadding,
  ] as const;
};

interface GeotabMapProps {
  api: GeotabApi;
  vehicles?: VehicleValidation[];
}

const GeotabMap = ({ api, vehicles = [] }: GeotabMapProps) => {
  const mapRef = useRef<MapRef>(null);
  const [animatedVehicles, setAnimatedVehicles] = useState<VehicleStatusInfo[]>(
    [],
  );
  const targetByIdRef = useRef<globalThis.Map<string, VehicleStatusInfo>>(
    new globalThis.Map(),
  );
  const lastFrameTimeRef = useRef<number | null>(null);
  const hasZoomedRef = useRef(false);

  useEffect(() => {
    hasZoomedRef.current = false;
  }, [api]);

  const data = useFetch<VehicleStatusInfo[]>({
    fn: () => callAsync(api, "Get", { typeName: "DeviceStatusInfo" }),
    key: "all-vehicle-status-info",
    refetchInterval: 2 * 1000,
  });

  useEffect(() => {
    const incoming = data.data ?? [];
    if (!incoming.length || hasZoomedRef.current || !mapRef.current) return;

    const bbox = getVehiclesBbox(incoming);
    if (!bbox) return;

    const [xmin, ymin, xmax, ymax] = bbox;
    mapRef.current.fitBounds(
      [
        [xmin, ymin],
        [xmax, ymax],
      ],
      {
        padding: PADDING_PX,
        duration: 2000,
      },
    );

    hasZoomedRef.current = true;
  }, [data.data]);

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
    <div style={{ width: "100%", height: "100vh" }}>
      <MapLibre
        ref={mapRef}
        initialViewState={{
          latitude: 30,
          longitude: 0,
          zoom: 1.5,
        }}
        {...{
          aroundCenter: false,
        }} /* Not documented feature for better interaction experience */
        mapStyle="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json"
      >
        {animatedVehicles.map((vehicle, idx) => {
          const find = vehicles.find((v) => v.device_id === vehicle.device.id);
          const className = getThresholdClassName(find?.percentage ?? 0);
          return (
            <Marker
              key={vehicle.device.id || idx}
              longitude={vehicle.longitude}
              latitude={vehicle.latitude}
              rotation={vehicle.bearing}
            >
              <VehicleIcon className={className} />
            </Marker>
          );
        })}
      </MapLibre>
    </div>
  );
};

export default GeotabMap;
