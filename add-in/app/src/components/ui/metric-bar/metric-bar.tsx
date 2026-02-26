import { THRESHOLD_LABEL } from "@/utils/threshold";
import "./style.css";

interface MetricBarProps {
  label: string;
  percentage: number;
  status: THRESHOLD_LABEL;
  icon?: React.ReactNode;
}

const statusClassNameMap: Record<THRESHOLD_LABEL, string> = {
  [THRESHOLD_LABEL.PASS]: "metric-pass",
  [THRESHOLD_LABEL.WARNING]: "metric-warning",
  [THRESHOLD_LABEL.FALL]: "metric-error",
};

const MetricBar = ({ label, percentage, status, icon }: MetricBarProps) => {
  return (
    <div className="metric-bar">
      <div
        className={`metric-bar-row ${statusClassNameMap[status]}`}
        style={{ transform: `scaleX(${percentage / 100})` }}
      />
      <div className="metric-bar-label">
        {icon && icon}
        {label}
      </div>
      <div className="metric-bar-percentage">{percentage}%</div>
    </div>
  );
};

export default MetricBar;
