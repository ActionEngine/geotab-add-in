**Introduction**

Represents a Defect entity. This defines the one to one relationship between a[DefectSeverity](../DefectSeverity/index.md)and[Group](../Group/index.md).

**Properties**

## Children

The Children of this group. A list of Group(s).

## Color

The[Color](../Color/index.md)used to render assets belonging to this group. Default [Blue].

## Comments

The free text field where any user information can be stored and referenced for this entity. Default [""].

## Id

The unique identifier for this entity. See[Id](../Id/index.md).

## IsHidden

A value indicating whether this defect is hidden in the UI. Used for parts to determine if 'other' should be shown or not.

## IsRequired

A value indicating whether this defect must be signed off on. Used for parts to determine if the part must be explicitly marked as having defect(s) or not.

## Name

The name of this entity which identifies it and is used when displaying this entity.

## Parent

The parent Group of the selected group.

## Reference

The string reference to add to the database entry for this group. Maximum length [255] Default [""].

## Severity

The[DefectSeverity](../DefectSeverity/index.md)of the Defect.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 300 Get requests per 1m. | 300 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 100 Add requests per 1m. | 100 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |