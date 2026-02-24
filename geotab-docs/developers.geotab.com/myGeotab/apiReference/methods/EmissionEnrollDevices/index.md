**Introduction**

Enrolls devices for Clean Truck Check emission reporting.Requires the AccessCleanTruckCheckCompliance security clearance.

**Parameters**

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## deviceEnrollmentInfoList

A list of[DeviceEnrollmentInfo](../../objects/DeviceEnrollmentInfo/index.md)s with the information of the devices to be enrolled. Maximum number of devices to be enrolled is 100.

**Return value**

An[Enumerable](https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable)of[DeviceEnrollmentResult](../../objects/DeviceEnrollmentResult/index.md)objects for the specified devices.

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| EmissionEnrollDevices | Limit of 10 requests per 1m. | 10 | 1m | Active |