import { useMemo } from "react";
import MetricBar from "@/components/ui/metric-bar/metric-bar";
import { VehicleValidation } from "@/types/schemas/validation";
import { getThresholdLabel, THRESHOLD_LABEL } from "@/utils/threshold";
import "./style.css";

interface VehiclesListProps {
  vehicles: VehicleValidation[];
  sortBy?: "percentage" | "status";
}
const statusOrder: Record<THRESHOLD_LABEL, number> = {
  [THRESHOLD_LABEL.FALL]: 0,
  [THRESHOLD_LABEL.WARNING]: 1,
  [THRESHOLD_LABEL.PASS]: 2,
};

const VehiclesList = ({
  vehicles,
  sortBy = "percentage",
}: VehiclesListProps) => {
  const sortedVehicles = useMemo(() => {
    const filtered = vehicles.filter((vehicle) => vehicle.percentage !== 0);

    if (sortBy === "status") {
      return filtered
        .sort((a, b) => {
          const statusDiff = statusOrder[a.status] - statusOrder[b.status];
          if (statusDiff !== 0) return statusDiff;
          return a.percentage - b.percentage;
        })
        .slice(0, 5);
    }

    return filtered.sort((a, b) => a.percentage - b.percentage).slice(0, 5);
  }, [vehicles, sortBy]);

  return (
    <div className="vehicles-list-container">
      <div className="vehicles-list-label">
        Top 5 Vehicles with Worst Battery Health
      </div>
      <div className="vehicles-list">
        {sortedVehicles.map((vehicle) => (
          <MetricBar
            label={vehicle.device_id}
            percentage={vehicle.percentage}
            status={getThresholdLabel(vehicle.percentage)}
          />
        ))}
      </div>
    </div>
  );
};

export default VehiclesList;
