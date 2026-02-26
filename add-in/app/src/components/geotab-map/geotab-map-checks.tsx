import { useRef } from "react";
import MapLibre, { MapRef } from "react-map-gl/maplibre";
import "maplibre-gl/dist/maplibre-gl.css";

const GeotabMapChecks = () => {
  const mapRef = useRef<MapRef>(null);

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
      ></MapLibre>
    </div>
  );
};

export default GeotabMapChecks;
