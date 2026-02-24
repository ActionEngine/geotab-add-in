**Introduction**

A DVIRDefect is a Defect that can be associated with a[DVIRLog](../DVIRLog/index.md). It contains repair information such as repair[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime), repair[User](../User/index.md), and[RepairStatusType](../RepairStatusType/index.md). DVIRDefect also consists a list of[DefectRemark](../DefectRemark/index.md)which can be used to store additional information for the defect.

**Properties**

## Defect

The[Defect](../Defect/index.md)which this DVIRDefect belongs to.

## DefectRemarks

The[DefectRemark](../DefectRemark/index.md)s which this DVIRDefect has.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Part

The[Group](../Group/index.md)part associated with this DVIRDefect, e.g., front left tire, rear right door, headlight.

## RepairDateTime

The date and time the DVIRDefect was repaired.

## RepairStatus

The[RepairStatusType](../RepairStatusType/index.md)of this DVIRDefect.

## RepairUser

The[User](../User/index.md)who repaired the DVIRDefect.