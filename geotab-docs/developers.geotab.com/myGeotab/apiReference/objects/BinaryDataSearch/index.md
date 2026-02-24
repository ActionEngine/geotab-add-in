**Introduction**

The object used to specify the arguments when searching for[BinaryData](../BinaryData/index.md).

**Properties**

## BinaryDataType

Search for BinaryData that has this[BinaryDataType](../BinaryDataType/index.md).

## ControllerSearch

The search options which are used to search for binary data for a controller[ControllerSearch](../ControllerSearch/index.md)by Id and protocol's Id. Available ControllerSearch options are:.
- Id
- SourceSearch.Id

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any BinaryData that are assigned to that Device. Providing the Groups will search for BinaryData for that have Devices in that group. Available DeviceSearch options are:
- Id
- Group

## FromDate

Search for BinaryData records that were logged at this date or after.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## ToDate

Search for BinaryData records that were logged at this date or before.