**Introduction**

A[Diagnostic](../Diagnostic/index.md)that represents measurement data from the vehicle (as opposed to fault codes).

**Properties**

## Code

The diagnostic parameter code number.

## Controller

The applicable[Controller](../Controller/index.md)for the diagnostic parameter.

## Conversion

The conversion factor for the diagnostic parameter; this is related to the[UnitOfMeasure](../UnitOfMeasure/index.md).

## DataLength

The length of the diagnostic data parameter in bytes.

## DiagnosticSignals

The DiagnosticSignal reference list. This property is obsolete and doesn't store or return any value except null.

## DiagnosticType

The[DiagnosticType](../DiagnosticType/index.md)(source) of the diagnostic parameter.

## FaultResetMode

The[FaultResetMode](../FaultResetMode/index.md)of the diagnostic (whether the fault resets automatically or manually).

## Id

The unique identifier for this entity.

## IsReadOnly

A value indicating whether the diagnostic is readonly

## Name

The name of this entity which identifies it and is used when displaying this entity.

## Offset

The offset value of the diagnostic parameter.

## Source

The[Source](../Source/index.md)for the diagnostic (the type of diagnostic code).

## TamperingDiagnostics

The tampering diagnostic codes.

## UnitOfMeasure

The[UnitOfMeasure](../UnitOfMeasure/index.md)applicable to the diagnostic parameter.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |