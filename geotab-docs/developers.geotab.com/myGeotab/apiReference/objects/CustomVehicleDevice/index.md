**Introduction**

A custom telematics automotive vehicle device that is used in MyGeotab. This is used for extensibility and is based on the[CustomDevice](../CustomDevice/index.md)object.

**Properties**

## ActiveFrom

The date the device is active from. Default [MinDate].

## ActiveTo

The date that the device is active to. Default [MaxDate].

## AutoGroups

## AutoHos

A toggle that represents automatic generation of[DutyStatusLog](../DutyStatusLog/index.md)s for a[Device](../Device/index.md). Default [null].

## Comment

Free text field where any user information can be stored and referenced for this entity.

## DeviceFlags

The device features which have been enabled whether the feature is in use (e.g. HOS, Iridium).

## DeviceType

Specifies the GO or Custom[DeviceType](../DeviceType/index.md).

## EngineHourOffset

The offset to be applied engine hours data reported by the engine computer. Default [0].

## FuelTankCapacity

The capacity of all usable fuel tanks in litres. Default [null].

## Groups

The list of[Group](../Group/index.md)(s) the device belongs to.

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## LicensePlate

The vehicle license plate details of the vehicle associated with the device. Maximum length [50] Default [""].

## LicenseState

The state or province of the vehicle associated with the device. Maximum length [50] Default [""].

## Name

The name of this entity which identifies it and is used when displaying this entity. Maximum length [50].

## OdometerFactor

A value used to correct the odometer value received from the engine. Default [1].

## OdometerOffset

The offset to be applied odometer reported by the engine computer. Default [0].

## ProductId

The product id. Each device is assigned a unique hardware product id.

## SerialNumber

The Serial Number of the device. Maximum length [12].

## TimeZoneId

The IANA Timezone Id of the device used to determine local work times. This is typically the "home location" of the device. Default ["UTC"].

## VehicleIdentificationNumber

The Vehicle Identification Number (VIN) of the vehicle associated with the device. Maximum length [50] Default [""].

## Version

The version of the entity.

## WorkTime

The[WorkTime](../WorkTime/index.md)rules to apply to the device. Default [WorkTimeStandardHours].

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |