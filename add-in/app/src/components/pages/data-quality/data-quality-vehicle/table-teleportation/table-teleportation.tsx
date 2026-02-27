import { useMemo } from "react";
import { ValidationTeleportationResponse } from "@/types/shemas/validaton";
import { Table } from "@geotab/zenith/esm/table/table";
import moment from "moment";

interface TableTeleportationProps {
  points: ValidationTeleportationResponse[];
}

const getSpeedStatus = (speed: number) => {
  if (speed > 200) {
    return { label: "Error", className: "fall" };
  }

  if (speed >= 100) {
    return { label: "Warning", className: "warning" };
  }

  return { label: "OK", className: "pass" };
};

const TableTeleportation = ({ points }: TableTeleportationProps) => {
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
    <Table columns={columns} entities={entities}>
      <Table.Empty description="No data yet" />
    </Table>
  );
};

export default TableTeleportation;
