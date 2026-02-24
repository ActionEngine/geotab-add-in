**Introduction**

Specify whether the fault resets automatically or manually.

**Properties**

## AutoReset

The engine[FaultData](../FaultData/index.md)data[ExceptionEvent](../ExceptionEvent/index.md)for this kind of[Diagnostic](../Diagnostic/index.md)will always contain single[FaultData](../FaultData/index.md)instance.

## None

The engine[FaultData](../FaultData/index.md)data[ExceptionEvent](../ExceptionEvent/index.md)for this kind of[Diagnostic](../Diagnostic/index.md)can contain a number of sequential[FaultData](../FaultData/index.md)instances. These instances will continue to grow until the fault condition ends.