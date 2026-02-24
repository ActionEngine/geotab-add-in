**Introduction**

The entity which describes the binary media.

**Properties**

## Device

The[Device](../Device/index.md)associated with the file.

## Driver

The[Driver](../Driver/index.md)associated with the file.

## FromDate

The from date.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## MediaType

The[MediaType](../MediaType/index.md).

## MetaData

File metadata in JSON format.

## Name

The name of this entity which identifies it and is used when displaying this entity.

## SolutionId

The user-generated unique[Id](../Id/index.md)to associate the MediaFile data to a particular solution/integration.

## Status

The file processing[Status](../Status/index.md).

## Tags

The list of tags to provide context to the file.

## Thumbnails

The list of files which serve as the thumbnail for this file.

## ToDate

The to date.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 350 Get requests per 1m. | 350 | 1m | Active |
| Set | Limit of 60 Set requests per 1m. | 60 | 1m | Active |
| Add | Limit of 60 Add requests per 1m. | 60 | 1m | Active |
| Remove | Limit of 60 Remove requests per 1m. | 60 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |