**Introduction**

Gets the[Entity](../../objects/Entity/index.md)(s) for the given entityType. This method can be used in various ways to return all, one or some specific set of data for the[Entity](../../objects/Entity/index.md)(s).

**Parameters**

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## propertySelector

The[PropertySelector](../../objects/PropertySelector/index.md)used to limit the[Entity](../../objects/Entity/index.md)properties retrieved from the server. >> Beta: not supported by all types.

## resultsLimit

Limit the number of results that can be returned to this search.

## search

If null, all[Entity](../../objects/Entity/index.md)(s) are returned. Pass a Search object (ex.[DeviceSearch](../../objects/DeviceSearch/index.md)) with the Id property set if you need to return a specific entity. Pass a Search with properties set that needs to be searched on. For example, setting the Name property for a[DeviceSearch](../../objects/DeviceSearch/index.md)object will return only devices that match the name provided.

## sort

Sort the result based on the sorting details. Refer to Pagination and Sorting sections in Guides > Concepts for more details. >> Beta: not supported by all types.

## typeName

Identifies the type of entity that is being passed to the next parameter. For example,[Device](../../objects/Device/index.md).

**Return value**

A[enumerable](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.iasyncenumerable`1)of[Entity](../../objects/Entity/index.md)(s).

**Code samples**