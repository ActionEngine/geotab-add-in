**Introduction**

The object used to specify the arguments when searching for[Route](../Route/index.md)(s).

**Properties**

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any Routes that are assigned to that Device. Providing the Groups will search for Routes for that have Devices in that group. Available DeviceSearch options are:
- Id
- Groups

## FromDate

Search for Routes that were active at this date or after.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## Name

Search for Routes with this Name. Wildcard can be used by prepending/appending "%" to string. Example "%comments%".

## RouteType

Search for Routes with this[RouteType](../RouteType/index.md).

## ServiceGroups

Search for ONLY Route Completion ([RouteType](../RouteType/index.md). Service) routes that are members of these[GroupSearch](../GroupSearch/index.md)(s) in the Service Group hierarchy. Available GroupSearch options are:
- Id

## ToDate

Search for Routes that were active at this date or before.

## ZoneSearch

Filter by the[ZoneSearch](../ZoneSearch/index.md)options. Providing a zone ID will search for any Routes that contain that Zone. Providing Groups will search for Routes that have Zones in that group. Available ZoneSearch options are:
- Id
- Groups