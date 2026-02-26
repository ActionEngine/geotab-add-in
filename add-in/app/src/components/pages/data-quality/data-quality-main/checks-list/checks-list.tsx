import { ValidationType } from "@/types/shemas/validaton";
import { getThresholdClassName, THRESHOLD_CLASSNAME } from "@/utils/threshold";
import { validationTypeLabelMap } from "../../constants";
import "./style.css";

interface ChecksListProps {
  vehicleWithWorstResult: {
    value: number;
    className: THRESHOLD_CLASSNAME;
  };
  validationsPercentage: {
    type: ValidationType;
    percentage: number;
  }[];
}

const ChecksList = ({
  vehicleWithWorstResult,
  validationsPercentage,
}: ChecksListProps) => {
  return (
    <>
      <div className="container-row">
        <span>Vehicles with worst results</span>
        <span className={vehicleWithWorstResult.className}>
          {vehicleWithWorstResult.value}
        </span>
      </div>
      <div className="checks">
        {validationsPercentage.map((v) => (
          <div className="container-row" key={v.type}>
            <span>{validationTypeLabelMap[v.type]}</span>
            <span className={getThresholdClassName(v.percentage)}>
              {v.percentage}%
            </span>
          </div>
        ))}
      </div>
    </>
  );
};

export default ChecksList;
