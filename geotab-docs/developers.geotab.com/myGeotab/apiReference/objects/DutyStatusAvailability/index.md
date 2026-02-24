**Introduction**

Driver Availability for Hours of Service regulations.

**Properties**

## Cycle

The duration of cycle duty hours left.

## CycleAvailabilities

Cycle available to the driver in the future.

## CycleDriving

The duration of cycle driving hours left.

## CycleRest

The duration left before cycle rest must be taken.

## Driver

The[User](../User/index.md)associated with the duty status availability.

## Driving

The duration left for driving.

## DrivingBreakDuration

The duration of the driving break (USA only)

## Duty

The duration of total on-duty time left in a day.

## DutySinceCycleRest

The duty hours left since Cycle Rest.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Is16HourExemptionAvailable

If 16 hour exemption is available.

## IsAdverseDrivingApplied

If adverse driving exemption is applied.

## IsAdverseDrivingExemptionAvailable

If adverse driving exemption is available.

## IsOffDutyDeferralExemptionAvailable

If off-duty deferral exemption is available.

## IsRailroadExemptionAvailable

If railroad exemption is available.

## Recap

Chronological array representing each day's On-duty time since beginning of cycle.

## Rest

The duration left before rest break must be taken.

## Workday

The duration of workday left in a day. Workday is a consecutive window that begins with first on-duty.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 2500 Get requests per 1m. | 2500 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |