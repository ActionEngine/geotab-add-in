**Introduction**

Represents an Iox Add-On (like modem or navigation device) that is attached to a GO unit. Each Iox Add-On is assigned a channel - which is the serial port number that it typically communicates with.

**Properties**

## Channel

The channel on which the Add-On is attached to the GO unit. This is typically just a serial port. 0 means the Add-On is not attached.

## DateTime

The DateTime this IoxAddOn was assigned it's[Channel](https://developers.geotab.com/myGeotab/apiReference/objects/Channel/).

## Device

The[Device](../Device/index.md)this IoxAddOn is connected to.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Type

The unique identifier for this Iox Add-On type. Iox Add-On types are assigned by Geotab. See[KnownIoxAddOnType](../KnownIoxAddOnType/index.md).

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 500 Get requests per 1m. | 500 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |