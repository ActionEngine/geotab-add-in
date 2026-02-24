**Introduction**

Submits a request to change the billing plan ([ApiDevicePlan](../../objects/ApiDevicePlan/index.md)) for the provided device.This method does not support the Terminate plan (See[TerminateDeviceBilling](../TerminateDeviceBilling/index.md)for device terminations). Note: When using the sandbox environment, this method will not affect live device configuration, but the billing changes will be saved in the sandbox environment.

**Parameters**

## apiKey

The active Api Key.

## devicePlanId

The new device plan ID. See[GetDevicePlans](../GetDevicePlans/index.md)to obtain a list of valid plans.

## isImei

Indicates whether the provided serial number is an IMEI. If true, the serial number is an IMEI. If False or not specified, the serial number is a Geotab device serial number.

## promoCode

An optional promo code, when applicable.

## serialNo

A Geotab GO Device serial number.

## sessionId

The active session ID.

## sharedDatabase

The name of the shared database.

**Return value**

**Remarks**

This method does not support the Terminate plan (See <see cref="M:MyAdminAPI.MyAdminApiStore.TerminateDeviceBilling(System.Guid,System.Guid,System.String,System.Int32,System.String,System.Boolean)"/> for device terminations). Note: When using the sandbox environment, this method will not affect live device configuration, but the billing changes will be saved in the sandbox environment.

**Code samples**