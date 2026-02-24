**Introduction**

A[DutyStatusLog](../DutyStatusLog/index.md)violation for a[User](../User/index.md).

**Properties**

## DaysLimit

The maximum or minimum days limit of the duty status violation.

## Driver

The[User](../User/index.md)associated with the duty status violation.

## DrivingDuration

The driving duration of the duty status violation.

## FromDate

The date and time that the duty status violation started.

## HoursLimit

The maximum or minimum hours limit of the duty status violation.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Reason

The stated reason why the duty status violation occurred.

## ToDate

The date and time that the duty status violation ended.

## Type

The[DutyStatusViolationType](../DutyStatusViolationType/index.md)of the duty status violation.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 750 Get requests per 1m. | 750 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |