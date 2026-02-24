**Introduction**

Generates a single use CAPTCHA image for the given key and serves the result as "image/png" content.

**Parameters**

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## id

The globally unique id used to identify the CAPTCHA image returned.

**Return value**

Serves a jpeg CAPTCHA image with content type "image/png". If they key is not unique, returns HTTP status code 409 (Conflict).

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| GenerateCaptcha | Limit of 10 requests per 1m. | 10 | 1m | Active |