**Introduction**

The object used to specify the arguments when searching for a[TextMessage](../TextMessage/index.md).

**Properties**

## ChannelNumbers

Search for TextMessages filtered based on channel numbers assigned. MessageContentTypes that support setting the channelNumber:
- [MimeContent](../MimeContent/index.md)
- [SerialIoxContent](../SerialIoxContent/index.md)
- [ColdChainFaultClearContent](../ColdChainFaultClearContent/index.md)
- [ColdChainSetpointSetContent](../ColdChainSetpointSetContent/index.md)

## ContentTypes

Search for TextMessages filtered based on the[MessageContentType](../MessageContentType/index.md).

## DeviceSearch

Filter by the[DeviceSearch](../DeviceSearch/index.md)options. Providing a device ID will search for any TextMessages that are assigned to that Device. Providing the Groups will search for TextMessages for that have Devices in that group. Available DeviceSearch options are:
- Id
- Groups

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IsDelivered

Search for delivered or undelivered TextMessages. If it's set to true, it will return all TextMessages that were delivered. If it set to false, it will return all TextMessages that were not delivered. If it is set to null, it will return both delivered and undelivered TextMessages.

## IsDirectionToVehicle

Search for TextMessages based on the "direction" of the message. If it's set to true, it will return all TextMessages that were sent to a[Device](../Device/index.md). If it set to false, it will return all TextMessages that were not sent to a[Device](../Device/index.md). If it is set to null, it will return TextMessages sent to or from any asset type.

## IsRead

Search for read or unread TextMessages. If it's set to true, it will return all TextMessages that were read. If it set to false, it will return all TextMessages that were not unread. If it is set to null, it will return both read and unread TextMessages.

## LatestMessageOnly

A value indicating whether when LatestMessageOnly is set to True; only a single most recent message that matches the search parameters will be returned per device (using the date sent time to determine most recent).

## MimeTypes

Search for TextMessages filtered based on the messages MIME type. MimeTypes search is available for[MimeContent](../MimeContent/index.md)only.

## ModifiedSinceDate

Search for TextMessages that were delivered/sent/read since this date.

## Notification

Search for TextMessages that have Notification in messageContent.

## ParentMessageId

Search for TextMessages that have parent id as this[Id](../Id/index.md).

## RecipientSearch

Search for TextMessages sent to this[UserSearch](../UserSearch/index.md). Available UserSearch options are:
- Id
- CompanyGroups
- DriverGroups
- DriverGroupFilterCondition

## ToDate

Search for TextMessages that were sent at this date or before.

## UserSearch

Search for TextMessages sent by this[UserSearch](../UserSearch/index.md). Available UserSearch options are:
- Id
- CompanyGroups
- DriverGroups
- DriverGroupFilterCondition