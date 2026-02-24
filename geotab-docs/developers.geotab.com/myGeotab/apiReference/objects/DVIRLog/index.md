**Introduction**

A DVIRLog is a Driver Vehicle Inspection Report which is prepared by a driver regarding defects in parts of a vehicle associated with a[Device](../Device/index.md)or[Trailer](../Trailer/index.md). Once the report is completed with optional driver remarks, the DVIR log will be acted upon, and marked as repairs made or not necessary (usually by another[User](../User/index.md)). The driver then will mark the log as certified for being safe or unsafe to operate based on the effectiveness of any repairs made or comments for repairs not performed.

**Properties**

## AuthorityAddress

The authority address for the driver at the time of this log. Maximum length [255] Default [""].

## AuthorityName

The authority name for the driver at the time of this log. Maximum length [255] Default [""].

## CertifiedBy

The[User](../User/index.md)who certified the repairs (or comments if no repairs were made) to the[Device](../Device/index.md)or[Trailer](../Trailer/index.md).

## CertifyDate

The date the[Device](../Device/index.md)or[Trailer](../Trailer/index.md)was certified.

## CertifyRemark

The remark recorded by the[User](../User/index.md)who certified the repairs (or no repairs made) to the[Device](../Device/index.md)or[Trailer](../Trailer/index.md).

## DateTime

The date and time the log was created.

## DefectList

The defect list[Group](../Group/index.md)of the log.

## Defects

The list of defect[Group](../Group/index.md)(s) for this log.

## Device

The[Device](../Device/index.md)associated with this log. Either a Device or a[Trailer](../Trailer/index.md)is defined for a log, not both (if the device is set, trailer must be null).

## Driver

The[User](../User/index.md)who created the log.

## DriverRemark

The remark recorded by the driver for this log.

## Duration

The total time spent to complete this dvir. Default [null].

## DVIRDefects

The list of DVIRDefects[DVIRDefect](../DVIRDefect/index.md)(s) for this log.

## EngineHours

The engine hours for the[Device](../Device/index.md)of this log. The unit is seconds (not hours). Default [null].

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## IsSafeToOperate

Identifier for whether or not the[Device](../Device/index.md)or[Trailer](../Trailer/index.md)was certified as safe to operate.

## LoadHeight

The load height, if it was manually recorded by the driver. The unit is in meters (m), not kilometers (km). Default [null].

## LoadWidth

The load width, if it was manually recorded by the driver. The unit is in meters (m), not kilometers (km). Default [null].

## Location

An object with the location information of the log.

## LogType

The[DVIRLogType](../DVIRLogType/index.md)of the log. Default [Unknown].

## Odometer

The odometer or hubometer of the vehicle or trailer. The unit is in meters (m), not kilometers (km). Default [null].

## RepairDate

The date the[Device](../Device/index.md)or[Trailer](../Trailer/index.md)was repaired.

## RepairedBy

The[User](../User/index.md)who repaired the[Device](../Device/index.md)or[Trailer](../Trailer/index.md).

## RepairRemark

The remark recorded by the[User](../User/index.md)who repaired the[Device](../Device/index.md)or[Trailer](../Trailer/index.md).

## Trailer

The[Trailer](../Trailer/index.md)associated with this log. Either a[Device](../Device/index.md)or a Trailer is defined for a log, not both (if the trailer is set, device must be null).

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1000 Get requests per 1m. | 1000 | 1m | Active |
| Set | Limit of 350 Set requests per 1m. | 350 | 1m | Active |
| Add | Limit of 350 Add requests per 1m. | 350 | 1m | Active |
| Remove | Limit of 350 Remove requests per 1m. | 350 | 1m | Active |
| GetCountOf | Limit of 350 GetCountOf requests per 1m. | 350 | 1m | Active |
| GetFeed | Limit of 350 GetFeed requests per 1m. | 350 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |