**Introduction**

The object used to specify the arguments when searching for[Zone](../Zone/index.md)(s).

**Properties**

## ExternalReference

Search for Zones with this External Reference. Wildcard can be used by prepending/appending "%" to string. Example "%reference%".

## FromDate

Search for Zones that were active at this date or after. Set to UTC now to search for only currently active (non-archived) zones.

## Groups

Search for Zones that are members of these[GroupSearch](../GroupSearch/index.md)(s) one of it's children or one of it's parents. Available GroupSearch options are:
- Id

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## IncludeGroups

Include zones that are in the in this hierarchy of the[GroupSearch](../GroupSearch/index.md)(s) provided. If no[GroupSearch](../GroupSearch/index.md)(s) are provided the user's data scope groups will be used. Default:[IncludeGroups](../IncludeGroups/index.md). ParentAndChild.

## Keywords

Search for entities that contain specific keywords in all wildcard string-searchable fields.

## MinimumRadiusInMeters

Exclude Zones whose radius is smaller than this size (meters).

## Name

Search for Zones with this Name. Wildcard can be used by prepending/appending "%" to string. Example "%name%".

## SearchArea

The[BoundingBox](../BoundingBox/index.md)search for Zones in this area extent, the zones being retrieved must be located in this area. Typically used for retrieving Zones in the extents of a bounding box. The SearchArea object should contain the minimum and maximum latitude and longitude representing the search area.

## ToDate

Search for Zones that were active at this date or before.

## ZoneTypes

Search for Zones that are of type[ZoneTypeSearch](../ZoneTypeSearch/index.md)(s). Available ZoneTypeSearch options are:
- Id