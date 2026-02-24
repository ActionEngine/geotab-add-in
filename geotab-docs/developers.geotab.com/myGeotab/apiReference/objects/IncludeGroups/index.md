**Introduction**

The IncludeGroups enum provides a method of querying for entities relative to the entity's position in the hierarchy of[Group](../Group/index.md)(s). Some entity types (such as[Zone](../Zone/index.md)(s)) have implications to entities in their child groups. For example; on a map, it may be useful to include[Zone](../Zone/index.md)(s) that are above the user's data scope groups. These[Zone](../Zone/index.md)(s) will also apply to vehicles that are at or below the selected[Group](../Group/index.md)(s) of the[Zone](../Zone/index.md).

**Properties**

## Child

Include Children groups in the query results.

## Direct

Directly related groups only in the query results.

## Parent

Include Parent groups in the query results.

## ParentAndChild

Include Parent and Children groups in the query results.