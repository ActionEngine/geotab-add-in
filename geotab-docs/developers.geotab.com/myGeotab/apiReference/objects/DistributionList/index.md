**Introduction**

A distribution list links a set of[Rule](../Rule/index.md)(s) to a set of[Recipient](../Recipient/index.md)(s). When a[Rule](../Rule/index.md)is violated each related[Recipient](../Recipient/index.md)will receive a notification of the kind defined by its[RecipientType](../RecipientType/index.md).

**Properties**

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Name

The name of this entity which identifies it and is used when displaying this entity.

## Recipients

A list of recipients that will be notified when the[Rule](../Rule/index.md)(s) are violated.

## Rules

The list of[Rule](../Rule/index.md)(s) that the[Recipient](../Recipient/index.md)(s) will be notified of when broken.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 200 Get requests per 1m. | 200 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |