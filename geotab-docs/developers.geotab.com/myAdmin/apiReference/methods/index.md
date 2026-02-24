### AddEditCustomerAsync (...)

Adds or edits a customer.

### Authenticate (...)

Authenticates the user and returns the required API Key and Session ID, used for all subsequent API calls. If too much time has elapsed between subsequent API calls, calling other methods will throw a SessionExpiredException. When this occurs, call Authenticate to obtain a new session ID. Session ID expires after one week.

### CalculateVinOemEligibilities (...)

API to get VinOemSupportEligibilityResult for given Vin numbers, according to requested region

### CancelDeviceTerminationAsync (...)

Submits requests to cancel pending terminations for the provided devices.

### CancelOrder (...)

Cancels an order at anytime before or after completion. If the order has already shipped an RMA request will be automaticly generated and a returns of[ApiRmaRequest](../objects/ApiRmaRequest/index.md)objects is return otherwise a null result is return. If orderId is specified the order is canceled by orderId and forAccount, otherwise specify forAccount with purchaseOrderNo to cancel order.

### ChangeDeviceBillingPlan (...)

Submits a request to change the billing plan ([ApiDevicePlan](../objects/ApiDevicePlan/index.md)) for the provided device.

### ChangeDeviceBillingPlanBulkAsync (...)

Submits a request to change the billing plan ([ApiDevicePlan](../objects/ApiDevicePlan/index.md)) for the provided devices.

### CreateRmaRequest (...)

Creates an RMA request and returns a[ApiRmaRequest](../objects/ApiRmaRequest/index.md).

### EditUserContact (...)

Adds or updates a user contact. The[ApiUserContact](../objects/ApiUserContact/index.md)must contain a valid country name and where applicable, a valid state name. Exceptions will be thrown if the country or state is invalid. A valid list of countries can be retrieved by calling[GetCountries](GetCountries/index.md). A valid list of states for a country can be retrieved by calling[GetStates](GetStates/index.md)- if no states are returned, then any state name will be accepted for that country. The[ApiUserContact](../objects/ApiUserContact/index.md)parameter must contain a[ApiUserCompany](../objects/ApiUserCompany/index.md). If the company does not already exist, the ID field should be set to 0 and a new company will be created. If the ID is greater than zero, the existing company will be updated. The[ApiUserCompany](../objects/ApiUserCompany/index.md)must contain a[ApiAccount](../objects/ApiAccount/index.md)with a valid account ID.

### ForceChangePasswordForUsersAsync (...)

API to bulk update ForceChangePassword for users

### GetAttachmentBinary (...)

Get the byte array of the Attachment

### GetAvailableProducts (...)

Returns an array of[ApiProductAndPricing](../objects/ApiProductAndPricing/index.md)available to an account.

### GetCountries (...)

Returns a list of valid country names.

### GetCurrentDeviceDatabases (...)

Returns an array of[ApiDeviceDatabaseExtended](../objects/ApiDeviceDatabaseExtended/index.md)containing devices and their current databases and VINs (if available) for the specified account. The result set is limited to 1000 records. If the result set contains 1000 records, call GetCurrentDeviceDatabases again passing the Id of the last record in the current set as the nextId parameter.

### GetCustomersAsync (...)

Gets a list of customers for the provided filters. Returns in pages of 50 records.

### GetDeviceContractAutoRequests (...)

Gets the device contract request history for the given user and account.

### GetDeviceContractCreditTransactions (...)

Returns an array of[ApiDeviceContractCreditTransaction](../objects/ApiDeviceContractCreditTransaction/index.md)objects for the given period and filters.

### GetDeviceContractTransactions (...)

Returns an array of[ApiDeviceContractTransaction](../objects/ApiDeviceContractTransaction/index.md)objects for the given period and filters. If nextId is specified, the result set is limited to 1000 records. To obtain the first set of records, pass 0 into nextId. If the result set contains 1000 records, call GetDeviceContractTransactions again passing the Id of the last record in the current result set as the nextId parameter.

### GetDeviceContracts (...)

