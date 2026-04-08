import { useContext, useMemo, useState } from "react";
import GeotabMap from "@/components/geotab-map/geotab-map";
import InfoDialog from "@/components/info-dialog/info-dialog";
import MapIcon from "@/image/map-icon";
import TrackIcon from "@/image/track-icon";
import { AppContext } from "@/provider/app-provider";
import {
  ValidationResponse,
  ValidationType,
  VehicleValidation,
} from "@/types/schemas/validation";
import { getValidationsPercentage } from "@/utils/validation";
import { IconInfoCircle } from "@geotab/zenith";
import { Card } from "@geotab/zenith/esm/card/card";
import { Select } from "@geotab/zenith/esm/select/select";
import { TextIconButton } from "@geotab/zenith/esm/textIconButton/textIconButton";
import moment from "moment";
import { validationTypeLabelMap } from "../constants";
import ChecksList from "./checks-list/checks-list";
import "./style.css";
import VehiclesList from "./vehicles-list/vehicles-list";
import VehiclesTable from "./vehicles-table/vehicles-table";

const ALL_CHECKS = {
  id: "ALL_CHECKS",
  children: "All Checks",
};

interface DataQualityMainProps {
  api: GeotabApi;
  vehicles: VehicleValidation[];
  validations: ValidationResponse[];
  onSelectVehicle: (id: string) => void;
}

const DataQualityMain = ({
  api,
  validations,
  vehicles,
  onSelectVehicle,
}: DataQualityMainProps) => {
  const { databaseInfo } = useContext(AppContext);
  const [selectCheck, setSelectCheck] = useState<string>(ALL_CHECKS.id);
  const [openInfo, setOpenInfo] = useState(false);

  const currentValidationId = useMemo(() => {
    if (selectCheck === ALL_CHECKS.id) return null;
    return (
      validations?.find((v) => v.validation_type === selectCheck)?.id ?? null
    );
  }, [selectCheck, validations]);

  const validationsPercentage = useMemo(
    () => getValidationsPercentage(validations || []),
    [validations],
  );

  const validationTitle = useMemo(() => {
    if (selectCheck === ALL_CHECKS.id) return "Overall Data Quality";
    return validationTypeLabelMap[selectCheck as ValidationType];
  }, [selectCheck]);

  const options = useMemo(
    () => [
      ALL_CHECKS,
      ...(validations?.map((v) => {
        return {
          id: v.validation_type,
          children: validationTypeLabelMap[v.validation_type],
        };
      }) ?? []),
    ],
    [validations],
  );

  const handleSelectCheck = (id: string | undefined) => {
    if (!id) return;

    setSelectCheck(id);
  };

  const handleOpenInfo = () => {
    setOpenInfo(true);
  };

  const handleCloseInfo = () => {
    setOpenInfo(false);
  };

  return (
    <div className="data-quality-main-container">
      <div className="data-quality-main-header">
        <h1>Aspen GIS Lite</h1>
        <div className="data-quality-main-header-right">
          <div>
            Last Data Sync:
            <div>
              {moment(databaseInfo?.last_sync).format("MMM DD, YYYY HH:mm")}
            </div>
          </div>
          <div>
            {validations.length > 0 && (
              <>
                Validated for:{" "}
                <div>
                  {moment(validations?.[0]?.finished_at)
                    .subtract(15, "minutes")
                    .format("MMM DD, YYYY HH:mm")}{" "}
                  -{" "}
                  {moment(validations?.[0]?.started_at).format(
                    "MMM DD, YYYY HH:mm",
                  )}
                </div>
              </>
            )}
          </div>
          <Select
            placeholder="Select"
            title="Select"
            items={options || []}
            value={selectCheck}
            onChange={handleSelectCheck}
            className="select-width"
            disabled={validations.length === 0}
          />
        </div>
      </div>
      <div className="data-quality-main-info-container">
        <Card size="L">
          <Card.Content>
            <div className="data-quality-main-info-card">
              <div className="block-header">
                {validationTitle}{" "}
                <TextIconButton
                  type="tertiary"
                  icon={IconInfoCircle}
                  onClick={handleOpenInfo}
                />
              </div>
              <div className="data-quality-main-info-validation">
                {validations.length > 0 ? (
                  <>
                    {selectCheck === "ALL_CHECKS" ? (
                      <ChecksList
                        validationsPercentage={validationsPercentage}
                      />
                    ) : (
                      <VehiclesList
                        vehicles={vehicles.filter(
                          (v) => v.validation_id === currentValidationId,
                        )}
                        selectedCheck={validationTitle}
                      />
                    )}
                  </>
                ) : (
                  <span className="vehicles-list-label">
                    Validation is being done
                  </span>
                )}
              </div>
            </div>
          </Card.Content>
        </Card>
        <Card size="L">
          <Card.Content>
            <div className="data-quality-main-info-card">
              <div className="block-header">
                <div className="icon-title-container">
                  <div className="card-icon">
                    <MapIcon />
                  </div>
                  Fleet Map Preview
                </div>
                <div>Live Demo View</div>
              </div>
              <div className="map-container">
                <GeotabMap api={api} vehicles={vehicles} />
              </div>
            </div>
          </Card.Content>
        </Card>
      </div>
      <Card size="L" fullWidth autoHeight={true}>
        <Card.Content>
          <div className="data-quality-main-info-card">
            <div className="block-header">
              <div className="icon-title-container">
                <div className="card-icon">
                  <TrackIcon />
                </div>
                Vehicles
              </div>
            </div>
            <VehiclesTable
              vehicles={vehicles}
              validations={validations}
              onSelectVehicle={onSelectVehicle}
            />
          </div>
        </Card.Content>
      </Card>
      <InfoDialog open={openInfo} onClose={handleCloseInfo} />
    </div>
  );
};

export default DataQualityMain;
