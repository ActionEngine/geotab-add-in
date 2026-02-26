import { useEffect, useRef } from "react";
import MapLibre, { MapRef, Marker } from "react-map-gl/maplibre";
import "maplibre-gl/dist/maplibre-gl.css";
import { PADDING_PX } from "./constants";
import { getBbox } from "./helper";

interface GeotabMapChecksProps {
  points?: { latitude: number; longitude: number }[];
}

const GeotabMapChecks = ({ points = [] }: GeotabMapChecksProps) => {
  const mapRef = useRef<MapRef>(null);

  useEffect(() => {
    if (!points.length || !mapRef.current) return;

    const bbox = getBbox(points);
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
  }, [points]);

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
        {points.map(({ latitude, longitude }, idx) => {
          return (
            <Marker
              key={`${latitude}-${longitude}-${idx}`}
              longitude={longitude}
              latitude={latitude}
            >
              <div className="circle" />
            </Marker>
          );
        })}
      </MapLibre>
    </div>
  );
};

export default GeotabMapChecks;
