**Introduction**

Detailed information for Hours of Service regulation for a driver.

**Properties**

## Availability

The[DutyStatusAvailability](../DutyStatusAvailability/index.md).

## CurrentDutyStatus

The latest duty status log type[DutyStatusLogType](../DutyStatusLogType/index.md)affecting availability or violations.

## CycleSummaries

The cycle summaries.

## DaySummaries

The day summaries.

## Driver

The[Driver](../Driver/index.md).

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## OffDutyNeeded

When off duty is needed.

## RestBreakNeeded

When rest break is needed.

## Violations

The[DutyStatusViolation](../DutyStatusViolation/index.md).

## WorkdaySummaries

The workday summaries.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 500 Get requests per 1m. | 500 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |