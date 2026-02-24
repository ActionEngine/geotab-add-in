**Introduction**

The recipient for a specific notification. A recipient is linked to[Rule](../Rule/index.md)(s) via a[DistributionList](../DistributionList/index.md). When a[Rule](../Rule/index.md)is violated the[DistributionList](../DistributionList/index.md)linked recipient receives a notification. The type of recipient is defined by it's[RecipientType](../RecipientType/index.md). Not all properties of this object will have a value at the same time they are dependent on the[RecipientType](../RecipientType/index.md). Recipient is represented by the string "NoRecipientId" where there is no recipient.

**Properties**

## Address

The email address used when sending notifications via Email.

## Group

The[Group](../Group/index.md)to assign the related device to.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## MediaTriggerSettings

The[MediaTriggerSettings](https://developers.geotab.com/myGeotab/apiReference/objects/MediaTriggerSettings/)to use for interacting with the media service.

## NotificationBinaryFile

The NotificationBinaryFile to notify with.

## RecipientType

The[RecipientType](../RecipientType/index.md)(type of notification message) this instance refers to.

## Severity

The severity level for CreateWorkRequest recipients.

## TripType

The[TripType](https://developers.geotab.com/myGeotab/apiReference/objects/TripType/)to assign the related device to.

## User

The[User](../User/index.md)to receive notification.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 100 Get requests per 1m. | 100 | 1m | Active |
| GetCountOf | Limit of 100 GetCountOf requests per 1m. | 100 | 1m | Active |