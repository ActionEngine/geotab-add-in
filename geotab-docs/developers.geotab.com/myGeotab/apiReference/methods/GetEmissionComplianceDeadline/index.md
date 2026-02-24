**Introduction**

Gets the Clean Check Truck compliance enrollment status including the next compliance deadline for a device.Requires one of the following security clearances: AccessCleanTruckCheckCompliance, AccessCleanTruckCheckComplianceEditor or AccessCleanTruckCheckComplianceViewer.

**Parameters**

## asOfDate

Optional date to check compliance deadlines as of a different time than now.

## credentials

The user's Geotab login[Credentials](../../objects/Credentials/index.md).

## device

The[Device](../../objects/Device/index.md)for which to retrieve compliance deadline information.

**Return value**

A[ComplianceEnrollmentStatus](../../objects/ComplianceEnrollmentStatus/index.md)object for the specified device.

**Code samples**

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| GetEmissionComplianceDeadline | Limit of 500 requests per 1m. | 500 | 1m | Active |