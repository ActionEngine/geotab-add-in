import GeotabMapChecks from "@/components/geotab-map/geotab-map-checks";
import { IconChevronRightSmall } from "@geotab/zenith/esm/icons/iconChevronRightSmall";
import "./style.css";

interface DataQualityVehicleProps {
  deviceId: string;
  onBack: () => void;
}

const DataQualityVehicle = ({ deviceId, onBack }: DataQualityVehicleProps) => {
  const handleBack = () => {
    onBack();
  };
  return (
    <div className="data-quality-vehicle">
      <div className="data-quality-vehicle-info">
        <div className="breadcrumbs">
          <span onClick={handleBack}>Source Tracking</span>
          <IconChevronRightSmall />
          <span>Vehicle {deviceId}</span>
        </div>
      </div>
      <GeotabMapChecks />
    </div>
  );
};

export default DataQualityVehicle;
