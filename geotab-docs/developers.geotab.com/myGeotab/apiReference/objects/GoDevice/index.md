**Introduction**

The base device for all Geotab GO products. Additional properties can be seen in[Device](../Device/index.md).

**Properties**

## ActiveFrom

The date that the device is active from. Default [MinDate].

## ActiveTo

The date that the device is active to. Default [MaxDate].

## AutoGroups

The messaging status[Group](../Group/index.md)(s). Default [Empty].

## AutoHos

A toggle that represents automatic generation of[DutyStatusLog](../DutyStatusLog/index.md)s for a[Device](../Device/index.md). Default [null].

## Comment

Free text field where any user information can be stored and referenced for this entity.

## CustomParameters

The set of CustomParameter(s) associated with this device. Custom parameters allow the activation of special features — limited to custom and beta firmware. Custom parameters are issued only when necessary. Default [Empty].

## DeviceFlags

The device features which have been enabled whether the feature is in use (e.g. HOS, Iridium).

## DeviceType

Specifies the GO or Custom[DeviceType](../DeviceType/index.md).

## DisableBuzzer

Master toggle to disable the device buzzer. When set to [true], the device will not provide driver feedback of any kind. Default [false].

## EnableBeepOnIdle

Toggle to enable beeping when the vehicle idles for more than IdleMinutes. Default [false].

## EnableMustReprogram

Flag to force the parameters to be updated between the store and a go device, the store will be updated with the parameter version of the go device +1.

## EnableSpeedWarning

Toggle to enable speed warning value for the vehicle. When enabled [true], only beep briefly (instead of continuously), when 'SpeedingOn' value is exceeded. 'IsSpeedIndicator' must also be enabled. Default [false].

## EnsureHotStart

A value indicating whether to wake up the GPS while the vehicle is parked: this will allow for a faster GPS latch when the vehicle begins its trip. Note: This will drain the vehicle's battery at a faster rate and should not be used with newer devices. Default [false].

## GoTalkLanguage

The[GoTalkLanguage](../GoTalkLanguage/index.md)of an attached GoTalk. Default [English].

## GpsOffDelay

The GPS off delay in minutes. When enabled this allows the device to keep the GPS on for a period after the vehicle has been turned off. Normally, the GPS turns off immediately. Keeping the GPS on can improve tracking on older devices when many stops are made. Default [0].

## Groups

The list of[Group](../Group/index.md)(s) the device belongs to.

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## IdleMinutes

The number of minutes of allowed idling before device beeping starts. EnableBeepOnIdle must be enabled. Default [3].

## IsSpeedIndicator

A toggle to beep constantly when the vehicle reaches the speed set in 'SpeedingOn', and do not stop until the vehicle slows below the 'SpeedingOff' speed. To only beep briefly (instead of continuously), enable 'EnableSpeedWarning'. Default [false].

## LicensePlate

The vehicle license plate details of the vehicle associated with the device. Maximum length [50] Default [""].

## LicenseState

The state or province of the vehicle associated with the device. Maximum length [50] Default [""].

## Major

The device major firmware version. Newer versions have more functionality. Live device firmware versions are managed automatically. Default [0].

## MinAccidentSpeed

The minimum accident speed in km/h. Default [4].

## Minor

The device minor firmware version. Newer versions have more functionality. Live device firmware versions are managed automatically. Default [0].

## MinSecondsBetweenLogs

The minimum allowable value for[MaxSecondsBetweenLogs](https://developers.geotab.com/myGeotab/apiReference/objects/MaxSecondsBetweenLogs/). For[GoDevice](index.md)s, this is the same as the default value of 200.0f.

## Name

The name of this entity which identifies it and is used when displaying this entity. Maximum length [50].

## ParameterVersion

The parameter version that is stored in MyGeotab. The parameter version should be increased by one when the parameters have been modified and need to be synced with the physical device. Default [2].

## ParameterVersionOnDevice

The parameter version that is on the device. Can be used to track the parameter version currently on the device by comparing to ParameterVersion. Default [0].

## ProductId

The product id. Each device is assigned a unique hardware product id.

## SerialNumber

The Serial Number of the device. Maximum length [12].

## SpeedingOff

The speeding off value in km/h. When 'IsSpeedIndicator' is enabled, once beeping starts, the vehicle must slow down to this speed for the beeping to stop. Default [90].

## SpeedingOn

The speeding on value in km/h. When 'IsSpeedIndicator' is enabled, the device will start beeping when the vehicle exceeds this speed. Default [100].

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

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |