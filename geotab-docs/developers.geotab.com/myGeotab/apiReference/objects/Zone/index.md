**Introduction**

Sometimes referred to as a "Geofence", a zone is a virtual geographic boundary, defined by its points representing a real-world geographic area.

**Properties**

## ActiveFrom

The date indicating when this zone begins it's active lifespan. Default [UtcNow].

## ActiveTo

The date indicating when this zone finishes it's active lifespan. Default [MaxDate].

## Comment

A free text field where any user information can be stored and referenced for this entity. Default [""].

## Displayed

A value indicating whether this zone must be displayed when viewing a map or it should be hidden. Default [true].

## ExternalReference

External Reference. Any type of external reference you would like to attach to the zone. For example; an ID from another data source referenced when exporting zone data into another program. Maximum length [255] Default [""].

## FillColor

The[Color](../Color/index.md)of the fill for this zone when showing on a map. Default [based on zone type; Customer: Orange, Office: Light Orange, Home: Green, Other: Blue].

## Groups

The group(s) this zone belongs to.

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## Metadata

The zone metadata.

## MustIdentifyStops

Whether this zone name must be shown when devices stop in this zone. If [true] a "zone stop rule" (Rule with BaseType: ZoneStop) will automatically be created for this zone. This is to facilitate reporting on zone stops. The rule is not visible via the UI. Default [true].

## Name

The name of this entity which identifies it and is used when displaying this entity.

## Points

The list of points (see[Coordinate](../Coordinate/index.md)) that make up this zone. A zone should be closed, the first point is the same coordinate as the last point.

## Version

The version of the entity.

## ZoneTypes

The list of[ZoneType](../ZoneType/index.md)(s) this zone belongs to. Default [Customer].

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 750 Get requests per 1m. | 750 | 1m | Active |
| Set | Limit of 200 Set requests per 1m. | 200 | 1m | Active |
| Add | Limit of 900 Add requests per 1m. | 900 | 1m | Active |
| Remove | Limit of 1000 Remove requests per 1m. | 1000 | 1m | Active |
| GetCountOf | Limit of 200 GetCountOf requests per 1m. | 200 | 1m | Active |
| GetFeed | Limit of 200 GetFeed requests per 1m. | 200 | 1m | Active |

**Pagination**

## Results limit

10000

## Supported sort

[SortBy Id](../SortById/index.md)

[SortBy Name](../SortByName/index.md)

**Timeout Limit**

| Method | Description | Limit | Status |
| --- | --- | --- | --- |

| GetFeed | Timeout of 180 seconds for GetFeed per request. | 180 | Active |