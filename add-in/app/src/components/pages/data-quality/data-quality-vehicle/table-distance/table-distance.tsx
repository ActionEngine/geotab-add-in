import { useMemo } from "react";
import { ValidationDistanceToRoadResponse } from "@/types/shemas/validaton";
import { Table } from "@geotab/zenith/esm/table/table";
import moment from "moment";

interface TableDistanceProps {
  points: ValidationDistanceToRoadResponse[];
}

const getDistanceStatus = (distance: number) => {
  if (distance > 10) {
    return { label: "Error", className: "fall" };
  }

  if (distance >= 5) {
    return { label: "Warning", className: "warning" };
  }

  return { label: "OK", className: "pass" };
};

const TableDistance = ({ points }: TableDistanceProps) => {
  const columns = useMemo(
    () => [
      {
        id: "col1",
        title: "Lon",
        meta: {
          defaultWidth: 120,
        },
      },
      {
        id: "col2",
        title: "Lat",
        meta: {
          defaultWidth: 120,
        },
      },
      {
        id: "col3",
        title: "Time",
        meta: {
          defaultWidth: 200,
        },
      },
      {
        id: "col4",
        title: "Distance",
        meta: {
          defaultWidth: 120,
        },
      },
      {
        id: "col5",
        title: "Status",
        meta: {
          defaultWidth: 120,
        },
      },
    ],
    [],
  );
  const entities = useMemo(
    () =>
      points.map((point, index) => {
        const status = getDistanceStatus(point.distance);

        return {
          id: `${point.geotab_location_id}_${index}`,
          col1: point.longitude.toFixed(6),
          col2: point.latitude.toFixed(6),
          col3: moment(point.datetime).format("MMM DD, YYYY HH:mm"),
          col4: `${point.distance.toFixed(2)} m`,
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

export default TableDistance;
