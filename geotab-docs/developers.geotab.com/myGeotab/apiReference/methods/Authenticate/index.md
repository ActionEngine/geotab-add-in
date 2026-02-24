**Introduction**

Authenticates a user and provides a[LoginResult](../../objects/LoginResult/index.md)if successful. The authentication pattern is documented in the Concepts sections of the SDK.Throws:
- [InvalidUserException](../../objects/InvalidUserException/index.md)
- [DbUnavailableException](../../objects/DbUnavailableException/index.md)
- [OverLimitException](../../objects/OverLimitException/index.md)

**Parameters**

## database

The database to authenticate against. If the user is registered on only one database; the user will be automatically authenticated against the correct database and this parameter can be omitted (the database name is returned in the[LoginResult](../../objects/LoginResult/index.md)object). If the user is registered in multiple databases; the database value for the particular database you are trying to authenticate against must be provided.

## password

The user's Geotab password.

## userName

The user name (typically an email address) that identifies the user being authenticated.

**Return value**

A[LoginResult](../../objects/LoginResult/index.md)object. It contains the Credentials property that can be used for further API calls.

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Authenticate | Limit of 10 requests per 1m. | 10 | 1m | Active |