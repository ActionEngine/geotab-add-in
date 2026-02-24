**Introduction**

The object used to specify the arguments when searching for[StatusData](../StatusData/index.md). When searching for status data including DeviceSearch and DiagnosticSearch the system will return all records that match the search criteria and interpolate the value at the provided from/to dates when there is no record that corresponds to the date. Interpolated records are dynamically created when the request is made and can be identified as not having the ID property populated. Records with an ID are stored in the database.This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + DiagnosticSearch + FromDate and/or ToDate

**Properties**

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any StatusData recorded for that Device. Providing the Groups will search for StatusData recorded for Devices in that group. Available DeviceSearch options are:
- Id
- Group

## DiagnosticSearch

Search for StatusData with this[DiagnosticSearch](../DiagnosticSearch/index.md) Id. Available DiagnosticSearch options are:
- Id

## FromDate

Search for StatusData records that were logged at this date or after.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## ToDate

Search for StatusData records that were logged at this date or before.