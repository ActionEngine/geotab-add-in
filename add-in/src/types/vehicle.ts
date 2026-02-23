export interface VehicleStatusInfo {
  bearing: number;
  currentStateDuration: string;
  dateTime: string;
  device: { id: string };
  driver: string;
  exceptionEvents: any[];
  groups: { id?: string; name?: string }[];
  isDeviceCommunicating: boolean;
  isDriving: boolean;
  isHistoricLastDriver: boolean;
  latitude: number;
  longitude: number;
  speed: number;
}
