**Introduction**

A record that represents a fault code record from the engine system of the specific[Device](../Device/index.md).

**Properties**

## AmberWarningLamp

Whether the amber warning lamp state.

## ClassCode

The[DtcClass](../DtcClass/index.md)code of the fault.

## Controller

The[Controller](../Controller/index.md)code related to the fault code; if applicable.

## Count

The number of times the fault occurred.

## DateTime

The date and time at which the event occurred.

## Device

The[Device](../Device/index.md)that generated the fault.

## Diagnostic

The[Diagnostic](../Diagnostic/index.md)associated with the fault.

## DismissDateTime

The date and time that the DismissUser dismissed the fault.

## DismissUser

The[User](../User/index.md)that dismissed the fault.

## EffectOnComponent

The effect on component for enriched fault.

## FailureMode

The[FailureMode](../FailureMode/index.md)of the fault; if applicable.

## FaultDescription

The fault description for enriched fault.

## FaultLampState

The[FaultLampState](../FaultLampState/index.md)of a J1939 vehicle. See[FaultLampState](../FaultLampState/index.md)for the possible values.

## FaultState

The[FaultState](../FaultState/index.md)code from the engine system of the specific device.

## FaultStates

The[FaultStatus](../FaultStatus/index.md)(s) from the engine system of the specific device.

## FlashCode

The[FlashCode](../FlashCode/index.md)associated with the fault.

## Id

The unique identifier for the entity. See[Id](../Id/index.md).

## MalfunctionLamp

The malfunction light state.

## ProtectWarningLamp

Whether the protect warning lamp is on.

## Recommendation

The recommendation for enriched fault.

## RedStopLamp

Whether the red stop lamp is on.

## RiskOfBreakdown

The risk of breakdown associated with the fault.

## Severity

The overall severity level of the fault. This value is determined by coalescing the following properties in order of precedence: Effectively, this property represents .

## SourceAddress

The source address for enhanced faults.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 500 Get requests per 1m. | 500 | 1m | Active |
| Set | Limit of 1200 Set requests per 1m. | 1200 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Pagination**

## Results limit

50000

## Supported sort

[SortBy Id](../SortById/index.md)

[SortBy Date](../SortByDate/index.md) sorts by the FaultData.DateTime property.

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |