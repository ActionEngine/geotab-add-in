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
  distance_to_road: number;
  teleportation: number;
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
          distance_to_road: 0,
          teleportation: 0,
        };
        grouped.set(vehicle.device_id, row);
      }

      const type = idToTypeMap.get(vehicle.validation_id);

      if (type === ValidationType.DISTANCE_TO_ROAD) {
        row.distance_to_road = vehicle.percentage;
      } else if (type === ValidationType.TELEPORTATION) {
        row.teleportation = vehicle.percentage;
      }
    });

    return Array.from(grouped.values());
  }, [vehicles, validations]);

  const columns = useMemo<IListColumn<GroupedVehicle>[]>(
    () => [
      {
        id: "device_id",
        title: "Vehicle ID",
        columnComponent: {
          render: (vehicle) => (
            <span>{vehicle.device_id}</span>
          ),
        },
      },
      {
        id: "distance_to_road",
        title: "Distance to Road",
        columnComponent: {
          render: (vehicle) => (
            <span
              className={`${getThresholdClassName(vehicle.distance_to_road)}`}
            >
              {vehicle.distance_to_road === 0 ? 100 : vehicle.distance_to_road}%
            </span>
          ),
        },
      },
      {
        id: "teleportation",
        title: "Teleportation",
        columnComponent: {
          render: (vehicle) => (
            <span
              className={`${getThresholdClassName(vehicle.teleportation)}`}
            >
              {vehicle.teleportation === 0 ? 100 : vehicle.teleportation}%
            </span>
          ),
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

  return <Table columns={columns} entities={mappedVehicles} />;
};

export default VehiclesTable;
