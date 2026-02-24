**Introduction**

Registers a new user account into MyAdmin. An activation email will be sent to the user's email address.

**Parameters**

## accountNos

String array of account numbers (see[ApiUser](../../objects/ApiUser/index.md). Accounts and[ApiAccount](../../objects/ApiAccount/index.md)) to be allocated to the user.

## apiKey

The active API Key.

## password

The new users' password (min 5 characters).

## roles

String array array of roles (see[ApiUser](../../objects/ApiUser/index.md). Roles and[ApiRole](../../objects/ApiRole/index.md)) to be allocated to the user.

## sessionId

The active session ID.

## username

The new users' email address.

## userTypeId

UserType Id for (see[ApiUser](../../objects/ApiUser/index.md).

**Return value**

Returns true when the user is successfully created, otherwise false.

**Code samples**