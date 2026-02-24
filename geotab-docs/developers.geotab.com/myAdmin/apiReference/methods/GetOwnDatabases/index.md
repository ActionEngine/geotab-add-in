**Introduction**

Finds a list of databases belonging to the specified account or all accounts associated with the calling user's accounts.

**Parameters**

## apiKey

The active API Key.

## forAccount

Filters the list of databases to the specified account. If omitted, all databases belonging to all of the user's accounts will be retrieved.

## sessionId

The active session ID.

**Return value**

List of databases belonging to the user's accounts.

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| GetOwnDatabases | Limit of 100 requests per 15 minutes. | 100 | 15m | Active |