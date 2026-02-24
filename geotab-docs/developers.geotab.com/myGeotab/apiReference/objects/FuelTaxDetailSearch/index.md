**Introduction**

The object used to specify the arguments when searching for[FuelTaxDetail](../FuelTaxDetail/index.md)elements.This search has been designed to work efficiently with these parameters:
- DeviceSearch
- FromDate
- ToDate

**Properties**

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any fuel tax details that are assigned to that Device. Providing the Groups will search for fuel tax details for that have Devices in that group.
- Id
- Groups

## FromDate

The beginning of the time interval. The search will adjust it to the nearest hour on or before this time. For instance, 8:20 AM will become 8 AM.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeBoundaries

A value indicating whether to include any parts of boundary details that fall outside the time interval.

## IncludeHourlyData

A value indicating whether to include hourly data.

## ToDate

The end of the time interval. The search will adjust it to the nearest hour on or after this time. For instance, 5:40 PM will become 6 PM.