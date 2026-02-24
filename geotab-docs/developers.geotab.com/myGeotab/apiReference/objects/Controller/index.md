**Introduction**

The controller that the diagnostic belongs to. Controllers could be ABS controller, suspension controller etc. The available controllers are listed in the[KnownId](../KnownId/index.md).

**Properties**

## Code

The controller diagnostic code (if applicable).

## CodeId

The message identification code for the controller of the diagnostic (if applicable).

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Name

The name of this entity which identifies it and is used when displaying this entity.

## Source

The standard (format) of the[Source](../Source/index.md).

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 750 Get requests per 1m. | 750 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |