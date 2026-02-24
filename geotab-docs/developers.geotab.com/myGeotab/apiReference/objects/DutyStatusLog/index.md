**Introduction**

A DutyStatusLog is a record of duty status for Hours of Service regulations. The log is first required to have a driver, dateTime, status, and device. Location is not required and will be calculated from the device's data.

**Properties**

## Annotations

The list of[AnnotationLog](../AnnotationLog/index.md)(s) which are associated with this log.

## CoDrivers

The list of the co-driver[User](../User/index.md)(s) for this log.

## DateTime

The date and time the log was created.

## DeferralMinutes

The deferral minutes.

## DeferralStatus

The[DutyStatusDeferralType](../DutyStatusDeferralType/index.md).

## Device

The[Device](../Device/index.md)associated with this log.

## Driver

The[User](../User/index.md)who created this log.

## EditDateTime

The date and time the log was edited. If the log has not been edited, this will not be set.

## EditRequestedByUser

The[User](../User/index.md)that requested an edit to this log.

## EngineHours

The engine hours for the[Device](../Device/index.md)at the[DateTime](https://developers.geotab.com/myGeotab/apiReference/objects/DateTime/)of this log. The unit is seconds (not hours).

## EventCode

The event code of this log (Table 6; 7.20 of the ELD Final Rule).

## EventRecordStatus

The record status number of this log 1 = active 2 = inactive - changed 3 = inactive - change requested 4 = inactive - change rejected.

## EventType

The event type number of this log 1 = A change in driver's duty-status 2 = An intermediate log 3 = A change in driver's indication of authorized personal use of CMV or yard moves 4 = A driver's certification/re-certification of records 5 = A driver's login/logout activity 6 = CMV's engine power up / shut down activity 7 = A malfunction or data diagnostic detection occurrence (Table 6; 7.25 of the ELD Final Rule).

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## IsIgnored

If the log is ignored. True means it will not affect the Driver's HOS availability.

## IsTransitioning

A value indicating whether the log is in transitioning state.

## Location

An object with the location information for the log data.

## Malfunction

The[DutyStatusMalfunctionTypes](../DutyStatusMalfunctionTypes/index.md)of the[DutyStatusLog](index.md)record. As a flag it can be both a diagnostic and malfunction state which is used to mark status based records (e.g. "D", "SB") as having a diagnostic or malfunction present at time of recording.

## Odometer

The odometer in meters for the[Device](../Device/index.md)at the[DateTime](https://developers.geotab.com/myGeotab/apiReference/objects/DateTime/)of this log.

## Origin

The[DutyStatusOrigin](../DutyStatusOrigin/index.md)from where this log originated.

## ParentId

The[Id](../Id/index.md)of the parent[DutyStatusLog](index.md). Used when a DutyStatusLog is edited. When returning history, this field will be populated.

## Sequence

The sequence number, which is used to generate the sequence ID.

## State

The[DutyStatusState](../DutyStatusState/index.md)of the[DutyStatusLog](index.md)record.

## Status

The[DutyStatusLogType](../DutyStatusLogType/index.md)representing the driver's duty status.

## VerifyDateTime

The date and time the log was verified. If the log is unverified, this will not be set.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 400 Get requests per 1m. | 400 | 1m | Active |
| Set | Limit of 250 Set requests per 1m. | 250 | 1m | Active |
| Add | Limit of 250 Add requests per 1m. | 250 | 1m | Active |
| Remove | Limit of 250 Remove requests per 1m. | 250 | 1m | Active |
| GetCountOf | Limit of 250 GetCountOf requests per 1m. | 250 | 1m | Active |
| GetFeed | Limit of 250 GetFeed requests per 1m. | 250 | 1m | Active |

**Pagination**

## Results limit

25000

## Supported sort

[SortBy Date](../SortByDate/index.md) sorts by the DutyStatusLog.DateTime property.

[SortBy Version](../SortByVersion/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |