**Introduction**

Search class for[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md).

**Properties**

## DeviceSearch

[DeviceSearch](../DeviceSearch/index.md)to filter[EmissionVehicleEnrollmentSearch](index.md)result. Available[DeviceSearch](../DeviceSearch/index.md)options are:
- Id
- DeviceIds

## EnrollmentIds

A list of enrollment[Id](../Id/index.md)(s) to search for[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)s matching one of the enrollment[Id](../Id/index.md)s.

## EnrollmentStatuses

A list of enrollment statuses to search for[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)s matching one of the statuses. Valid "EnrollmentStatus" values are:
- NotEnrolled
- Pending
- Enrolled
- Rejected

## FromDate

A value to search for all[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)s from this date.

## FromDmvRegistrationDateTime

Search for all[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)s with DMV registration[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)from this date.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeDisenrolledEnrollments

A value indicating whether previously disenrolled[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)s are included. If true, returns active enrollments and disenrolled enrollments; Otherwise, only returns current active enrollments. (An active enrollment has enrollment status Pending or Enrolled.) Default is false.

## IncludeRejectedEnrollments

A value indicating whether rejected[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)s are included. If true, returns all active enrollments and rejected enrollments; Otherwise, only returns active enrollments. (An active enrollment has enrollment status Pending or Enrolled.) Default is false.

## LoggingFrequencyType

Search for all[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)s with the given[EmissionEnrollmentLoggingFrequencyType](../EmissionEnrollmentLoggingFrequencyType/index.md)value.

## ToDate

A value to search for all[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)s to this date.

## ToDmvRegistrationDateTime

Search for all[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)s with DMV registration[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)to this date.