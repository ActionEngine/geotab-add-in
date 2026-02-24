**Introduction**

This is binary data representing anything that can be stored. BinaryData can use this to store images but the data can be any custom data, including custom engine information types. The type of the data is defined by the[BinaryDataType](../BinaryDataType/index.md).

**Properties**

## BinaryType

The[BinaryDataType](../BinaryDataType/index.md).

## Controller

The[Controller](../Controller/index.md)for the[BinaryData](index.md)specified.

## Data

The binary data for the[BinaryData](index.md)object.

## DateTime

The date and time of the logging of the data.

## Device

The[Device](../Device/index.md)on which the binary data was recorded.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 500 Get requests per 1m. | 500 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |