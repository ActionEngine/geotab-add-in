import { ValidationType } from "@/types/shemas/validaton";

export const validationTypeLabelMap: Record<ValidationType, string> = {
  [ValidationType.TELEPORTATION]: "Teleportation",
  [ValidationType.DISTANCE_TO_ROAD]: "Distance to road",
  [ValidationType.ROAD_COUNTER_2H]: "Road counter 2h",
};
