**Introduction**

Posts a new order to MyAdmin. Create a[ApiOrderHeader](../../objects/ApiOrderHeader/index.md)with details of the order. Required[ApiOrderHeader](../../objects/ApiOrderHeader/index.md)fields are:
- devicePlanLevel
- forAccount
- orderItems
- purchaseOrderNumber
- shipToId
- shippingFeeId
- warrantyOptionId

Note that an Order which contains OrderItems for which a Bulk Price exists may be adjusted for applicable Bulk Price discounts. To take advantage of these discounts, either post an order with the desired quantity at the normal purchase price (the discounts will be applied automatically) or post an order with exactly BulkPriceMinQuantity (see[ApiProductPricing](../../objects/ApiProductPricing/index.md)) quantity at the normal purchase price, and any additional quantity using the BulkPrice. Other combinations of order items may result in errors.

**Parameters**

## apiInstallRequestItems

The list of apiInstallRequestItem

## apiKey

The active API Key.

## apiOrderHeader

The[ApiOrderHeader](../../objects/ApiOrderHeader/index.md)with details of the order.

## apiReplacementDetails

The[ApiReplacementDetails](https://developers.geotab.com/myAdmin/apiReference/objects/ApiReplacementDetails/)with details of replacement.

## apiVehicleInfoList

The list of apiVehicleInfo

## sessionId

The active session ID.

**Return value**

An integer that represents the orderheaderId

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| PostOrder | Limit of 100 requests per 15 minutes. | 100 | 15m | Active |