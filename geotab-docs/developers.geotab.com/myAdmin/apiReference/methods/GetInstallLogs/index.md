**Introduction**

Gets an array of[ApiDeviceInstallResult](../../objects/ApiDeviceInstallResult/index.md). The method returns all install logs that occurred within the provided date range, filtered by the other parameters.The maximum date range is 60 days. This is a legacy API and will be subject to deprecation in the near future. Please use the newer 'GetMyInstallLogs' API

**Parameters**

## apiKey

The active API Key.

## assetNumber

Device asset number to filter by.

## companyNameFilter

Name of the company to filter by.

## fromDate

Start of the date range. This field is required if serialNoFilter is not specified.

## installerFilter

Name of the installer to filter by.

## serialNoFilter

Device serial number to filter by.

## sessionId

The active session ID.

## toDate

End of the date range. This field is required if serialNoFilter is not specified.

**Return value**

Array of[ApiDeviceInstallResult](../../objects/ApiDeviceInstallResult/index.md).

**Remarks**

The maximum date range is 60 days. This is a legacy API and will be subject to deprecation in the near future. Please use the newer 'GetMyInstallLogs' API

**Code samples**