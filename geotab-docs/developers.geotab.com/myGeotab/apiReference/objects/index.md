### API

Used to make API calls against a MyGeotab web server. This object is typically used when using the API from a Microsoft .Net language, like C#, VB.Net or managed C++. It makes it easy to invoke the various methods and receive the results. It also automates of some tasks such as handling a database that was moved from one server to another or credentials expiring. This class is thread safe.

### AddIn

Add-Ins are used to extend the functionality provided by MyGeotab and Geotab Drive. An Add-In is JavaScript, HTML and CSS loaded into the MyGeotab or Geotab Drive portal and resides directly inside the user interface. This allows third-parties to create a seamless user experience and provide solutions that would otherwise require the user to visit a different website altogether.[More information on developing Add-Ins.](https://geotab.github.io/sdk/software/guides/developing-addins/)

### AddInConfiguration

Represents populated Add-In with configuration.

### AddInConfigurationSearch

The object used to specify the arguments when searching for[AddInConfiguration](AddInConfiguration/index.md).

### AddInData

A class that holds data stored by an add-in.

### AddInSearch

The object used to specify the arguments when searching for[AddIn](AddIn/index.md).

### AnnotationLog

An AnnotationLog is a comment that can be associated with a[DutyStatusLog](DutyStatusLog/index.md). The[Driver](Driver/index.md)is the author of the AnnotationLog.

### AnnotationLogSearch

The object used to specify the arguments when searching for[AnnotationLog](AnnotationLog/index.md)(s).

### ApplicationVersionInformation

The inner object for the ApplicationInformation information in VersionInformation.

### Audit

Entry of events, operations and issues for tracking purposes. Entries can be added and read but cannot be edited.

### AuditSearch

The object used to specify the arguments when searching[Audit](Audit/index.md)entries.

### BatteryStateOfHealth

This entity allows you to track high voltage battery degradation over the lifetime of your BEVs and PHEVs. We use historical driving and charging data to estimate usable battery capacity.

### BatteryStateOfHealthSearch

The object used to specify the arguments when searching for a[BatteryStateOfHealth](BatteryStateOfHealth/index.md).

### BinaryData

This is binary data representing anything that can be stored. BinaryData can use this to store images but the data can be any custom data, including custom engine information types. The type of the data is defined by the[BinaryDataType](BinaryDataType/index.md).

### BinaryDataSearch

The object used to specify the arguments when searching for[BinaryData](BinaryData/index.md).

### BinaryDataType

Represents the specific binary format of data being stored in the[BinaryData](BinaryData/index.md)object.

### BinaryPayload

A message containing a binary payload which is usually forwarded to a target device.

### BinaryPayloadType

The[BinaryPayload](BinaryPayload/index.md)type.

### BoundingBox

A geographic area defined by the top-left and bottom-right coordinates.

### Button

Represents the Add-In Button item.

### CannedResponseContent

Text message content including a list of predetermined responses. Derived from[TextContent](TextContent/index.md).

### CannedResponseOption

Specifies the allowed responses to a[TextMessage](TextMessage/index.md).

### CaptchaAnswer

The answer to a CAPTCHA.

### CaptchaException

A CAPTCHA error occurred.

### ChargeEvent

A ChargeEvent summarizes important details about EV charging: where vehicles have been charging, when vehicles have been charging, and how much energy they have consumed.

### ChargeEventSearch

The object used to specify the arguments when searching for a[ChargeEvent](ChargeEvent/index.md).

### ChargeType

Represents the current type of the charge.

### CoachingSessionState

Represents the state of a[CoachingSession](https://developers.geotab.com/myGeotab/apiReference/objects/CoachingSession/).

### ColdChainContent

Generates message content to trigger changes on a cooling unit (e.g. reefer). For more details on how the data is sent to the device, see[MimeContentBase](MimeContentBase/index.md).

### ColdChainFaultClearContent

Generates message content to trigger the clearing of a fault code on a cooling unit (e.g. reefer). For more details on how the data is sent to the device, see[MimeContentBase](MimeContentBase/index.md).

### ColdChainSetpointSetContent

Generates message content to trigger the setting of a setpoint on a cooling unit (e.g. reefer). For more details on how the data is sent to the device, see[MimeContentBase](MimeContentBase/index.md).

### Color

Specifies the color to use to identify the[Group](Group/index.md),[Rule](Rule/index.md),[SecurityClearance](SecurityClearance/index.md)or[Zone](Zone/index.md).

### CompanyDetails

Company details for registration.

### ComplianceEnrollmentStatus

Represents the Clean Truck Check compliance enrollment status of a[Device](Device/index.md).

### Condition

Conditions model the logic that govern a[Rule](Rule/index.md)and can apply to many different types of data and entities. Conditions are structured in hierarchical tree. A condition's type (see[ConditionType](ConditionType/index.md)) defines the meaning of each condition in the tree and can be an operator, special operator, data or an asset.Depending on the type of condition, it can have a minimum of 0 and maximum of 1 entity properties (Device, Driver, Diagnostic, WorkTime, Zone or ZoneType) defined per condition. Operator conditions (OR, AND, >, <, ==, NOT) will not have any entity properties populated. Special Operator conditions evaluate against special types of data such as Aux data, Zones, WorkHours, etc. and may have the entity property populated and/or a child condition populated with a Data condition. Asset conditions will only have the asset entity property populated.The unit of measure for data is described either by the related[Diagnostic](Diagnostic/index.md)'s[UnitOfMeasure](UnitOfMeasure/index.md)or as follows:
- Distance: Meters (m)
- Speed: Kilometers Per Hour (km/h)
- Duration: Seconds

A tree of conditions can define simple or complex rules and can be very powerful. Please take into consideration all possible consequences of a series of rules. Overly complex, poorly written or an excessive number of rules can have undesirable performance effects.

### ConditionType

Defines the different types of[Condition](Condition/index.md)(s).

### Controller

The controller that the diagnostic belongs to. Controllers could be ABS controller, suspension controller etc. The available controllers are listed in the[KnownId](KnownId/index.md).

### ControllerSearch

The object used to specify the arguments when searching for[Controller](Controller/index.md)(s).

### Coordinate

A coordinate on the earth's surface. "x" is longitude and "y" is latitude.

### Credentials

The authentication credentials for a[User](User/index.md)used when making calls to MyGeotab.

### CustomData

Generic Custom Data from a GO unit that was sent through from a third-party device that is attached to the serial port.

### CustomDataSearch

The object used to specify the arguments when searching for[CustomData](CustomData/index.md).

### CustomDevice

A custom telematics device that is used in MyGeotab. This is used for extensibility and is based on the[Device](Device/index.md)object.

### CustomSecurityId

A custom security ID which can be used to control access to custom Add-Ins.

### CustomVehicleDevice

A custom telematics automotive vehicle device that is used in MyGeotab. This is used for extensibility and is based on the[CustomDevice](CustomDevice/index.md)object.

### DVIRDefect

A DVIRDefect is a Defect that can be associated with a[DVIRLog](DVIRLog/index.md). It contains repair information such as repair[DateTime](https://docs.microsoft.com/en-us/dotnet/api/system.datetime), repair[User](User/index.md), and[RepairStatusType](RepairStatusType/index.md). DVIRDefect also consists a list of[DefectRemark](DefectRemark/index.md)which can be used to store additional information for the defect.

### DVIRLog

A DVIRLog is a Driver Vehicle Inspection Report which is prepared by a driver regarding defects in parts of a vehicle associated with a[Device](Device/index.md)or[Trailer](Trailer/index.md). Once the report is completed with optional driver remarks, the DVIR log will be acted upon, and marked as repairs made or not necessary (usually by another[User](User/index.md)). The driver then will mark the log as certified for being safe or unsafe to operate based on the effectiveness of any repairs made or comments for repairs not performed.

### DVIRLogSearch

The object used to specify the arguments when searching for[DVIRLog](DVIRLog/index.md)(s). A trailerSearch and deviceSearch cannot be used at the same time because a DVIR log entry is only ever associated with one asset type (for instance, if the "device" is set, "trailer" is always null and vice versa).

### DVIRLogType

The type of[DVIRLog](DVIRLog/index.md).

### DataDiagnostic

A[Diagnostic](Diagnostic/index.md)that represents measurement data from the vehicle (as opposed to fault codes).

### DataToComponentContent

Message that can deliver data to a component of a GO device.

### DateTimeComparator

The[DateTimeComparator](DateTimeComparator/index.md).

### DbUnavailableException

This exception occurs if the system makes a database request that could not succeed because of connection failure or data change.

### DebugData

DebugData is generated by Geotab GO devices for internal debugging or troubleshooting purposes. This may include information regarding the state of the modem, firmware or conditions that the device is experiencing.

### DebugDataSearch

The object used to specify the arguments when searching[DebugData](DebugData/index.md).

### Defect

Represents a Defect entity. This defines the one to one relationship between a[DefectSeverity](DefectSeverity/index.md)and[Group](Group/index.md).

### DefectRemark

An DefectRemark is a remark that can be associated with a[DVIRDefect](DVIRDefect/index.md).

### DefectSeverity

The severity of a defect for a[DVIRLog](DVIRLog/index.md).

### DeploymentType

The server's deployment type.

### Device

A Device represents the physical tracking device installed in the vehicle. A device and vehicle is typically synonymous since the GO tracking device is installed in a vehicle. In the case where there is no device; this is represented by "NoDeviceId". The device types that are supported are:
- [GoAnywhere](GoAnywhere/index.md)
- [Go9](Go9/index.md)
- [Go8](Go8/index.md)
- [Go7](Go7/index.md)
- [Go6](Go6/index.md)
- [Go5](Go5/index.md)
- [CustomDevice](CustomDevice/index.md)

### DeviceCommunicationStatusCount

Represents a record that holds the count of devices for a specific communication status.

### DeviceEnrollmentInfo

Represents the info of a device to be enrolled for Clean Truck Check emission reporting.

### DeviceEnrollmentResult

Represent the result of device enrollment for Clean Truck Check emission reporting.

### DeviceSearch

The object used to specify the arguments when searching for a[Device](Device/index.md).

### DeviceShare

A device share represents the sharing of steaming data from a device into multiple databases. A database which is the primary device subscriber may share the data with one or many other databases.

### DeviceShareOptions

The class that contains device share options flags.

### DeviceShareSearch

The object used to specify the arguments when searching for[DeviceShare](DeviceShare/index.md)(s).

### DeviceShareStatus

The various statuses that a[DeviceShare](DeviceShare/index.md)can have.

### DeviceShareType

Represents the data flow type for a[DeviceShare](DeviceShare/index.md).

### DeviceStatusInfo

Represents the current state of a vehicle by providing information such as the vehicle bearing location and speed, active exception events and whether the device is currently communicating.

### DeviceStatusInfoSearch

The object used to specify the arguments when searching for[DeviceStatusInfo](DeviceStatusInfo/index.md)(s).

### DeviceType

The Geotab GO device type enumeration. Geotab has produced various types of tracking devices and this device type enumeration can be used to determine which type of hardware a particular device is.

### Diagnostic

Vehicle diagnostic information from the engine computer that can either be measurement data or fault code data.

### DiagnosticSearch

The object used to specify the arguments when searching for[Diagnostic](Diagnostic/index.md)(s).

### DiagnosticType

Diagnostic source type of the diagnostic.

### Directions

A sequential set of[Leg](Leg/index.md)s and[Step](Step/index.md)s that make up directions.

### DistributionList

A distribution list links a set of[Rule](Rule/index.md)(s) to a set of[Recipient](Recipient/index.md)(s). When a[Rule](Rule/index.md)is violated each related[Recipient](Recipient/index.md)will receive a notification of the kind defined by its[RecipientType](RecipientType/index.md).

### Driver

A driver in the system, and it is derived from[User](User/index.md), with key ids and driver groups. If the driver is unknown then the driver is represented by "UnknownDriver".

### DriverAuthListContent

Message content to control a[GoDevice](GoDevice/index.md)'s[Driver](Driver/index.md)auth list.

### DriverChange

Information about timing of a[Driver](Driver/index.md)change.

### DriverChangeSearch

The object used to specify the arguments when searching for a[DriverChange](DriverChange/index.md). This search defaults to searching[DriverChange](DriverChange/index.md)(s) by[Driver](Driver/index.md) Id when no[DeviceSearch](DeviceSearch/index.md)is provided.

### DriverChangeType

Supported Driver Change Types.

### DriverRegulation

Detailed information for Hours of Service regulation for a driver.

### DriverRegulationSearch

The object used to specify the arguments when searching for[DriverRegulation](DriverRegulation/index.md)objects.

### DtcClass

Represents a severity/class code from the engine system of the specific[Device](Device/index.md).

### DtcSeverity

Represents a severity/class code from the engine system of the specific[Device](Device/index.md).

### DuplicateException

An exception that occurs when adding a new object or when updating an existing object that would cause a duplicate entry to occur.

### DutyStatusAvailability

Driver Availability for Hours of Service regulations.

### DutyStatusAvailabilitySearch

The object used to specify the arguments when searching for[DutyStatusAvailability](DutyStatusAvailability/index.md)objects.

### DutyStatusDeferralType

The type of[DutyStatusLog](DutyStatusLog/index.md).

### DutyStatusLog

A DutyStatusLog is a record of duty status for Hours of Service regulations. The log is first required to have a driver, dateTime, status, and device. Location is not required and will be calculated from the device's data.

### DutyStatusLogSearch

The object used to specify the arguments when searching for[DutyStatusLog](DutyStatusLog/index.md)(s).

### DutyStatusLogType

The type of[DutyStatusLog](DutyStatusLog/index.md).

### DutyStatusMalfunctionTypes

Malfunction or Diagnostic type of the[DutyStatusLog](DutyStatusLog/index.md).

### DutyStatusOrigin

The origin of a[DutyStatusLog](DutyStatusLog/index.md).

### DutyStatusState

The state of the[DutyStatusLog](DutyStatusLog/index.md)record.

### DutyStatusViolation

A[DutyStatusLog](DutyStatusLog/index.md)violation for a[User](User/index.md).

### DutyStatusViolationSearch

The object used to specify the arguments when searching for[DutyStatusViolation](DutyStatusViolation/index.md)(s). This search has been designed to work efficiently with these combinations of parameters:
- UserSearch + FromDate and/or ToDate

### DutyStatusViolationType

The different types of[DutyStatusViolation](DutyStatusViolation/index.md).

### EVStatusInfo

The EVStatusInfo entity provides insights about the current state of an electric vehicle.

### EVStatusInfoSearch

The object used to specify the arguments when searching for a[EVStatusInfo](EVStatusInfo/index.md).

### ElectricEnergyEconomyUnit

Various Electric Energy Economy units Geotab supports. Currently supported units: L-e/100 km, km/L-e, kWh/100 km, Wh/km, km/kWh, MPG-e (US), MPG-e (Imp), kWh/100 miles, Wh/mile and mile/kWh.

### ElectricEnergyUnit

Various supported Electric Energy units Geotab supports.

### EmissionComplianceEvent

Represents a significant event in the compliance timeline of a vehicle's Clean Truck Check (CTC) enrollment.This entity logs key milestones, such as the initial enrollment, scheduled compliance actions, report submissions to the Californian Air Resources Board (CARB), and the resulting compliance status feedback.Security clearance requirements:
- Creating/Updating (Add/Set requests) for EmissionComplianceEvent are not available to API users.
- Retrieving (Get requests) requires one of the following clearances: AccessCleanTruckCheckCompliance, AccessCleanTruckCheckComplianceEditor, or AccessCleanTruckCheckComplianceViewer.

### EmissionComplianceEventSearch

A search object for finding specific[EmissionComplianceEvent](EmissionComplianceEvent/index.md)records.

### EmissionEnrollmentLoggingFrequencyType

Represents Clean Truck Check emission enrollment logging frequency types.

### EmissionVehicleEnrollment

A Clean Check Truck emission vehicle enrollment. One[Device](Device/index.md)should only have one active enrollment with status Pending or Enrolled.Security clearance requirements:Creating EmissionVehicleEnrollment (Add requests) requires security clearances AccessCleanTruckCheckCompliance;Updating EmissionVehicleEnrollment (Set requests) requires one of the following security clearances AccessCleanTruckCheckCompliance or AccessCleanTruckCheckComplianceEditor;Note: AccessCleanTruckCheckComplianceEditor is not allowed for disenrolling an enrollment.Retrieving EmissionVehicleEnrollment (Get requests) requires one of the following security clearances AccessCleanTruckCheckCompliance, AccessCleanTruckCheckComplianceEditor or AccessCleanTruckCheckComplianceViewer.

### EmissionVehicleEnrollmentSearch

Search class for[EmissionVehicleEnrollment](EmissionVehicleEnrollment/index.md).

### Entity

All objects that are stored in the database are entities. They are uniquely identified by their[Id](Id/index.md)which is used later to Get, modify (Set) or Remove that object. The following entities are supported:
- [A1](https://developers.geotab.com/myGeotab/apiReference/objects/A1/)
- [AddInData](AddInData/index.md)
- [AnnotationLog](AnnotationLog/index.md)
- [Audit](Audit/index.md)
- [BinaryPayload](BinaryPayload/index.md)
- [Condition](Condition/index.md)
- [Controller](Controller/index.md)
- [CustomData](CustomData/index.md)
- [CustomDevice](CustomDevice/index.md)
- [DataDiagnostic](DataDiagnostic/index.md)
- [DebugData](DebugData/index.md)
- [Device](Device/index.md)
- [DeviceShare](DeviceShare/index.md)
- [DeviceStatusInfo](DeviceStatusInfo/index.md)
- [Diagnostic](Diagnostic/index.md)
- [DistributionList](DistributionList/index.md)
- [Driver](Driver/index.md)
- [DriverChange](DriverChange/index.md)
- [DutyStatusAvailability](DutyStatusAvailability/index.md)
- [DutyStatusLog](DutyStatusLog/index.md)
- [DutyStatusViolation](DutyStatusViolation/index.md)
- [DVIRLog](DVIRLog/index.md)
- [EmissionComplianceEvent](EmissionComplianceEvent/index.md)
- [EmissionVehicleEnrollment](EmissionVehicleEnrollment/index.md)
- [ExceptionEvent](ExceptionEvent/index.md)
- [FailureMode](FailureMode/index.md)
- [FaultData](FaultData/index.md)
- [FillUp](FillUp/index.md)
- [FlashCode](FlashCode/index.md)
- [FuelTaxDetail](FuelTaxDetail/index.md)
- [FuelUsed](FuelUsed/index.md)
- [FuelTransaction](FuelTransaction/index.md)
- [Go5](Go5/index.md)
- [Go6](Go6/index.md)
- [Go7](Go7/index.md)
- [Go8](Go8/index.md)
- [Go9](Go9/index.md)
- [Go9B](https://developers.geotab.com/myGeotab/apiReference/objects/Go9B/)
- [GoCurve](GoCurve/index.md)
- [GoCurveAuxiliary](GoCurveAuxiliary/index.md)
- [GoDevice](GoDevice/index.md)
- [Group](Group/index.md)
- [GroupSecurity](GroupSecurity/index.md)
- [IoxAddOn](IoxAddOn/index.md)
- [LogRecord](LogRecord/index.md)
- [MediaFile](MediaFile/index.md)
- [ParameterGroup](ParameterGroup/index.md)
- [Recipient](Recipient/index.md)
- [RequestLocation](RequestLocation/index.md)
- [Route](Route/index.md)
- [RoutePlanItem](RoutePlanItem/index.md)
- [Rule](Rule/index.md)
- [SecurityClearance](SecurityClearance/index.md)
- [ShipmentLog](ShipmentLog/index.md)
- [Source](Source/index.md)
- [StatusData](StatusData/index.md)
- [TachographDataFile](TachographDataFile/index.md)
- [TextMessage](TextMessage/index.md)
- [Trailer](Trailer/index.md)
- [TrailerAttachment](TrailerAttachment/index.md)
- [Trip](Trip/index.md)
- [UnitOfMeasure](UnitOfMeasure/index.md)
- [User](User/index.md)
- [WifiHotspot](WifiHotspot/index.md)
- [WorkHoliday](WorkHoliday/index.md)
- [WorkTime](WorkTime/index.md)
- [WorkTimeDetail](WorkTimeDetail/index.md)
- [Zone](Zone/index.md)

### EntityWithVersion

An Entity with a version.

### ExceptionEvent

The event of an exception generated by Rule violation.

### ExceptionEventSearch

The object used to specify the arguments when searching for[ExceptionEvent](ExceptionEvent/index.md). This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + RuleSearch + FromDate and/or ToDate

### ExceptionEventState

Specify the current state of the[ExceptionEvent](ExceptionEvent/index.md).

### ExceptionRuleBaseType

When exceptions are created based on built-in rules, the base type is always set to "Stock". For rules which are defined by you, the base type will be "Custom". The ZoneStop base type is used to designate exceptions created specifically when a zone is configured with the "MustIdentifyStops" property set to true.

### ExceptionRuleCategory

Specific categories to which the exception rules belong.

### ExceptionRuleType

This enumerated type allows designating rules to be of a certain type to assist with differentiating them from one another.

### ExpiredPasswordException

This exception is thrown if a user makes a request while their ChangePassword flag is true. The user must change their password before they are able to successfully make further requests.

### FailureMode

The Failure Mode Identifier (FMI) used to describe engine fault codes. This is represented by the string "NoFailureModeId" when there is no applicable FMI.

### FailureModeSearch

The object used to specify the arguments when searching for a[FailureMode](FailureMode/index.md).

### FaultData

A record that represents a fault code record from the engine system of the specific[Device](Device/index.md).

### FaultDataSearch

The object used to specify the arguments when searching for a[FaultData](FaultData/index.md). This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + DiagnosticSearch + FromDate and/or ToDate
- GroupSearch + DiagnosticSearch + FromDate and/or ToDate

### FaultLampState

Represents the lamp status of a J1939 fault, see[FaultData](FaultData/index.md).

### FaultResetMode

Specify whether the fault resets automatically or manually.

### FaultState

Represents a fault code state code from the engine system of the specific[Device](Device/index.md). This properties using this enum will be deprecated in the near future and replaced by a property of the[FaultStatus](FaultStatus/index.md)type.

### FaultStateProvider

Class to describe the current FaultState when a single one is present.

### FaultStatus

Class to describe FaultState.

### FeedResult

An object containing the result of a feed method.

### FieldSelector

An abstract class for different types of field selectors.

### FillUp

An event representing adding fuel to an asset. Many sources of data are evaluated to determine a fill-up.[FuelTransaction](FuelTransaction/index.md)s,[StatusData](StatusData/index.md)(fuel level percent, fuel level volume, fuel used, tank capacity, odometer),[LogRecord](LogRecord/index.md)s,[Trip](Trip/index.md)s are all used to calculate fill-up events.

### FillUpExtrema

Represents the low and high values of fuel level for a fill-up.

### FillUpExtremum

An event representing fuel level of a vehicle. An extremum representing either the minimum or maximum point of fuel used for a given[FillUp](FillUp/index.md).

### FillUpSearch

The object used to specify the arguments when searching for[FillUp](FillUp/index.md). This search has been designed to work efficiently with these parameters:
- Id
- DeviceSearch + FromDate and/or ToDate

### FlashCode

The optional summary code references for specific[Diagnostic](Diagnostic/index.md)items referencing[FaultData](FaultData/index.md)records.

### FuelAndEnergyUsed

An event representing fuel and energy used for a vehicle.

### FuelAndEnergyUsedSearch

The object used to specify the arguments when searching for[FuelAndEnergyUsed](FuelAndEnergyUsed/index.md). This search has been designed to work efficiently with these parameters:
- Id
- DeviceSearch + FromDate and/or ToDate

### FuelEconomyUnit

Various Fuel Economy units Geotab supports. Currently supported units: L/100 km, km/L, MPG (US), MPG (Imperial), km/gallon (US), and gal/100km.

### FuelEvent

Log of fueling events.

### FuelTankCapacity

Represent a vehicle's fuel tank capacity and how it was derived.

### FuelTankCapacitySource

The source from which tank capacity was derived.

### FuelTaxData

A collection of properties based on[FuelTaxDetail](FuelTaxDetail/index.md)elements. Used to populate a row in a fuel tax report.

### FuelTaxDetail

Fuel tax reporting element. The available driving history for a[Device](Device/index.md)is stored as a sequence of such details. Each next detail starts when and where the previous detail ended. A detail is identified by its parameters (enter and exit time, odometer, GPS odometer, latitude and longitude) and its attributes (jurisdiction,[Driver](Driver/index.md), toll road, authority). When any of the attributes changes, the current detail ends and a new detail begins. For more information, see[IFTA Guide](https://docs.google.com/document/d/1vqQYJEIrUqOJ0LlFEeY1iVddcC-I4DTY2z73NE0Nzug).

### FuelTaxDetailSearch

The object used to specify the arguments when searching for[FuelTaxDetail](FuelTaxDetail/index.md)elements.This search has been designed to work efficiently with these parameters:
- DeviceSearch
- FromDate
- ToDate

### FuelTransaction

Information from a fuel card provider representing a fuel transaction. Fuel card information will be matched to a[Device](Device/index.md)by one of these fields: vehicleIdentificationNumber, serialNumber, licencePlate or comments.

### FuelTransactionProductType

Represents the type of product purchased in a[FuelTransaction](FuelTransaction/index.md).

### FuelTransactionProvider

[FuelTransaction](FuelTransaction/index.md)data providers.

### FuelUsed

An event representing fuel used for a vehicle.

### FuelUsedSearch

The object used to specify the arguments when searching for[FuelUsed](FuelUsed/index.md). This search has been designed to work efficiently with these parameters:
- Id
- DeviceSearch + FromDate and/or ToDate

### GenericException

This default exception returned undefined issues.

### Go5

The Geotab GO5 device. Additional properties can be seen in[GoCurve](GoCurve/index.md).

### Go6

The Geotab GO6 device. Additional properties can be seen in[GoCurveAuxiliary](GoCurveAuxiliary/index.md).

### Go7

The Geotab GO7 device. Additional properties can be seen in[GoCurveAuxiliary](GoCurveAuxiliary/index.md).

### Go8

The Geotab GO8 device. Additional properties can be seen in[GoCurveAuxiliary](GoCurveAuxiliary/index.md).

### Go9

The Geotab GO9 device. Additional properties can be seen in[GoCurveAuxiliary](GoCurveAuxiliary/index.md).

### GoAnywhere

The GO Anywhere device. Additional properties can be seen in[XDevice](XDevice/index.md).

### GoAnywhereLite

The GO Anywhere Lite device. Additional properties can be seen in[XDevice](XDevice/index.md).

### GoCurve

A GoCurve device. Additional properties can be seen in[GoDevice](GoDevice/index.md).

### GoCurveAuxiliary

Device that supports curve logging and auxiliaries. Additional properties can be seen in[GoCurve](GoCurve/index.md).

### GoDevice

The base device for all Geotab GO products. Additional properties can be seen in[Device](Device/index.md).

### GoDriveDevice

A mobile tracking device that is used in MyGeotab. This is used for extensibility and is based on the[Device](Device/index.md)object.

### GoTalkContent

The contents of a[TextMessage](TextMessage/index.md)that will be delivered to a GoTalk.

### GoTalkLanguage

The language used by a GoTalk attached to a.[GoDevice](GoDevice/index.md)

### GoogleMapStyle

Used to represent different Google Map styles.

### GpsAccelerationResult

GPS acceleration result.

### Group

A group is one element in a hierarchical tree. Each group can have none or many children, it is the children that define the shape of the hierarchical tree. The parent is not a property of the group object and is only defined by who the group is a child of. It is necessary to know the id of the parent group when adding a new group.There are three core Group branches used in MyGeotab. The most common are "Company Groups", company Groups are used to organize entities ([Zone](Zone/index.md),[User](User/index.md),[Device](Device/index.md),[Driver](Driver/index.md)and[Rule](Rule/index.md)) into logical groups related to the organization. A Group structure can be constructed by region, vocation, reporting or anything that makes sense to the business, this allows aggregate reports and rolling up data in a flexible way. These groups have a many to many type of relationship with the entities that are members and are not limited to one type of entity.The second type is "Security Groups", these are Groups to which[User](User/index.md)(s) are members of and can only be applied to Users. Each Group has a list of[SecurityFilter](SecurityFilter/index.md)(s) associated to it. Security Filters control what parts of the application/API a User has access to.The third type of group is a "Private User Group", this group is used only for scheduling reports and displaying dashboard reports for a User. This Group will only ever apply to one User and will typically be named the user's name.There is a base structure of Groups which cannot be removed, these are considered to be "System"Some of these groups are:
- Company Group
- Asset Information Group
- Driver Activity Group
- Security Group
- Supervisor Security Group
- View Only Security Group
- Drive User Security Group
- Private User Group

When Groups are retrieved they will always be in a flat list of groups. The hierarchically tree(s) can be reconstructed by looking at the "Children" property of each Group. The "Root" group will never be returned and is only for system use.

### GroupRelationViolatedException

Exception with information about the grouped linked entities that hold a relation preventing removal.

### GroupRelations

Used in GroupRelationViolatedException. When a user tries to remove a group but there are entities which are members of those groups the remove is blocked (fails) until the entities are moved out of the group which is to be removed. When the group remove operation fails, the exception returned is a GroupRelationViolatedException with populated GroupRelations to show which entities are blocking the group removal.

### GroupSearch

The object used to specify the arguments when searching for a[Group](Group/index.md).

### GroupSecurity

Represents a GroupSecurity entity. This defines the many to many relationship between a[SecurityFilter](SecurityFilter/index.md)and[Group](Group/index.md).

### HereMapStyle

Here Map Style.

### HosOption

The HOS log generation options.

### HosRuleSet

HOS rulesets for the[User](User/index.md).

### Id

This is an identifier for an[Entity](Entity/index.md)object in the Geotab system. In JavaScript this is a string.

### IncludeGroups

The IncludeGroups enum provides a method of querying for entities relative to the entity's position in the hierarchy of[Group](Group/index.md)(s). Some entity types (such as[Zone](Zone/index.md)(s)) have implications to entities in their child groups. For example; on a map, it may be useful to include[Zone](Zone/index.md)(s) that are above the user's data scope groups. These[Zone](Zone/index.md)(s) will also apply to vehicles that are at or below the selected[Group](Group/index.md)(s) of the[Zone](Zone/index.md).

### InvalidApiOperationException

This exception is thrown when a user attempts to perform an action that is not valid according to the API process.

### InvalidMyAdminUserException

This exception is thrown on a MyAdmin databaseName logon with an incorrect user/password combination or when the MyAdmin user's credentials become invalid on a databaseName.

### InvalidPermissionsException

This exception is thrown when a user attempts to perform an action without sufficient permissions.

### InvalidUserException

This exception is thrown on a logon with an incorrect user/password combination or when the user's credentials become invalid.

### IoxAddOn

Represents an Iox Add-On (like modem or navigation device) that is attached to a GO unit. Each Iox Add-On is assigned a channel - which is the serial port number that it typically communicates with.

### IoxAddOnSearch

The object used to specify the arguments when searching for[IoxAddOn](IoxAddOn/index.md)(s).

### IoxAddOnStatus

Represents the status of an IoxAddOn that is attached to a GO unit.

### IoxAddOnStatusSearch

The object used to specify the arguments when searching for[IoxAddOnStatus](IoxAddOnStatus/index.md)(s).

### IoxOutputContent

The contents of a[TextMessage](TextMessage/index.md)that can be used to control the state of an IOX-OUTPUT.

### ItemName

An object containing key value pairs for the text that appears on the item. The key is the language and the value is the text, for example: {"EN", "New item"}.

### JsonRpcError

Models a JSON-RPC error provided as "error" property of JSON-RPC response object when an error is encountered while making a request. http://www.jsonrpc.org/specification#error_object.

### JsonRpcErrorData

The implementation specific error data for a JSON-RPC request error.

### Jurisdiction

Mapping of jurisdiction regions.

### KnownId

All the system Ids.

### KnownIoxAddOnType

A unique identifier for different types[IoxAddOn](IoxAddOn/index.md)s. The range of valid values is between 4096 (inclusive) and 8192.

### Language

Type that represents language options

### Leg

A single leg of[Directions](Directions/index.md)between origin and destination[Waypoint](Waypoint/index.md)s.

### LocationContent

Message content that can send a GPS location to a device. Derived from[TextContent](TextContent/index.md).

### LogRecord

Record of log entries containing data for a device's position and speed at a specific date and time.

### LogRecordSearch

The object used to specify the arguments when searching for[LogRecord](LogRecord/index.md)(s). When searching for log records the system will return all records that match the search criteria and interpolate the value at the provided from/to dates when there is no record that corresponds to the date. Interpolated records are dynamically created when the request is made and can be identified as not having the ID property populated. Records with an ID are stored in the database.This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + FromDate and/or ToDate

### LoginResult

The results of an authentication attempt.

### Map

Represents the Map Add-in item.

### MapScript

Represents the MapScript for Map item.

### MapView

A Map View with a name and a viewport.

### MaxRoadSpeedResult

Maximum road speed result.

### MediaFile

The entity which describes the binary media.

### MediaFileSearch

The object used to specify the arguments when searching for[MediaFile](MediaFile/index.md). This will return the data describing a file, not the actual file.

### MediaType

The type of a[MediaFile](MediaFile/index.md).

### Menu

Represents the Add-In Menu item.

### MessageContentType

The type of[TextMessage](TextMessage/index.md)content.

### MimeContent

The contents of a[TextMessage](TextMessage/index.md)containing data to give to a IOX Add-On over an RS232. It holds more data than[SerialIoxContent](SerialIoxContent/index.md)and is not compatible with all Add-Ons. For more information regarding Add-On compatible please contact your reseller. MimeContent is converted into bytes with a specific format. The first byte is the length of the MimeType (N). The next N bytes are the ASCII encoded bytes of the MimeType string. The next two bytes are the length of the Data (L). Finally, the next L bytes are the Data. Messages from MyGeotab will be delivered in this format and messages to MyGeotab must be in this format as well.

### MimeContentBase

The contents of a[TextMessage](TextMessage/index.md)containing data to give to a IOX Add-On over an RS232. It holds more data than[SerialIoxContent](SerialIoxContent/index.md)and is not compatible with all Add-Ons. For more information regarding Add-On compatible please contact your reseller. MimeContent is converted into bytes with a specific format. The first byte is the length of the MimeType (N). The next N bytes are the ASCII encoded bytes of the MimeType string. The next two bytes are the length of the Data (L). Finally, the next L bytes are the Data. Messages from MyGeotab will be delivered in this format and messages to MyGeotab must be in this format as well.

### NameEntity

An[Entity](Entity/index.md)that has a name field.

### NameEntityWithVersion

An entity with a name and a version.

### OpenStreetMapStyle

Used to represent different Open Street Map (OSM) styles.

### OverLimitException

Represents an exception thrown when a users has exceeded the query limit of an API.

### ParameterGroup

Standard Parameter Group Number (PGN). Where there is no parameter group it is represented by "ParameterGroupNoneId".

### ParameterGroupSearch

The object used to specify the arguments when searching for a[ParameterGroup](ParameterGroup/index.md).

### PointF

A point with a float X and Y.

### PostedRoadSpeedOptions

Defines options for a posted road speed request.

### PropertySelector

The class contains the collection of object property names. The fields are matched on case-insensitive basis and included or excluded from the result, depending on isIncluded flag.

### RangeEstimate

The distance a BEV or PHEV can travel on a full charge. The range estimate is based on historical energy consumption, distance traveled, and battery capacity.

### RangeEstimateSearch

The object used to specify the arguments when searching for a[RangeEstimate](RangeEstimate/index.md).

### RateLimitInfo

Information about the rate limits.

### Recipient

The recipient for a specific notification. A recipient is linked to[Rule](Rule/index.md)(s) via a[DistributionList](DistributionList/index.md). When a[Rule](Rule/index.md)is violated the[DistributionList](DistributionList/index.md)linked recipient receives a notification. The type of recipient is defined by it's[RecipientType](RecipientType/index.md). Not all properties of this object will have a value at the same time they are dependent on the[RecipientType](RecipientType/index.md). Recipient is represented by the string "NoRecipientId" where there is no recipient.

### RecipientType

The type of notification message that is generated for a[Recipient](Recipient/index.md).

### RectangleF

A Rectangle with a float X, Y, Width and Height.

### Region

Type that represents a region option

### RegistrationException

This exception is thrown when there is an exception creating/registering a new database.

### RepairStatusType

The Repair Status for[DVIRDefect](DVIRDefect/index.md).

### RequestLocation

A message that requests the current location of a device through Iridium.

### ReverseGeocodeAddress

The address and[Zone](Zone/index.md)(if any found) returned by a reverse geocode operation.

### Route

A connected sequence of zones which create a path for the vehicle to follow.

### RoutePlanItem

The class representing an individual item in a planned[Route](Route/index.md).

### RouteSearch

The object used to specify the arguments when searching for[Route](Route/index.md)(s).

### RouteType

A type of[Route](Route/index.md).

### Rule

A rule is the definition of conditions that, when "violated", will generate an[ExceptionEvent](ExceptionEvent/index.md). The rule's logic is defined by it's tree of[Condition](Condition/index.md)(s). It's condition tree will be evaluated against data for device(s) that are members of the rule's assigned group(s) or the device(s)/driver(s) defined in the rule condition tree. The conditions will be evaluated independently against the assets in the selected groups.

### RuleSearch

The object used to specify the arguments when searching for a[Rule](Rule/index.md).

### Search

Search that implements IEntity for search objects.

### SecurityClearance

Represents a[Group](Group/index.md)with[SecurityFilter](SecurityFilter/index.md)(s) that are used to determine security access to different parts of the application.

### SecurityFilter

Represents an item that either Adds or Removes a particular[SecurityIdentifier](SecurityIdentifier/index.md)to a user's set of allowed items.

### SecurityIdentifier

The list of identifiers that gives a security identity to something whose access can be controlled.

### SerialIoxContent

The contents of a[TextMessage](TextMessage/index.md)containing data to give to a third-party IOX Add-On over an RS232. The SerialIoxContent is a 'dumb pipe' type of message. Whatever data is put in the data property will be delivered, as is, to the system on the other end of the IOX-RS232.

### ShipmentLog

A ShipmentLog is a record of shipment transported by a specified vehicle for a duration of time.

### ShipmentLogSearch

The object used to specify the arguments when searching for[ShipmentLog](ShipmentLog/index.md)(s).

### SortByDate

Implementation of ISort for sorting by the date field in[Entity](Entity/index.md)s.

### SortById

Implementation of ISort for sorting by the Id field in[Entity](Entity/index.md)s.

### SortByName

Implementation of ISort for sorting by name field in[Entity](Entity/index.md)s.

### SortByStart

Implementation of ISort for sorting by the start date field in[Entity](Entity/index.md)s.

### SortByStop

Implementation of ISort for sorting by the stop date field in[Entity](Entity/index.md)s.

### SortByVersion

Implementation of ISort for sorting by the version field in[Entity](Entity/index.md)s.

### Source

The source is the underlying producer of the engine data.

### SourceSearch

The object used to specify the arguments when searching for a[Source](Source/index.md).

### Status

The status of an uploaded file.

### StatusData

A record that represents an engine status record from the engine system of the specific[Device](Device/index.md).

### StatusDataSearch

The object used to specify the arguments when searching for[StatusData](StatusData/index.md). When searching for status data including DeviceSearch and DiagnosticSearch the system will return all records that match the search criteria and interpolate the value at the provided from/to dates when there is no record that corresponds to the date. Interpolated records are dynamically created when the request is made and can be identified as not having the ID property populated. Records with an ID are stored in the database.This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + DiagnosticSearch + FromDate and/or ToDate

### Step

A single step in a sequence of step-by-step instructions to complete[Leg](Leg/index.md)of[Directions](Directions/index.md).

### TachographDataFile

The entity which describes the tachograph data file.Notes: Although possible, it is not recommended to directly introduce new entities of this type with the Add API call. New entities are created through other means in the application (i.e. scheduled remote downloads from the Tachograph).

### TachographDataFileSearch

The object used to specify the arguments when searching for[TachographDataFile](TachographDataFile/index.md).

### TachographDriverActivity

The entity that contains the data for the[TachographDriverActivity](TachographDriverActivity/index.md)tachograph driver activity extractor.

### TachographDriverActivitySearch

The object used to specify the arguments when searching for[TachographDriverActivity](TachographDriverActivity/index.md).

### TachographDrivingTimeStatus

The entity that contains the data for the[TachographDrivingTimeStatus](TachographDrivingTimeStatus/index.md)tachograph driving time status extractor.

### TachographDrivingTimeStatusSearch

The object used to specify the arguments when searching for[TachographDrivingTimeStatus](TachographDrivingTimeStatus/index.md).

### Tag

A named tag to provide context to an entity.

### TagSearch

The object used to specify the arguments when searching[Tag](Tag/index.md)entries.

### TextContent

The contents of a GPS Text Message. See also:.
- [CannedResponseContent](CannedResponseContent/index.md)
- [LocationContent](LocationContent/index.md)

### TextMessage

A message to send or received from a device.When working with text messages it is important to make the distinction between a "Reply" and a "Response".
- Reply: A reply is a Text Message that is a Reply to another text message. For example: A text message is sent to a device and the device replies with a text message of it's own.
- Response: A response is a predefined ("canned") response within a text message. For example: A text message is sent to a device with a number of canned responses to reply with (Yes, No, Maybe). One of those responses is selected by the driver and is the message of the Reply from the device.

### TextMessageContentType

The type of the text message content.

### TextMessageSearch

The object used to specify the arguments when searching for a[TextMessage](TextMessage/index.md).

### TimeZoneInfo

Data for Olson Timezone conversion.

### TimeZoneInfoAdjustmentRule

Adjustment rule for timezones.

### TimeZoneInfoWithRules

Timezone info with its day light saving rules.

### Trailer

A trailer which can be attached and detached from a vehicle with a[TrailerAttachment](TrailerAttachment/index.md)record.

### TrailerAttachment

A TrailerAttachment is a record of the attachment of a[Trailer](Trailer/index.md)to a[Device](Device/index.md)over a period of time.

### TrailerAttachmentSearch

The object used to specify the arguments when searching for[TrailerAttachment](TrailerAttachment/index.md)record(s).

### TrailerSearch

The object used to specify the arguments when searching for[Trailer](Trailer/index.md)(s).

### TransitionTime

Transition time for adjustment rule.

### Trip

This is a vehicles trip and a summary of the driving activity during that trip. To get more information about stops during a trip please see[ExceptionEvent](ExceptionEvent/index.md). A complete "trip" is defined as starting at the time in which the vehicle starts and begins being driven. The trip continues after the vehicle has been stopped and ends at the time the vehicle restarts and begins being driven again; which then starts the next trip.

### TripSearch

The object used to specify the arguments when searching for[Trip](Trip/index.md)(s). This search has been designed to work efficiently with these combinations of parameters:
- Id
- DeviceSearch + FromDate and/or ToDate (+ IncludeOverlappedTrips)
- UserSearch + FromDate and/or ToDate (+ IncludeOverlappedTrips)

### UnitOfMeasure

Describes the unit of measure (UOM) for engine data logs. In the case where no unit of measure is available; this is represented by "UnitOfMeasureNoneId".

### UnitOfMeasureSearch

The object used to specify the arguments when searching for a[UnitOfMeasure](UnitOfMeasure/index.md).

### UntrackedAsset

An untracked asset that is used in MyGeotab without a serial number. This is used for extensibility and is based on the[Device](Device/index.md)object.

### User

A user of the system. A user can be a MyGeotab user or a user that is a[Driver](Driver/index.md).

### UserAuthenticationType

The user authentication type.

### UserSearch

The object used to specify the arguments when searching for a[User](User/index.md)/[Driver](Driver/index.md).

### UserSearchType

The type of[UserSearchType](UserSearchType/index.md)to search for.

### VehicleConfiguration

VehicleConfiguration parameters entity.

### VehicleConfigurationSearch

The object used to specify the arguments when searching for[VehicleConfiguration](../../../index.md#VehicleConfiguration)(s).

### VersionInformation

Software version information for the server.

### VersionInformationResult

Software version information for the Gateway.

### VolumeUnit

Various supported Volume units Geotab supports.

### Waypoint

A set of coordinates that reference a location.

### WifiHotspot

WifiHotspot is used to configure WiFi hotspot settings on telematics devices.

### WifiHotspotData

Parameters for WiFi hotspot.

### WifiHotspotSearch

The object used to specify the arguments when searching for a[WifiHotspot](WifiHotspot/index.md).

### WorkHoliday

Day that is specified as not being a regular working day.

### WorkHolidaySearch

The object used to specify the arguments when searching for a[WorkHoliday](WorkHoliday/index.md).

### WorkTime

The set of[WorkTimeDetail](WorkTimeDetail/index.md)(s) defining periods during the week that are considered as part of regular working hours. Work times that apply to all times are represented by "WorkTimeAllHoursId".

### WorkTimeDetail

The times during the week that are working times.

### WorkTimeHolidayGroupId

Work holidays. See[WorkHoliday](WorkHoliday/index.md)and[WorkTime](WorkTime/index.md). Items can be grouped together by giving them all the same GroupId number.

### WorkTimeSearch

The object used to specify the arguments when searching for a[WorkTime](WorkTime/index.md).

### XDevice

The base device for all Geotab GO products. Additional properties can be seen in[Device](Device/index.md).

### Zone

Sometimes referred to as a "Geofence", a zone is a virtual geographic boundary, defined by its points representing a real-world geographic area.

### ZoneDisplayMode

The[Zone](Zone/index.md)s which will be displayed to a given user on the map.

### ZoneSearch

The object used to specify the arguments when searching for[Zone](Zone/index.md)(s).

### ZoneType

The type of the zone.

### ZoneTypeSearch

The object used to specify the arguments when searching for[ZoneType](ZoneType/index.md)(s).