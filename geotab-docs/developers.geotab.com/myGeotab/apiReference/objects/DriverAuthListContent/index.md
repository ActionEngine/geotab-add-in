**Introduction**

Message content to control a[GoDevice](../GoDevice/index.md)'s[Driver](../Driver/index.md)auth list.

**Properties**

## AddToAuthList

A value indicating whether to add to or remove from the auth list. If [true] "ClearAuthList" will be set to [false] and the driver will be added to the auth list. If [false] the driver will be removed from the auth list.

## ClearAuthList

A value indicating whether to clear the auth list. If [true] "AddToAuthList" will be set to [false] and "DriverKey" will be set to [null].

## ContentType

The type of message. See[MessageContentType](../MessageContentType/index.md).

## DriverKey

The[Driver](../Driver/index.md)s[Key](https://developers.geotab.com/myGeotab/apiReference/objects/Key/).