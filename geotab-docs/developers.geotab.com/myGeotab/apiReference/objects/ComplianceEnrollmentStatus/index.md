**Introduction**

Represents the Clean Truck Check compliance enrollment status of a[Device](../Device/index.md).

**Properties**

## CurrentComplianceDeadlineDateTime

The current compliance due date and time for the device if it is enrolled for Clean Truck Check emission reporting. The datetime of the current compliance due, or null if the device is not enrolled or if there is no due date set.

## CurrentCompliancePeriodStartDateTime

The current compliance reporting period start date.

## EnrollmentStatus

A string value indicating the enrollment status. Valid values are:
- NotEnrolled
- Pending
- Enrolled
- Rejected

## NextComplianceDeadlineDateTime

The next compliance due date and time for the device if it is enrolled. The datetime of the next compliance due, or null if the device is not enrolled or if there is no due date set.