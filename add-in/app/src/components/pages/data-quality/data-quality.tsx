import { useContext, useEffect, useState } from "react";
import { getValidationAndByDevice } from "@/api/validation";
import { useFetch } from "@/hooks/useFetch";
import { AppContext } from "@/provider/app-provider";
import {
  ValidationDeviceResponse,
  ValidationResponse,
  VehicleValidation,
} from "@/types/schemas/validation";
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

  const { data: validationData } = useFetch<{
    validations: ValidationResponse[];
    byDevice: ValidationDeviceResponse[];
  }>({
    fn: () => getValidationAndByDevice(session as GeotabCredentials),
    key: "all-validation-and-by-device",
    refetchInterval: 10 * 1000,
  });

  useEffect(() => {
    if (!validationData) return;
    if (
      validationData.validations?.length &&
      JSON.stringify(validationData.validations) !== JSON.stringify(validations)
    ) {
      setValidations(validationData.validations);
      setVehicles(makeVehiclesByStatus(validationData.byDevice));
    }
  }, [validationData]);

  const clearSelectedVehicle = () => {
    setSelectedVehicle(null);
  };

  if (selectedVehicle) {
    return (
      <DataQualityVehicle
        deviceId={selectedVehicle}
        onBack={clearSelectedVehicle}
        validations={validations || []}
        validationByDevice={validationData?.byDevice || []}
        isValidationByDeviceLoading={!validationData}
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
