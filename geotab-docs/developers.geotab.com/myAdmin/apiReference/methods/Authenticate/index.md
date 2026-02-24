**Introduction**

Authenticates the user and returns the required API Key and Session ID, used for all subsequent API calls. If too much time has elapsed between subsequent API calls, calling other methods will throw a SessionExpiredException. When this occurs, call Authenticate to obtain a new session ID. Session ID expires after one week.Calls to this method will be rate limited. Ensure reauthentication is ONLY performed when a SessionExpiredException is thrown.

**Parameters**

## password

Your existing MyAdmin User Password.

## username

Your existing MyAdmin User Name (email address).

**Return value**

The active[ApiUser](../../objects/ApiUser/index.md)object that contains your API Key, which is required for all API calls.

**Remarks**

Calls to this method will be rate limited. Ensure reauthentication is ONLY performed when a SessionExpiredException is thrown.

**Code samples**