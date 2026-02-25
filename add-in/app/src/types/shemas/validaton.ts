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
  device_id: string;
  total: number;
  warnings: number;
  errors: number;
}

export interface ValidationPercentage {
  type: ValidationType;
  percentage: number;
}
