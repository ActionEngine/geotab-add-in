import {
  ValidationDeviceResponse,
  ValidationPercentage,
  ValidationResponse,
} from "@/types/shemas/validaton";
import {
  getThresholdLabel,
  THRESHOLD_CLASSNAME,
  THRESHOLD_LABEL,
} from "./threshold";

export const getAnomalyPercentage = (errors: number, total: number) => {
  if (total === 0 || errors === 0) return 0;
  return Number((100 - (errors / total) * 100).toFixed(0));
};

export const getValidationsPercentage = (
  validations: ValidationResponse[],
): ValidationPercentage[] => {
  return validations.map((v) => {
    return {
      type: v.validation_type,
      percentage: getAnomalyPercentage(v.errors, v.total),
    };
  });
};

const uniqById = <T extends { id: string | number }>(items: T[]) => {
  return Array.from(new Map(items.map((item) => [item.id, item])).values());
};

export const getVehicleWithWorstResult = (
  vehicles: ValidationDeviceResponse[],
) => {
  const vehiclesRaw = vehicles?.map((vd) => {
    return {
      id: vd.device_id,
      validation_id: vd.validation_id,
      label: getThresholdLabel(getAnomalyPercentage(vd.errors, vd.total)),
    };
  });

  const errorVehicles = vehiclesRaw?.filter(
    (v) => v.label === THRESHOLD_LABEL.FALL,
  );
  const warningVehicles = vehiclesRaw?.filter(
    (v) => v.label === THRESHOLD_LABEL.WARNING,
  );

  const uniqueErrorVehicles = uniqById(errorVehicles);
  const uniqueWarningVehicles = uniqById(warningVehicles);

  const value =
    uniqueErrorVehicles.length > 0
      ? uniqueErrorVehicles.length
      : uniqueWarningVehicles.length > 0
        ? uniqueWarningVehicles.length
        : 0;

  const className =
    uniqueErrorVehicles.length > 0
      ? THRESHOLD_CLASSNAME.FALL
      : uniqueWarningVehicles.length > 0
        ? THRESHOLD_CLASSNAME.WARNING
        : THRESHOLD_CLASSNAME.PASS;

  return {
    value,
    className,
  };
};
