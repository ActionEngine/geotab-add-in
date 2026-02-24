**Introduction**

A class that holds data stored by an add-in.

**Properties**

## AddInId

The add-in identifier.

## Details

The Details string as a serialized JSON object.

## Groups

The list of[Group](../Group/index.md)(s) the[AddInData](index.md)belongs to.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 650 Get requests per 1m. | 650 | 1m | Active |
| Set | Limit of 1700 Set requests per 1m. | 1700 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 2250 Remove requests per 1m. | 2250 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |