**Introduction**

The object used to specify the arguments when searching for a[DriverChange](../DriverChange/index.md). This search defaults to searching[DriverChange](../DriverChange/index.md)(s) by[Driver](../Driver/index.md) Id when no[DeviceSearch](../DeviceSearch/index.md)is provided.

**Properties**

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any DriverChanges that are assigned to that Device. Providing the Groups will search for DriverChanges for that have Devices in that group. Available DeviceSearch options are:
- Id
- Groups

## FromDate

Search for DriverChange records at this date or after.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeOverlappedChanges

A value indicating whether to include the last driver change before the from date or the most recent driver change (if dates are not provided).

## ToDate

Search for DriverChange records at this date or before.

## Type

A value indicating the[DriverChangeType](../DriverChangeType/index.md)to search for exclusively.

## UserSearch

Search for DriverChanges with this[UserSearch](../UserSearch/index.md) Id or DriverGroups. Available UserSearch options are:.
- Id
- DriverGroups
- DriverGroupFilterCondition