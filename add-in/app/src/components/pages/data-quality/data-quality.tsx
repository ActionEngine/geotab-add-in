import { useState } from "react";
import DataQualityMain from "./data-quality-main/data-quality-main";
import DataQualityVihicle from "./data-quality-vihicle/data-quality-vihicle";

interface DataQualityProps {
  api: GeotabApi;
}

const DataQuality = ({ api }: DataQualityProps) => {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [selectedVehicle, setSelectedVehicle] = useState<string | null>(null);

  if (selectedVehicle) {
    return <DataQualityVihicle />;
  }
  return (
    <DataQualityMain
      api={api}
      onSelectVehicle={(id) => setSelectedVehicle(id)}
    />
  );
};

export default DataQuality;
