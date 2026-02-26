import { useState } from "react";
import DataQualityMain from "./data-quality-main/data-quality-main";
import DataQualityVehicle from "./data-quality-vehicle/data-quality-vehicle";

interface DataQualityProps {
  api: GeotabApi;
}

const DataQuality = ({ api }: DataQualityProps) => {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [selectedVehicle, setSelectedVehicle] = useState<string | null>("b19");

  const clearSelectedVehicle = () => {
    setSelectedVehicle(null);
  };

  if (selectedVehicle) {
    return (
      <DataQualityVehicle
        deviceId={selectedVehicle}
        onBack={clearSelectedVehicle}
      />
    );
  }
  return <DataQualityMain api={api} />;
};

export default DataQuality;
