**Introduction**

A TrailerAttachment is a record of the attachment of a[Trailer](../Trailer/index.md)to a[Device](../Device/index.md)over a period of time.

**Properties**

## ActiveFrom

The date and time the[Trailer](../Trailer/index.md)was attached. Default [UtcNow].

## ActiveTo

The date and time the[Trailer](../Trailer/index.md)was detached. Default [MaxDate].

## Device

The[Device](../Device/index.md)which the[Trailer](../Trailer/index.md)is associated with.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Trailer

The attached[Trailer](../Trailer/index.md).

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 300 Get requests per 1m. | 300 | 1m | Active |
| Set | Limit of 150 Set requests per 1m. | 150 | 1m | Active |
| Add | Limit of 150 Add requests per 1m. | 150 | 1m | Active |
| Remove | Limit of 150 Remove requests per 1m. | 150 | 1m | Active |
| GetCountOf | Limit of 150 GetCountOf requests per 1m. | 150 | 1m | Active |
| GetFeed | Limit of 150 GetFeed requests per 1m. | 150 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |