**Introduction**

Vehicle diagnostic information from the engine computer that can either be measurement data or fault code data.

**Properties**

## Code

The diagnostic parameter code number.

## Controller

The applicable[Controller](../Controller/index.md)for the diagnostic parameter.

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

| Get | Limit of 650 Get requests per 1m. | 650 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Pagination**

## Results limit

1300000

## Supported sort

[SortBy Version](../SortByVersion/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |