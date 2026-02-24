**Introduction**

A ShipmentLog is a record of shipment transported by a specified vehicle for a duration of time.

**Properties**

## ActiveFrom

The date the shipment was started. Default [UtcNow].

## ActiveTo

The date the shipment was ended. Default [MaxDate].

## Commodity

The commodity shipped. Maximum length [255] Default [""].

## DateTime

The date and time the log was created.

## Device

The[Device](../Device/index.md)associated with this log.

## DocumentNumber

The identifier of the shipment document. Default [""].

## Driver

The[User](../User/index.md)who created this log.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## ShipperName

The name of the shipper. Default [""].

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 350 Get requests per 1m. | 350 | 1m | Active |
| Set | Limit of 350 Set requests per 1m. | 350 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Pagination**

## Results limit

50000

## Supported sort

[SortBy Date](../SortByDate/index.md) sorts by the ShipmentLog.DateTime property.

[SortBy Version](../SortByVersion/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |