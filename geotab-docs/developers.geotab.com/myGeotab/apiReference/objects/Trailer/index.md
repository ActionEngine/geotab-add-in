**Introduction**

A trailer which can be attached and detached from a vehicle with a[TrailerAttachment](../TrailerAttachment/index.md)record.

**Properties**

## Comment

Free text field where any user information can be stored and referenced for this entity. Default [""].

## Groups

The list of trailer groups.

## Id

The unique[Id](../Id/index.md)of the trailer.

## Name

The name of the trailer. Maximum length [255].

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 300 Get requests per 1m. | 300 | 1m | Active |
| Set | Limit of 300 Set requests per 1m. | 300 | 1m | Active |
| Add | Limit of 300 Add requests per 1m. | 300 | 1m | Active |
| Remove | Limit of 300 Remove requests per 1m. | 300 | 1m | Active |
| GetCountOf | Limit of 300 GetCountOf requests per 1m. | 300 | 1m | Active |
| GetFeed | Limit of 300 GetFeed requests per 1m. | 300 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |