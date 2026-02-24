import { useRef, useMemo } from "react";
import Map, { MapRef, Marker } from "react-map-gl/maplibre";
import { useFetch } from "@/hooks/useFetch";
import VehicleIcon from "@/image/vehicle-icon";
import { VehicleStatusInfo } from "@/types/shemas/geotab";
import { callAsync } from "@/utils/geotabApi";
import "maplibre-gl/dist/maplibre-gl.css";

interface GeotabMapProps {
  api: GeotabApi;
}

const GeotabMap = ({ api }: GeotabMapProps) => {
  const mapRef = useRef<MapRef>(null);

  const data = useFetch<VehicleStatusInfo[]>({
    fn: () => callAsync(api, "Get", { typeName: "DeviceStatusInfo" }),
    key: "all-vehicle-status-info",
    refetchInterval: 5 * 1000,
  });

  const vehicles = useMemo(() => data?.data ?? [], [data]);

  return (
    <Map
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
      {vehicles.map((vehicle, idx) => (
        <Marker
          key={`${vehicle.longitude}_${vehicle.latitude}_${idx}`}
          longitude={vehicle.longitude}
          latitude={vehicle.latitude}
          rotation={vehicle.bearing}
        >
          <VehicleIcon />
        </Marker>
      ))}
    </Map>
  );
};

export default GeotabMap;
