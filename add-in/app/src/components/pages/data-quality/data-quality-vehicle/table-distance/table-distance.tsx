import { useMemo } from "react";
import { ValidationDistanceToRoadResponse } from "@/types/shemas/validaton";
import { Table } from "@geotab/zenith/esm/table/table";
import moment from "moment";

interface TableDistanceProps {
  points: ValidationDistanceToRoadResponse[];
}

const TableDistance = ({ points }: TableDistanceProps) => {
  const columns = useMemo(
    () => [
      {
        id: "col1",
        title: "Device ID",
        meta: {
          defaultWidth: 100,
        },
      },
      {
        id: "col2",
        title: "Time",
        meta: {
          defaultWidth: 200,
        },
      },
      {
        id: "col3",
        title: "Distance",
        meta: {
          defaultWidth: 200,
        },
      },
    ],
    [],
  );
  const entities = useMemo(
    () =>
      points.map((point, index) => {
        return {
          id: `${point.device_id}_${index}`,
          col1: point.device_id,
          col2: moment(point.datetime).format("MMM DD, YYYY HH:mm"),
          col3: `${point.distance.toFixed(2)} m`,
        };
      }),
    [points],
  );

  return <Table columns={columns} entities={entities}></Table>;
};

export default TableDistance;
