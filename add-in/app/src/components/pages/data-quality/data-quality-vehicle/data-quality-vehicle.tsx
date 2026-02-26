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
import { getThresholdClassName } from "@/utils/threshold";
import { getValidationsPercentage } from "@/utils/validation";
import { IconChevronRightSmall } from "@geotab/zenith/esm/icons/iconChevronRightSmall";
import { Select } from "@geotab/zenith/esm/select/select";
import { GeotabCredentials } from "mg-api-js";
import moment from "moment";
import { validationTypeLabelMap } from "../constants";
import "./style.css";
import TableDistance from "./table-distance/table-distance";
import TableTeleportation from "./table-teleportation/table-teleportation";

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
  const { session, databaseInfo } = useContext(AppContext);
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
  }, [selectCheck]);

  const mapPoints = useMemo(
    () =>
      points.map((point) => {
        return { latitude: point.latitude, longitude: point.longitude };
      }),
    [points],
  );

  const validationsPercentage = useMemo(
    () => getValidationsPercentage(validations || []),
    [validations],
  );

  const handleSelectCheck = (id: string | undefined) => {
    if (!id) return;

    setPoints([]);
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
        <h2>{deviceId}</h2>
        <div className="data-quality-vehicle-checks ">
          {validationsPercentage.map((v) => (
            <div className="data-quality-vehicle-row" key={v.type}>
              <span>{validationTypeLabelMap[v.type]}</span>
              <span className={getThresholdClassName(v.percentage)}>
                {v.percentage}%
              </span>
            </div>
          ))}
        </div>
        <div className="data-quality-vehicle-info-details">
          <div className="data-quality-vehicle-info-details-item">
            Last Data Sync:
            <div>
              {moment(databaseInfo?.last_sync).format("MMM DD, YYYY HH:mm")}
            </div>
          </div>
          <div className="data-quality-vehicle-info-details-item">
            Validated for:
            <div>
              {moment(validations?.[0]?.finished_at)
                .subtract(15, "minutes")
                .format("MMM DD, YYYY HH:mm")}{" "}
              -{" "}
              {moment(validations?.[0]?.started_at).format(
                "MMM DD, YYYY HH:mm",
              )}
            </div>
          </div>
        </div>
        <div className="data-quality-vehicle-separate" />
        <div className="data-quality-vehicle-select-container">
          <h3>Validation Details</h3>
          <Select
            placeholder="Select"
            title="Select"
            items={options || []}
            value={selectCheck}
            onChange={handleSelectCheck}
            className="select-width"
          />
        </div>
        {selectCheck === ValidationType.TELEPORTATION && (
          <TableTeleportation
            points={points as ValidationTeleportationResponse[]}
          />
        )}
        {selectCheck === ValidationType.DISTANCE_TO_ROAD && (
          <TableDistance
            points={points as ValidationDistanceToRoadResponse[]}
          />
        )}
      </div>
      <GeotabMapChecks points={mapPoints} />
    </div>
  );
};

export default DataQualityVehicle;
