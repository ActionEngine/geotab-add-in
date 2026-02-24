**Introduction**

The object used to specify the arguments when searching for a[User](../User/index.md)/[Driver](../Driver/index.md).

**Properties**

## AuthenticationTypes

Search for Users who are associated with these[UserAuthenticationType](../UserAuthenticationType/index.md)s.

## CompanyGroups

Search for Users who are a member of this[GroupSearch](../GroupSearch/index.md). Available GroupSearch options are:.
- Id

## DriverGroups

Search for Users who are assigned a Driver Key which is a member of the[GroupSearch](../GroupSearch/index.md). Available GroupSearch options are:.
- Id

## EmployeeNumber

Search for a User who is associated with this Driver Employee Number. Wildcard can be used by prepending/appending "%" to string. Example "%EmployeeNumber%". This property is negatable. If the first character of this search property is '!', then the API will know to negate the search logic. (e.g. field = "!EmployeeNumber%", is equivalent to: WHERE NOT LIKE 'EmployeeNumber%')

## FirstName

Search for Users with this first name. Wildcard can be used by prepending/appending "%" to string. Example "%firstName%". This property is negatable. If the first character of this search property is '!', then the API will know to negate the search logic. (e.g. field = "!John%", is equivalent to: WHERE NOT LIKE 'John%')

## FromDate

Search for Users that were active at this date or after. Set to UTC now to search for only currently active (non-archived) users.

## HosRuleSets

Search for Users who are associated with these[HosRuleSet](../HosRuleSet/index.md)s.

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## KeyId

Search for a User who is associated with this Driver Key Id.

## Keywords

Search for entities that contain specific keywords in all wildcard string-searchable fields.

## LastLogin

For LastLogin search. Must be used with LastLoginComparator. If user's[UserAuthenticationType](../UserAuthenticationType/index.md)is 'MyAdmin' and LastLoginComparator is 'After', user is returned regardless of LastLogin criteria. If user's[UserAuthenticationType](../UserAuthenticationType/index.md)is 'MyAdmin' and LastLoginComparator is 'Before', user is not returned regardless of LastLogin criteria.

## LastLoginComparator

For[DateTimeComparator](../DateTimeComparator/index.md)for LastLogin search.

## LastName

Search for Users with this last name. Wildcard can be used by prepending/appending "%" to string. Example "%lastName%". This property is negatable. If the first character of this search property is '!', then the API will know to negate the search logic. (e.g. field = "!John%", is equivalent to: WHERE NOT LIKE 'John%')

## LicenseNumber

Search for a User who is associated with this Driver License Number. Wildcard can be used by prepending/appending "%" to string. Example "%LicenseNumber%". This property is negatable. If the first character of this search property is '!', then the API will know to negate the search logic. (e.g. field = "!LicenseNumber%", is equivalent to: WHERE NOT LIKE 'LicenseNumber%')

## Name

Search for Users with this email/log-on name. Wildcard can be used by prepending/appending "%" to string. Example "%name%". This property is negatable. If the first character of this search property is '!', then the API will know to negate the search logic. (e.g. field = "!John%", is equivalent to: WHERE NOT LIKE 'John%')

## SecurityGroups

Search for Users who are assigned to a specific Security Clearance which is a member of the[GroupSearch](../GroupSearch/index.md). Available GroupSearch options are:.
- Id

## SerialNumber

Search for a User who is associated with this Driver Serial Number.

## ToDate

Search for Users that were active at this date or before.

## UserIds

Search for Users with these unique[Id](../Id/index.md)(s).

## UserSearchType

For[UserSearchType](../UserSearchType/index.md)search.