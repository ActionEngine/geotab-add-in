**Introduction**

The distance a BEV or PHEV can travel on a full charge. The range estimate is based on historical energy consumption, distance traveled, and battery capacity.

**Properties**

## DetectionDate

The date and time (UTC, ISO 8601 format) when the[RangeEstimate](index.md)was calculated.

## Device

The[Device](../Device/index.md)associated with the[RangeEstimate](index.md).

## RangeEstimateLowerBoundKm

The lower bound range estimate (for 90% confidence interval), measured in kilometers.This means there is a 90% probability that the vehicle’s range is between RangeEstimateLowerBoundKm and RangeEstimateUpperBoundKm.

## RangeEstimateMeanKm

The mean range estimate, measured in kilometers.

## RangeEstimateUpperBoundKm

The upper bound range estimate (for 90% confidence interval), measured in kilometers.This means that there is a 90% probability that the vehicle’s range is between RangeEstimateLowerBoundKm and RangeEstimateUpperBoundKm.

## RangeEstimationMethod

The estimation method used to calculate the range estimates.If the method is BatteryEstimation, the calculation is based on the energy readings coming in and out of the battery.If the method is SoCEstimation, the calculation is based on the detected state-of-charge deltas at the beginning and end of trips.

## Vin

The vehicle identification number (VIN). Must be 17 characters.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |