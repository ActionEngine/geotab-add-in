**Introduction**

Defines the different types of[Condition](../Condition/index.md)(s).

**Properties**

## ActiveOrInactiveFault

Data: Evaluate the condition against active or inactive[FaultData](../FaultData/index.md). Include a child diagnostic condition with related fault[Diagnostic](../Diagnostic/index.md)or NoDiagnostic to detect any[FaultData](../FaultData/index.md).

## AfterDeviceWorkHours

Work Hours Operator: Occurs after the[Device](../Device/index.md)'s assigned[WorkTime](../WorkTime/index.md).

## AfterRuleWorkHours

Work Hours Operator: Occurs after the[WorkTime](../WorkTime/index.md)assigned to this condition.

## And

Operator: Condition for "And" operations. "And" conditions must have two or more children that will act as the operands in the equation.

## Aux1

Auxiliary Operator: Evaluate against the asset(s) Auxiliary 1 value. Auxiliary conditions can have the value of 0 (False) or 1 (True).

## Aux2

Auxiliary Operator: Evaluate against the asset(s) Auxiliary 2 value. Auxiliary conditions can have the value of 0 (False) or 1 (True).

## Aux3

Auxiliary Operator: Evaluate against the asset(s) Auxiliary 3 value. Auxiliary conditions can have the value of 0 (False) or 1 (True).

## Aux4

Auxiliary Operator: Evaluate against the asset(s) Auxiliary 4 value. Auxiliary conditions can have the value of 0 (False) or 1 (True).

## Aux5

Auxiliary Operator: Evaluate against the asset(s) Auxiliary 5 value. Auxiliary conditions can have the value of 0 (False) or 1 (True).

## Aux6

Auxiliary Operator: Evaluate against the asset(s) Auxiliary 6 value. Auxiliary conditions can have the value of 0 (False) or 1 (True).

## Aux7

Auxiliary Operator: Evaluate against the asset(s) Auxiliary 7 value. Auxiliary conditions can have the value of 0 (False) or 1 (True).

## Aux8

Auxiliary Operator: Evaluate against the asset(s) Auxiliary 8 value. Auxiliary conditions can have the value of 0 (False) or 1 (True).

## Device

