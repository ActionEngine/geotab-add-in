import { forwardRef, type HTMLAttributes, type ReactNode } from "react";
import { THRESHOLD_LABEL } from "@/utils/threshold";
import "./style.css";

interface MetricBarProps extends HTMLAttributes<HTMLDivElement> {
  label: string;
  percentage: number;
  status: THRESHOLD_LABEL;
  icon?: ReactNode;
}

const statusClassNameMap: Record<THRESHOLD_LABEL, string> = {
  [THRESHOLD_LABEL.PASS]: "metric-pass",
  [THRESHOLD_LABEL.WARNING]: "metric-warning",
  [THRESHOLD_LABEL.FALL]: "metric-error",
};

const MetricBar = forwardRef<HTMLDivElement, MetricBarProps>(
  ({ label, percentage, status, icon, className, ...rest }, ref) => {
    return (
      <div
        className={["metric-bar", className].filter(Boolean).join(" ")}
        ref={ref}
        {...rest}
      >
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
  },
);

MetricBar.displayName = "MetricBar";

export default MetricBar;
