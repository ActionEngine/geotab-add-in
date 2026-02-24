**Introduction**

Gets addresses from the list of[Coordinate](../../objects/Coordinate/index.md)(s), as well as any[Zone](../../objects/Zone/index.md)s in the system that contain the given coordinates.

**Parameters**

## coordinates

The array of[Coordinate](../../objects/Coordinate/index.md)(s).

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## hosAddresses

The default is false and is used for ELD compliant addresses. When set to true we will return the direction and distance to the nearest city with a population greater than 5000.

## movingAddresses

The default is false and is used for static/immobile addresses. When set to true, the coordinates are being specified for a moving object. The parameter should be set true if it is known that the object being tracked has a speed.

## pillar

The functional pillar for usage tracking.

**Return value**

A list of populated[ReverseGeocodeAddress](../../objects/ReverseGeocodeAddress/index.md)(s).

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| GetAddresses | Limit of 450 requests per 1m. | 450 | 1m | Active |