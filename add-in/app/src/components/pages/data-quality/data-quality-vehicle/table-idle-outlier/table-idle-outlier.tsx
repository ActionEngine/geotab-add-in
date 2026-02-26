import { useMemo } from "react";
import { ValidationIdleOutlierResponse } from "@/types/shemas/validaton";
import { Table } from "@geotab/zenith/esm/table/table";
import moment from "moment";

interface TableIdleOutlierProps {
  points: ValidationIdleOutlierResponse[];
}

const TableIdleOutlier = ({ points }: TableIdleOutlierProps) => {
  const columns = useMemo(
    () => [
      {
        id: "col1",
        title: "Device ID",
        meta: {
          defaultWidth: 120,
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
        title: "Type",
        meta: {
          defaultWidth: 140,
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
          col3: point.is_outlier ? "Outlier" : "Normal",
        };
      }),
    [points],
  );

  return <Table columns={columns} entities={entities}></Table>;
};

export default TableIdleOutlier;
