**Introduction**

Cancels an order at anytime before or after completion. If the order has already shipped an RMA request will be automaticly generated and a returns of[ApiRmaRequest](../../objects/ApiRmaRequest/index.md)objects is return otherwise a null result is return. If orderId is specified the order is canceled by orderId and forAccount, otherwise specify forAccount with purchaseOrderNo to cancel order.

**Parameters**

## apiKey

The active API Key.

## forAccount

Account to cancel order for

## orderId

The order Id to cancel for, otherwise Empty.

## purchaseOrderNo

Filter by purchase order number, otherwise Empty.

## sessionId

The active session ID.

**Return value**

Object of[ApiRmaRequest](../../objects/ApiRmaRequest/index.md)or[Nullable](https://docs.microsoft.com/en-us/dotnet/api/system.nullable)

**Code samples**