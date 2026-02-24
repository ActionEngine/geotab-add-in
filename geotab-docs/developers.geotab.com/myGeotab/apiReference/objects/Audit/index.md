**Introduction**

Entry of events, operations and issues for tracking purposes. Entries can be added and read but cannot be edited.

**Properties**

## Comment

Free text field where any user information can be stored and referenced for this entity.

## DateTime

The date and time the audit was logged.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Name

The audit type name.

## UserName

The name of the user associated with the audit entry. Specifies the non-empty, validated myg user name for display in MyGeotab reports. Defaults to the authenticated account if null or blank.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 300 Get requests per 1m. | 300 | 1m | Active |
| Add | Limit of 250 Add requests per 1m. | 250 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Pagination**

## Results limit

50000

## Supported sort

[SortBy Date](../SortByDate/index.md) sorts by the Audit.DateTime property.

[SortBy Version](../SortByVersion/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |