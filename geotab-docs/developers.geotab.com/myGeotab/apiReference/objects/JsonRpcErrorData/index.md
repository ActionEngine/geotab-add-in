**Introduction**

The implementation specific error data for a JSON-RPC request error.

**Properties**

## Id

The error instance identifier.

## Info

A primitive or structured value that contains additional information about the error.
- [GroupRelationViolatedException](../GroupRelationViolatedException/index.md)
- [DbUnavailableException](../DbUnavailableException/index.md)

## RequestIndex

The index of the request in a "multicall" at which a failure occurred, otherwise [null].

## Type

The type of error.