**Introduction**

A group is one element in a hierarchical tree. Each group can have none or many children, it is the children that define the shape of the hierarchical tree. The parent is not a property of the group object and is only defined by who the group is a child of. It is necessary to know the id of the parent group when adding a new group.There are three core Group branches used in MyGeotab. The most common are "Company Groups", company Groups are used to organize entities ([Zone](../Zone/index.md),[User](../User/index.md),[Device](../Device/index.md),[Driver](../Driver/index.md)and[Rule](../Rule/index.md)) into logical groups related to the organization. A Group structure can be constructed by region, vocation, reporting or anything that makes sense to the business, this allows aggregate reports and rolling up data in a flexible way. These groups have a many to many type of relationship with the entities that are members and are not limited to one type of entity.The second type is "Security Groups", these are Groups to which[User](../User/index.md)(s) are members of and can only be applied to Users. Each Group has a list of[SecurityFilter](../SecurityFilter/index.md)(s) associated to it. Security Filters control what parts of the application/API a User has access to.The third type of group is a "Private User Group", this group is used only for scheduling reports and displaying dashboard reports for a User. This Group will only ever apply to one User and will typically be named the user's name.There is a base structure of Groups which cannot be removed, these are considered to be "System"Some of these groups are:
- Company Group
- Asset Information Group
- Driver Activity Group
- Security Group
- Supervisor Security Group
- View Only Security Group
- Drive User Security Group
- Private User Group

When Groups are retrieved they will always be in a flat list of groups. The hierarchically tree(s) can be reconstructed by looking at the "Children" property of each Group. The "Root" group will never be returned and is only for system use.

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

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 350 Get requests per 1m. | 350 | 1m | Active |
| Set | Limit of 350 Set requests per 1m. | 350 | 1m | Active |
| Add | Limit of 350 Add requests per 1m. | 350 | 1m | Active |
| Remove | Limit of 350 Remove requests per 1m. | 350 | 1m | Active |
| GetCountOf | Limit of 350 GetCountOf requests per 1m. | 350 | 1m | Active |