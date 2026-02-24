**Introduction**

Information about timing of a[Driver](../Driver/index.md)change.

**Properties**

## DateTime

The date and time of the driver change. Note: When adding a DriverChange through API, the DateTime must NOT be in the future.

## Device

The[Device](../Device/index.md)that had the driver change.

## Driver

The[Driver](../Driver/index.md)associated with the change.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Type

The[DriverChangeType](../DriverChangeType/index.md).

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1000 Get requests per 1m. | 1000 | 1m | Active |
| Add | Limit of 250 Add requests per 1m. | 250 | 1m | Active |
| Remove | Limit of 250 Remove requests per 1m. | 250 | 1m | Active |
| GetCountOf | Limit of 250 GetCountOf requests per 1m. | 250 | 1m | Active |
| GetFeed | Limit of 250 GetFeed requests per 1m. | 250 | 1m | Active |

**Pagination**

## Results limit

50000

## Supported sort

[SortBy Date](../SortByDate/index.md) sorts by the DriverChange.DateTime property.

[SortBy Version](../SortByVersion/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |