**Introduction**

A device share represents the sharing of steaming data from a device into multiple databases. A database which is the primary device subscriber may share the data with one or many other databases.

**Properties**

## AcceptedDateTime

The date that the[DeviceShare](index.md)was accepted.

## DateTime

The date time of when the[DeviceShare](index.md)was created.

## ExpirationDateTime

When the[DeviceShare](index.md)is set to expire.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## MyAdminId

The[Int32](https://docs.microsoft.com/en-us/dotnet/api/system.int32)id that MyAdmin associates with this[DeviceShare](index.md).

## Name

The name of this entity which identifies it and is used when displaying this entity.

## Options

The[DeviceShareOptions](../DeviceShareOptions/index.md)of this DeviceShare.

## SerialNumber

The[String](https://docs.microsoft.com/en-us/dotnet/api/system.string)serial number of the device associated with this[DeviceShare](index.md).

## ShareStatus

The[DeviceShareStatus](../DeviceShareStatus/index.md)of this DeviceShare.

## ShareType

The[DeviceShareType](../DeviceShareType/index.md)of this DeviceShare.

## SourceDatabaseName

The name of the source database for this device share. This is the database that owns the device and is allowing the sharing to occur.

## TargetDatabaseName

The name of the target database for this device share. This is the database that the device's data is being shared to, and does not own the device.

## TerminatedDateTime

The date that the[DeviceShare](index.md)was terminated.

## UpdatedDateTime

The date time of when the[DeviceShare](index.md)status was updated. This is when the share request was accepted/rejected by a target-database user or cancelled by a source-database user.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 800 Get requests per 1m. | 800 | 1m | Active |
| Set | Limit of 250 Set requests per 1m. | 250 | 1m | Active |
| Add | Limit of 250 Add requests per 1m. | 250 | 1m | Active |
| GetCountOf | Limit of 250 GetCountOf requests per 1m. | 250 | 1m | Active |
| GetFeed | Limit of 250 GetFeed requests per 1m. | 250 | 1m | Active |
| Remove | Limit of 250 Remove requests per 1m. | 250 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |