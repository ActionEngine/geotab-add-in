**Introduction**

Request support for VINs that require a manual check to determine vehicle eligibility. On success, a confirmation email for each unique vehicle manufacturer will be sent to the email address associated with your account.Do not use this API for data that must remain within the CONUS. VINs transmitted via this API may be transmitted outside of the CONUS.

**Parameters**

## apiKey

The active API Key.

## regionId

ID of the region in which eligibility support should be checked (1 - North America, 2 - Europe), only one region must be specified

## sessionId

The active session ID.

## vins

List of VINs to request manual support for

**Return value**

A comma delimited string of case numbers for each vehicle manufacturer

**Remarks**

Do not use this API for data that must remain within the CONUS. VINs transmitted via this API may be transmitted outside of the CONUS.

**Code samples**