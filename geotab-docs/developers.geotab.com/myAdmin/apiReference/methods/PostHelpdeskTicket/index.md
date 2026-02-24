**Introduction**

Creates a new Helpdesk ticket through MyAdmin using the legacy (old) API.This method allows authorized users to submit a Helpdesk ticket associated with a specific ERP account. The request must include valid authentication credentials (`apiKey` and `sessionId`) and a properly structured object containing all required ticket details.

**Parameters**

## apiKey

The active API key used to authenticate the request.

## sessionId

The active session ID associated with the authenticated user.

## ticket

The[HelpdeskTicket](../../objects/HelpdeskTicket/index.md)object containing the details of the issue or request.

**Return value**

A[PostHelpdeskTicketResponse](https://developers.geotab.com/myAdmin/apiReference/objects/PostHelpdeskTicketResponse/)object containing the newly created ticket ID and the associated comment ID (if available; may be ).

**Remarks**

This method allows authorized users to submit a Helpdesk ticket associated with a specific ERP account. The request must include valid authentication credentials (`apiKey` and `sessionId`) and a properly structured object containing all required ticket details.

**Code samples**