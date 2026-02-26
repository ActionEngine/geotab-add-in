import MetricBar from "@/components/ui/metric-bar/metric-bar";
import { ValidationType } from "@/types/shemas/validaton";
import { getThresholdLabel } from "@/utils/threshold";
import { validationTypeLabelMap } from "../../constants";
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
        <MetricBar
          key={idx}
          label={validationTypeLabelMap[v.type]}
          percentage={v.percentage}
          status={getThresholdLabel(v.percentage)}
        />
      ))}
    </div>
  );
};

export default ChecksList;