Returns an array of[ApiDeviceContract](../objects/ApiDeviceContract/index.md). This method returns all contracts that are active within the specified date range, filtered based on other parameters.

### GetDeviceContractsByPage (...)

Returns an array of[ApiDeviceContract](../objects/ApiDeviceContract/index.md). This method returns all contracts that are active within the specified date range, filtered based on other parameters. The result set is limited to 1000 records. To obtain the first set of records, pass 0 into nextId. If the result set contains 1000 records, call GetDeviceContracts again passing the Id of the last record in the current result set as the nextId parameter. This method returns device contracts that are active during the specified date range.

### GetDeviceDatabaseNamesAsync (...)

Returns an array of[ApiDeviceDatabaseOwnerShared](../objects/ApiDeviceDatabaseOwnerShared/index.md)containing devices and their owner databases and shared databases (if available).

### GetDeviceJurisdictionAsync (...)

Returns an array of[ApiDeviceJurisdiction](../objects/ApiDeviceJurisdiction/index.md)containing devices and their jurisdiction and dig url.

### GetDeviceOrderEntries (...)

Returns an array of[ApiDeviceOrderEntry](../objects/ApiDeviceOrderEntry/index.md)containing status of orders.

### GetDevicePlans (...)

Returns an array of active[ApiDevicePlan](../objects/ApiDevicePlan/index.md), available to all assigned accounts.

### GetDeviceTimelinesAsync (...)

Gets a list of device timelines[ApiTimeline](../objects/ApiTimeline/index.md)for the specified device.

### GetHelpdeskAttachment (...)

Get a single Helpdesk Attachment Object in the comment of the ticket

### GetHelpdeskAttachments (...)

Get all Helpdesk Attachment Objects in the comment of the ticket

### GetHelpdeskComment (...)

Get a single comment of a Helpdesk Ticket

### GetHelpdeskComments (...)

Get all comments of a Helpdesk Ticket

### GetHelpdeskTicket (...)

Get Single Ticket from MyAdmin Helpdesk By TicketId and Account Number

### GetHelpdeskTickets (...)

Get all tickets from MyAdmin Helpdesk By Account Number

### GetIndustriesAsync (...)

Returns an array of valid Industry names.

### GetInstallLogs (...)

Gets an array of[ApiDeviceInstallResult](../objects/ApiDeviceInstallResult/index.md). The method returns all install logs that occurred within the provided date range, filtered by the other parameters.

### GetMake (...)

API to get vehicle makes

### GetMinedVehicleData (...)

Gets all details of vehicles with option to include engine data. Returns a list of[MinedVehicleData](../objects/MinedVehicleData/index.md).

### GetMinedVehicleDataByVins (...)

Gets all details of vehicles with option to include engine data. Returns a list of[MinedVehicleData](../objects/MinedVehicleData/index.md).

### GetModel (...)

API to get vehicle models based on a provided make

### GetMyInstallLogs (...)

Gets a list of[InstallLog](../objects/InstallLog/index.md). The method returns all install logs that occurred within the provided date range, filtered by the other parameters.

### GetOemSupportEligibilityForMake (...)

API to get OemSupportEligibility for given Make, according to requested region

### GetOnlineOrderStatus (...)

Returns an array of[ApiOnlineOrder](../objects/ApiOnlineOrder/index.md)containing status of orders. If all of the following params (purchaseOrderNo, orderNo, orderDateFrom-orderDateTo) are null, last one month orders data will be returned by default.

### GetOwnDatabases (...)

Finds a list of databases belonging to the specified account or all accounts associated with the calling user's accounts.

### GetPartnerDeviceContractsAsync (...)

Returns a list of third party devices that the user's ERPs can manage.

### GetReturnReasons (...)

Returns a list of[ApiReturnReason](../objects/ApiReturnReason/index.md)used for Sales Return RMAs.

### GetRmaRequestItems (...)

Gets an array of devices ([ApiRmaRequestItem](../objects/ApiRmaRequestItem/index.md)) that belong to a[ApiRmaRequest](../objects/ApiRmaRequest/index.md).

### GetRmaRequests (...)

Gets an array of active[ApiRmaRequest](../objects/ApiRmaRequest/index.md)for the specified account.

### GetRmaTypes (...)

Returns a list of[ApiRmaType](../objects/ApiRmaType/index.md).

### GetRmas (...)

Gets an array of[ApiRma](../objects/ApiRma/index.md)for the specified account. If no deviceFilter or resellerReferenceFilter are specified, the method returns all active RMAs in the account. If a deviceFilter or resellerReferenceFilter are specified, the method returns the RMA(s) matching the filter(s), regardless of active status.

### GetSecondaryTerminationReasons (...)

Returns an array of[ApiDeviceContractRequestReason](../objects/ApiDeviceContractRequestReason/index.md)that are possible reasons for termination.

### GetSharedDatabases (...)

Returns an array of[ApiSharedDatabase](../objects/ApiSharedDatabase/index.md)containing databases the device has been assigned to and whether they are the owner or a shared database.

### GetShippingFees (...)

Returns an array of shipping fees (used for Orders).

### GetStates (...)

Returns an array of valid state names for a given country or an empty array if no states exist for the country. Throws[ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/system.argumentexception)if an invalid country name is provided.

### GetTerminationReasons (...)

Returns an array of[ApiDeviceContractRequestReason](../objects/ApiDeviceContractRequestReason/index.md)that are possible reasons for termination.

### GetUser (...)

Returns the user[ApiUser](../objects/ApiUser/index.md), associated with a given email account.

### GetUserContacts (...)

Returns an array of[ApiUserContact](../objects/ApiUserContact/index.md)for the API user, for the specified account.

### GetYear (...)

API to get vehicle years based on a provided make and model

### LogInstall (...)

Logs a device installation and returns the status of the device.

### LookupDevice (...)

Returns current information relating to the device serial number provided.

### PatchHelpdeskTicket (...)

Update an existing Helpdesk Ticket

### PostHelpdeskAttachment (...)

Create a Helpdesk Attachment Object for a ticket

### PostHelpdeskComment (...)

Creates a new comment on an existing Helpdesk ticket.

### PostHelpdeskTicket (...)

Creates a new Helpdesk ticket through MyAdmin using the legacy (old) API.

### PostOrder (...)

Posts a new order to MyAdmin. Create a[ApiOrderHeader](../objects/ApiOrderHeader/index.md)with details of the order. Required[ApiOrderHeader](../objects/ApiOrderHeader/index.md)fields are:
- devicePlanLevel
- forAccount
- orderItems
- purchaseOrderNumber
- shipToId
- shippingFeeId
- warrantyOptionId

Note that an Order which contains OrderItems for which a Bulk Price exists may be adjusted for applicable Bulk Price discounts. To take advantage of these discounts, either post an order with the desired quantity at the normal purchase price (the discounts will be applied automatically) or post an order with exactly BulkPriceMinQuantity (see[ApiProductPricing](../objects/ApiProductPricing/index.md)) quantity at the normal purchase price, and any additional quantity using the BulkPrice. Other combinations of order items may result in errors.

### ProvisionDevice (...)

Provisions a device to the user's default account.

### ProvisionDeviceToAccount (...)

Provisions a device to an account.

### ProvisionDevicesBulk (...)

Provisions multiple devices to an account.

### RegisterNewUser (...)

Registers a new user account into MyAdmin. An activation email will be sent to the user's email address.

### RequestManualSupportVins (...)

Request support for VINs that require a manual check to determine vehicle eligibility. On success, a confirmation email for each unique vehicle manufacturer will be sent to the email address associated with your account.

### ShareDevice (...)

Shares a device from myadmin by instructing the gateway to forward data to an additional database, and initiates billing as per multi stream billing.

### TerminateDeviceBilling (...)

Submits a request to terminate a billing plan for the provided device.

### TerminateDeviceBillingBulk (...)

Submits a request to terminate a billing plan for the provided list of devices.

### UpdateDatabaseAsync (...)

Updates the specified columns for a MyGeotab database using the provided admin credentials.

### UpdateDeviceContracts (...)

Updates the comment and/or user contact (eg. assigned customer) for one or more Device Contracts.