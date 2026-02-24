**Introduction**

The contents of a[TextMessage](../TextMessage/index.md)containing data to give to a third-party IOX Add-On over an RS232. The SerialIoxContent is a 'dumb pipe' type of message. Whatever data is put in the data property will be delivered, as is, to the system on the other end of the IOX-RS232.

**Properties**

## Channel

The channel the[IoxAddOn](../IoxAddOn/index.md)is communicating over. 0 means the Add-On is not attached.

## ContentType

The type of message. See[MessageContentType](../MessageContentType/index.md).

## Data

The data to send to the[IoxAddOn](../IoxAddOn/index.md). Up to 235 bytes can be sent.