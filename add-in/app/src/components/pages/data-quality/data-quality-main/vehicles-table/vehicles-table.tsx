import { useMemo } from "react";
import {
  ValidationResponse,
  ValidationType,
  VehicleValidation,
} from "@/types/shemas/validaton";
import { getThresholdClassName } from "@/utils/threshold";
import { Table, IListColumn } from "@geotab/zenith";
import { Button } from "@geotab/zenith/esm/button/button";
import "./style.css";

interface VehiclesTableProps {
  vehicles: VehicleValidation[];
  validations: ValidationResponse[];
  onSelectVehicle: (id: string) => void;
}

interface GroupedVehicle {
  id: string;
  device_id: string;
  distance_to_road: number | null;
  teleportation: number | null;
  idle_outlier: number | null;
  road_counter_fuel_consumption: number | null;
  road_counter_coolant_temp: number | null;
  road_counter_ev_battery_discharge: number | null;
}

const VehiclesTable = ({
  vehicles,
  validations,
  onSelectVehicle,
}: VehiclesTableProps) => {
  const mappedVehicles = useMemo<GroupedVehicle[]>(() => {
    const grouped = new Map<string, GroupedVehicle>();

    const idToTypeMap = new Map<number, ValidationType>();
    validations.forEach((v) => idToTypeMap.set(v.id, v.validation_type));

    vehicles.forEach((vehicle) => {
      let row = grouped.get(vehicle.device_id);

      if (!row) {
        row = {
          id: vehicle.device_id,
          device_id: vehicle.device_id,
          distance_to_road: null,
          teleportation: null,
          idle_outlier: null,
          road_counter_fuel_consumption: null,
          road_counter_coolant_temp: null,
          road_counter_ev_battery_discharge: null,
        };
        grouped.set(vehicle.device_id, row);
      }

      const type = idToTypeMap.get(vehicle.validation_id);

      // Only set the value if it's not already populated — validationByDevice is sorted
      // by validation_id DESC (newest first), so the first occurrence is the latest run.
      // Without this guard, older runs (often 100%) would overwrite newer anomaly data.
      if (
        type === ValidationType.DISTANCE_TO_ROAD &&
        row.distance_to_road === null
      ) {
        row.distance_to_road = vehicle.percentage;
      } else if (
        type === ValidationType.TELEPORTATION &&
        row.teleportation === null
      ) {
        row.teleportation = vehicle.percentage;
      } else if (
        type === ValidationType.IDLE_OUTLIER &&
        row.idle_outlier === null
      ) {
        row.idle_outlier = vehicle.percentage;
      } else if (
        type === ValidationType.ROAD_COUNTER_FUEL_CONSUMPTION &&
        row.road_counter_fuel_consumption === null
      ) {
        row.road_counter_fuel_consumption = vehicle.percentage;
      } else if (
        type === ValidationType.ROAD_COUNTER_COOLANT_TEMP &&
        row.road_counter_coolant_temp === null
      ) {
        row.road_counter_coolant_temp = vehicle.percentage;
      } else if (
        type === ValidationType.ROAD_COUNTER_EV_BATTERY_DISCHARGE &&
        row.road_counter_ev_battery_discharge === null
      ) {
        row.road_counter_ev_battery_discharge = vehicle.percentage;
      }
    });

    return Array.from(grouped.values());
  }, [vehicles, validations]);

  const renderValidationValue = (value: number | null) => {
    if (value === null) {
      return <span className="no-data">No Data</span>;
    }

    return <span className={getThresholdClassName(value)}>{value}%</span>;
  };

  const columns = useMemo<IListColumn<GroupedVehicle>[]>(
    () => [
      {
        id: "device_id",
        title: "Vehicle ID",
        columnComponent: {
          render: (vehicle) => <span>{vehicle.device_id}</span>,
        },
      },
      {
        id: "distance_to_road",
        title: "Distance to Road",
        columnComponent: {
          render: (vehicle) => renderValidationValue(vehicle.distance_to_road),
        },
      },
      {
        id: "teleportation",
        title: "Teleportation",
        columnComponent: {
          render: (vehicle) => renderValidationValue(vehicle.teleportation),
        },
      },
      {
        id: "idle_outlier",
        title: "Idle outlier",
        columnComponent: {
          render: (vehicle) => renderValidationValue(vehicle.idle_outlier),
        },
      },
      {
        id: "road_counter_fuel_consumption",
        title: "Fuel Consumption",
        columnComponent: {
          render: (vehicle) =>
            renderValidationValue(vehicle.road_counter_fuel_consumption),
        },
      },
      {
        id: "road_counter_coolant_temp",
        title: "Coolant Temp",
        columnComponent: {
          render: (vehicle) =>
            renderValidationValue(vehicle.road_counter_coolant_temp),
        },
      },
      {
        id: "road_counter_ev_battery_discharge",
        title: "EV Battery Discharge",
        columnComponent: {
          render: (vehicle) =>
            renderValidationValue(vehicle.road_counter_ev_battery_discharge),
        },
      },
      {
        id: "actions",
        title: "Actions",
        columnComponent: {
          render: (vehicle) => (
            <Button
              type="secondary"
              onClick={() => onSelectVehicle(vehicle.device_id)}
            >
              View Details
            </Button>
          ),
        },
      },
    ],
    [onSelectVehicle],
  );

  return (
    <div className="table-container">
      <Table columns={columns} entities={mappedVehicles}>
        <Table.Empty description="No data yet" />
      </Table>
    </div>
  );
};

export default VehiclesTable;
