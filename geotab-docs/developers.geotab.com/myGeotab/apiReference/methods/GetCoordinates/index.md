**Introduction**

Geocodes or looks up the latitude and longitude from a list of addresses.

**Parameters**

## addresses

The formatted addresses in an array of[String](https://docs.microsoft.com/en-us/dotnet/api/system.string)(s).

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## pillar

The functional pillar for usage tracking.

**Return value**

The array of[Coordinate](../../objects/Coordinate/index.md)(s) for the address or null if it cannot be found.

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| GetCoordinates | Limit of 300 requests per 1m. | 300 | 1m | Active |