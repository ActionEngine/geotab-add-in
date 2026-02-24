**Introduction**

A rule is the definition of conditions that, when "violated", will generate an[ExceptionEvent](../ExceptionEvent/index.md). The rule's logic is defined by it's tree of[Condition](../Condition/index.md)(s). It's condition tree will be evaluated against data for device(s) that are members of the rule's assigned group(s) or the device(s)/driver(s) defined in the rule condition tree. The conditions will be evaluated independently against the assets in the selected groups.

**Properties**

## ActiveFrom

Start date of the Rule's notification activity period.

## ActiveTo

End date of the Rule's notification activity period.

## BaseType

The[ExceptionRuleBaseType](../ExceptionRuleBaseType/index.md)of the rule; either Custom, Stock or ZoneStop.

## Color

The[Color](../Color/index.md)associated with this rule. Used when rendering[ExceptionEvent](../ExceptionEvent/index.md)(s) related to this rule. Color is defined by the parameters "Red", "Green" and "Blue".

## Comment

Free text field where any user information can be stored and referenced for this entity.

## Condition

The hierarchical tree of[Condition](../Condition/index.md)(s) defining the logic of a rule. A rule should have one or more conditions in it's tree.

## Groups

A list of[Group](../Group/index.md)(s) assigned to the rule. Device in these groups will have the rule evaluated against their data.

## Id

The unique identifier for this entity.

## Name

The name of this entity which identifies it and is used when displaying this entity.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 300 Get requests per 1m. | 300 | 1m | Active |
| Set | Limit of 150 Set requests per 1m. | 150 | 1m | Active |
| Add | Limit of 150 Add requests per 1m. | 150 | 1m | Active |
| Remove | Limit of 150 Remove requests per 1m. | 150 | 1m | Active |
| GetCountOf | Limit of 150 GetCountOf requests per 1m. | 150 | 1m | Active |
| GetFeed | Limit of 150 GetFeed requests per 1m. | 150 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |