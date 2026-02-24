**Introduction**

The object used to specify the arguments when searching for[TachographDataFile](../TachographDataFile/index.md).

**Properties**

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options.Providing a device ID will search for any file that is assigned to that Device.Providing the Groups will search for files that have Devices in that group.Providing the device IDs will search for files that have Devices in that list.Available DeviceSearch options are:
- Id
- Group
- DeviceIds

## FromUploadDate

Search for file records that were uploaded at this date or after.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeArchived

The flag to include archived files. By default archived tachograph data file records are not returned, set this flag to true to return all records.

## IncludeBinaryData

The flag to include binary data in the response.

## Keywords

Search for entities that contain specific keywords into FileName, FileNameDdd, FileNameTgd, FileNameV1B,in case the “type = Driver” it will look into the driver's first name and last name, or when “type = Device” in the license plate.Note: It is currently limited to only one keyword. To use keywords it is necessary to use the “type” filter too.

## ToUploadDate

Search for file records that were uploaded at this date or before.

## Type

Search for file records based on the file type. The available values are:
- "Driver": To filter by file type Driver.
- "Device": To filter by file type Device.

## UserSearch

Filter by the[UserSearch](../UserSearch/index.md)options.Providing a user ID will search for any file that is assigned to that user.Providing the Groups will search for files that have Users in that group.Providing the user IDs will search for files that have Users in that list, in this case the users will be drivers.Available UserSearch options are:
- Id
- Group
- UserIds

## Version

The row version of the[TachographDataFile](../TachographDataFile/index.md)search criteria.