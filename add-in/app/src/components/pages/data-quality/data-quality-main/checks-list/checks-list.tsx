import MetricBar from "@/components/ui/metric-bar/metric-bar";
import { ValidationType } from "@/types/shemas/validaton";
import { getThresholdLabel } from "@/utils/threshold";
import { Tooltip } from "@geotab/zenith/esm/tooltip/tooltip";
import {
  validationTypeLabelMap,
  validationTypeTooltipMap,
} from "../../constants";
import "./style.css";

interface ChecksListProps {
  validationsPercentage: {
    type: ValidationType;
    percentage: number;
  }[];
}

const ChecksList = ({ validationsPercentage }: ChecksListProps) => {
  return (
    <div className="checks">
      {validationsPercentage.map((v, idx) => (
        <Tooltip
          key={idx}
          alignment="top"
          trigger={
            <MetricBar
              label={validationTypeLabelMap[v.type]}
              percentage={v.percentage}
              status={getThresholdLabel(v.percentage)}
            />
          }
        >
          {validationTypeTooltipMap[v.type]}
        </Tooltip>
      ))}
    </div>
  );
};

export default ChecksList;
