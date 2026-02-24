**Introduction**

Gets a list of customers for the provided filters. Returns in pages of 50 records.

**Parameters**

## accounts

List of accounts to fetch associated customers for. A maximum of ten can be provided.

## apiKey

The active API Key.

## customerIds

List of ids of the customers to fetch.

## databases

List of database names whose linked customers should be fetched. Names are case-sensitive.

## partnerCustomerIds

List of external customer ids (strings) of the customers to fetch.

## sessionId

The active session ID.

## status

Status of the customers to fetch. Options are 'active', 'archived', and 'all'.

**Return value**

List of[ApiCustomer](../../objects/ApiCustomer/index.md).

**Code samples**