Asset: Apply to the[Device](../Device/index.md)specified in this condition. This will take priority over the[Group](../../../../index.md#Group)(s) assigned to the[Rule](../Rule/index.md). When no asset condition is specified the rule will apply to all assets in the rule's groups.

## DeviceWorkHours

Work Hours Operator: Occurs during the[Device](../Device/index.md)'s assigned[WorkTime](../WorkTime/index.md).

## DistanceBetweenGps

Data: Distance Between GPS points in meters.

## DistanceLongerThan

Value Operator: The duration of the child condition must continue to be true for a distance longer than the value of this condition in km.

## DistanceShorterThan

Value Operator: The duration of the child condition must continue to be true for no longer distance than the value of this condition in km.

## Driver

Asset: Apply to the[Device](../Device/index.md)that the[Driver](../Driver/index.md)specified in this condition is assigned to. This will take priority over the[Group](../../../../index.md#Group)(s) assigned to the[Rule](../Rule/index.md). When no asset condition is specified the rule will apply to all assets in the rule's groups.

## DurationBetweenGps

Data: Time Between GPS points in seconds.

## DurationLongerThan

Value Operator: The duration of the child condition must continue to be true for longer than the value of this condition in seconds.

## DurationShorterThan

Value Operator: The duration of the child condition must continue to be true for no longer than the value of this condition in seconds.

## DVIRDefect

Data: Exception event for whenever[DVIRDefect](../../../../index.md#DVIRDefect)is detected.

## EnteringArea

Zone Operator: Evaluate if the related asset(s) are entering the bounds a[Zone](../Zone/index.md)specified in this condition.

## ExitingArea

Zone Operator: Evaluate if the related asset(s) are exiting the bounds a[Zone](../Zone/index.md)specified in this condition.

## ExpectedDistance

Operator: True when the expected distance of the child condition meets this conditions value in km.

## ExpectedDuration

Operator: True when the expected duration of the child condition meets this conditions value in seconds.

## Fault

Data: Evaluate the condition against active[FaultData](../FaultData/index.md). Include a child diagnostic condition with related fault[Diagnostic](../Diagnostic/index.md)or NoDiagnostic to detect any[FaultData](../FaultData/index.md).

## FilterStatusDataByDiagnostic

Data: Evaluate the condition against[StatusData](../StatusData/index.md)related to a particular[Diagnostic](../Diagnostic/index.md). This condition will have the Diagnostic property populated and is used in conjunction with (as child of) an operator (IsValueMoreThan, IsValueLessThan, IsValueEqualTo, AnyData).

## Group

Operator : Condition applies to a fine grained[Group](../../../../index.md#Group)under the[Rule](../Rule/index.md)'s[Group](../../../../index.md#Group)hierarchy. This is used to separate conditions in a single rule where different groups require different conditions. For example group "Heavy Truck" has a lower harsh braking value than group "Passenger Car" with those conditions "Or"ed together in the same rule.

## Ignition

Ignition Operator: Evaluate against the asset(s) ignition value. Ignition conditions can have the value of 0 (Off) or 1 (On).

## InsideArea

Zone Operator: Evaluate if related the asset(s) are inside the[Zone](../Zone/index.md)specified by this condition.

## InvertResult

Operator: Invert the results of the child condition(s).

## IsDriving

Data: Is the asset driving. Extract a sequence of values of +1 (at start of driving), -1 (at beginning of stoppage), 0 (state unknown: usually occurs at start and the end of available span of the[LogRecord](../LogRecord/index.md)(s)).

## IsValueEqualTo

Operator: The result of the child condition is equal to value of this condition.

## IsValueLessThan

Operator: The result of the child condition is less than value of this condition.

## IsValueLessThanPercent

Operator: The result of the child condition is less than a percentage of the value of this condition.

## IsValueMoreThan

Operator: The result of the child condition is greater than value of this condition.

## IsValueMoreThanPercent

Operator: The result of the child condition is greater than a percentage of the value of this condition.

## IsValueThreshold

Operator: The result of the child condition is plus/minus the value of this condition.

## NoDVIRCheck

Data: No Pre or Post DVIR check is performed between working days.

## NoPostDVIRCheck

Data: No Pre or Post DVIR check is performed between working days.

## NoPreDVIRCheck

Data: No Pre or Post DVIR check is performed between working days.

## Or

Operator: Condition for "Or" operations. "Or" conditions must have two or more children that will act as the operands in the equation.

## OutsideArea

Zone Operator: Evaluate if the related asset(s) are outside the[Zone](../Zone/index.md)specified in this condition.

## RuleWorkHours

Work Hours Operator: Occurs during the[WorkTime](../WorkTime/index.md)assigned to this condition.

## Speed

Data: The speed of the asset in km/h. Compare against this value using an operator. Example: IsValueMoreThan(value) - child of Speed condition.

## SpeedLimit

Data: The posted road speed of the road the asset is located on in km/h. Compare against this value using an operator and comparing to speed.

## SpeedLimitAsMeasurement

Data: The posted road speed of the road the asset is located on in km/h. Used as measurement and filtered by its parent filters.

## SpeedLimitCommercial

Data: The posted road speed of the road the asset is located on in km/h. Compare against this value using an operator and comparing to speed, uses commercial speed data only.

## SpeedLimitCommercialExcludingEstimates

Data: The posted road speed of the road the asset is located on in km/h. Compare against this value using an operator and comparing to speed, uses commercial speed data only; excludes estimate speed values.

## SpeedLimitCommunity

Data: The posted road speed of the road the asset is located on in km/h. Compare against this value using an operator and comparing to speed, uses community speed data only.

## SpeedLimitCommunityExcludingEstimates

Data: The posted road speed of the road the asset is located on in km/h. Compare against this value using an operator and comparing to speed, uses community speed data only; excludes estimate speed values.

## SpeedLimitExcludingEstimates

Data: The posted road speed of the road the asset is located on in km/h. Compare against this value using an operator and comparing to speed; excludes estimate speed values.

## Stop

Data: Evaluate against the related asset(s) trip stop value.

## TripDistance

Data: The trip distance of the asset in km. Compare against this value using an operator. Example: DistanceLongerThan(value) - child of TripDistance condition.

## TripDuration

Data: The trip duration of the asset in seconds. Compare against this value using an operator. Example: DurationLongerThan(value) - child of TripDuration condition.

## ZoneStop

Zone Operator: Evaluate if the related asset(s) are stopped inside the[Zone](../Zone/index.md)specified in this condition.