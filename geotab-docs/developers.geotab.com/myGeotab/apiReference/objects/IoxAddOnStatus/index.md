**Introduction**

Represents the status of an IoxAddOn that is attached to a GO unit.

**Properties**

## Delivered

Date/time the message was delivered.

## Device

The[Device](../Device/index.md)this IoxAddOn is connected to.

## DeviceConnectionStatus

The device connection status (Active = 0, Inactive = 4, Disconnected = 1).

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## LastCommunicated

The date/time of last IOX/Passthrough communication for the device.

## QueueSize

The queue size of pending messages.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |