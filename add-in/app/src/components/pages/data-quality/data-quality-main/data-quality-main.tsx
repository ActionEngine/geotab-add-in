import { useContext, useMemo, useState } from "react";
import { getValidation, getValidationByDevice } from "@/api/validation";
import GeotabMap from "@/components/geotab-map/geotab-map";
import { useFetch } from "@/hooks/useFetch";
import { AppContext } from "@/provider/app-provider";
import {
  ValidationDeviceResponse,
  ValidationResponse,
  ValidationType,
} from "@/types/shemas/validaton";
import { getThresholdClassName } from "@/utils/threshold";
import {
  getValidationsPercentage,
  getVehicleWithWorstResult,
  makeVehiclesByStatus,
} from "@/utils/validation";
import { Button } from "@geotab/zenith/esm/button/button";
import { Card } from "@geotab/zenith/esm/card/card";
import { Select } from "@geotab/zenith/esm/select/select";
import { GeotabCredentials } from "mg-api-js";
import moment from "moment";
import { validationTypeLabelMap } from "../constants";
import ChecksList from "./checks-list/checks-list";
import "./style.css";
import VehiclesList from "./vehicles-list/vehicles-list";

const ALL_CHECKS = {
  id: "ALL_CHECKS",
  children: "All Checks",
};

interface DataQualityMainProps {
  api: GeotabApi;
}

const DataQualityMain = ({ api }: DataQualityMainProps) => {
  const { session, databaseInfo } = useContext(AppContext);
  const [selectCheck, setSelectCheck] = useState<string>(ALL_CHECKS.id);
  const [selectedVehicleId, setSelectedVehicleId] = useState<number | null>(null);

  const { data: validation } = useFetch<ValidationResponse[]>({
    fn: () => getValidation(session as GeotabCredentials),
    key: "all-validation",
  });

  const { data: validationByDevice } = useFetch<ValidationDeviceResponse[]>({
    fn: () => getValidationByDevice(session as GeotabCredentials),
    key: "all-validation-by-device",
  });

  const vehicles = useMemo(
    () => makeVehiclesByStatus(validationByDevice || []),
    [validationByDevice],
  );

  const currentValidationId = useMemo(() => {
    if (selectCheck === ALL_CHECKS.id) return null;
    return (
      validation?.find((v) => v.validation_type === selectCheck)?.id ?? null
    );
  }, [selectCheck, validation]);

  const validationsPercentage = useMemo(
    () => getValidationsPercentage(validation || []),
    [validation],
  );
  const minPercentage = useMemo(() => {
    if (!validationsPercentage.length) return 0;
    return Math.min(...validationsPercentage.map((v) => v.percentage));
  }, [validationsPercentage]);

  const vehicleWithWorstResult = useMemo(
    () => getVehicleWithWorstResult(validationByDevice || []),
    [validationByDevice],
  );

  const validationTitle = useMemo(() => {
    if (selectCheck === ALL_CHECKS.id) return "Overall Data Quality";
    return validationTypeLabelMap[selectCheck as ValidationType];
  }, [selectCheck]);

  const validationAnomalyPercentage = useMemo(() => {
    if (selectCheck === ALL_CHECKS.id) return minPercentage;
    const validationSelected = validationsPercentage.find(
      (v) => v.type === selectCheck,
    );
    if (!validationSelected) return 0;
    return validationSelected.percentage;
  }, [selectCheck, validationsPercentage, minPercentage]);

  const options = useMemo(
    () => [
      ALL_CHECKS,
      ...(validation?.map((v) => {
        return {
          id: v.validation_type,
          children: validationTypeLabelMap[v.validation_type],
        };
      }) ?? []),
    ],
    [validation],
  );

  const handleSelectCheck = (id: string | undefined) => {
    if (!id) return;

    setSelectCheck(id);
  };

  return (
    <div className="data-quality-main-container">
      <div className="data-quality-main-header">
        <h1>Data Quality</h1>
        <div className="data-quality-main-header-right">
          <div>
            Last Data Sync:
            <div>
              {moment(databaseInfo?.last_sync).format("MMM DD, YYYY HH:mm")}
            </div>
          </div>
          <div>
            Validated for:
            <div>
              {moment(validation?.[0]?.finished_at)
                .subtract(15, "minutes")
                .format("MMM DD, YYYY HH:mm")}{" "}
              -{" "}
              {moment(validation?.[0]?.started_at).format("MMM DD, YYYY HH:mm")}
            </div>
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
      </div>
      <div className="data-quality-main-info-container">
        <Card size="L">
          <Card.Content>
            <div className="data-quality-main-info-card">
              <h2>{validationTitle}</h2>
              <div className="data-quality-main-info-validation">
                <div
                  className={`min-percentage ${getThresholdClassName(validationAnomalyPercentage)}`}
                >
                  {validationAnomalyPercentage}%
                </div>
                {selectCheck === "ALL_CHECKS" ? (
                  <ChecksList
                    vehicleWithWorstResult={vehicleWithWorstResult}
                    validationsPercentage={validationsPercentage}
                  />
                ) : (
                  <VehiclesList
                    vehicles={vehicles.filter(
                      (v) => v.validation_id === currentValidationId,
                    )}
                  />
                )}
              </div>
            </div>
          </Card.Content>
        </Card>
        <Card size="L">
          <Card.Content>
            <div className="data-quality-main-info-card">
              <h2>Fleet Map Preview</h2>
              <div className="map-container">
                <GeotabMap api={api} />
              </div>
            </div>
          </Card.Content>
        </Card>
      </div>
      <Card size="L" fullWidth>
        <Card.Content>
          <div className="data-quality-main-info-card">
            <h2>
              Vehicles
            </h2>
            <div>
              {validationByDevice?.map((item) => (
                <div
                  key={item.device_id}
                  style={{
                    display: "flex",
                    gap: "12px",
                    alignItems: "center",
                    padding: "8px",
                  }}
                >
                  <span>ID: {item.device_id}</span>
                  <Button
                    type="primary"
                    onClick={() => setSelectedVehicleId(item.device_id)}
                  >
                    View Details
                  </Button>
                </div>
              ))}
            </div>
          </div>
        </Card.Content>
      </Card>
    </div>
  );
};

export default DataQualityMain;
