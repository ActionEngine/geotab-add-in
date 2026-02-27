import { THRESHOLD_LABEL } from "@/utils/threshold";

export enum ValidationType {
  TELEPORTATION = "TELEPORTATION",
  DISTANCE_TO_ROAD = "DISTANCE_TO_ROAD",
  IDLE_OUTLIER = "IDLE_OUTLIER",
  ROAD_COUNTER_2H = "ROAD_COUNTER_2h",
}

export interface ValidationResponse {
  id: number;
  geotab_database_id: number;
  started_at: string;
  finished_at: string;
  validation_type: ValidationType;
  warnings: number;
  errors: number;
  total: number;
  status: string;
}

export interface ValidationDeviceResponse {
  validation_id: number;
  device_id: string;
  total: number;
  warnings: number;
  errors: number;
}

export interface ValidationPercentage {
  type: ValidationType;
  percentage: number;
}

export interface VehicleValidation extends ValidationDeviceResponse {
  status: THRESHOLD_LABEL;
  percentage: number;
}

interface ValidationCheckResponse {
  datetime: string;
  device_id: string;
  external_id: string;
  geotab_location_id: number;
  latitude: number;
  longitude: number;
  validation_id: number;
}
export interface ValidationTeleportationResponse extends ValidationCheckResponse {
  implied_speed_kmh: number;
}
export interface ValidationDistanceToRoadResponse extends ValidationCheckResponse {
  distance: number;
  speed: number;
}

export interface ValidationIdleOutlierResponse extends ValidationCheckResponse {
  is_outlier: boolean;
}

export interface ValidationSegmentAnomalyResponse {
  aggregate_deviation: number;
  current_values: number[];
  device_ids: string[];
  diagnostic_ids: string[];
  geotab_database_id: number;
  is_error: boolean;
  is_warning: boolean;
  reference_values: number[];
  segment_id: number;
  validation_id: number;
  value_deviations: number[];
}
