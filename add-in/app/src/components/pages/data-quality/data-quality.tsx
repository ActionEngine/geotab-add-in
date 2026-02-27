import { useContext, useState } from "react";
import { getValidation } from "@/api/validation";
import { useFetch } from "@/hooks/useFetch";
import { AppContext } from "@/provider/app-provider";
import { ValidationResponse } from "@/types/shemas/validaton";
import { GeotabCredentials } from "mg-api-js";
import DataQualityMain from "./data-quality-main/data-quality-main";
import DataQualityVehicle from "./data-quality-vehicle/data-quality-vehicle";

interface DataQualityProps {
  api: GeotabApi;
}

const DataQuality = ({ api }: DataQualityProps) => {
  const { session } = useContext(AppContext);
  const [selectedVehicle, setSelectedVehicle] = useState<string | null>(null);

  const { data: validations } = useFetch<ValidationResponse[]>({
    fn: () => getValidation(session as GeotabCredentials),
    key: "all-validation",
    refetchInterval: 10 * 1000,
  });

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
    />
  );
};

export default DataQuality;
