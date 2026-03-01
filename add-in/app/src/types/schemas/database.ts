export enum DATABASE_STATUS {
  IN_PROGRESS = "IN_PROGRESS",
  DONE = "DONE",
}

export interface DatabaseResponse {
  database_name: string;
  email: string;
  ingestion_status: DATABASE_STATUS;
  last_sync: string;
  stats: {
    actual_last_sync: string;
    device_count: number;
    location_rows: number;
    status_data_rows: number;
  };
}
