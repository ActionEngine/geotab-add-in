**Introduction**

Adds or updates a user contact. The[ApiUserContact](../../objects/ApiUserContact/index.md)must contain a valid country name and where applicable, a valid state name. Exceptions will be thrown if the country or state is invalid. A valid list of countries can be retrieved by calling[GetCountries](../GetCountries/index.md). A valid list of states for a country can be retrieved by calling[GetStates](../GetStates/index.md)- if no states are returned, then any state name will be accepted for that country. The[ApiUserContact](../../objects/ApiUserContact/index.md)parameter must contain a[ApiUserCompany](../../objects/ApiUserCompany/index.md). If the company does not already exist, the ID field should be set to 0 and a new company will be created. If the ID is greater than zero, the existing company will be updated. The[ApiUserCompany](../../objects/ApiUserCompany/index.md)must contain a[ApiAccount](../../objects/ApiAccount/index.md)with a valid account ID.

**Parameters**

## apiKey

The active API Key.

## overrideAddressValidation

Whether a user with Contact-Override role would like to override address validation.

## sessionId

The active session ID.

## userContact

The[ApiUserContact](../../objects/ApiUserContact/index.md)to add or update.

**Return value**

The new or updated[ApiUserContact](../../objects/ApiUserContact/index.md).

**Code samples**