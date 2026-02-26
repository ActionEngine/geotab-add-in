import { BBOX_PADDING_FACTOR, MIN_BBOX_PADDING_DEGREES } from "./constants";

interface Points {
  latitude: number;
  longitude: number;
}

export const getBbox = (
  points: Points[],
): readonly [number, number, number, number] | null => {
  if (!points.length) return null;

  let xmin = points[0].longitude;
  let xmax = points[0].longitude;
  let ymin = points[0].latitude;
  let ymax = points[0].latitude;

  for (const point of points) {
    if (point.longitude < xmin) xmin = point.longitude;
    if (point.longitude > xmax) xmax = point.longitude;
    if (point.latitude < ymin) ymin = point.latitude;
    if (point.latitude > ymax) ymax = point.latitude;
  }

  const width = xmax - xmin;
  const height = ymax - ymin;
  const xPadding = Math.max(
    width * BBOX_PADDING_FACTOR,
    MIN_BBOX_PADDING_DEGREES,
  );
  const yPadding = Math.max(
    height * BBOX_PADDING_FACTOR,
    MIN_BBOX_PADDING_DEGREES,
  );

  return [
    xmin - xPadding,
    ymin - yPadding,
    xmax + xPadding,
    ymax + yPadding,
  ] as const;
};
