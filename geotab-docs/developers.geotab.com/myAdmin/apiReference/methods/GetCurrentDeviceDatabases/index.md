**Introduction**

Returns an array of[ApiDeviceDatabaseExtended](../../objects/ApiDeviceDatabaseExtended/index.md)containing devices and their current databases and VINs (if available) for the specified account. The result set is limited to 1000 records. If the result set contains 1000 records, call GetCurrentDeviceDatabases again passing the Id of the last record in the current set as the nextId parameter.

**Parameters**

## apiKey

The active API Key.

## forAccount

The account to from which to retrieve the current list of device database.

## nextId

If specified, returns device database records for those deviceIDs that belong to Device Contract IDs greater than this value.

## sessionId

The active session ID.

**Return value**

Array of[ApiDeviceDatabaseExtended](../../objects/ApiDeviceDatabaseExtended/index.md).

**Code samples**