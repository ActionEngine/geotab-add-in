import { useMemo } from "react";
import { VehicleValidation } from "@/types/shemas/validaton";
import { getThresholdClassName, THRESHOLD_LABEL } from "@/utils/threshold";
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
    <>
      <div className="vehicles-list-text">
        Top 5 Vehicles with Worst Battery Health
      </div>
      <div className="vehicles-list">
        {sortedVehicles.map((vehicle) => (
          <div className="vehicle-item" key={vehicle.device_id}>
            <span>{vehicle.device_id}</span>
            <span className={getThresholdClassName(vehicle.percentage)}>
              {vehicle.status}
            </span>
          </div>
        ))}
      </div>
    </>
  );
};

export default VehiclesList;
