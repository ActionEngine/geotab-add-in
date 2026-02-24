**Introduction**

The object used to specify the arguments when searching for[MediaFile](../MediaFile/index.md). This will return the data describing a file, not the actual file.

**Properties**

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any MediaFiles that are assigned to that Device. Providing the Groups will search for MediaFiles for that have Devices in that group. Available DeviceSearch options are:
- Id
- Group

## DriverSearch

Search for MediaFile with this[UserSearch](../UserSearch/index.md) Id. Available UserSearch options are:.
- Id

## FromDate

Search for MediaFile records at this date or after. Includes overlapping dates.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## SolutionId

Search for MediaFile records with this SolutionId.

## TagSearch

Search for MediaFile with this[TagSearch](../TagSearch/index.md). Available TagSearch options are:.
- Id
- TagIds

## ToDate

Search for MediaFile records at this date or before. Includes overlapping dates.