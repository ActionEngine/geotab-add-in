**Introduction**

Provisions a device to an account.Note: This method cannot be called in the sandbox environment and will throw an exception.

**Parameters**

## apiKey

The active API Key.

## erpNo

Account number for new activation.

## hardwareId

Optional parameter with HWID to be used when provisioning.

## productId

Product ID to provision.

## promoCode

Promo Code for third-party device.

## sessionId

The active session ID.

## subPlan

Subscription Plan to provision OEM devices

**Return value**

A[ProvisionResult](../../objects/ProvisionResult/index.md)if provision was successful, null if not.

**Remarks**

Note: This method cannot be called in the sandbox environment and will throw an exception.

**Code samples**