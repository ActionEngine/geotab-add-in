**Introduction**

Get all tickets from MyAdmin Helpdesk By Account Number

**Parameters**

## accountNumber

The Account Number that the tickets belong to

## apiKey

The active API key used to authenticate the request.

## databaseName

Filter Resellers' or Customers' tickets by database name

## endDate

Only return tickets created before endDate

## includeAccountTickets

Include tickets from everyone under the account, default is false

## onlyClosedTickets

Only return tickets that the status is closed, default is false

## onlyOpenTickets

Only return tickets that the status is open, default is true

## searchString

Filter result by ticket number or ticket title

## sessionId

The active session ID.

## showCustomerTickets

Shows Resellers' or Customers' tickets, default is false

## startDate

Only return tickets created after startDate

**Return value**

A list of[HelpdeskTicket](../../objects/HelpdeskTicket/index.md)objects

**Code samples**