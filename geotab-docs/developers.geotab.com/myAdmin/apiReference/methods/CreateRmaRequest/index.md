**Introduction**

Creates an RMA request and returns a[ApiRmaRequest](../../objects/ApiRmaRequest/index.md). The itemsForRepair, reasonsForRepair, and quantitiesForRepair arrays must contain the same number of elements (eg. one reason and quantity per item). All devices should have their quantity set to one.

**Parameters**

## apiKey

The active API Key.

## caseNo

The ID of the[HelpdeskTicket](../../objects/HelpdeskTicket/index.md)associated with the RMA request. If no caseNo is provided, a new case will be created.

## comments

Comments related to the RMA request.

## forAccount

The account under which the RMA request will be created.

## internalComments

## itemsForRepair

String array of device serial numbers or product codes to be repaired.

## quantitiesForRepair

Int array of quantities for each product to be repaired.

## reasonsForRepair

String array of reasons for each product to be repaired. For Sales Returns, pass in the[ApiReturnReason](../../objects/ApiReturnReason/index.md)name.

## resellerReference

Reseller reference number/code.

## rmaTypeId

ID of the[ApiRmaType](../../objects/ApiRmaType/index.md).

## sessionId

The active session ID.

## shipToId

ID of the[ApiUserContact](../../objects/ApiUserContact/index.md)whose address will be associated with the RMA.

**Return value**

The[ApiRmaRequest](../../objects/ApiRmaRequest/index.md)that was created.

**Remarks**

The itemsForRepair, reasonsForRepair, and quantitiesForRepair arrays must contain the same number of elements (eg. one reason and quantity per item). All devices should have their quantity set to one.

**Code samples**