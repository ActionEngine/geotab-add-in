**Introduction**

Returns an array of[ApiDeviceContract](../../objects/ApiDeviceContract/index.md). This method returns all contracts that are active within the specified date range, filtered based on other parameters. The result set is limited to 1000 records. To obtain the first set of records, pass 0 into nextId. If the result set contains 1000 records, call GetDeviceContracts again passing the Id of the last record in the current result set as the nextId parameter. This method returns device contracts that are active during the specified date range.

**Parameters**

## apiKey

The active API Key.

## commentsFilter

Filter array by comment.

## devicePlanId

ID of the[ApiDevicePlan](../../objects/ApiDevicePlan/index.md)to filter. -1 = show all device plans, 0 = show unassigned.

## forAccount

Account number (see[ApiUser](../../objects/ApiUser/index.md). Accounts) for which to retrieve the device contracts.

## fromDate

Start of the date range (value in UTC). Leave blank for all date range.

## groupIdFilter

Filter array by groupId.

## imeis

String array of device IMEI numbers to filter.

## includeConnectInfo

Includes device connection info.

## nextId

Limits the result set to 1000 records and returns device contracts that have IDs greater than this value. To obtain the first limited result set, pass 0 as this value.

## ordersAddedFrom

Start of the date range to limit results based on order date (value in UTC). Usage requires purchase order filter.

## ordersAddedTo

End of the date range to limit results based on order date (value in UTC). Usage requires purchase order filter.

## purchaseOrderFilter

Filter for a specified purchase order number. Required when using order date range.

## serialNos

String array of device serial numbers to filter.

## sessionId

The active session ID.

## showNoDatabaseOnly

Filters for devices that are not registered in a MyGeotab database.

## showShelfStockOnly

Filters for devices that have never activated.

## toDate

End of the date range (value in UTC). Leave blank for all date range.

## userCompanyId

ID of the[ApiUserCompany](../../objects/ApiUserCompany/index.md)to filter. -1 = show all companies, 0 = show unassigned.

**Return value**

Array of[ApiDeviceContract](../../objects/ApiDeviceContract/index.md).

**Code samples**