**Introduction**

Submits a request to terminate a billing plan for the provided device.

**Parameters**

## apiKey

The active Api Key.

## comments

A comment to add to the termination record.

## isImei

Indicates whether the provided serial number is an IMEI. If true, the serial number is an IMEI. If False or not specified, the serial number is a Geotab device serial number.

## reasonId

ID of the[ApiDeviceContractRequestReason](../../objects/ApiDeviceContractRequestReason/index.md)that the plan is being terminated. Call[GetTerminationReasons](../GetTerminationReasons/index.md)for a list of possible reasons.

## serialNo

A Geotab GO Device serial number.

## sessionId

The active session ID.

## sharedDatabase

The name of the shared database you want the data sharing to be terminated.

**Return value**

**Code samples**