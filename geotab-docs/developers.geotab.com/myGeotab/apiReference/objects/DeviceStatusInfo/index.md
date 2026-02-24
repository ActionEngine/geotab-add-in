**Introduction**

Represents the current state of a vehicle by providing information such as the vehicle bearing location and speed, active exception events and whether the device is currently communicating.

**Properties**

## Bearing

The bearing (heading) in integer degrees.

## CurrentStateDuration

The duration between the last Trip state change (i.e. driving or stop), and the most recent date of location information.

## DateTime

The most recent[DateTime](https://developers.geotab.com/myGeotab/apiReference/objects/DateTime/)of the latest piece of status, gps or fault data.

## Device

The[Device](../Device/index.md)this DeviceStatusInfo belongs to.

## Driver

The[Driver](../Driver/index.md)associated to the current[Device](../Device/index.md).

## ExceptionEvents

The[ExceptionEvent](../ExceptionEvent/index.md)(s) that are currently active.

## Groups

The[Group](../Group/index.md)(s) that the[Device](../Device/index.md)currently belongs to.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## IsDeviceCommunicating

A value indicating whether the[Device](../Device/index.md)is communicating.

## IsDriving

A value indicating whether the current[Device](../Device/index.md)state. If set true, is driving. Otherwise, it is stopped.

## Latitude

The current latitude of the[Device](../Device/index.md).

## Longitude

The current longitude of the[Device](../Device/index.md).

## Speed

The current vehicle speed.

## StatusData

A list of the latest[StatusData](../StatusData/index.md)records for the current[Device](../Device/index.md).

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 900 Get requests per 1m. | 900 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Pagination**

## Results limit

50000

## Supported sort

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |