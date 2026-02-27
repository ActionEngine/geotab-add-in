import { useMemo } from "react";
import { ValidationSegmentAnomalyResponse } from "@/types/shemas/validaton";
import { IconArrowBottom, IconArrowTop } from "@geotab/zenith";
import { Table } from "@geotab/zenith/esm/table/table";
import "./style.css";

interface TableRoadCounterProps {
  points: ValidationSegmentAnomalyResponse[];
}

const getRoadConterStatus = ({
  is_error,
  is_warning,
  aggregate_deviation,
}: ValidationSegmentAnomalyResponse) => {
  const prefix =
    aggregate_deviation > 0 ? "+" : aggregate_deviation < 0 ? "-" : "";
  const icon =
    aggregate_deviation > 0 ? (
      <IconArrowTop />
    ) : aggregate_deviation < 0 ? (
      <IconArrowBottom />
    ) : null;

  return {
    className: is_error ? "fall" : is_warning ? "warning" : "pass",
    prefix,
    icon,
  };
};

const TableRoadCounter = ({ points }: TableRoadCounterProps) => {
  const columns = useMemo(
    () => [
      {
        id: "col1",
        title: "Segment",
        meta: {
          defaultWidth: 120,
        },
      },
      {
        id: "col2",
        title: "Id",
        meta: {
          defaultWidth: 120,
        },
      },
      {
        id: "col3",
        title: "Check Result",
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
        const { className, prefix, icon } = getRoadConterStatus(point);

        return {
          id: `${point.segment_id}_${index}`,
          col1: point.segment_id,
          col2: "",
          col3: (
            <div className={`check-result ${className}`}>
              {prefix}
              {(point.aggregate_deviation * 100).toFixed(2)}
              {icon}
            </div>
          ),
        };
      }),
    [points],
  );
  return <Table columns={columns} entities={entities} />;
};

export default TableRoadCounter;
