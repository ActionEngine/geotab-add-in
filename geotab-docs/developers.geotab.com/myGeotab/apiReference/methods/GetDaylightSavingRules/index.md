**Introduction**

Get a Timezone's TimeZoneInfoWithRules by the timeZoneId.

**Parameters**

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## minYear

Adjustment rules which end before minYear will not be returned. Default is 2000.

## timeZoneId

The ID of the[TimeZoneInfo](../../objects/TimeZoneInfo/index.md).

**Return value**

The resulting[TimeZoneInfoWithRules](../../objects/TimeZoneInfoWithRules/index.md)collection.

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| GetDaylightSavingRules | Limit of 250 requests per 1m. | 250 | 1m | Active |