**Introduction**

A ChargeEvent summarizes important details about EV charging: where vehicles have been charging, when vehicles have been charging, and how much energy they have consumed.

**Properties**

## ChargeIsEstimated

A value indicating whether EnergyConsumedKwh and PeakPowerKw have been measured directly, or estimated based on other available data.Geotab aims to provide high accuracy data on all EV makes and models. However, when a primary (preferred) raw data signal is not available, we may have to estimate EnergyConsumedKwh based on secondary (non-preferred) raw data signals. For these vehicles, chargeIsEstimated will be true.

## ChargeType

The[ChargeType](../ChargeType/index.md)provided by the external power source. Possible types are AC (Alternating Current), DC (Direct Current), or Unknown if the signal received from the charger does not match AC or DC.

## ChargingStartedOdometerKm

The odometer reading at[ChargeEvent](index.md)start, measured in kilometers.

## Device

The[Device](../Device/index.md)associated with the[ChargeEvent](index.md).

## Duration

The length of time the vehicle was charging, formatted as follows: “d.hh:mm:ss.fffffff”, where "d" represents days and “fffffff” represents fractional seconds.

## EndStateOfCharge

The battery charge % (state of charge) at the end of the associated[ChargeEvent](index.md). [0-100]

## EnergyConsumedKwh

The total energy going into the vehicle (at the charge station interface) during the[ChargeEvent](index.md), in kWh. This may be different from the energy added to the vehicle battery due to losses incurred by other internal vehicle components, such as on-board chargers.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Location

The[Coordinate](../Coordinate/index.md)where the[ChargeEvent](index.md)occurred.

## MaxACVoltage

The maximum AC Voltage reported during the[ChargeEvent](index.md), measured in Volts.

## PeakPowerKw

The peak power used during the[ChargeEvent](index.md), measured in Kilowatts.

## StartStateOfCharge

The battery charge % (state of charge) at the start of the associated[ChargeEvent](index.md). [0-100]

## StartTime

The UTC date and time when the[ChargeEvent](index.md)started, following the ISO 8601 standard.

## TripStop

The UTC date and time of the EV’s trip stop where the[ChargeEvent](index.md)took place, following the ISO 8601 standard. Charging happens during a trip stop.

## Version

The version of the entity.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 350 Get requests per 1m. | 350 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |