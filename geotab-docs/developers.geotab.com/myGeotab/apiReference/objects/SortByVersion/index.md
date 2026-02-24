**Introduction**

Implementation of ISort for sorting by the version field in[Entity](../Entity/index.md)s.

**Properties**

## LastId

The lastId. Not required when sorting by version.

## Offset

The offset. Used in paging to indicate where the last page left off, the value can be null for the first page then becomes the last known value of the "version" property for subsequent pages.

## SortBy

The field to sort by.

## SortDirection

The sort direction. Default is[Asc](../../../../index.md#Asc).