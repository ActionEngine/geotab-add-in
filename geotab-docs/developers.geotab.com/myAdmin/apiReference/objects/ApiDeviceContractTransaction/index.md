**Introduction**

Stores device billing information. Extends[ApiNameEntity](../ApiNameEntity/index.md).

**Properties**

## AccountNo

The assigned[ApiAccount](../ApiAccount/index.md)account number.

## AssignedPurchaseOrderNo

The assigned purchase order number, where applicable.

## CurrencyCode

The applicable currency code

## DatabaseName

The Latest Device Database Name.

## EndDate

The effective end date of the device contract, where applicable.

## Id

The database ID of this record.

## PeriodFrom

The effective start date of the billing period.

## PeriodTo

The effective end date of the billing period.

## Quantity

The billing period for the device, in days. This property is deprecated. Please use QuantityInDays for more accurate results.

## QuantityFraction

The fraction of the billing period where the device was billing (eg. for a device that was active for an entire month, this value will be 1; for a device that was active for half a month, this value would be 0.5).

## QuantityInDays

The billing period for the device, in days.

## RatePlanName

The Rate Plan info of the billing record.

## Reference

The assigned reseller reference info, where applicable.

## Region

The region where the device was primarily domiciled for the billing period.

## SerialNo

The assigned[ApiGeotabDevice](../ApiGeotabDevice/index.md)serial number.

## SimCardNo

The assigned SIM/IMEI number, where applicable.

## StartDate

The effective start date of the device contract.

## UserCompany

The company associated with the user for this transaction.

## UserContact

The assigned[ApiUserContact](../ApiUserContact/index.md)name, where applicable.

## UserContactId

The assigned[ApiUserContact](../ApiUserContact/index.md) Id, where applicable.

## ValueLocal

The billing fee for the device, for the period, in local currency.

## ValueUsd

The billing fee for the device, for the period, in US Dollars.