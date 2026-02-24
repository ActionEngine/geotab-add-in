**Introduction**

The object used to specify the arguments when searching for[DVIRLog](../DVIRLog/index.md)(s). A trailerSearch and deviceSearch cannot be used at the same time because a DVIR log entry is only ever associated with one asset type (for instance, if the "device" is set, "trailer" is always null and vice versa).

**Properties**

## CertifiedBySearch

Search for DVIRLogs certified by a[User](../User/index.md). Available[UserSearch](../UserSearch/index.md)options are:.
- Id

## DefectSearch

Search for DVIRLogs that are a member of these defect[Group](../Group/index.md)(s). Available[GroupSearch](../GroupSearch/index.md)options are:.
- Id

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any DVIRLogs that are assigned to that Device. Providing the Groups will search for DVIRLogs for that have Devices in that group. Available DeviceSearch options are:
- Id
- Groups

## FromDate

Search for DVIRLogs that were recorded at this date or after.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeBoundaryLogs

Search for DVIRLogs and include boundary logs outside the from and to dates (for example, the log immediately preceding the from date).

## IsSafeToOperate

Search for DVIRLogs which are safe or are not safe to operate.

## LogTypes

Search for[DVIRLog](../DVIRLog/index.md)s that match the specified[DVIRLogType](../DVIRLogType/index.md)s.

## RepairedBySearch

Search for DVIRLogs repaired by a[User](../User/index.md). Available[UserSearch](../UserSearch/index.md)options are:.
- Id

## ToDate

Search for DVIRLogs that were recorded at this date or before.

## TrailerSearch

Filter by the[TrailerSearch](../TrailerSearch/index.md)options. Providing a trailer ID will search for any DVIRLogs that are assigned to that Trailer. Providing the Groups will search for DVIRLogs for that have Trailer in that group. Available TrailerSearch options are:
- Id
- Groups

## UserSearch

Search for DVIRLogs with this[UserSearch](../UserSearch/index.md) Id. Available UserSearch options are:.
- Id