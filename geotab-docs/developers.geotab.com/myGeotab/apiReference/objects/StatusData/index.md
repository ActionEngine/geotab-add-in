**Introduction**

A record that represents an engine status record from the engine system of the specific[Device](../Device/index.md).

**Properties**

## Data

The recorded value of the diagnostic parameter.

## DateTime

The date and time of the logged event.

## Device

The StatusData for the[Device](../Device/index.md)specified.

## Diagnostic

The[Diagnostic](../Diagnostic/index.md)for the[Device](../Device/index.md)specified.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1000 Get requests per 1m. | 1000 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 250 Add requests per 1m. | 250 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Pagination**

## Results limit

50000

## Supported sort

[SortBy Date](../SortByDate/index.md) sorts by the StatusData.DateTime property.

[SortBy Version](../SortByVersion/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |