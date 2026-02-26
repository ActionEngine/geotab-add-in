import { useMemo } from "react";
import { ValidationTeleportationResponse } from "@/types/shemas/validaton";
import { Table } from "@geotab/zenith/esm/table/table";
import moment from "moment";

interface TableTeleportationProps {
  points: ValidationTeleportationResponse[];
}

const TableTeleportation = ({ points }: TableTeleportationProps) => {
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
        title: "Speed",
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
          col3: `${point.implied_speed_kmh.toFixed(2)} km/h`,
        };
      }),
    [points],
  );

  return <Table columns={columns} entities={entities}></Table>;
};

export default TableTeleportation;
