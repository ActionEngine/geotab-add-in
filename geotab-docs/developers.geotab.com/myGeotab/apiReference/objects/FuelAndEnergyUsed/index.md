**Introduction**

An event representing fuel and energy used for a vehicle.

**Properties**

## DateTime

The UTC date and time of the entity.

## Device

The[Device](../Device/index.md)associated with the entity.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## TotalEnergyUsedKwh

The amount of energy used in Kwh. Default [null].

## TotalFuelUsed

The volume of fuel used in Liters. Default [null].

## TotalIdlingEnergyUsedKwh

The amount of idling energy used in Kwh. Default [null].

## TotalIdlingFuelUsedL

The volume of idling fuel used in Liters. Default [null].

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1500 Get requests per 1m. | 1500 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |