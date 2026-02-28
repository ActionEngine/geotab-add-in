import { useMemo } from "react";
import { ValidationTeleportationResponse } from "@/types/shemas/validaton";
import {
  TELEPORTATION_ERROR_THRESHOLD_KMH,
  TELEPORTATION_WARNING_THRESHOLD_KMH,
} from "@/utils/validation-thresholds";
import { Table } from "@geotab/zenith/esm/table/table";
import moment from "moment";

interface TableTeleportationProps {
  points: ValidationTeleportationResponse[];
  loading: boolean;
}

const getSpeedStatus = (speed: number) => {
  if (speed > TELEPORTATION_ERROR_THRESHOLD_KMH) {
    return { label: "Error", className: "fall" };
  }

  if (speed >= TELEPORTATION_WARNING_THRESHOLD_KMH) {
    return { label: "Warning", className: "warning" };
  }

  return { label: "OK", className: "pass" };
};

const TableTeleportation = ({ points, loading }: TableTeleportationProps) => {
  const columns = useMemo(
    () => [
      {
        id: "col1",
        title: "Lon",
      },
      {
        id: "col2",
        title: "Lat",
      },
      {
        id: "col3",
        title: "Time",
      },
      {
        id: "col4",
        title: "Speed",
      },
      {
        id: "col5",
        title: "Status",
      },
    ],
    [],
  );
  const entities = useMemo(
    () =>
      points.map((point, index) => {
        const status = getSpeedStatus(point.implied_speed_kmh);

        return {
          id: `${point.geotab_location_id}_${index}`,
          col1: point.longitude?.toFixed(6),
          col2: point.latitude?.toFixed(6),
          col3: moment(point.datetime).format("MMM DD, YYYY HH:mm"),
          col4: `${point.implied_speed_kmh?.toFixed(2)} km/h`,
          col5: <span className={status.className}>{status.label}</span>,
        };
      }),
    [points],
  );

  return (
    <Table columns={columns} entities={entities} isLoading={loading}>
      <Table.Empty description="No data yet" />
    </Table>
  );
};

export default TableTeleportation;
