**Introduction**

The authentication credentials for a[User](../User/index.md)used when making calls to MyGeotab.

**Properties**

## Database

The database name.

## Password

The users login password. This can be used instead of providing a session Id. It is mutually exclusive with SessionId.

## SessionId

The session Id is a token which is generated from an authentication call and can be used instead of providing the password each time. It is mutually exclusive with Password.

## UserName

The MyGeotab username.