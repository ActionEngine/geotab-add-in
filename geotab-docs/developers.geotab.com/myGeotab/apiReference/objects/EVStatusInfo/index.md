**Introduction**

The EVStatusInfo entity provides insights about the current state of an electric vehicle.

**Properties**

## DateTime

The date and time (UTC, ISO 8601 format) when[EVStatusInfo](index.md)was last updated.

## Device

The[Device](../Device/index.md)associated with the EVStatusInfo.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md). Note: This property is not available in Beta.

## RealTimeRangeRemainingLowerBoundKm

The lower bound estimate for remaining EV range in kilometers (for 90% confidence interval). This means there is a 90% probability that the vehicle’s remaining range is between RealTimeRangeRemainingLowerBoundKm and RealTimeRangeRemainingUpperBoundKm.

## RealTimeRangeRemainingMeanKm

The estimated remaining range of the electric vehicle in kilometers.

## RealTimeRangeRemainingUpperBoundKm

The upper bound estimate for remaining EV range in kilometers (for 90% confidence interval). This means there is a 90% probability that the vehicle’s remaining range is between RealTimeRangeRemainingLowerBoundKm and RealTimeRangeRemainingUpperBoundKm.

## TimeToChargeTo100Percent

The estimated time (UTC, ISO 8601 format) when the EV battery will reach 100% charge.

## TimeToChargeTo80Percent

The estimated time (UTC, ISO 8601 format) when the EV battery will reach 80% charge.

## TimeToChargeTo90Percent

The estimated time (UTC, ISO 8601 format) when the EV battery will reach 90% charge.

## Version

The version of the entity.Note: This property is not available in Beta.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |