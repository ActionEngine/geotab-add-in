**Introduction**

The Geotab GO7 device. Additional properties can be seen in[GoCurveAuxiliary](../GoCurveAuxiliary/index.md).

**Properties**

## AccelerationWarningThreshold

The acceleration warning accelerometer threshold (y axis) value for the vehicle. A positive value that when exceeded will trigger device beeping. Threshold value to mS2 conversion (threshold * 18 = milli-g / 1000 = g / 1.0197162 = mS2). Default [22].

## AccelerometerThresholdWarningFactor

The accelerometer threshold warning factor value for this vehicle. Default [0].

## ActiveFrom

The date that the device is active from. Default [MinDate].

## ActiveTo

The date that the device is active to. Default [MaxDate].

## AutoGroups

The messaging status[Group](../Group/index.md)(s). Default [Empty].

## AutoHos

A toggle that represents automatic generation of[DutyStatusLog](../DutyStatusLog/index.md)s for a[Device](../Device/index.md). Default [null].

## AuxWarningSpeed

An array of the auxiliary warning speeds for the vehicle. The auxiliary is triggered when the speed is greater than or equal to this value. Maximum length [8] Default [0,0,0,0,0,0,0,0].

## BrakingWarningThreshold

The braking warning accelerometer threshold (y axis) value for the vehicle. A negative value that when exceeded will trigger device beeping. Threshold value to mS2 conversion (threshold * 18 = milli-g / 1000 = g / 1.0197162 = mS2). Default [-34].

## Comment

Free text field where any user information can be stored and referenced for this entity.

## CorneringWarningThreshold

The cornering warning threshold (x axis) value for the vehicle. A positive value that when exceeded will trigger device beeping (the additive inverse is automatically applied: 26/-26). Threshold value to mS2 conversion (threshold * 18 = milli-g / 1000 = g / 1.0197162 = mS2). Default [26].

## CustomParameters

The set of CustomParameter(s) associated with this device. Custom parameters allow the activation of special features — limited to custom and beta firmware. Custom parameters are issued only when necessary. Default [Empty].

## DeviceFlags

The device features which have been enabled whether the feature is in use (e.g. HOS, Iridium).

## DeviceType

Specifies the GO or Custom[DeviceType](../DeviceType/index.md).

## DisableBuzzer

Master toggle to disable the device buzzer. When set to [true], the device will not provide driver feedback of any kind. Default [false].

## EnableAuxWarning

Toggle to enable auxiliary warnings. Maximum length [8] Default [false,false,false,false,false,false,false,false].

## EnableBeepOnDangerousDriving

Toggle to enable beeping when any of the acceleration thresholds are exceeded by device accelerometer readings. Default [false].

## EnableBeepOnIdle

Toggle to enable beeping when the vehicle idles for more than IdleMinutes. Default [false].

## EnableBeepOnRpm

Toggle to enable beeping when the vehicle's RPM exceeds the 'RpmValue'. Default [false].

## EnableControlExternalRelay

Toggle to enable control external relay value for the vehicle. Default [false].

## EnableMustReprogram

Flag to force the parameters to be updated between the store and a go device, the store will be updated with the parameter version of the go device +1.

## EnableSpeedWarning

Toggle to enable speed warning value for the vehicle. When enabled [true], only beep briefly (instead of continuously), when 'SpeedingOn' value is exceeded. 'IsSpeedIndicator' must also be enabled. Default [false].

## EngineHourOffset

The offset to be applied engine hours data reported by the engine computer. Default [0].

## EnsureHotStart

A value indicating whether to wake up the GPS while the vehicle is parked: this will allow for a faster GPS latch when the vehicle begins its trip. Note: This will drain the vehicle's battery at a faster rate and should not be used with newer devices. Default [false].

## ExternalDeviceShutDownDelay

The option which controls how long any attached external devices (Garmin, Iridium, HOS, RFID, RS232, CAN, and USB) are kept on after the vehicle is turned off in minutes. Default [0].

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

## ImmobilizeArming

With[ImmobilizeUnit](https://developers.geotab.com/myGeotab/apiReference/objects/ImmobilizeUnit/)being true, it is used to define the delay before the driver identification reminder is sent out if the driver key has not been not swiped. The maximum value of this property is 255. When it is less or equal to 180, it indicates the number of seconds of the delay. When it is greater than 180, the delay increases 30 seconds for every increment of one of this property. For example, 180 indicates 180 seconds, 181 indicates 210 seconds, and 182 indicates 240 seconds. Maximum [255] Default [30].

## ImmobilizeUnit

A value mainly used for enable or disable driver identification reminder. If it is used in conjunction with vehicle relay circuits, it can force the driver to swipe the driver key before starting the vehicle. Default [false].

## IsActiveTrackingEnabled

Toggle to enable active tracking on the device. enables Active Tracking which triggers the device to transmit data more frequently. This allows for continuously up-to-date vehicle positions animated on the live map. It also enables live server-side driver alerts. Default [false].

## IsAuxInverted

An array of[Boolean](https://docs.microsoft.com/en-us/dotnet/api/system.boolean)(s) indicating if a corresponding Aux signal should be inverted on importing the device data. Maximum length [8] Default [false,false,false,false,false,false,false,false].

## IsDriverSeatbeltWarningOn

Value which toggles beeping if an unbuckled seat belt is detected. This will only work if the device is able to obtain seat belt information from the vehicle. Default [false].

## IsIoxConnectionEnabled

Value which toggles device IOX USB connection. Default [true].

## IsPassengerSeatbeltWarningOn

Value which toggles monitoring both passenger and driver unbuckled seat belt, otherwise only the driver is monitored. Default [false].

## IsReverseDetectOn

Value which toggles device beeping when the vehicle is reversing. Default [false].

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

The minimum allowable value for[MaxSecondsBetweenLogs](https://developers.geotab.com/myGeotab/apiReference/objects/MaxSecondsBetweenLogs/). For[GoDevice](../GoDevice/index.md)s, this is the same as the default value of 200.0f.

## Name

The name of this entity which identifies it and is used when displaying this entity. Maximum length [50].

## OdometerFactor

A[Single](https://docs.microsoft.com/en-us/dotnet/api/system.single)used to correct the odometer value received from the engine. Default [1].

## OdometerOffset

The offset to be applied odometer reported by the engine computer. Default [0].

## ParameterVersion

The parameter version that is stored in MyGeotab. The parameter version should be increased by one when the parameters have been modified and need to be synced with the physical device. Default [2].

## ParameterVersionOnDevice

The parameter version that is on the device. Can be used to track the parameter version currently on the device by comparing to ParameterVersion. Default [0].

## ProductId

The product id. Each device is assigned a unique hardware product id.

## RpmValue

The RPM value that when exceeded triggers device beeping. Default [3500].

## SeatbeltWarningSpeed

The value in km/h that below will not trigger 'Seat belt Warning'. Default [10].

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

| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |