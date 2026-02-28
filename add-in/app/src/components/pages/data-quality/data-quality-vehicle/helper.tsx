import {
  ValidationDistanceToRoadResponse,
  ValidationIdleOutlierResponse,
  ValidationSegmentAnomalyResponse,
  ValidationTeleportationResponse,
  ValidationType,
} from "@/types/shemas/validaton";
import {
  TELEPORTATION_ERROR_THRESHOLD_KMH,
  TELEPORTATION_WARNING_THRESHOLD_KMH,
  DISTANCE_ERROR_THRESHOLD_METERS,
  DISTANCE_WARNING_THRESHOLD_METERS,
} from "@/utils/validation-thresholds";
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
  if (point.implied_speed_kmh > TELEPORTATION_ERROR_THRESHOLD_KMH) {
    return "fall";
  }

  if (point.implied_speed_kmh >= TELEPORTATION_WARNING_THRESHOLD_KMH) {
    return "warning";
  }

  return "pass";
};

const getDistanceMapClassName = (point: ValidationDistanceToRoadResponse) => {
  if (point.distance > DISTANCE_ERROR_THRESHOLD_METERS) {
    return "fall";
  }

  if (point.distance >= DISTANCE_WARNING_THRESHOLD_METERS) {
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
  if (
    selectCheck === ValidationType.ROAD_COUNTER_FUEL_CONSUMPTION ||
    selectCheck === ValidationType.ROAD_COUNTER_COOLANT_TEMP ||
    selectCheck === ValidationType.ROAD_COUNTER_EV_BATTERY_DISCHARGE
  ) {
    return (
      <TableRoadCounter
        points={points as ValidationSegmentAnomalyResponse[]}
        loading={loading}
      />
    );
  }
};
export const getPointsForMap = (selectCheck: string, points: Points) => {
  if (
    selectCheck === ValidationType.ROAD_COUNTER_FUEL_CONSUMPTION ||
    selectCheck === ValidationType.ROAD_COUNTER_COOLANT_TEMP ||
    selectCheck === ValidationType.ROAD_COUNTER_EV_BATTERY_DISCHARGE
  ) {
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
