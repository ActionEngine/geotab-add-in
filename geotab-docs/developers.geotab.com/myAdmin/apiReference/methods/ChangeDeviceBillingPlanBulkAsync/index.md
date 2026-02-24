**Introduction**

Submits a request to change the billing plan ([ApiDevicePlan](../../objects/ApiDevicePlan/index.md)) for the provided devices.This method does not support the Terminate plan (See[TerminateDeviceBilling](../TerminateDeviceBilling/index.md)for device terminations). Note: When using the sandbox environment, this method will not affect live device configuration, but the billing changes will be saved in the sandbox environment.

**Parameters**

## apiKey

The active Api Key.

## devicePlanId

The new device plan ID. See[GetDevicePlans](../GetDevicePlans/index.md)to obtain a list of valid plans.

## isImei

Indicates whether the provided serial numbers are IMEIs. If true, the serial numbers are IMEI. If False or not specified, the serial numbers are Geotab device serial numbers.

## promoCode

An optional promo code, when applicable.

## serialNos

Geotab GO Device serial numbers.

## sessionId

The active session ID.

## sharedDatabase

**Return value**

**Remarks**

This method does not support the Terminate plan (See <see cref="M:MyAdminAPI.MyAdminApiStore.TerminateDeviceBilling(System.Guid,System.Guid,System.String,System.Int32,System.String,System.Boolean)"/> for device terminations). Note: When using the sandbox environment, this method will not affect live device configuration, but the billing changes will be saved in the sandbox environment.

**Code samples**