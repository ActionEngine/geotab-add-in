**Introduction**

Creates new uniquely named database on a server in the federation. Requires either a valid CaptchaAnswer and/or valid MyAdmin user credentials. See https://github.com/Geotab/sample-registration for an example.

**Parameters**

## companyDetails

The[CompanyDetails](../../objects/CompanyDetails/index.md)for the database.

## database

The database name (short company name with the demo_ prefix). Spaces and non alphanumeric characters will be converted to the underscore character. Maximum 58 characters.

## password

The database administrator password.

## userName

The database administrator email address.

**Return value**

A string with the direct server the database was created on and database name. Ex. "my0.geotab.com/abc_company".

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| CreateDatabase | Limit of 15 requests per 1m. | 15 | 1m | Active |