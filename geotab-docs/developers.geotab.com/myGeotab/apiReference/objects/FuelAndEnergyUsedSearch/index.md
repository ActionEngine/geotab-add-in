**Introduction**

The object used to specify the arguments when searching for[FuelAndEnergyUsed](../FuelAndEnergyUsed/index.md). This search has been designed to work efficiently with these parameters:
- Id
- DeviceSearch + FromDate and/or ToDate

**Properties**

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any data that are assigned to that Device. Providing the Groups will search for data for that have Devices in that group. Available DeviceSearch options are:
- Id
- Groups

## FromDate

The from date, which is used to search for records recorded on or after this date.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## ToDate

The to date, which is used to search for records recorded on or before this date.