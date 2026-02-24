**Introduction**

Log of fueling events.

**Properties**

## Cost

The cost of the fuel transaction. Default [0].

## CurrencyCode

The three digit ISO 427 currency code (http://www.xe.com/iso4217.php). Default ["USD"].

## DateTime

The UTC date and time of the fuel event.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Location

The[Coordinate](../Coordinate/index.md)of the transaction retailer. Default [0,0].

## Odometer

The driver recorded odometer reading in km. Default [0].

## ProductType

The[FuelTransactionProductType](../FuelTransactionProductType/index.md)of this transaction. Default [Unknown].

## Version

The version of the entity.

## Volume

The volume of fuel purchased in Liters. Default [0].

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |