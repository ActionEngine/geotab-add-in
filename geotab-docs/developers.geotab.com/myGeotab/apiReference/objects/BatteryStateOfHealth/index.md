**Introduction**

This entity allows you to track high voltage battery degradation over the lifetime of your BEVs and PHEVs. We use historical driving and charging data to estimate usable battery capacity.

**Properties**

## CurrentBatteryCapacityLowerBoundKwh

The lower bound of the vehicle's usable battery capacity on the detection date, measured in kWh.This means that there is a 90% probability that the true usable battery capacity is between CurrentBatteryCapacityLowerBoundKwh and CurrentBatteryCapacityUpperBoundKwh.

## CurrentBatteryCapacityMeanKwh

The usable battery capacity on the detection date, measured in kWh.The mean value is our best guess at the vehicle's true usable battery capacity.

## CurrentBatteryCapacityUpperBoundKwh

The upper bound of the vehicle's usable battery capacity on the detection date, measured in kWh.This means that there is a 90% probability that the true usable battery capacity is between CurrentBatteryCapacityLowerBoundKwh and CurrentBatteryCapacityUpperBoundKwh.

## DetectionDate

The date and time (UTC, ISO 8601 format) when the[BatteryStateOfHealth](index.md)was calculated.

## Device

The[Device](../Device/index.md)associated with the[BatteryStateOfHealth](index.md).

## OriginalBatteryCapacityLowerBoundKwh

The lower bound of the vehicle's usable battery capacity when the vehicle was new, measured in kWh.This means that there is a 90% probability that the true usable battery capacity is between OriginalBatteryCapacityLowerBoundKwh and OriginalBatteryCapacityUpperBoundKwh.The original capacity is calculated based on data collected from other vehicles of the same make, model, year and trim. This value may be updated as we gather more information on this particular trim.

## OriginalBatteryCapacityMeanKwh

The mean original battery capacity value, measured in kWh.The mean value is our best guess at the true original battery capacity when the vehicle was new.The original capacity is calculated based on data collected from other vehicles of the same make, model, year and trim. This value may be updated as we gather more information on this particular trim.

## OriginalBatteryCapacityUpperBoundKwh

The upper bound of the vehicle's usable battery capacity when the vehicle was new, measured in kWh.This means that there is a 90% probability that the true usable battery capacity is between OriginalBatteryCapacityLowerBoundKwh and OriginalBatteryCapacityUpperBoundKwh.The original capacity is calculated based on data collected from other vehicles of the same make, model, year and trim. This value may be updated as we gather more information on this particular trim.

## StateOfHealthLowerBound

The state of health's lower bound value.state of health = current battery capacity / original battery capacityThere is a 90% probability that the true usable battery capacity is between StateOfHealthLowerBound and StateOfHealthUpperBound.

## StateOfHealthMean

The mean state of health value.The mean value is our best guess at the true battery State of Health. It is calculated via the following formula:state of health = current battery capacity / original battery capacity

## StateOfHealthUpperBound

The state of health's upper bound value.state of health = current battery capacity / original battery capacityThere is a 90% probability that the true usable battery capacity is between StateOfHealthLowerBound and StateOfHealthUpperBound.

## Vin

The vehicle identification number (VIN). Must be 17 characters.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |