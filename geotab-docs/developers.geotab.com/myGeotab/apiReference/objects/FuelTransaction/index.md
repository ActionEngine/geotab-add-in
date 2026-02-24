**Introduction**

Information from a fuel card provider representing a fuel transaction. Fuel card information will be matched to a[Device](../Device/index.md)by one of these fields: vehicleIdentificationNumber, serialNumber, licencePlate or comments.

**Properties**

## CardNumber

The masked or partial purchasing card number.

## Comments

The free text field where any user information can be stored and referenced for this entity. This can be used to associate the transaction with a[Device](../Device/index.md). Maximum length [1024] Default [""].

## Cost

The cost of the fuel transaction. Default [0].

## CurrencyCode

The three digit ISO 427 currency code (http://www.xe.com/iso4217.php). Default ["USD"].

## DateTime

The UTC date and time of the fuel event.

## Description

The vehicle description of the vehicle. This can be used to associate the transaction with a[Device](../Device/index.md). Maximum length [255] Default [""].

## Device

The[Device](../Device/index.md)the transaction belongs to. Default [null].

## Driver

The[Driver](../Driver/index.md)the transaction belongs to.

## DriverName

The fuel card holder name. This can be used to associate the transaction with a[Driver](../Driver/index.md). Maximum length [255] Default [""].

## ExternalReference

The external reference to the transaction. Typically this is an external identifier. Maximum length [255] Default [""].

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## LicencePlate

The licence plate of the vehicle of the vehicle. This can be used to associate the transaction with a[Device](../Device/index.md). Maximum length [255] Default [""].

## Location

The[Coordinate](../Coordinate/index.md)of the transaction retailer. Default [0,0].

## Odometer

The driver recorded odometer reading in km. Default [0].

## ProductType

The[FuelTransactionProductType](../FuelTransactionProductType/index.md)of this transaction. Default [Unknown].

## Provider

The[FuelTransactionProvider](../FuelTransactionProvider/index.md)of this transaction. Default [Unknown].

## ProviderProductDescription

The Product Description given by the Provider.

## SerialNumber

The serial number of the device. This can be used to associate the transaction with a[Device](../Device/index.md). Maximum length [255] Default [""].

## SiteName

The site/merchant name where the transaction took place.

## SourceData

The JSON string representing the source data. Default [""].

## VehicleIdentificationNumber

The vehicle identification number (VIN) of the vehicle. This is used to associate the transaction with a[Device](../Device/index.md). Maximum length [255] Default [""].

## Version

The version of the entity.

## Volume

The volume of fuel purchased in Liters. Default [0].

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 250 Get requests per 1m. | 250 | 1m | Active |
| Set | Limit of 200 Set requests per 1m. | 200 | 1m | Active |
| Add | Limit of 1000 Add requests per 1m. | 1000 | 1m | Active |
| Remove | Limit of 200 Remove requests per 1m. | 200 | 1m | Active |
| GetCountOf | Limit of 200 GetCountOf requests per 1m. | 200 | 1m | Active |
| GetFeed | Limit of 250 GetFeed requests per 1m. | 250 | 1m | Active |

**Pagination**

## Results limit

50000

## Supported sort

[SortBy Date](../SortByDate/index.md) sorts by the FuelTransaction.DateTime property.

[SortBy Name](../SortByName/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |