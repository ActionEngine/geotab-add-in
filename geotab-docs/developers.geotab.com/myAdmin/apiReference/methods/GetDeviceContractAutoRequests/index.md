**Introduction**

Gets the device contract request history for the given user and account.The maximum date range is 60 days.

**Parameters**

## apiKey

The active Api Key.

## forAccount

Account number (see[ApiUser](../../objects/ApiUser/index.md). Accounts) to retrieve contract request history from.

## fromDate

Start of the date range.

## imeis

Array of modem serial numbers (IMEIs) to filter by.

## serialNos

Array of device serial numbers to filter by.

## sessionId

The active session ID.

## toDate

End of the date range.

## userCompanyIdFilter

Customer company ID to filter by.

**Return value**

Array of[ApiDeviceContractAutoRequest](../../objects/ApiDeviceContractAutoRequest/index.md).

**Remarks**

The maximum date range is 60 days.

**Code samples**