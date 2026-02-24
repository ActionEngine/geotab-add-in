**Introduction**

Represents a[Group](../Group/index.md)with[SecurityFilter](../SecurityFilter/index.md)(s) that are used to determine security access to different parts of the application.

**Properties**

## Children

The Children of this group. A list of Group(s).

## Color

The[Color](../Color/index.md)used to render assets belonging to this group. Default [Blue].

## Comments

The free text field where any user information can be stored and referenced for this entity. Default [""].

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## Name

The name of this entity which identifies it and is used when displaying this entity.

## Parent

The parent Group of the selected group.

## Reference

The string reference to add to the database entry for this group. Maximum length [255] Default [""].

## SecurityFilters

The[SecurityFilter](../SecurityFilter/index.md)(s) either adds or removes a particular SecurityIdentifier to a user's set of allowed items.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |