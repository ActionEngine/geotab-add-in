**Introduction**

The entity which describes the tachograph data file.Notes: Although possible, it is not recommended to directly introduce new entities of this type with the Add API call. New entities are created through other means in the application (i.e. scheduled remote downloads from the Tachograph).

**Properties**

## Archived

The value that indicates whether it's archived.

## BinaryData

The associated binary data object.

## Device

The[Device](../Device/index.md)related with the file data.

## Driver

The[Driver](../Driver/index.md)related with the file data.

## Errors

The string with the errors found in the download, the download is NOT valid and will have to be repeated.

## FileName

The file name.

## FileNameDdd

The DDD file name.

## FileNameTgd

The TGD file name.

## FileNameV1B

The V1B file name.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Origin

The origin of the file.

## OriginDescription

The description of the origin of the file.

## Signature

The signature.

## Summary

The summary about the information of the file.

## UploadDateTime

The date on which the file was uploaded.

## Version

The version of the entity.

## Warnings

The string with the warnings found in the download, the download is correct for the administration.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1000 Get requests per 1m. | 1000 | 1m | Active |
| Set | Limit of 60 Set requests per 1m. | 60 | 1m | Active |
| Add | Limit of 800 Add requests per 1m. | 800 | 1m | Active |
| GetCountOf | Limit of 1000 GetCountOf requests per 1m. | 1000 | 1m | Active |
| GetFeed | Limit of 1000 GetFeed requests per 1m. | 1000 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |