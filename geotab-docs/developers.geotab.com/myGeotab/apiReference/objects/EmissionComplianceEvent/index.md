**Introduction**

Represents a significant event in the compliance timeline of a vehicle's Clean Truck Check (CTC) enrollment.This entity logs key milestones, such as the initial enrollment, scheduled compliance actions, report submissions to the Californian Air Resources Board (CARB), and the resulting compliance status feedback.Security clearance requirements:
- Creating/Updating (Add/Set requests) for EmissionComplianceEvent are not available to API users.
- Retrieving (Get requests) requires one of the following clearances: AccessCleanTruckCheckCompliance, AccessCleanTruckCheckComplianceEditor, or AccessCleanTruckCheckComplianceViewer.

**Properties**

## ComplianceErrorCount

The compliance error count.

## ComplianceStatus

The compliance status associated with this event. This can represent an initial state (NoCompleteCycles) or feedback from CARB. Note: NoCompleteCycles indicates that no completed valid Clean Truck Check cycle has been received for an enrolled device. Valid values are:
- Fail
- Pass
- NotReady
- Incomplete
- InvalidTesterId
- InvalidSoftwareVersion
- VehicleNotApplicableForObdTesting
- TestResultCouldNotBeDetermined
- VehicleNotApplicableForCleanTruckCheck
- InvalidTest
- NoCompleteCycles
- PendingReportSubmissionWindow
- FailDueToApparentChangeInConfiguration
- RefereeReferral

## CreatedDateTime

The[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)when the emission compliance event record was created. Timestamp of the last response received from CARB for a submitted report.

## EmissionVehicleEnrollment

The[EmissionVehicleEnrollment](../EmissionVehicleEnrollment/index.md)the event is associated with.

## EventType

The event type for the compliance event. Valid values are:
- InitialDeadlineSet
- ResponseReceived

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## NextComplianceDueDateTime

The[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)the next compliance action is due following this event.

## Protocol

The emission reporting protocol.

## ScheduledDateTime

The[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)this event was scheduled for.

## SubmittedDateTime

The[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime)a report related to this event was submitted to CARB. Timestamp of the finalized event record. A response has been received.

## TestResultMessage

The emission compliance event test result message.

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

[SortBy Date](../SortByDate/index.md) sorts by the EmissionComplianceEvent.SubmittedDateTime property.

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |