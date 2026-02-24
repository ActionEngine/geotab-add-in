**Introduction**

Returns an array of[ApiUserContact](../../objects/ApiUserContact/index.md)for the API user, for the specified account.

**Parameters**

## activeStatus

Boolean value to show active users (true), archived users (false), or all users (null).

## apiKey

The active API Key.

## filter

String to filter users from a particular company, otherwise[Empty](https://docs.microsoft.com/en-us/dotnet/api/system.string.empty).

## forAccount

Account number (see[ApiUser](../../objects/ApiUser/index.md). Accounts) to retrieve user contacts from.

## sessionId

The active session ID.

**Return value**

Array of[ApiUserContact](../../objects/ApiUserContact/index.md)if user and account are valid, or null if not.

**Code samples**