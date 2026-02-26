import { THRESHOLD_LABEL } from "@/utils/threshold";

export enum ValidationType {
  TELEPORTATION = "TELEPORTATION",
  DISTANCE_TO_ROAD = "DISTANCE_TO_ROAD",
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
  device_id: number;
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
