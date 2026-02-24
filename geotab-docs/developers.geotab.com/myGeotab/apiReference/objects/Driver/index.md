**Introduction**

A driver in the system, and it is derived from[User](../User/index.md), with key ids and driver groups. If the driver is unknown then the driver is represented by "UnknownDriver".

**Properties**

## AcceptedEULA

A value indicating the user accepted MyGeotab EULA revision number. Default [null].

## ActiveDashboardReports

The list of active dashboards for the user, displayed on the dashboard page. Default [empty].

## ActiveDefaultDashboards

The list of default dashboards which must show real data. Default [empty].

## ActiveFrom

The date the user is active from. Default [UtcNow].

## ActiveTo

The date the user is active to. Default [MaxDate].

## AuthorityAddress

The HOS authority address of the user. Default [""].

## AuthorityName

The HOS authority name of the user. Default [""].

## AvailableDashboardReports

List of all available dashboard reports to the user. Default [empty].

## Bookmarks

The list of bookmarked pages. Default [empty].

## CannedResponseOptions

The user's stored list of custom response options to choose from when sending a[TextMessage](../TextMessage/index.md). Each item is a set of predefined response options. Default [empty].

## CarrierNumber

The carrier number. Default [""].

## ChangePassword

A flag indicating whether the user's password requires resetting. If [true], the user will be forced to change their password on next login. Default [false].

## Comment

Free text field where any user information can be stored and referenced for this entity. Default [""].

## CompanyAddress

The company address for the user. Default [""].

## CompanyGroups

The list of organization[Group](../Group/index.md)(s) that the user belongs to.

## CompanyName

The name of the company for the user. Default [""].

## CountryCode

The user two symbols country ISO code (https://www.iso.org/iso-3166-country-codes.html). Maximum length [2] Default [""]

## DateFormat

The format dates will be displayed to this user. Default ["MM/dd/yy HH:mm:ss"].

## DefaultGoogleMapStyle

The default[GoogleMapStyle](../GoogleMapStyle/index.md)tiles when using Google maps. Default [Roadmap].

## DefaultHereMapStyle

The default[HereMapStyle](../HereMapStyle/index.md)tiles when using Here Maps. Default [Roadmap].

## DefaultMapEngine

The default map engine to use for this user. System map engines are:
- GoogleMaps
- HereMap
- MapBox Default ["MapBox"].

## DefaultOpenStreetMapStyle

The default[OpenStreetMapStyle](../OpenStreetMapStyle/index.md)tiles when using Open Street Maps. Default [MapBox].

## DefaultPage

The default start page to view when login is complete. Maps to the hash portion of the web site URL (https://url/enpoint/[#page]). Default [map].

## Designation

The designation or title of the employee. Maximum length [50] Default [""].

## DisplayCurrency

The user's preferred currency for display in the UI.

## DriveGuideVersion

The driver's last viewed guide version. Default [0].

## DriverGroups

The home[Group](../Group/index.md)(s) for the driver.

## ElectricEnergyEconomyUnit

The user's preferred[ElectricEnergyEconomyUnit](../ElectricEnergyEconomyUnit/index.md)for viewing fuel economy. Default [LitersEPer100Km].

## EmployeeNo

The employee number or external identifier. Maximum length [50] Default [""].

## FeaturePreview

A comma-separated string value indicating which features user enabled to preview. Default [""].

## FirstDayOfWeek

The user's preferred day to represent the start of the week. Default ["Sunday"].

## FirstName

The first name of the user. Maximum length [255].

## FuelEconomyUnit

The user's preferred[FuelEconomyUnit](../FuelEconomyUnit/index.md)for viewing fuel economy. Default [LitersPer100Km].

## HosRuleSet

The[HosRuleSet](../HosRuleSet/index.md)the user follows. Default [None].

## Id

The unique identifier for the User. See[Id](../Id/index.md).

## IsAdverseDrivingEnabled

A value indicating whether the user is allowed to Adverse Driving conditions exempt. Default [true].

## IsDriver

The isDriver toggle, if [true] the user is a driver, otherwise [false]. Default [false].

## IsEmailReportEnabled

The isEmailReportEnabled toggle, if [true] the user will receive the emailed report, otherwise [false]. Default [true].

## IsEULAAccepted

A value indicating whether the old EULA has been accepted by the end user. Default [false].

## IsExemptHOSEnabled

A value indicating whether the user is allowed to HOS personal conveyance. Default [false].

## IsLabsEnabled

A value indicating whether labs are enabled for this user. When set to true this will enable experimental features that are still in the process of being developed. Default [false].

## IsMetric

Whether the current regional settings is in metric units of measurement (or US/Imperial). Default [true].

## IsNewsEnabled

A value that indicates whether news notifications are enabled for this user. Default [true].

## IsPersonalConveyanceEnabled

A value indicating whether the user is allowed to HOS personal conveyance. Default [false].

## IsYardMoveEnabled

A value indicating whether the user is allowed to HOS yard move. Default [false].

## JobPriorities

The list of selected job priorities. Default [empty].

## Keys

The NFC Key's serial number associated with the driver.

## Language

The user's culture identifier as a predefined[CultureInfo](https://docs.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo)name,[Name](https://docs.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo.name)of an existing System.Globalization.CultureInfo, or Windows-only culture name. Default: ["en"] for English.

## LastAccessDate

The user's last access date of the system.

## LastName

The last name of the user. Maximum length [255].

## LicenseNumber

The driver license number of the user. Default [""].

## LicenseProvince

The driver license province or state of the user. Default [""].

## MapViews

The list of the of the available[MapView](../MapView/index.md)s from the live map. Default [continent of the user's selected Timezone].

## MaxPCDistancePerDay

A value indicating the maximum personal conveyance distance per day in meters. Default [0].

## MediaFiles

The list of[MediaFile](../MediaFile/index.md)(s) photos of this user. Currently, a user can only be associated with at most one photo.

## Name

The user's email address / login name. Maximum length [255].

## Password

The user's password.

## PhoneNumber

The user phone number with space separated country phone code. Example +1 5555555555. Maximum length [20] Default [""]

## PhoneNumberExtension

The user phone number without formatting. Maximum length [5] Default [""]

## PrivateUserGroups

The private[Group](../Group/index.md)(s) that the user belongs to.

## ReportGroups

The report[Group](../Group/index.md)(s) for reporting that this user belongs to. The selected reporting groups will allow the user to sort entities that are children of the selected groups. It will not allow them to see entities that are outside of their data access. Default [empty].

## SecurityGroups

The security[Group](../Group/index.md)(s) this user belongs to; which define the user's access.

## ShowClickOnceWarning

A flag indicating whether to show ClickOnce support warning as the default page. (legacy) Default [false].

## TimeZoneId

The IANA Timezone Id of the user. All data will be displayed in this Timezone. Default ["America/New_York"].

## UserAuthenticationType

The[UserAuthenticationType](../UserAuthenticationType/index.md). This value indicates the type of a user's account. "BasicAuthentication" indicates a basic user. "MyAdmin" indicates a user with MyAdmin credentials. "MyAdmin" users are not visible to "BasicAuthentication" users. Default [Basic].

## Version

The version of the entity.

## ViewDriversOwnDataOnly

A value indicating whether the driver can view their own data.

## WifiEULA

A value indicating the user accepted Wifi specific EULA revision number. Default [0].

## ZoneDisplayMode

The default[ZoneDisplayMode](../ZoneDisplayMode/index.md)used on the map. Default [Default].

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| Set | Limit of 100 Set requests per 1m. | 100 | 1m | Active |
| Add | Limit of 150 Add requests per 1m. | 150 | 1m | Active |
| Remove | Limit of 100 Remove requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |
| GetFeed | Limit of 60 GetFeed requests per 1m. | 60 | 1m | Active |