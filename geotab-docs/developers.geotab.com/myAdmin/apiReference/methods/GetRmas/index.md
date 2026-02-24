**Introduction**

Gets an array of[ApiRma](../../objects/ApiRma/index.md)for the specified account. If no deviceFilter or resellerReferenceFilter are specified, the method returns all active RMAs in the account. If a deviceFilter or resellerReferenceFilter are specified, the method returns the RMA(s) matching the filter(s), regardless of active status.

**Parameters**

## apiKey

The active API Key.

## deviceFilter

Device serial number to search.

## displayReplacementDetails

If true, the replacement details will be displayed.

## forAccount

The account from which to retrieve RMA.

## resellerReferenceFilter

Reseller reference number/code to search.

## sessionId

The active session ID.

**Return value**

Array of[ApiRma](../../objects/ApiRma/index.md).

**Code samples**