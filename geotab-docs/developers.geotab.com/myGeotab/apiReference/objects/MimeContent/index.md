**Introduction**

The contents of a[TextMessage](../TextMessage/index.md)containing data to give to a IOX Add-On over an RS232. It holds more data than[SerialIoxContent](../SerialIoxContent/index.md)and is not compatible with all Add-Ons. For more information regarding Add-On compatible please contact your reseller. MimeContent is converted into bytes with a specific format. The first byte is the length of the MimeType (N). The next N bytes are the ASCII encoded bytes of the MimeType string. The next two bytes are the length of the Data (L). Finally, the next L bytes are the Data. Messages from MyGeotab will be delivered in this format and messages to MyGeotab must be in this format as well.

**Properties**

## ChannelNumber

The channel number to send to an Add-On or that were received from an Add-On. Mandatory field.

## ContentType

The type of message. See[MessageContentType](../MessageContentType/index.md).

## Data

The raw bytes to either send to an Add-On or that were received from an Add-On. Maximum 2GB can be sent in a single message.

## MimeType

The media type of content contained in the data field. Free string, Maximum 255 characters.