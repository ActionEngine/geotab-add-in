**Introduction**

The Failure Mode Identifier (FMI) used to describe engine fault codes. This is represented by the string "NoFailureModeId" when there is no applicable FMI.

**Properties**

## Code

The specific FMI code number.

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## Name

The name of this entity which identifies it and is used when displaying this entity.

## Source

The[Source](../Source/index.md)type for the FMI.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 200 Get requests per 1m. | 200 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |