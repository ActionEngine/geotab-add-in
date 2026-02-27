import { useEffect, useMemo, useRef } from "react";
import MapLibre, { MapRef, Marker } from "react-map-gl/maplibre";
import { getHeaders } from "@/api/helper";
import "maplibre-gl/dist/maplibre-gl.css";
import { GeotabCredentials } from "mg-api-js";
import { PADDING_PX } from "./constants";
import { getBbox } from "./helper";

interface GeotabMapChecksProps {
  points?: { latitude: number; longitude: number; className?: string }[];
  showOvertureSegments?: boolean;
  showTeleportationMvtDots?: boolean;
  showIdleOutlierMvtDots?: boolean;
  showRoadCounterDots?: boolean;
  roadCounterDeviceId?: string;
  session?: GeotabCredentials | null;
}

const ROAD_COUNTER_SEGMENTS_SOURCE_ID = "segment-anomaly-source";
const ROAD_COUNTER_SEGMENTS_LAYER_ID = "segment-anomaly-layer";
const OVERTURE_SEGMENTS_SOURCE_ID = "overture-segments-source";
const OVERTURE_SEGMENTS_LAYER_ID = "overture-segments-layer";
const TELEPORTATION_SOURCE_ID = "teleportation-source";
const TELEPORTATION_DOTS_LAYER_ID = "teleportation-dots-layer";
const IDLE_OUTLIER_SOURCE_ID = "idle-outlier-source";
const IDLE_DOTS_LAYER_ID = "idle-dots-layer";

const GeotabMapChecks = ({
  points = [],
  showOvertureSegments = false,
  showTeleportationMvtDots = false,
  showIdleOutlierMvtDots = false,
  showRoadCounterDots = false,
  roadCounterDeviceId,
  session = null,
}: GeotabMapChecksProps) => {
  const mapRef = useRef<MapRef>(null);
  const segmentsTilesUrl = useMemo(() => {
    const baseUrl = import.meta.env.VITE_BASE_URL;
    return `${baseUrl}/tiles/segments?z={z}&x={x}&y={y}`;
  }, []);
  const teleportationTilesUrl = useMemo(() => {
    const baseUrl = import.meta.env.VITE_BASE_URL;
    return `${baseUrl}/tiles?z={z}&x={x}&y={y}`;
  }, []);
  const idleOutliersTilesUrl = useMemo(() => {
    const baseUrl = import.meta.env.VITE_BASE_URL;
    return `${baseUrl}/tiles?z={z}&x={x}&y={y}`;
  }, []);
  const roadCounterTilesUrl = useMemo(() => {
    const baseUrl = import.meta.env.VITE_BASE_URL;
    const query = roadCounterDeviceId
      ? `&device_id=${encodeURIComponent(roadCounterDeviceId)}`
      : "";
    return `${baseUrl}/tiles/segment-anomaly?z={z}&x={x}&y={y}${query}`;
  }, [roadCounterDeviceId]);

  const sessionHeaders = useMemo(() => {
    if (!session) return null;
    return getHeaders(session);
  }, [session]);

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

  useEffect(() => {
    const map = mapRef.current?.getMap();
    if (!map) return;

    const removeRoadCounterLayer = () => {
      if (map.getLayer(ROAD_COUNTER_SEGMENTS_LAYER_ID)) {
        map.removeLayer(ROAD_COUNTER_SEGMENTS_LAYER_ID);
      }
      if (map.getSource(ROAD_COUNTER_SEGMENTS_SOURCE_ID)) {
        map.removeSource(ROAD_COUNTER_SEGMENTS_SOURCE_ID);
      }
    };

    const removeOvertureLayer = () => {
      if (map.getLayer(OVERTURE_SEGMENTS_LAYER_ID)) {
        map.removeLayer(OVERTURE_SEGMENTS_LAYER_ID);
      }
      if (map.getSource(OVERTURE_SEGMENTS_SOURCE_ID)) {
        map.removeSource(OVERTURE_SEGMENTS_SOURCE_ID);
      }
    };

    const removeTeleportationLayer = () => {
      if (map.getLayer(TELEPORTATION_DOTS_LAYER_ID)) {
        map.removeLayer(TELEPORTATION_DOTS_LAYER_ID);
      }
      if (map.getSource(TELEPORTATION_SOURCE_ID)) {
        map.removeSource(TELEPORTATION_SOURCE_ID);
      }
    };

    const removeIdleOutlierLayer = () => {
      if (map.getLayer(IDLE_DOTS_LAYER_ID)) {
        map.removeLayer(IDLE_DOTS_LAYER_ID);
      }
      if (map.getSource(IDLE_OUTLIER_SOURCE_ID)) {
        map.removeSource(IDLE_OUTLIER_SOURCE_ID);
      }
    };

    const applyOvertureLayer = () => {
      if (!map.isStyleLoaded()) return;

      if (!showRoadCounterDots) {
        removeRoadCounterLayer();
      } else {
        if (!map.getSource(ROAD_COUNTER_SEGMENTS_SOURCE_ID)) {
          map.addSource(ROAD_COUNTER_SEGMENTS_SOURCE_ID, {
            type: "vector",
            tiles: [roadCounterTilesUrl],
          });
        }

        if (!map.getLayer(ROAD_COUNTER_SEGMENTS_LAYER_ID)) {
          map.addLayer({
            id: ROAD_COUNTER_SEGMENTS_LAYER_ID,
            type: "line",
            source: ROAD_COUNTER_SEGMENTS_SOURCE_ID,
            "source-layer": "segment_anomaly",
            paint: {
              "line-color": [
                "case",
                ["==", ["get", "is_error"], true],
                "#D92D20",
                ["==", ["get", "is_warning"], true],
                "#F79009",
                "#12B76A",
              ],
              "line-opacity": 0.45,
              "line-width": [
                "interpolate",
                ["linear"],
                ["zoom"],
                8,
                1,
                14,
                2.5,
              ],
            },
          });
        }
      }

      if (!showOvertureSegments) {
        removeOvertureLayer();
      } else {
        if (!map.getSource(OVERTURE_SEGMENTS_SOURCE_ID)) {
          map.addSource(OVERTURE_SEGMENTS_SOURCE_ID, {
            type: "vector",
            tiles: [segmentsTilesUrl],
          });
        }

        if (!map.getLayer(OVERTURE_SEGMENTS_LAYER_ID)) {
          map.addLayer({
            id: OVERTURE_SEGMENTS_LAYER_ID,
            type: "line",
            source: OVERTURE_SEGMENTS_SOURCE_ID,
            "source-layer": "overture_segments",
            paint: {
              "line-color": "#8e8e8e",
              "line-opacity": 0.45,
              "line-width": [
                "interpolate",
                ["linear"],
                ["zoom"],
                8,
                1,
                14,
                2.5,
              ],
            },
          });
        }
      }

      if (!showTeleportationMvtDots) {
        removeTeleportationLayer();
      } else {
        if (!map.getSource(TELEPORTATION_SOURCE_ID)) {
          map.addSource(TELEPORTATION_SOURCE_ID, {
            type: "vector",
            tiles: [teleportationTilesUrl],
          });
        }

        if (!map.getLayer(TELEPORTATION_DOTS_LAYER_ID)) {
          map.addLayer({
            id: TELEPORTATION_DOTS_LAYER_ID,
            type: "circle",
            source: TELEPORTATION_SOURCE_ID,
            "source-layer": "geotab_locations",
            paint: {
              "circle-color": "#AEAEAE",
              "circle-radius": [
                "interpolate",
                ["linear"],
                ["zoom"],
                8,
                2,
                14,
                4,
              ],
              "circle-opacity": 0.3,
              "circle-stroke-width": 0,
              "circle-stroke-color": "#ffffff",
            },
          });
        }
      }

      if (!showIdleOutlierMvtDots) {
        removeIdleOutlierLayer();
      } else {
        if (!map.getSource(IDLE_OUTLIER_SOURCE_ID)) {
          map.addSource(IDLE_OUTLIER_SOURCE_ID, {
            type: "vector",
            tiles: [idleOutliersTilesUrl],
          });
        }

        if (!map.getLayer(IDLE_DOTS_LAYER_ID)) {
          map.addLayer({
            id: IDLE_DOTS_LAYER_ID,
            type: "circle",
            source: IDLE_OUTLIER_SOURCE_ID,
            "source-layer": "geotab_locations",
            paint: {
              "circle-color": "#8e8e8e",
              "circle-radius": [
                "interpolate",
                ["linear"],
                ["zoom"],
                8,
                2,
                14,
                4,
              ],
              "circle-opacity": 0.3,
              "circle-stroke-width": 0,
              "circle-stroke-opacity": 0,
              "circle-stroke-color": "#ffffff",
            },
          });
        }
      }
    };

    applyOvertureLayer();
    map.on("styledata", applyOvertureLayer);

    return () => {
      map.off("styledata", applyOvertureLayer);
      removeRoadCounterLayer();
      removeOvertureLayer();
      removeTeleportationLayer();
      removeIdleOutlierLayer();
    };
  }, [
    idleOutliersTilesUrl,
    segmentsTilesUrl,
    roadCounterTilesUrl,
    teleportationTilesUrl,
    showRoadCounterDots,
    showIdleOutlierMvtDots,
    showOvertureSegments,
    showTeleportationMvtDots,
  ]);

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
        transformRequest={(url) => {
          if (!sessionHeaders) {
            return { url };
          }

          const baseUrl = import.meta.env.VITE_BASE_URL;
          if (!url.startsWith(baseUrl)) {
            return { url };
          }

          return {
            url,
            headers: sessionHeaders,
          };
        }}
      >
        {points.map(({ latitude, longitude, className }, idx) => {
          return (
            <Marker
              key={`${latitude}-${longitude}-${idx}`}
              longitude={longitude}
              latitude={latitude}
            >
              <div className={`circle ${className || ""}`} />
            </Marker>
          );
        })}
      </MapLibre>
    </div>
  );
};

export default GeotabMapChecks;
