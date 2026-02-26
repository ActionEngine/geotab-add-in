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
        const type = point.is_outlier
          ? { label: "Outlier", className: "fall" }
          : { label: "Normal", className: "pass" };

        return {
          id: `${point.geotab_location_id}_${index}`,
          col1: point.longitude.toFixed(6),
          col2: point.latitude.toFixed(6),
          col3: moment(point.datetime).format("MMM DD, YYYY HH:mm"),
          col4: <span className={type.className}>{type.label}</span>,
        };
      }),
    [points],
  );

  return <Table columns={columns} entities={entities}></Table>;
};

export default TableIdleOutlier;
