**Introduction**

Gets a list of device timelines[ApiTimeline](../../objects/ApiTimeline/index.md)for the specified device.

**Parameters**

## apiKey

The active API Key.

## deviceSerialNumber

The account to retrieve RMA requests for.

## fromDate

From date filter to filter timeline.

## sessionId

The active session ID.

## toDate

To date filter to filter timeline.

**Return value**

a list of[ApiTimeline](../../objects/ApiTimeline/index.md)for the specified device.

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| GetDeviceTimelinesAsync | Limit of 300 requests per 15 minutes. | 300 | 15m | Active |