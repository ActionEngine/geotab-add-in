**Introduction**

Returns an array of[ApiOnlineOrder](../../objects/ApiOnlineOrder/index.md)containing status of orders. If all of the following params (purchaseOrderNo, orderNo, orderDateFrom-orderDateTo) are null, last one month orders data will be returned by default.

**Parameters**

## apiKey

The active API Key.

## forAccount

Account where the order was created.

## includeCancelledOrders

If true, retrieves cancelled orders as well.

## orderDateFrom

If specified, retrieves orders with order dates greater than this value (value in UTC).

## orderDateTo

If specified, retrieves orders with order dates less than this value (value in UTC).

## orderNo

Filter by Geotab order number.

## orderSource

Filter by order source (where the order originated, e.g. Store, Bulk, API, Marketplace).

## purchaseOrderNo

Filter by purchase order number.

## resellerReference

Filter by reseller reference number.

## savedOrdersOnly

If true, only retrieve orders saved as planning orders.

## sessionId

The active session ID.

**Return value**

Array of[ApiOnlineOrder](../../objects/ApiOnlineOrder/index.md).

**Code samples**