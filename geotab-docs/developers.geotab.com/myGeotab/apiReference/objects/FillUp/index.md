**Introduction**

An event representing adding fuel to an asset. Many sources of data are evaluated to determine a fill-up.[FuelTransaction](../FuelTransaction/index.md)s,[StatusData](../StatusData/index.md)(fuel level percent, fuel level volume, fuel used, tank capacity, odometer),[LogRecord](../LogRecord/index.md)s,[Trip](../Trip/index.md)s are all used to calculate fill-up events.

**Properties**

## Cost

The cost of the fuel transaction. Default [0].

## CurrencyCode

The three digit ISO 427 currency code (http://www.xe.com/iso4217.php). Default ["USD"].

## DateTime

The UTC date and time of the fuel event.

## DerivedVolume

The volume in Liters derived from fuel tank capacity. Default [-1].

## Device

The[Device](../Device/index.md)associated with the fuel used event.

## Distance

The distance in meters traveled since the last fill-up.

## Driver

The[Driver](../Driver/index.md)associated with the transaction.

## FuelTransactions

The[FuelTransaction](../FuelTransaction/index.md)s matched to this fill-up.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Location

The[Coordinate](../Coordinate/index.md)of the transaction retailer. Default [0,0].

## Odometer

The odometer reading in meters. Default [0].

## ProductType

The[FuelTransactionProductType](../FuelTransactionProductType/index.md)of this transaction. Default [Unknown].

## TankCapacity

The[FuelTankCapacity](../FuelTankCapacity/index.md)and how it was derived.

## TankLevelExtrema

The[FillUpExtrema](../FillUpExtrema/index.md)representing the fuel tank level change at the time of the fill-up.

## TotalFuelUsed

The total fuel used in Liters up to this point in time. Default [-1].

## Version

The version of the entity.

## Volume

The volume of fuel added in Liters. Default [0].

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1200 Get requests per 1m. | 1200 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |