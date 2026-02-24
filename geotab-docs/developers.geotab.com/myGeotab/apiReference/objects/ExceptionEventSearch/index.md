**Introduction**

The object used to specify the arguments when searching for[ExceptionEvent](../ExceptionEvent/index.md). This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + RuleSearch + FromDate and/or ToDate

**Properties**

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a Device ID will search for any Exception Events recorded for that Device. Providing Groups will search Exception Events recorded for Devices that are members of the provided GroupSearch(s) or their children. Available DeviceSearch options are:.
- Id
- Groups

## FromDate

Search for Exception Events that occurred at this date or after.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeExceptionCount

A value indicating whether to include the count of exception instances for the returned exception events. When set to true, the[ExceptionCount](https://developers.geotab.com/myGeotab/apiReference/objects/ExceptionCount/)property will be populated.

## IncludeInvalidated

Search for[ExceptionEvent](../ExceptionEvent/index.md)s that have been invalidated because of new data being processed. The default value is [false] while using "Get" and "GetFeed" APIs.

## RuleSearch

Filter by the[RuleSearch](../RuleSearch/index.md)options. Providing a Rule ID will search for any Exception Events recorded for that Rule. Providing a[ExceptionRuleBaseType](../ExceptionRuleBaseType/index.md)will search for any Exception Events with the given Base Type. Available RuleSearch options are:.
- Id
- BaseType

## ToDate

Search for Exception Events that occurred at this date or before.