**Introduction**

Get all posted road speed changes for a device's trips for the given dates. If the from date and to date are in the middle of the trip, the data for the whole trip are included.

**Parameters**

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## deviceSearch

Search for RoadMaxSpeeds with this[DeviceSearch](../../objects/DeviceSearch/index.md). Available DeviceSearch options are:.
- Id

## fromDate

Search for maximum road speed limits that were encountered at this date or after.

## postedRoadSpeedOptions

Road data options[PostedRoadSpeedOptions](../../objects/PostedRoadSpeedOptions/index.md)

## toDate

Search for maximum road speed limits that were encountered at this date or before.

**Return value**

A list of[MaxRoadSpeedResult](../../objects/MaxRoadSpeedResult/index.md)objects.

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| GetPostedRoadSpeedsForDevice | Limit of 300 requests per 1m. | 300 | 1m | Active |