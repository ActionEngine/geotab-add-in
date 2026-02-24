### Add (...)

Adds a new[Entity](../objects/Entity/index.md)to the database. This method is used to add the different entities to the database, for example[Device](../objects/Device/index.md),[User](../objects/User/index.md)or[Zone](../objects/Zone/index.md). In addition to the credentials, the method will require a minimum of two parameters - the type of entity that is being added (typeName) and the entity itself. In most cases, the entity being added will need to be fully constructed. In other words, all its properties need to be defined. These requirements are defined in each of the entity definitions below.

### Authenticate (...)

Authenticates a user and provides a[LoginResult](../objects/LoginResult/index.md)if successful. The authentication pattern is documented in the Concepts sections of the SDK.Throws:
- [InvalidUserException](../objects/InvalidUserException/index.md)
- [DbUnavailableException](../objects/DbUnavailableException/index.md)
- [OverLimitException](../objects/OverLimitException/index.md)

### CreateDatabase (...)

Creates new uniquely named database on a server in the federation. Requires either a valid CaptchaAnswer and/or valid MyAdmin user credentials. See https://github.com/Geotab/sample-registration for an example.

### DownloadMediaFile (...)

Download a file for the given[MediaFile](../objects/MediaFile/index.md). The Content-Type is determined by the file extension. Range headers are supported.

### EmissionEnrollDevices (...)

Enrolls devices for Clean Truck Check emission reporting.Requires the AccessCleanTruckCheckCompliance security clearance.

### GenerateCaptcha (...)

Generates a single use CAPTCHA image for the given key and serves the result as "image/png" content.

### Get (...)

Gets the[Entity](../objects/Entity/index.md)(s) for the given entityType. This method can be used in various ways to return all, one or some specific set of data for the[Entity](../objects/Entity/index.md)(s).

### GetAddresses (...)

Gets addresses from the list of[Coordinate](../objects/Coordinate/index.md)(s), as well as any[Zone](../objects/Zone/index.md)s in the system that contain the given coordinates.

### GetCoordinates (...)

Geocodes or looks up the latitude and longitude from a list of addresses.

### GetCountOf (...)

