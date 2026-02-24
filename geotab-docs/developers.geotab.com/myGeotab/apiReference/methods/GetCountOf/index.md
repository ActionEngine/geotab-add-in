**Introduction**

Gets the count of the specified[Entity](../../objects/Entity/index.md)type from the database. Entities that are currently inactive (the Entity's ActiveTo date is before the current time) are counted as well.

**Parameters**

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## typeName

Identifies the type of entity that is being passed to the next parameter. For example,[Device](../../objects/Device/index.md).

**Return value**

The number of entities in the database.

**Code samples**