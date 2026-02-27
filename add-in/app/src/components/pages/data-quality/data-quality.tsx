import { useContext, useEffect, useState } from "react";
import { getValidation, getValidationByDevice } from "@/api/validation";
import { useFetch } from "@/hooks/useFetch";
import { AppContext } from "@/provider/app-provider";
import {
  ValidationDeviceResponse,
  ValidationResponse,
  VehicleValidation,
} from "@/types/shemas/validaton";
import { makeVehiclesByStatus } from "@/utils/validation";
import { GeotabCredentials } from "mg-api-js";
import DataQualityMain from "./data-quality-main/data-quality-main";
import DataQualityVehicle from "./data-quality-vehicle/data-quality-vehicle";

interface DataQualityProps {
  api: GeotabApi;
}

const DataQuality = ({ api }: DataQualityProps) => {
  const { session } = useContext(AppContext);
  const [selectedVehicle, setSelectedVehicle] = useState<string | null>(null);
  const [validations, setValidations] = useState<ValidationResponse[]>([]);
  const [vehicles, setVehicles] = useState<VehicleValidation[]>([]);

  const { data: validationsRes } = useFetch<ValidationResponse[]>({
    fn: () => getValidation(session as GeotabCredentials),
    key: "all-validation",
    refetchInterval: 10 * 1000,
  });

  const { data: validationByDevice } = useFetch<ValidationDeviceResponse[]>({
    fn: () => getValidationByDevice(session as GeotabCredentials),
    key: "all-validation-by-device",
    refetchInterval: 10 * 1000,
  });

  useEffect(() => {
    if (
      validationsRes?.length &&
      JSON.stringify(validationsRes) !== JSON.stringify(validations)
    ) {
      setValidations(validationsRes);
    }
  }, [validationsRes]);

  useEffect(() => {
    if (
      validationByDevice?.length &&
      JSON.stringify(validationByDevice) !== JSON.stringify(vehicles)
    ) {
      setVehicles(makeVehiclesByStatus(validationByDevice || []));
    }
  }, [validationByDevice]);

  const clearSelectedVehicle = () => {
    setSelectedVehicle(null);
  };

  if (selectedVehicle) {
    return (
      <DataQualityVehicle
        deviceId={selectedVehicle}
        onBack={clearSelectedVehicle}
        validations={validations || []}
      />
    );
  }
  return (
    <DataQualityMain
      api={api}
      onSelectVehicle={(id) => setSelectedVehicle(id)}
      validations={validations || []}
      vehicles={vehicles || []}
    />
  );
};

export default DataQuality;
