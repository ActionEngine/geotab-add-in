**Introduction**

Represents a GroupSecurity entity. This defines the many to many relationship between a[SecurityFilter](../SecurityFilter/index.md)and[Group](../Group/index.md).

**Properties**

## Group

The[Group](../Group/index.md)associated with the GroupSecurity.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## SecurityFilter

The[SecurityFilter](../SecurityFilter/index.md)associated with the GroupSecurity.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |