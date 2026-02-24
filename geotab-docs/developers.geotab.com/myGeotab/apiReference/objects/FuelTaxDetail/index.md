**Introduction**

Fuel tax reporting element. The available driving history for a[Device](../Device/index.md)is stored as a sequence of such details. Each next detail starts when and where the previous detail ended. A detail is identified by its parameters (enter and exit time, odometer, GPS odometer, latitude and longitude) and its attributes (jurisdiction,[Driver](../Driver/index.md), toll road, authority). When any of the attributes changes, the current detail ends and a new detail begins. For more information, see[IFTA Guide](https://docs.google.com/document/d/1vqQYJEIrUqOJ0LlFEeY1iVddcC-I4DTY2z73NE0Nzug).

**Properties**

## Authority

The authority. 'None' by default.

## Device

The[Device](../Device/index.md).

## Driver

The[Driver](../Driver/index.md).

## EnterGpsOdometer

The GPS odometer, in km, at the enter time.

## EnterLatitude

The latitude at the enter time.

## EnterLongitude

The longitude at the enter time.

## EnterOdometer

The odometer, in km, at the enter time.

## EnterTime

The time at which the detail begins.

## ExitGpsOdometer

The GPS odometer, in km, at the exit time.

## ExitLatitude

The latitude at the exit time.

## ExitLongitude

The longitude at the exit time.

## ExitOdometer

The odometer, in km, at the exit time.

## ExitTime

The time at which the detail ends.

## HourlyGpsOdometer

The GPS odometer values, in km, at each hour within the detail's time interval.

## HourlyIsOdometerInterpolated

A list of values indicating whether the odometer at the corresponding hour is interpolated.

## HourlyLatitude

The latitude values at each hour within the detail's time interval.

## HourlyLongitude

The longitude values at each hour within the detail's time interval.

## HourlyOdometer

The odometer values, in km, at each hour within the detail's time interval.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## IsEnterOdometerInterpolated

A value indicating whether the odometer at enter time is interpolated.

## IsExitOdometerInterpolated

A value indicating whether the odometer at exit time is interpolated.

## Jurisdiction

The jurisdiction, such as a U.S. state or a Canadian province.

## TollRoad

The toll road name. null by default.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1000 Get requests per 1m. | 1000 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Pagination**

## Results limit

1000

## Supported sort

[SortBy Id](../SortById/index.md)

[SortBy Date](../SortByDate/index.md) sorts by the FuelTaxDetail.ExitTime property.

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |