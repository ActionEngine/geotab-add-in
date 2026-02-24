**Introduction**

The object used to specify the arguments when searching for[DutyStatusLog](../DutyStatusLog/index.md)(s).

**Properties**

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any DutyStatusLogs that are assigned to that Device. Providing the Groups will search for DutyStatusLogs for that have Devices in that group. Available DeviceSearch options are:
- Id
- Groups

## FromDate

Search for DutyStatusLogs that were recorded at this date or after.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeBoundaryLogs

Search for DutyStatusLogs and include boundary logs outside the from and to dates (for example, the log immediately preceding the from date).

## IncludeModifications

Include modification history of the[DutyStatusLog](../DutyStatusLog/index.md)results.

## States

Search for DutyStatusLogs with the provided[DutyStatusState](../DutyStatusState/index.md)s. By default, only[Active](../../../../index.md#Active)logs are returned.

## Statuses

Search for DutyStatusLogs with the provided[DutyStatusLogType](../DutyStatusLogType/index.md)s.

## ToDate

Search for DutyStatusLogs that were recorded at this date or before.

## UserSearch

Search for DutyStatusLogs with this[UserSearch](../UserSearch/index.md) Id. Available UserSearch options are:.
- Id
- GroupSearch