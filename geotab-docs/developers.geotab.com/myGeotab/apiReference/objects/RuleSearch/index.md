**Introduction**

The object used to specify the arguments when searching for a[Rule](../Rule/index.md).

**Properties**

## BaseType

Search for Rules that are this[ExceptionRuleBaseType](../ExceptionRuleBaseType/index.md); either Custom, Stock, or ZoneStop.

## Category

Search for Rules that are in this[ExceptionRuleCategory](../ExceptionRuleCategory/index.md); either ApplicationExceptionRule, UserExceptionRules or ZoneStopExceptionRules.

## Groups

Search for Rules that are members of these[GroupSearch](../GroupSearch/index.md)(s) one of it's children or one of it's parents. Available GroupSearch options are:.
- Id

## Id

Search for a[Rule](../Rule/index.md)with this[Id](../Id/index.md).

## Name

Search for Rules with this Name. Wildcard can be used by prepending/appending "%" to string. Example "%comments%".

## Status

Search for Rules with status that is either active or archived.