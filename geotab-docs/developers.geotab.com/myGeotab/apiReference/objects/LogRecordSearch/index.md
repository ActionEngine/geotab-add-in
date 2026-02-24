**Introduction**

The object used to specify the arguments when searching for[LogRecord](../LogRecord/index.md)(s). When searching for log records the system will return all records that match the search criteria and interpolate the value at the provided from/to dates when there is no record that corresponds to the date. Interpolated records are dynamically created when the request is made and can be identified as not having the ID property populated. Records with an ID are stored in the database.This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + FromDate and/or ToDate

**Properties**

## DeviceSearch

Search for LogRecords for this[DeviceSearch](../DeviceSearch/index.md) Id. Available DeviceSearch options are:.
- Id

## FromDate

Search for LogRecords at this date or after.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## ToDate

Search for LogRecords at this date or before.