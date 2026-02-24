**Introduction**

Record of log entries containing data for a device's position and speed at a specific date and time.

**Properties**

## DateTime

The date and time the log was recorded.

## Device

The[Device](../Device/index.md)this log belongs to.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Latitude

The latitude of the log record.

## Longitude

The longitude of the log record.

## Speed

The logged speed or an invalid speed (in km/h).

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1000 Get requests per 1m. | 1000 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Pagination**

## Results limit

50000

## Supported sort

[SortBy Id](../SortById/index.md)

[SortBy Date](../SortByDate/index.md) sorts by the LogRecord.DateTime property.

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |