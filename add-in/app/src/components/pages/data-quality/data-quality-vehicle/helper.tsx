import {
  ValidationDistanceToRoadResponse,
  ValidationIdleOutlierResponse,
  ValidationSegmentAnomalyResponse,
  ValidationTeleportationResponse,
  ValidationType,
} from "@/types/shemas/validaton";
import TableDistance from "./table-distance/table-distance";
import TableIdleOutlier from "./table-idle-outlier/table-idle-outlier";
import TableRoadCounter from "./table-road-counter/table-road-counter";
import TableTeleportation from "./table-teleportation/table-teleportation";

export type Points =
  | ValidationTeleportationResponse[]
  | ValidationDistanceToRoadResponse[]
  | ValidationIdleOutlierResponse[]
  | ValidationSegmentAnomalyResponse[];

const getTeleportationMapClassName = (
  point: ValidationTeleportationResponse,
) => {
  if (point.implied_speed_kmh > 200) {
    return "fall";
  }

  if (point.implied_speed_kmh >= 100) {
    return "warning";
  }

  return "pass";
};

const getDistanceMapClassName = (point: ValidationDistanceToRoadResponse) => {
  if (point.distance > 10) {
    return "fall";
  }

  if (point.distance >= 5) {
    return "warning";
  }

  return "pass";
};

const getIdleOutlierMapClassName = (point: ValidationIdleOutlierResponse) => {
  return point.is_outlier ? "fall" : "pass";
};

export const getTableComponent = (
  selectCheck: string,
  points: Points,
  loading: boolean,
) => {
  if (selectCheck === ValidationType.TELEPORTATION) {
    return (
      <TableTeleportation
        points={points as ValidationTeleportationResponse[]}
        loading={loading}
      />
    );
  }
  if (selectCheck === ValidationType.DISTANCE_TO_ROAD) {
    return (
      <TableDistance
        points={points as ValidationDistanceToRoadResponse[]}
        loading={loading}
      />
    );
  }
  if (selectCheck === ValidationType.IDLE_OUTLIER) {
    return (
      <TableIdleOutlier
        points={points as ValidationIdleOutlierResponse[]}
        loading={loading}
      />
    );
  }
  if (selectCheck === ValidationType.ROAD_COUNTER_2H) {
    return (
      <TableRoadCounter
        points={points as ValidationSegmentAnomalyResponse[]}
        loading={loading}
      />
    );
  }
};
export const getPointsForMap = (selectCheck: string, points: Points) => {
  if (selectCheck === ValidationType.ROAD_COUNTER_2H) {
    return [];
  }

  if (selectCheck === ValidationType.TELEPORTATION && points.length > 0) {
    return (points as ValidationTeleportationResponse[]).map((point) => ({
      latitude: point.latitude,
      longitude: point.longitude,
      className: getTeleportationMapClassName(point),
    }));
  }

  if (selectCheck === ValidationType.DISTANCE_TO_ROAD && points.length > 0) {
    return (points as ValidationDistanceToRoadResponse[]).map((point) => ({
      latitude: point.latitude,
      longitude: point.longitude,
      className: getDistanceMapClassName(point),
    }));
  }

  if (selectCheck === ValidationType.IDLE_OUTLIER && points.length > 0) {
    return (points as ValidationIdleOutlierResponse[]).map((point) => ({
      latitude: point.latitude,
      longitude: point.longitude,
      className: getIdleOutlierMapClassName(point),
    }));
  }

  return [];
};
