**Introduction**

Download a file for the given[MediaFile](../../objects/MediaFile/index.md). The Content-Type is determined by the file extension. Range headers are supported.

**Parameters**

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## mediaFile

The[MediaFile](../../objects/MediaFile/index.md)of which to add the file for.

**Return value**

The file stream of the given[MediaFile](../../objects/MediaFile/index.md)content-type.

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| DownloadMediaFile | Limit of 240 requests per 1m. | 240 | 1m | Active |