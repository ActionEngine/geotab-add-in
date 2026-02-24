**Introduction**

Adds a new[Entity](../../objects/Entity/index.md)to the database. This method is used to add the different entities to the database, for example[Device](../../objects/Device/index.md),[User](../../objects/User/index.md)or[Zone](../../objects/Zone/index.md). In addition to the credentials, the method will require a minimum of two parameters - the type of entity that is being added (typeName) and the entity itself. In most cases, the entity being added will need to be fully constructed. In other words, all its properties need to be defined. These requirements are defined in each of the entity definitions below.

**Parameters**

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## entity

The new[Entity](../../objects/Entity/index.md)to add to the database.

## typeName

Identifies the type of entity that is being passed to the next parameter. For example,[Device](../../objects/Device/index.md).

**Return value**

The[Id](../../objects/Id/index.md)for the newly added[Entity](../../objects/Entity/index.md).

**Code samples**