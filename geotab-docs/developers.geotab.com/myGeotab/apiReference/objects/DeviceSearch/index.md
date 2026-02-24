**Introduction**

The object used to specify the arguments when searching for a[Device](../Device/index.md).

**Properties**

## Comment

Search for Devices with comments matching this value. Wildcard can be used by prepending/appending "%" to string. Example "%comments%".

## DeviceIds

Search for Devices with these unique[Id](../Id/index.md)(s). Not Supported for searching for devices, only for[DeviceStatusInfo](../DeviceStatusInfo/index.md),[TachographDataFile](../TachographDataFile/index.md),[FaultData](../FaultData/index.md),[ChargeEvent](../ChargeEvent/index.md)and[AddInDeviceLink](https://developers.geotab.com/myGeotab/apiReference/objects/AddInDeviceLink/).

## DeviceType

Search for Devices of this[DeviceType](../DeviceType/index.md).

## ExcludeActiveCommunicationStatusReason

The boolean to filter out devices that currently have an active DeviceCommunicationStatus.When true it will not return any devices that have a[IsActive](https://developers.geotab.com/myGeotab/apiReference/objects/IsActive/)= true; when false it only return devices with an[DeviceCommunicationStatus](https://developers.geotab.com/myGeotab/apiReference/objects/DeviceCommunicationStatus/)!= true. This property is mostly used with[IsCommunicating](https://developers.geotab.com/myGeotab/apiReference/objects/IsCommunicating/)to filter devices that are offline with an unknown reason

## FromDate

Search for Devices that were active at this date or after. Set to UTC now to search for only currently active (non-archived) devices.

## Groups

Search for Devices that are a member of these[GroupSearch](../GroupSearch/index.md)(s). Each GroupSearch is an object within the array. Available GroupSearch options are:
- Id

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## Keywords

Search for entities that contain specific keywords in all wildcard string-searchable fields.

## LicensePlate

Search for Devices with a license plate matching this value. Wildcard can be used by prepending/appending "%" to string. Example "%LicensePlate%".

## MacAddress

Search for Devices with this MacAddress.

## Name

Search for Devices with this Name. Name is the primary description of the Device. Wildcard can be used by prepending/appending "%" to string. Example "%name%".

## SerialNumber

Search for a Device by its unique serial number. Wildcard can be used by prepending/appending "%" to string. Example "%SerialNumber%".

## ToDate

Search for Devices that were active at this date or before.

## VehicleIdentificationNumber

Search for a Device by Vehicle Identification Number (VIN). This is the unique number assigned to the vehicle during manufacturing. This differs from[EngineVehicleIdentificationNumber](https://developers.geotab.com/myGeotab/apiReference/objects/EngineVehicleIdentificationNumber/)in that it is the last VIN reported from the Device that was determined to be valid. Wildcard can be used by prepending/appending "%" to string. Example "%VehicleIdentificationNumber%".