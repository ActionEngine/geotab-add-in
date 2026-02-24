**Introduction**

Permanently removes an[Entity](../../objects/Entity/index.md)and its associated data. The[Entity](../../objects/Entity/index.md)object must have an[Id](../../objects/Id/index.md)field. Remaining fields are optional. Note: the[Entity](../../objects/Entity/index.md)does not function as a filter.

**Parameters**

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## entity

The[Entity](../../objects/Entity/index.md)to be removed.

## typeName

Identifies the type of entity that is being passed to the next parameter. For example,[Device](../../objects/Device/index.md).

**Return value**

A[Task](https://docs.microsoft.com/en-us/dotnet/api/system.threading.tasks.task)representing the asynchronous operation.

**Code samples**