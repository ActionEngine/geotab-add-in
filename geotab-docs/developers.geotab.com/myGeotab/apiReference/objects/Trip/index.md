**Introduction**

This is a vehicles trip and a summary of the driving activity during that trip. To get more information about stops during a trip please see[ExceptionEvent](../ExceptionEvent/index.md). A complete "trip" is defined as starting at the time in which the vehicle starts and begins being driven. The trip continues after the vehicle has been stopped and ends at the time the vehicle restarts and begins being driven again; which then starts the next trip.

**Properties**

## AfterHoursDistance

The distance the vehicle was driven after work hours (in km).

## AfterHoursDrivingDuration

The duration the vehicle was driven after work hours.

## AfterHoursEnd

Whether the trip ends after hours.

## AfterHoursStart

Whether the trip starts after hours.

## AfterHoursStopDuration

The duration the vehicle was stopped after work hours.

## AverageSpeed

The average speed in km/h. This only includes the average speed while driving.

## DeletedDateTime

## Device

The[Device](../Device/index.md)associated with the trip.

## Distance

The distance the vehicle was driven during this trip (in km).

## Driver

The[Driver](../Driver/index.md)for the trip.

## DrivingDuration

The duration between the start and stop of the trip.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## IdlingDuration

Total end of trip idling (idling is defined as speed is 0 and ignition on). It is calculated from the beginning of this trip to beginning of next trip.

## MaximumSpeed

The maximum speed of the vehicle during this trip (in km/h).

## NextTripStart

The start date of the next trip, as well as the end of the current trip session.

## SpeedRange1

The number of incidents where the vehicle reached the first range of speeding triggers.

## SpeedRange1Duration

The duration where the vehicle drove in the first range of speeding triggers.

## SpeedRange2

The number of incidents where the vehicle reached the second range of speeding triggers.

## SpeedRange2Duration

The duration where the vehicle drove in the second range of speeding triggers.

## SpeedRange3

The number of incidents where the vehicle reached the third range of speeding triggers.

## SpeedRange3Duration

The duration where the vehicle drove in the third range of speeding triggers.

## Start

The date and time that the drive session started. This also signals the start of the trip.

## Stop

The date and time the trip drive session ended, and the vehicle stopped moving. Note that this doesn't correspond to end of the trip session.

## StopDuration

The duration the vehicle was stopped at the end of the trip. This also includes any idling done at the end of a trip.

## StopPoint

The[Coordinate](../Coordinate/index.md)associated with this Trip's stop.

## Version

The version of the entity.

## WorkDistance

The distance the vehicle was driven during work hours.

## WorkDrivingDuration

The duration the vehicle was driven during work hours.

## WorkStopDuration

The duration the vehicle was stopped during work hours.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1000 Get requests per 1m. | 1000 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Pagination**

## Results limit

25000

## Supported sort

[SortBy Id](../SortById/index.md)

[SortBy Start](../SortByStart/index.md)

[SortBy Stop](../SortByStop/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |