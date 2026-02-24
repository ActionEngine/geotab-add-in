**Introduction**

The object used to specify the arguments when searching for[DeviceStatusInfo](../DeviceStatusInfo/index.md)(s).

**Properties**

## ClosestAssetLimit

The maximum number of Devices to search for when specifying a "Position".

## DeviceSearch

Search for[DeviceStatusInfo](../DeviceStatusInfo/index.md)(s) from a device that matches the[DeviceSearch](../DeviceSearch/index.md) Id or in the Groups specified. This includes archived and deleted devices. Available DeviceSearch options are:.
- Id
- Groups

## Diagnostics

A list of[Diagnostics](https://developers.geotab.com/myGeotab/apiReference/objects/Diagnostics/)to look for the latest values for those diagnostics. Maximum amount [200] Available Diagnostics options are:.
- Id

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeUntrackedDevices

A value indicating whether to include untracked and archived vehicles in the search results. Defaults to <see langword="false".

## Position

Search for Status Info for Devices in the vicinity of the provided[Coordinate](../Coordinate/index.md). Starting from this position, an outward search for Devices will continue until the number of devices found matches the number defined in the "ClosestAssetLimit" property.

## UserSearch

Search for Device Status Info associated with this[UserSearch](../UserSearch/index.md) Id. Available UserSearch options are:.
- Id