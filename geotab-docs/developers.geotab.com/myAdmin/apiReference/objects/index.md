### AddDataResult

The result object returned when adding data for a third-party device.

### ApiAccount

Stores account information for API accounts.

### ApiAccountGroup

Stores account information for API account groups.

### ApiAccountIdGroupMapping

Stores account ID and accountGroup mapping information.

### ApiCancelPendingTerminationResult

Contains information on whether a termination cancellation request was successfully processed or not

### ApiConnectedDevice

Contains information related to a device's connection information.

### ApiCurrency

Stores currency information. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiCurrencyRate

Stores currency rate information. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiCustomer

Class statement. Api version of CustomerDto

### ApiDeviceBillingChangeResult

Contains information on whether a billing change request was successfully added or not

### ApiDeviceContract

Contains information related to a device's contract.

### ApiDeviceContractAutoRequest

Contains device contract request information.

### ApiDeviceContractBilling

Stores device billing information. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiDeviceContractCreditTransaction

Stores device credit information.".

### ApiDeviceContractRatePlan

Contains rate plan information for a device contract.

### ApiDeviceContractRequestReason

Contains the reason that a contract was terminated. This class extends[ApiNameEntity](ApiNameEntity/index.md)- the "Name" property contains the reason description.

### ApiDeviceContractTransaction

Stores device billing information. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiDeviceDatabase

Contains the most recent database and VIN for a device.

### ApiDeviceDatabaseExtended

Contains the most recent database and VIN for a device including the device's serial number. This object extends[ApiDeviceDatabase](ApiDeviceDatabase/index.md).

### ApiDeviceDatabaseOwnerShared

Contains the most recent owner and shared database for a device.

### ApiDeviceInstallRequest

Class to track device lookups.

### ApiDeviceInstallResult

The result returned from a[ApiDeviceInstallRequest](ApiDeviceInstallRequest/index.md).

### ApiDeviceJurisdiction

Contains the most recent jurisdiction for a device.

### ApiDeviceMeta

Contains Device Metadata for DeviceOrderEntry

### ApiDeviceOrderEntry

Contains order status information.

### ApiDevicePlan

Stores device plan information. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiDeviceRma

Device contained in a[ApiRma](ApiRma/index.md).

### ApiDeviceRmaWithReplacementDetails

Device contained in a[ApiRma](ApiRma/index.md).

### ApiForceChangePassword

Force Change Password Details.

### ApiGeotabDevice

Stores information about a Geotab device.

### ApiInstallRequestItem

Stores installation service request information for a single item in an order.

### ApiNameEntity

Base class for all entity items.

### ApiOnlineOrder

Contains order status information.

### ApiOnlineOrderItem

Contains status information about an item in an order.

### ApiOrderHeader

Stores header information for an order.

### ApiOrderItem

Stores information related to an item in an order.

### ApiOrderItemProductAttribute

Stores product attribute configuration for an item on an order.

### ApiOrderItemProductAttributeGroup

Stores a grouping of product attribute configurations for an item on an order.

### ApiOrderShipItem

Contains information related to a shipment.

### ApiOrderVehicleInfo

Stores vehicle information for a single item in an order.

### ApiPartnerDevice

Contains information related to a partner device.

### ApiPricingType

The available category of pricing for the product. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiProductAndPricing

A group object that contains a product and its associated costs as at a specific point in time, for a particular[ApiAccount](ApiAccount/index.md). Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiProductAttribute

Stores a product attribute configuration.

### ApiProductCategory

Category a product belongs to. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiProductPricing

Pricing entry for a specific product

### ApiRatePlan

Contains information about a rate plan.

### ApiRatePlanType

The available type of[ApiRatePlan](ApiRatePlan/index.md). Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiRegion

Contains the name of the region where a device is domiciled

### ApiReturnReason

Return Reasons for Sales Return RMAs. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiRma

Contains details of an RMA.

### ApiRmaRequest

RMA request details.

### ApiRmaRequestItem

Item contained in a[ApiRmaRequest](ApiRmaRequest/index.md).

### ApiRmaType

The type of RMA.

### ApiRmaWithReplacementDetails

Contains details of an RMA with replacement details.

### ApiRmaWithoutReplacementDetails

Contains details of an RMA withour replacement details.

### ApiRole

User role entry. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiSharedDatabase

Contains a database GUID and whether it is the owner or not for a specific device.

### ApiShippingFee

Shipping fee type, indicates whether shipping fee is Standard, Priority or Local Pickup. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiTimeline

Device timelines

### ApiUser

Your public User account, including your UserId which you use for your Api Key. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiUserCompany

The company that a[ApiUserContact](ApiUserContact/index.md)belongs to. Extends[ApiNameEntity](ApiNameEntity/index.md).

### ApiUserContact

Contact information for MyAdmin user.

### ApiWarrantyOption

Warranty option entry. Extends[ApiNameEntity](ApiNameEntity/index.md).

### HelpdeskAttachment

This object describes the Attachment for the comment of an Helpdesk Ticket

### HelpdeskComment

This is the helpdesk comment object that describing each comment of the Helpdesk Ticket

### HelpdeskTicket

This is the base object for MyAdmin Helpdesk Ticket

### InstallLog

Details about installation

### ProvisionResult

The result object returned when provisioning a third party device.

### ThirdPartyAccelerationRecord

A data record class used to add acceleration data for third-party devices.

### ThirdPartyDataRecord

An abstract base class for third-party device data added through the MyAdmin API.

### ThirdPartyDataRecordType

The[ThirdPartyDataRecord](ThirdPartyDataRecord/index.md)type.

### ThirdPartyGpsRecord

A data record class used to add log record data for third-party devices.

### ThirdPartyLogRecord

A log record class used to add log record data for third party devices.

### ThirdPartyStatusRecord

A data record class used to add status data for third-party devices.