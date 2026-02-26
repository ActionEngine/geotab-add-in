export enum THRESHOLD_CLASSNAME {
  PASS = "pass",
  WARNING = "warning",
  FALL = "fall",
}

export enum THRESHOLD_LABEL {
  PASS = "Pass",
  WARNING = "Warning",
  FALL = "Fall",
}

export const getThresholdClassName = (value: number) => {
  if (value < 60) return THRESHOLD_CLASSNAME.FALL;
  if (value <= 90) return THRESHOLD_CLASSNAME.WARNING;
  return THRESHOLD_CLASSNAME.PASS;
};

export const getThresholdLabel = (value: number) => {
  if (value < 60) return THRESHOLD_LABEL.FALL;
  if (value <= 90) return THRESHOLD_LABEL.WARNING;
  return THRESHOLD_LABEL.PASS;
};