Gets the count of the specified[Entity](../objects/Entity/index.md)type from the database. Entities that are currently inactive (the Entity's ActiveTo date is before the current time) are counted as well.

### GetDaylightSavingRules (...)

Get a Timezone's TimeZoneInfoWithRules by the timeZoneId.

### GetDirections (...)

Gets step-by-step driving[Directions](../objects/Directions/index.md)for a sequence of[Waypoint](../objects/Waypoint/index.md)s including estimate travel time and distances.

### GetEmissionComplianceDeadline (...)

Gets the Clean Check Truck compliance enrollment status including the next compliance deadline for a device.Requires one of the following security clearances: AccessCleanTruckCheckCompliance, AccessCleanTruckCheckComplianceEditor or AccessCleanTruckCheckComplianceViewer.

### GetFeed (...)

This is the primary method used to sync data from the MyGeotab system for example all the GPS positions. The following entities are currently supported and must be set in the typeName.See[AnnotationLog](../objects/AnnotationLog/index.md)and[AnnotationLogSearch](../objects/AnnotationLogSearch/index.md)for Annotation Log related parameters.See[Audit](../objects/Audit/index.md)and[AuditSearch](../objects/AuditSearch/index.md)to provide a fromDate from which to seed the feed.See[ChargeEvent](../objects/ChargeEvent/index.md)and[ChargeEventSearch](../objects/ChargeEventSearch/index.md)for Charge Event related parameters.See[CustomData](../objects/CustomData/index.md)and[CustomDataSearch](../objects/CustomDataSearch/index.md)for Custom Data related parameters.See[DebugData](../objects/DebugData/index.md)and[DebugDataSearch](../objects/DebugDataSearch/index.md)for Debug Data related parameters.See[Device](../objects/Device/index.md)*search not supported. Maximum results: 5,000.See[DeviceShare](../objects/DeviceShare/index.md)*search not supported.See[DeviceStatusInfo](../objects/DeviceStatusInfo/index.md)*search not supported other than[DeviceStatusInfoSearch](../objects/DeviceStatusInfoSearch/index.md). Diagnostics property.See[Diagnostic](../objects/Diagnostic/index.md)*search not supported.See[DriverChange](../objects/DriverChange/index.md)and[DriverChangeSearch](../objects/DriverChangeSearch/index.md)to provide a fromDate from which to seed the feed.See[DutyStatusLog](../objects/DutyStatusLog/index.md)and[DutyStatusLogSearch](../objects/DutyStatusLogSearch/index.md)for Duty Status Log related parameters.See[DVIRLog](../objects/DVIRLog/index.md)and[DVIRLogSearch](../objects/DVIRLogSearch/index.md)for DVIR Log related parameters.See[EmissionComplianceEvent](../objects/EmissionComplianceEvent/index.md)and[EmissionComplianceEventSearch](../objects/EmissionComplianceEventSearch/index.md)for Emission Compliance Event related parameters.See[EmissionVehicleEnrollment](../objects/EmissionVehicleEnrollment/index.md)and[EmissionVehicleEnrollmentSearch](../objects/EmissionVehicleEnrollmentSearch/index.md)for Emission Vehicle Enrollment related parameters.See[ExceptionEvent](../objects/ExceptionEvent/index.md)and[ExceptionEventSearch](../objects/ExceptionEventSearch/index.md)for Exception Event related parameters.See[FailureMode](../objects/FailureMode/index.md)*search not supported.See[FaultData](../objects/FaultData/index.md)and[FaultDataSearch](../objects/FaultDataSearch/index.md)for Fault Data related parameters.See[FillUp](../objects/FillUp/index.md)and[FillUpSearch](../objects/FillUpSearch/index.md)for Fill Up related parameters. Maximum results: 10,000.See[FuelTaxDetail](../objects/FuelTaxDetail/index.md)and[FuelTaxDetailSearch](../objects/FuelTaxDetailSearch/index.md)for Fuel Tax Detail related parameters.See[FuelUsed](../objects/FuelUsed/index.md)and[FuelUsedSearch](../objects/FuelUsedSearch/index.md)for Fuel Used related parameters.See[FuelAndEnergyUsed](../objects/FuelAndEnergyUsed/index.md)and[FuelAndEnergyUsedSearch](../objects/FuelAndEnergyUsedSearch/index.md)for Fuel and Energy Used related parameters.See[IoxAddOn](../objects/IoxAddOn/index.md)and[IoxAddOnSearch](../objects/IoxAddOnSearch/index.md)for Iox Add-On related parameters.See[LogRecord](../objects/LogRecord/index.md)and[LogRecordSearch](../objects/LogRecordSearch/index.md)for Log Record related parameters.See[MediaFile](../objects/MediaFile/index.md)*search not supported. Maximum results: 10,000.See[Route](../objects/Route/index.md)and[RouteSearch](../objects/RouteSearch/index.md)to provide a fromDate from which to seed the feed. Maximum results: 10,000.See[Rule](../objects/Rule/index.md)(including ZoneStop[ExceptionRuleBaseType](../objects/ExceptionRuleBaseType/index.md)) *search not supported. Maximum results: 10,000.See[ShipmentLog](../objects/ShipmentLog/index.md)and[ShipmentLogSearch](../objects/ShipmentLogSearch/index.md)for Shipment Log related parameters.See[StatusData](../objects/StatusData/index.md)*search not supported.See[TextMessage](../objects/TextMessage/index.md)and[TextMessageSearch](../objects/TextMessageSearch/index.md)to provide a fromDate from which to seed the feed.See[Trailer](../objects/Trailer/index.md)*search not supported.See[TachographDataFile](../objects/TachographDataFile/index.md)and[TachographDataFileSearch](../objects/TachographDataFileSearch/index.md)to provide a user, device, type or from timestamp date to seed the feed.See[TrailerAttachment](../objects/TrailerAttachment/index.md)and[TrailerAttachmentSearch](../objects/TrailerAttachmentSearch/index.md)for Trailer Attachment related parameters.See[Trip](../objects/Trip/index.md)and[TripSearch](../objects/TripSearch/index.md)for Trip related parameters.See[User](../objects/User/index.md)(including[Driver](../objects/Driver/index.md)) *search not supported. Maximum results: 5,000.See[Zone](../objects/Zone/index.md)*search not supported. Maximum results: 10,000.This call is designed to allow incremental updates by returning a[FeedResult](../objects/FeedResult/index.md)which contains the last version from the set of data returned. This return version is then used as the fromVersion argument for the next call. This guarantees that no changes in the data can be missed and that all data is consistently returned. It is important to understand that this feed call only returns changes in the data; so that at least one change must be received, otherwise the state is considered unknown. This call would typically be made every minute or more, to keep the data near real-time and up to date. Provide search parameters to limit the scope of the data being returned. In some rare circumstances old data in the system can be modified. If this happens, that old data is resent (with the changes) as it will have a newer version. In your design you must consider this.It may be required to provide an entity search using from date to "back-fill" or "seed" data from a date in the past. Providing a from date guarantees that the feed will start at a version with all entities that have a date greater than or equal to the date provided. However, it is possible that the feed will return entities before the provided date. Searching using from date should be used independent of fromVersion and only on the first request.

### GetLanguages (...)

Gets all Languages as[Language](../objects/Language/index.md).

### GetPostedRoadSpeedsForDevice (...)

Get all posted road speed changes for a device's trips for the given dates. If the from date and to date are in the middle of the trip, the data for the whole trip are included.

### GetRegions (...)

Gets all Regions as[Region](../objects/Region/index.md).

### GetSystemTimeUtc (...)

Gets system time in UTC (Coordinated Universal Time).

### GetTimeZones (...)

Get a collection of[TimeZoneInfo](../objects/TimeZoneInfo/index.md)(Olson time zones).

### GetVersion (...)

The version of the server.

### GetVersionInformation (...)

The version information of the server.

### OptimizeWaypoints (...)

Optimizes a set of[Waypoint](../objects/Waypoint/index.md)(s).

### Remove (...)

Permanently removes an[Entity](../objects/Entity/index.md)and its associated data. The[Entity](../objects/Entity/index.md)object must have an[Id](../objects/Id/index.md)field. Remaining fields are optional. Note: the[Entity](../objects/Entity/index.md)does not function as a filter.

### Set (...)

Modify an[Entity](../objects/Entity/index.md)which is an object in the database. The id of the object must be populated.

### SetUserPassword (...)

Set the[User](../objects/User/index.md)'s password.

### UploadMediaFile (...)

Upload a file for the corresponding[MediaFile](../objects/MediaFile/index.md)using multipart/form-data POST request.