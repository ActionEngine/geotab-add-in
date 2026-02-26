import { useEffect, useRef } from "react";
import MapLibre, { MapRef, Marker } from "react-map-gl/maplibre";
import "maplibre-gl/dist/maplibre-gl.css";

const PADDING_PX = 80;
const BBOX_PADDING_FACTOR = 0.1;
const MIN_BBOX_PADDING_DEGREES = 0.002;

const getPointsBbox = (points: { latitude: number; longitude: number }[]) => {
  if (!points.length) return null;

  let xmin = points[0].longitude;
  let xmax = points[0].longitude;
  let ymin = points[0].latitude;
  let ymax = points[0].latitude;

  for (const point of points) {
    if (point.longitude < xmin) xmin = point.longitude;
    if (point.longitude > xmax) xmax = point.longitude;
    if (point.latitude < ymin) ymin = point.latitude;
    if (point.latitude > ymax) ymax = point.latitude;
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

interface GeotabMapChecksProps {
  points?: { latitude: number; longitude: number }[];
}

const GeotabMapChecks = ({ points = [] }: GeotabMapChecksProps) => {
  const mapRef = useRef<MapRef>(null);

  useEffect(() => {
    if (!points.length || !mapRef.current) return;

    const bbox = getPointsBbox(points);
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
