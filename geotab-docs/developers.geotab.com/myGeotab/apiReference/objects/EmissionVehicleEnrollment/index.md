**Introduction**

A Clean Check Truck emission vehicle enrollment. One[Device](../Device/index.md)should only have one active enrollment with status Pending or Enrolled.Security clearance requirements:Creating EmissionVehicleEnrollment (Add requests) requires security clearances AccessCleanTruckCheckCompliance;Updating EmissionVehicleEnrollment (Set requests) requires one of the following security clearances AccessCleanTruckCheckCompliance or AccessCleanTruckCheckComplianceEditor;Note: AccessCleanTruckCheckComplianceEditor is not allowed for disenrolling an enrollment.Retrieving EmissionVehicleEnrollment (Get requests) requires one of the following security clearances AccessCleanTruckCheckCompliance, AccessCleanTruckCheckComplianceEditor or AccessCleanTruckCheckComplianceViewer.

**Properties**

## Device

The[Device](../Device/index.md).

## DisenrolledDateTime

The disenrolled[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)if the[EmissionVehicleEnrollment](index.md)is disenrolled. If null, the[EmissionVehicleEnrollment](index.md)is not disenrolled.To disenroll a device, cancel its enrollment by:
- Setting DisenrolledDateTime to a not-null timestamp;
- Setting the EnrollmentStatus to NotEnrolled;
- Setting the LoggingFrequency to 0 (Disabled).

## DmvRegistrationDateTime

The DMV registration[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)for the[EmissionVehicleEnrollment](index.md).

## EnrollmentStatus

The enrollment status for the[EmissionVehicleEnrollment](index.md). Valid values are:
- NotEnrolled: When an enrollment's status is set to NotEnrolled or the DisenrolledDateTime is set, the enrollment is cancelled and the device is disenrolled.
- Pending: Active enrollment status. A new enrollment should be created with Pending status.
- Enrolled: Active enrollment status. Once a complete cycle has been received, a Pending enrollment will be marked as Enrolled.
- Rejected: When an enrollment attempt fails, an enrollment record with Rejected status will be created for the device with the failure reason. If later enrollment succeeds, the enrollment will be updated with an active enrollment status.

## FailureReason

The reason for enrollment failure. Valid values are:
- None
- DeviceIsNotProPlusOrGoPlan
- NoCompleteCycleReceived
- DeviceRatePlanNotFound
- VehicleNotApplicableForObdTesting
- VehicleNotApplicableForCleanTruckCheck
- DeviceIsArchived
- UncertifiedHarnessDetected
- Unknown The default value is "None".

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## LastLoggingFrequencyUpdateDateTime

The[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)when the logging frequency value was last updated.

## LoggingFrequencyType

The[EmissionEnrollmentLoggingFrequencyType](../EmissionEnrollmentLoggingFrequencyType/index.md)for the[EmissionVehicleEnrollment](index.md). Sets the Value property of[EmissionEnrollmentLoggingFrequencyType](../EmissionEnrollmentLoggingFrequencyType/index.md)to the one of the following numeric values to configure the emission logging frequency type:
- 0 (Disabled)
- 1~250 (Every 1~125 Day)
- 251 (Every Ignition)
- 253 (On Demand)

## SelectedLoggingFrequencyType

The selected[EmissionEnrollmentLoggingFrequencyType](../EmissionEnrollmentLoggingFrequencyType/index.md)for the[EmissionVehicleEnrollment](index.md).

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 500 Get requests per 1m. | 500 | 1m | Active |
| Set | Limit of 500 Set requests per 1m. | 500 | 1m | Active |
| Add | Limit of 500 Add requests per 1m. | 500 | 1m | Active |
| GetCountOf | Limit of 500 GetCountOf requests per 1m. | 500 | 1m | Active |
| Remove | Limit of 500 Remove requests per 1m. | 500 | 1m | Active |
| GetFeed | Limit of 250 GetFeed requests per 1m. | 250 | 1m | Active |

**Pagination**

## Results limit

10000

## Supported sort

[SortBy Id](../SortById/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |