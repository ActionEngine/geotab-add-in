import {
  ValidationDeviceResponse,
  ValidationPercentage,
  ValidationResponse,
  VehicleValidation,
} from "@/types/shemas/validaton";
import {
  getThresholdLabel,
  THRESHOLD_CLASSNAME,
  THRESHOLD_LABEL,
} from "./threshold";

export const getAnomalyPercentage = (
  warnings: number,
  errors: number,
  total: number,
) => {
  const anomalies = warnings + errors;
  if (anomalies === 0) return 100;
  return Number((100 - (anomalies / total) * 100)?.toFixed(0));
};

export const getValidationsPercentage = (
  validations: ValidationResponse[],
): ValidationPercentage[] => {
  return validations.map((v) => {
    return {
      type: v.validation_type,
      percentage: getAnomalyPercentage(v.warnings, v.errors, v.total),
    };
  });
};

export const makeVehiclesByStatus = (
  vehicles: ValidationDeviceResponse[],
): VehicleValidation[] => {
  return vehicles.map((vd) => {
    const percentage = getAnomalyPercentage(vd.warnings, vd.errors, vd.total);
    return {
      ...vd,
      status: getThresholdLabel(percentage),
      percentage,
    };
  });
};

const uniqById = <T extends { device_id: string | number }>(items: T[]) => {
  return Array.from(
    new Map(items.map((item) => [item.device_id, item])).values(),
  );
};

export const getVehicleWithWorstResult = (
  vehicles: ValidationDeviceResponse[],
) => {
  const vehiclesRaw = makeVehiclesByStatus(vehicles);

  const errorVehicles = vehiclesRaw?.filter(
    (v) => v.status === THRESHOLD_LABEL.FALL,
  );
  const warningVehicles = vehiclesRaw?.filter(
    (v) => v.status === THRESHOLD_LABEL.WARNING,
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
