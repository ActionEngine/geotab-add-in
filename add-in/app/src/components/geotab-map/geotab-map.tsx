import { useContext, useEffect, useRef, useState } from "react";
import MapLibre, {
  MapRef,
  Marker,
  ViewStateChangeEvent,
} from "react-map-gl/maplibre";
import { useFetch } from "@/hooks/useFetch";
import VehicleIcon from "@/image/vehicle-icon";
import { AppContext } from "@/provider/app-provider";
import { VehicleStatusInfo } from "@/types/schemas/geotab";
import { VehicleValidation } from "@/types/schemas/validation";
import { callAsync } from "@/utils/geotabApi";
import { getThresholdClassName } from "@/utils/threshold";
import "maplibre-gl/dist/maplibre-gl.css";
import { getBbox, zoomToBBox } from "./helper";

const getVehicleId = (vehicle: VehicleStatusInfo) => vehicle.device.id;

const lerp = (from: number, to: number, t: number) => from + (to - from) * t;

const lerpAngle = (from: number, to: number, t: number) => {
  const diff = ((to - from + 540) % 360) - 180;
  return from + diff * t;
};

interface GeotabMapProps {
  api: GeotabApi;
  vehicles?: VehicleValidation[];
  isAuthPage?: boolean;
}

const GeotabMap = ({
  api,
  vehicles = [],
  isAuthPage = false,
}: GeotabMapProps) => {
  const mapRef = useRef<MapRef>(null);
  const { globalBbox, updateGlobalBbox, mapStateMain, updateMapStateMain } =
    useContext(AppContext);
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
    if (globalBbox && mapRef.current) {
      zoomToBBox(mapRef.current, globalBbox);
    }
  }, []);

  useEffect(() => {
    if (globalBbox) return;

    const incoming = data.data ?? [];
    if (!incoming.length || !mapRef.current) return;

    const bbox = getBbox(
      incoming.map((vehicle) => ({
        latitude: vehicle.latitude,
        longitude: vehicle.longitude,
      })),
    );
    if (!bbox) return;
    zoomToBBox(mapRef.current, bbox);
    updateGlobalBbox(bbox);
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

  const handleLoadMap = () => {
    if (isAuthPage) return;
    if (mapRef.current && globalBbox) {
      zoomToBBox(mapRef.current, globalBbox);
    }
  };

  const handleMapMove = (e: ViewStateChangeEvent) => {
    if (isAuthPage) return;
    updateMapStateMain(e.viewState);
  };

  return (
    <div style={{ width: "100%", height: "100%" }}>
      <MapLibre
        ref={mapRef}
        initialViewState={
          mapStateMain
            ? { ...mapStateMain }
            : {
                latitude: 30,
                longitude: 0,
                zoom: 1.5,
              }
        }
        onLoad={handleLoadMap}
        onMove={handleMapMove}
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
