import { VehicleStatusInfo } from "@/types/vehicle";
import { apiGet } from "./api";

export const getAllVehicleStatusInfo = async () => {
  return await apiGet<VehicleStatusInfo[]>("DeviceStatusInfo");
};
