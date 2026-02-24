**Introduction**

The object used to specify the arguments when searching for[Trip](../Trip/index.md)(s). This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + FromDate and/or ToDate (+ IncludeOverlappedTrips)
- UserSearch + FromDate and/or ToDate (+ IncludeOverlappedTrips)

**Properties**

## DeviceSearch

Search for Trips with this[DeviceSearch](../DeviceSearch/index.md) Id. Available DeviceSearch options are:.
- Id

## FromDate

Search for Trips recorded at this date or after. When "IncludeOverlappedTrips" is set to True, search for Trips where the NextTripStartTime is at this date, after or NULL.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeOverlappedTrips

A value indicating whether when OverlappedTrips is set to True; any part of a trip that overlaps with the FromDate or ToDate boundary will have the entire trip included in the data.

## SearchArea

Search rectangular area for Trips; the trips being retrieved must be located in this area. The[BoundingBox](../BoundingBox/index.md)object should contain the bottom left and top right coordinates of the searching rectangle.

## ToDate

Search for Trips recorded at this date or before. When "IncludeOverlappedTrips" is set to True, search for Trips where the StartDateTime is this date or before.

## UserSearch

Search for Trips with this[UserSearch](../UserSearch/index.md) Id. Available UserSearch options are:.
- Id