**Introduction**

Contains information related to a device's contract.

**Properties**

## Account

The[ApiAccount](../ApiAccount/index.md)the the device contract belongs to.

## ActiveDevicePlan

The active[ApiDevicePlan](../ApiDevicePlan/index.md).

## ActiveRatePlans

List of[ApiDeviceContractRatePlan](../ApiDeviceContractRatePlan/index.md)active on this device contract.

## ActiveTrackingDisabled

True if Active Tracking has been disallowed for this device, false otherwise.

## AssignedPurchaseOrderNo

Purchase order number assigned to this device contract.

## BillingStartDate

Returns the date that the device was auto-activated, installed, or transferred from another Partner. ✱ NOTE: For devices shipped prior to September 9, 2023, this property will always be NULL.

## Comments

Comments related to this device contract.

## ConnectedDevice

The Contracts'[ApiConnectedDevice](../ApiConnectedDevice/index.md)

## ContractEndDate

This date reflects the end of bundle's contract term.

## ContractStartDate

This date reflects the start of a bundle's contract term.

## Device

The[ApiGeotabDevice](../ApiGeotabDevice/index.md)that belongs to this contract.

## EndDate

Contract end date.

## FirstDeviceActivationDate

The date in UTC that the device communicated for the first time.

## GroupId

ID to allow resellers to group their devices.

## Id

Database Id of the device contract.

## IsAutoActivated

Returns True if the device was automatically activated by Geotab, False if the device was activated by installation, and NULL if the device has been shipped, but has not been installed, or auto-activated. ✱ NOTE: For devices shipped prior to September 9, 2023, this property will always be NULL.

## IsTerminated

True if the device has been terminated, false otherwise.

## IsUnactivated

True if the device has never activated, false otherwise.

## LatestDeviceDatabase

The most recent[ApiDeviceDatabase](../ApiDeviceDatabase/index.md)the device was assigned to.

## ProductCode

Product code of the device associated with this contract.

## PromoCode

The active PromoCode tied to the device if applicable.

## SimCardNumber

Sim card number of the device

## StartDate

Contract start date.

## TerminatedDate

The date that the device was terminated or null if not terminated.

## UserCompany

The company associated with the user for this contract.

## UserContact

The[ApiUserContact](../ApiUserContact/index.md)associated with this contract.

## WarrantyStatus

Status of the warranty.