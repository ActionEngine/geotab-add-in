**Introduction**

A Device represents the physical tracking device installed in the vehicle. A device and vehicle is typically synonymous since the GO tracking device is installed in a vehicle. In the case where there is no device; this is represented by "NoDeviceId". The device types that are supported are:
- [GoAnywhere](../GoAnywhere/index.md)
- [Go9](../Go9/index.md)
- [Go8](../Go8/index.md)
- [Go7](../Go7/index.md)
- [Go6](../Go6/index.md)
- [Go5](../Go5/index.md)
- [CustomDevice](../CustomDevice/index.md)

**Properties**

## ActiveFrom

The date the device is active from. Default [MinDate].

## ActiveTo

The date that the device is active to. Default [MaxDate].

## Comment

Free text field where any user information can be stored and referenced for this entity.

## DeviceFlags

The device features which have been enabled whether the feature is in use (e.g. HOS, Iridium).

## DeviceType

Specifies the GO or Custom[DeviceType](../DeviceType/index.md).

## Groups

The list of[Group](../Group/index.md)(s) the device belongs to.

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## Name

The name of this entity which identifies it and is used when displaying this entity. Maximum length [50].

## ProductId

The product id. Each device is assigned a unique hardware product id.

## SerialNumber

The Serial Number of the device. Maximum length [12].

## TimeZoneId

The IANA Timezone Id of the device used to determine local work times. This is typically the "home location" of the device. Default ["UTC"].

## Version

The version of the entity.

## WorkTime

The[WorkTime](../WorkTime/index.md)rules to apply to the device. Default [WorkTimeStandardHours].

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 650 Get requests per 1m. | 650 | 1m | Active |
| Set | Limit of 250 Set requests per 1m. | 250 | 1m | Active |
| Add | Limit of 250 Add requests per 1m. | 250 | 1m | Active |
| Remove | Limit of 250 Remove requests per 1m. | 250 | 1m | Active |
| GetCountOf | Limit of 250 GetCountOf requests per 1m. | 250 | 1m | Active |
| GetFeed | Limit of 250 GetFeed requests per 1m. | 250 | 1m | Active |

**Pagination**

## Results limit

5000

## Supported sort

[SortBy Id](../SortById/index.md)

[SortBy Name](../SortByName/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |