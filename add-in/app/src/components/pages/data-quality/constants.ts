import { ValidationType } from "@/types/shemas/validaton";

export const validationTypeLabelMap: Record<ValidationType, string> = {
  [ValidationType.TELEPORTATION]: "Teleportation",
  [ValidationType.DISTANCE_TO_ROAD]: "Distance to road",
  [ValidationType.IDLE_OUTLIER]: "Idle outlier",
  [ValidationType.ROAD_COUNTER_FUEL_CONSUMPTION]: "Fuel Consumption",
  [ValidationType.ROAD_COUNTER_COOLANT_TEMP]: "Coolant Temp",
  [ValidationType.ROAD_COUNTER_EV_BATTERY_DISCHARGE]: "EV Battery Discharge",
};

export const validationTypeTooltipMap: Record<ValidationType, string> = {
  [ValidationType.TELEPORTATION]:
    "This check monitors for impossible or illogical jumps in geographical coordinates between consecutive data pings.",
  [ValidationType.DISTANCE_TO_ROAD]:
    "This metric evaluates the positioning accuracy of devices by analyzing the variance between the reported GPS coordinates and known road networks.",
  [ValidationType.IDLE_OUTLIER]:
    "This metric identifies vehicles that report excessive or unusual stationary durations.",
  [ValidationType.ROAD_COUNTER_FUEL_CONSUMPTION]: "Fuel Consumption",
  [ValidationType.ROAD_COUNTER_COOLANT_TEMP]: "Coolant Temp",
  [ValidationType.ROAD_COUNTER_EV_BATTERY_DISCHARGE]: "EV Battery Discharge",
};
