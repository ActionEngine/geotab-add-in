**Introduction**

A search object for finding specific[EmissionComplianceEvent](../EmissionComplianceEvent/index.md)records.

**Properties**

## ComplianceStatuses

A list of ComplianceStatus to search for all[EmissionComplianceEvent](../EmissionComplianceEvent/index.md)records matching one of the compliance statuses. Valid "ComplianceStatus" values are:
- Fail
- Pass
- NotReady
- Incomplete
- InvalidTesterId
- OutdatedSoftwareVersion
- VehicleNotApplicableForObdTesting
- TestResultCouldNotBeDetermined
- VehicleNotApplicableForCleanTruckCheck
- InvalidTest
- NoCompleteCycles

## EmissionVehicleEnrollmentSearch

An[EmissionVehicleEnrollmentSearch](../EmissionVehicleEnrollmentSearch/index.md)to filter events based on their parent enrollment. Available search options are:
- Id
- EnrollmentIds

## FromDate

The start of the date range (exclusive) to search for events. This property typically filters on the CreatedDateTime of the entity.

## FromScheduledDateTime

The start of the date range (inclusive) to search for[EmissionComplianceEvent](../EmissionComplianceEvent/index.md)records by their ScheduledDateTime.

## FromSubmittedDateTime

The start of the date range (inclusive) to search for[EmissionComplianceEvent](../EmissionComplianceEvent/index.md)records by their SubmittedDateTime.

## HasComplianceError

A value to search for[EmissionComplianceEvent](../EmissionComplianceEvent/index.md)records that have a compliance error. If true, returns records with ComplianceErrorCount greater than 0. If false, returns records with a zero or null error count. If unset (null), this filter is not applied.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## OnlyLatestSubmission

A value indicating whether to return only the latest[EmissionComplianceEvent](../EmissionComplianceEvent/index.md)for each associated[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md). If true, returns only the most recent event record (by version) per enrollment. The default value is false.

## ToDate

The end of the date range (exclusive) to search for events. This property typically filters on the CreatedDateTime of the entity.

## ToScheduledDateTime

The end of the date range (inclusive) to search for[EmissionComplianceEvent](../EmissionComplianceEvent/index.md)records by their ScheduledDateTime.

## ToSubmittedDateTime

The end of the date range (inclusive) to search for[EmissionComplianceEvent](../EmissionComplianceEvent/index.md)records by their SubmittedDateTime.