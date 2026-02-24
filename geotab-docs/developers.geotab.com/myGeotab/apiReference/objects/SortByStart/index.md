**Introduction**

Implementation of ISort for sorting by the start date field in[Entity](../Entity/index.md)s.

**Properties**

## LastId

The lastId. This can be null for the initial page request. For subsequent pages, when sorting by start, lastId should be populated with the ID of the last record returned.

## Offset

The offset. Used in paging to indicate where the last page left off, the value can be null for the first page then becomes the last known value of the "start" property for subsequent pages.

## SortBy

The field to sort by.

## SortDirection

The sort direction. Default is[Asc](../../../../index.md#Asc).