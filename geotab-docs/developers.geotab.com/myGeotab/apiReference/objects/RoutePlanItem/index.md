**Introduction**

The class representing an individual item in a planned[Route](../Route/index.md).

**Properties**

## ActiveFrom

The start date for the plan item.

## ActiveTo

The end date for the plan item.

## Comment

A free text field where any user information can be stored and referenced for this entity. Default [""].

## DateTime

Expected date and time of arrival.

## ExpectedDistanceToArrival

Expected trip distance to arrival.

## ExpectedStopDuration

Expected stop duration in milliseconds.

## ExpectedTripDurationToArrival

Expected trip time to arrival in milliseconds.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## PassCount

The expected number of passes through the[Zone](../Zone/index.md).

## Route

The associated[Route](../Route/index.md)of the plan.

## Sequence

The sequence number of the route plan item.

## Zone

The associated[Zone](../Zone/index.md)in the route.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |