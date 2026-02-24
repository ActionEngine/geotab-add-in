**Introduction**

Conditions model the logic that govern a[Rule](../Rule/index.md)and can apply to many different types of data and entities. Conditions are structured in hierarchical tree. A condition's type (see[ConditionType](../ConditionType/index.md)) defines the meaning of each condition in the tree and can be an operator, special operator, data or an asset.Depending on the type of condition, it can have a minimum of 0 and maximum of 1 entity properties (Device, Driver, Diagnostic, WorkTime, Zone or ZoneType) defined per condition. Operator conditions (OR, AND, >, <, ==, NOT) will not have any entity properties populated. Special Operator conditions evaluate against special types of data such as Aux data, Zones, WorkHours, etc. and may have the entity property populated and/or a child condition populated with a Data condition. Asset conditions will only have the asset entity property populated.The unit of measure for data is described either by the related[Diagnostic](../Diagnostic/index.md)'s[UnitOfMeasure](../UnitOfMeasure/index.md)or as follows:
- Distance: Meters (m)
- Speed: Kilometers Per Hour (km/h)
- Duration: Seconds

A tree of conditions can define simple or complex rules and can be very powerful. Please take into consideration all possible consequences of a series of rules. Overly complex, poorly written or an excessive number of rules can have undesirable performance effects.

**Properties**

## Children

Child condition(s) of this condition.

## ConditionType

The[ConditionType](../ConditionType/index.md)defines the meaning of this condition.

## Device

Specified[Device](../Device/index.md)associated with the condition.

## Diagnostic

The[Diagnostic](../Diagnostic/index.md)to compare the value of.

## Driver

Specified[Driver](../Driver/index.md)associated with the condition.

## Group

Specified[Group](../Group/index.md)associated with the condition.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Value

The specified value to evaluate against.

## WorkTime

The[WorkTime](../WorkTime/index.md)that the event must occur inside/outside of for the violation to occur.

## Zone

Specified[Zone](../Zone/index.md)associated with the condition.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |