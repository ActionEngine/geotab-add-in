**Introduction**

The various statuses that a[DeviceShare](../DeviceShare/index.md)can have.

**Properties**

## Active

The device share request has been approved and is active.

## Cancelled

The device share has been cancelled by the source database before it was accepted by the target.

## Error

The data stream failed to start for the device share.

## Pending

The device share request is pending.

## Rejected

The device share has been rejected by the target database.

## RequestApproved

The incoming device share request has been accepted by a user on this database. This status will change to Active once the updated request has been processed.

## RequestCancelled

The incoming device share request has been cancelled by a user on this database before it was accepted by the target database (via the UI). This status will change to Cancelled once the updated request has been pulled from MyAdmin by the DeviceShareDownloaderService.

## RequestDeclined

The incoming device share request has been declined by a user on this database (via the UI). This status will change to Rejected once the updated request has been pulled from MyAdmin by the DeviceShareDownloaderService.

## RequestPending

The outgoing device share request has been created by a user on the source database and is waiting for MyAdmin to confirm the device share has been successfully created. This status will change to Pending once MyAdmin confirms.

## RequestTerminated

Termination of an incoming active device share has been requested by a user on this database. This status will change to Terminated once the updated request has been processed.

## Terminated

The active device share has been terminated by the target database.