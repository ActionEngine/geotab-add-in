import { useContext, useEffect, useMemo, useState } from "react";
import {
  getValidationByDevice,
  getValidationDistanceToRoad,
  getValidationIdleOutliers,
  getValidationTeleportation,
} from "@/api/validation";
import GeotabMapChecks from "@/components/geotab-map/geotab-map-checks";
import { useFetch } from "@/hooks/useFetch";
import { AppContext } from "@/provider/app-provider";
import {
  ValidationDeviceResponse,
  ValidationDistanceToRoadResponse,
  ValidationIdleOutlierResponse,
  ValidationResponse,
  ValidationTeleportationResponse,
  ValidationType,
} from "@/types/shemas/validaton";
import { getThresholdClassName } from "@/utils/threshold";
import { getAnomalyPercentage } from "@/utils/validation";
import { IconChevronRightSmall } from "@geotab/zenith/esm/icons/iconChevronRightSmall";
import { Select } from "@geotab/zenith/esm/select/select";
import { GeotabCredentials } from "mg-api-js";
import moment from "moment";
import { validationTypeLabelMap } from "../constants";
import "./style.css";
import TableDistance from "./table-distance/table-distance";
import TableIdleOutlier from "./table-idle-outlier/table-idle-outlier";
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

  const { data: validationByDevice } = useFetch<ValidationDeviceResponse[]>({
    fn: () => getValidationByDevice(session as GeotabCredentials),
    key: `all-validation-by-device-${deviceId}`,
  });

  const [points, setPoints] = useState<
    | ValidationTeleportationResponse[]
    | ValidationDistanceToRoadResponse[]
    | ValidationIdleOutlierResponse[]
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

    if (selectCheck === ValidationType.IDLE_OUTLIER) {
      getValidationIdleOutliers(session as GeotabCredentials, deviceId).then(
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

  const validationsPercentage = useMemo(() => {
    const validationTypeById = new Map<number, ValidationType>(
      validations.map((v) => [v.id, v.validation_type]),
    );

    const percentageByType = new Map<ValidationType, number>();
    (validationByDevice || [])
      .filter((v) => v.device_id === deviceId)
      .forEach((v) => {
        const validationType = validationTypeById.get(v.validation_id);
        if (!validationType) return;

        percentageByType.set(
          validationType,
          getAnomalyPercentage(v.warnings, v.errors, v.total),
        );
      });

    return validations.map((validation) => ({
      type: validation.validation_type,
      percentage: percentageByType.get(validation.validation_type) ?? 100,
    }));
  }, [validations, validationByDevice, deviceId]);

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
        {selectCheck === ValidationType.IDLE_OUTLIER && (
          <TableIdleOutlier
            points={points as ValidationIdleOutlierResponse[]}
          />
        )}
      </div>
      <GeotabMapChecks points={mapPoints} />
    </div>
  );
};

export default DataQualityVehicle;
