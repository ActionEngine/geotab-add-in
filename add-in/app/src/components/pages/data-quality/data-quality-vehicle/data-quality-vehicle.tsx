import { useContext, useEffect, useMemo, useState } from "react";
import {
  getValidationDistanceToRoad,
  getValidationTeleportation,
} from "@/api/validation";
import GeotabMapChecks from "@/components/geotab-map/geotab-map-checks";
import { AppContext } from "@/provider/app-provider";
import {
  ValidationDistanceToRoadResponse,
  ValidationResponse,
  ValidationTeleportationResponse,
  ValidationType,
} from "@/types/shemas/validaton";
import { IconChevronRightSmall } from "@geotab/zenith/esm/icons/iconChevronRightSmall";
import { Select } from "@geotab/zenith/esm/select/select";
import { GeotabCredentials } from "mg-api-js";
import { validationTypeLabelMap } from "../constants";
import "./style.css";

interface DataQualityVehicleProps {
  deviceId: string;
  validations: ValidationResponse[] | [];
  onBack: () => void;
}

const DataQualityVehicle = ({
  deviceId,
  validations,
  onBack,
}: DataQualityVehicleProps) => {
  const { session } = useContext(AppContext);
  const [selectCheck, setSelectCheck] = useState<string>("");
  const [points, setPoints] = useState<
    ValidationTeleportationResponse[] | ValidationDistanceToRoadResponse[]
  >([]);

  const options = useMemo(
    () =>
      validations?.map((v) => {
        return {
          id: v.validation_type,
          children: validationTypeLabelMap[v.validation_type],
        };
      }),
    [validations],
  );

  useEffect(() => {
    if (selectCheck || options.length === 0) return;
    setSelectCheck(options[0].id);
  }, [options]);

  useEffect(() => {
    if (!selectCheck) return;

    if (selectCheck === ValidationType.TELEPORTATION) {
      getValidationTeleportation(session as GeotabCredentials, deviceId).then(
        (res) => {
          setPoints(res);
        },
      );
    }
    if (selectCheck === ValidationType.DISTANCE_TO_ROAD) {
      getValidationDistanceToRoad(session as GeotabCredentials, deviceId).then(
        (res) => {
          setPoints(res);
        },
      );
    }
    setPoints([]);
  }, [selectCheck]);

  const mapPoints = useMemo(
    () =>
      points.map((point) => {
        return { latitude: point.latitude, longitude: point.longitude };
      }),
    [points],
  );

  const handleSelectCheck = (id: string | undefined) => {
    if (!id) return;

    setSelectCheck(id);
  };

  const handleBack = () => {
    onBack();
  };

  return (
    <div className="data-quality-vehicle">
      <div className="data-quality-vehicle-info">
        <div className="header">
          <span onClick={handleBack}>Source Tracking</span>
          <IconChevronRightSmall />
          <span>Vehicle {deviceId}</span>
        </div>
        <Select
          placeholder="Select"
          title="Select"
          items={options || []}
          value={selectCheck}
          onChange={handleSelectCheck}
          className="select-width"
        />
      </div>
      <GeotabMapChecks points={mapPoints} />
    </div>
  );
};

export default DataQualityVehicle;
