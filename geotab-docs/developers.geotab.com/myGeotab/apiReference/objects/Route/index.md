**Introduction**

A connected sequence of zones which create a path for the vehicle to follow.

**Properties**

## Comment

Free text field where any user information can be stored and referenced for this entity. Default [""].

## Device

The[Device](../Device/index.md)linked to the route. Only applies to "Plan" type routes.

## EndTime

The end date and time of the route which is the arrival time of the last stop.

## Id

The unique identifier for this entity.

## Name

The name of this entity which identifies it and is used when displaying this entity. Maximum length [255].

## ResourceShiftEndTime

The end of a driver's shift hours

## ResourceShiftStartTime

The start of a driver's shift hours

## RoutePlanItemCollection

The[RoutePlanItem](../RoutePlanItem/index.md)item collection (sequence of stops which make up the route).

## RouteType

The[RouteType](../RouteType/index.md). Default [Basic].

## StartTime

The start date and time or the route which is the arrival time of the 1st stop.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 200 Get requests per 1m. | 200 | 1m | Active |
| Set | Limit of 200 Set requests per 1m. | 200 | 1m | Active |
| Add | Limit of 200 Add requests per 1m. | 200 | 1m | Active |
| Remove | Limit of 200 Remove requests per 1m. | 200 | 1m | Active |
| GetCountOf | Limit of 200 GetCountOf requests per 1m. | 200 | 1m | Active |
| GetFeed | Limit of 200 GetFeed requests per 1m. | 200 | 1m | Active |

**Pagination**

## Results limit

5000

## Supported sort

[SortBy Id](../SortById/index.md)

[SortBy Name](../SortByName/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |