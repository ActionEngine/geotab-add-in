**Introduction**

Gets a list of[InstallLog](../../objects/InstallLog/index.md). The method returns all install logs that occurred within the provided date range, filtered by the other parameters.The maximum date range is 60 days.

**Parameters**

## apiKey

The active API Key.

## fromDate

Start of the date range. This field is required if serialNumber is not specified.

## installerCompany

Name of the company to filter by.

## installerName

Installer name to filter by.

## partnerAccount

Partner account to filter by.

## serialNumber

Device serial number to filter by.

## sessionId

The active session ID.

## toDate

End of the date range. This field is required if serialNumber is not specified.

## vehicleName

Vehicle name to filter by.

**Return value**

List of[InstallLog](../../objects/InstallLog/index.md).

**Remarks**

The maximum date range is 60 days.

**Code samples**