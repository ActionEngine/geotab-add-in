**Introduction**

The GO Anywhere Lite device. Additional properties can be seen in[XDevice](../XDevice/index.md).

**Properties**

## AccelerationThreshold

Value for the Accelerometer threshold, in mg. Default [2000].

## ActiveFrom

The date that the device is active from. Default [MinDate].

## ActiveTo

The date that the device is active to. Default [MaxDate].

## AssetRecoveryInterval

The value for the Asset Recovery Interval in seconds.

## AssetRecoveryModeEnabled

Value for indicating if the Go Anywhere device high frequency update mode is enabled. Default [false]. To activate Asset Recovery Mode, the following parameter must be set: CheckInOnTripEnabled = false. To deactivate Asset Recovery Mode, the following parameter must be set: CheckInOnTripEnabled = true.

## AutoGroups

The messaging status[Group](../Group/index.md)(s). Default [Empty].

## BistStartupDelay

Value for the Built In Self Test startup delay in seconds. Default [60].

## CheckInOnTripEnabled

Value for indicating if the Go Anywhere device movement alert or trip start alert is enabled. Default [false].

## Comment

Free text field where any user information can be stored and referenced for this entity.

## CommunicationFrequency

Value for the Go Anywhere device communication rate in minutes. Default [1440].

## CommunicationRetryMax

Maximum number of communication retries. Default [5].

## CustomParameters

The set of CustomParameter(s) associated with this device. Custom parameters allow the activation of special features — limited to custom and beta firmware. Custom parameters are issued only when necessary. Default [Empty].

## DeviceFlags

The device features which have been enabled whether the feature is in use (e.g. HOS, Iridium).

## DeviceFotaDisabled

The value for Disable FOTA updates. Default [false].

## DeviceType

Specifies the GO or Custom[DeviceType](../DeviceType/index.md).

## EnableModemFota

The value for Enable modem FOTA updates. Default [true].

## EnableMustReprogram

Flag to force the parameters to be updated between the store and a go device, the store will be updated with the parameter version of the go device +1.

## EnsureHotStart

A value indicating whether to wake up the GPS while the vehicle is parked: this will allow for a faster GPS latch when the vehicle begins its trip. Note: This will drain the vehicle's battery at a faster rate and should not be used with newer devices. Default [false].

## ExpectedParameterVersionOnDeviceToSyncRecovery

## GnssAidingDataDisabled

The value for Disable GNSS aiding data. Default [false].

## GnssFixCount

Value for the Number of GNSS fixes to confirm movement. Default [2].

## GnssFixInterval

Value for the Movement GNSS fix interval in seconds. Default [900].

## GnssMinDistance

Value for the Minimum distance traveled to confirm movement, in meters. Default [200].

## GpsOffDelay

The GPS off delay in minutes. When enabled this allows the device to keep the GPS on for a period after the vehicle has been turned off. Normally, the GPS turns off immediately. Keeping the GPS on can improve tracking on older devices when many stops are made. Default [0].

## Groups

The list of[Group](../Group/index.md)(s) the device belongs to.

## GsmRssiMin

Modem GSM Received Signal Strength Indicator (127 = disabled). Default [-90].

## GsmSinrMin

Modem GSM Signal to Interference & Noise Ratio (127 = disabled). Default [127].

## HfuExpirationDateTimeInSeconds

The value for the High Frequency Update expiration in seconds since Jan 1st 2002 (Gateway epoch).

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## LicensePlate

The vehicle license plate details of the vehicle associated with the device. Maximum length [50] Default [""].

## LicenseState

The state or province of the vehicle associated with the device. Maximum length [50] Default [""].

## LteRssiMin

Modem LTE Received Signal Strength Indicator (127 = disabled). Default [-95].

## LteSinrMin

Modem LTE Signal to Interference & Noise Ratio (127 = disabled). Default [127].

## Major

The device major firmware version. Newer versions have more functionality. Live device firmware versions are managed automatically. Default [0].

## MaxTemperature

Value for the Shipping maximum temperature in degree Celsius. Default [80].

## MinBatteryVoltage

Value for the Shipping minimum battery voltage in milli-volts. Default [4000].

## Minor

The device minor firmware version. Newer versions have more functionality. Live device firmware versions are managed automatically. Default [0].

## MinSecondsBetweenLogs

The minimum allowable value for[MaxSecondsBetweenLogs](https://developers.geotab.com/myGeotab/apiReference/objects/MaxSecondsBetweenLogs/). For[XDevice](../XDevice/index.md)s, this is the same as the default value of 200.0f.

## ModemMaxConnectionTime

Maximum modem connection time in seconds. Default [300].

## ModemMinVoltage

Minimum battery voltage required to allow modem communication, in milli-volts. Default [4000].

## MovementDetectionDistanceThreshold

Movement detection distance, in cm. Default [70].

## MovementHealthCheckInterval

Value for the Movement health check interval in seconds. Default [86400].

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

## ShippingCommunicationInterval

Value for the Shipping Communication interval in seconds (-1 is never). Default [-1].

## ShippingGwTimeout

Value for the Shipping gateway connection timeout in seconds. Default [60].

## ShippingHealthCheckInterval

Value for the Shipping Health check interval in seconds (-1 is never). Default [-1].

## ShippingNetworkTimeout

Value for the Shipping network registration timeout value in seconds. Default [120].

## SleepGwTimeout

Value for the Sleep gateway connection timeout in seconds. Default [60].

## SleepHealthCheckIntervalReduced

Value for the Sleep health check interval in seconds if alarm is active. Default [86400].

## SleepNetworkTimeout

Value for the Sleep Network registration timeout value in seconds. Default [120].

## SpeedDetectionMin

Accelerometer sustained speed minimum for impact detection, in m/s. Default [0].

## SpeedThreshold

GNSS reported speed in m/s used to confirm movement, start of trip. Default [4].

## TimeZoneId

The IANA Timezone Id of the device used to determine local work times. This is typically the "home location" of the device. Default ["UTC"].

## VehicleIdentificationNumber

The Vehicle Identification Number (VIN) of the vehicle associated with the device. Maximum length [50] Default [""].

## Version

The version of the entity.

## VoltageLoggingDisabled

The value for Disable battery voltage logging. Default [false].

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