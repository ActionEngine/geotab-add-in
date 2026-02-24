**Introduction**

The object used to specify the arguments when searching for a[FaultData](../FaultData/index.md). This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + DiagnosticSearch + FromDate and/or ToDate
- GroupSearch + DiagnosticSearch + FromDate and/or ToDate

**Properties**

## ControllerSearch

The search options which are used to search for fault data for a controller[ControllerSearch](../ControllerSearch/index.md)by Id. Available ControllerSearch options are:.
- Id

## DeviceSearch

Search for[FaultData](../FaultData/index.md)(s) from a device that matches the[DeviceSearch](../DeviceSearch/index.md) Id or in the Groups specified. This includes archived and deleted devices. Available DeviceSearch options are:.
- Id
- DeviceIds
- Groups

## DiagnosticSearch

Search for FaultData recorded for the diagnostic code using the[DiagnosticSearch](../DiagnosticSearch/index.md) Id. Available DiagnosticSearch options are:.
- Id
- Code
- Name
- SourceSearch.Name
- SourceSearch.Id

## FromDate

The from date. The FaultData logs are searched for events which were recorded on or after this date.

## Groups

The groups which should be searched.[GroupSearch](../GroupSearch/index.md)(s). Available GroupSearch options are:.
- Id

## Id

Search for an entry based on the specific[Id](../Id/index.md).

## Ids

Search for FaultData with these unique[Id](../Id/index.md)(s).

## InclusiveSearch

Inclusive search flag.

## SeverityCodes

A value indicating the severity codes to search for.

## State

The to state of the fault. The Fault data logs are searched for events which are under the this state.

## ToDate

The to date. The Fault data logs are searched for events which were recorded on or before this date.