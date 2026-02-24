**Introduction**

Returns an array of[ApiDeviceContractTransaction](../../objects/ApiDeviceContractTransaction/index.md)objects for the given period and filters. If nextId is specified, the result set is limited to 1000 records. To obtain the first set of records, pass 0 into nextId. If the result set contains 1000 records, call GetDeviceContractTransactions again passing the Id of the last record in the current result set as the nextId parameter.

**Parameters**

## apiKey

The active API Key.

## forAccount

Account to retrieve billing records for, otherwise Empty .

## includeDatabase

## monthFilter

The month number for the billing period (1 = January, 12 = December)

## nextId

If specified, returns transaction records that have IDs greater than this value.

## serialNoFilter

Device serial number filter, otherwise Empty .

## sessionId

The active session ID.

## yearFilter

The 4-digit year for the billing period

**Return value**

Array of[ApiDeviceContractTransaction](../../objects/ApiDeviceContractTransaction/index.md)objects for the given period and filters

**Code samples**