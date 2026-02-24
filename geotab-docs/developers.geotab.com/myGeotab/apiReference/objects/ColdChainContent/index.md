**Introduction**

Generates message content to trigger changes on a cooling unit (e.g. reefer). For more details on how the data is sent to the device, see[MimeContentBase](../MimeContentBase/index.md).

**Properties**

## ChannelNumber

The channel number to send to an Add-On or that were received from an Add-On. Mandatory field.

## ContentType

The type of message. See[MessageContentType](../MessageContentType/index.md).

## Data

The raw bytes to either send to an Add-On or that were received from an Add-On. Maximum 2GB can be sent in a single message.

## MimeType

The media type of content contained in the data field. Free string, Maximum 255 characters.