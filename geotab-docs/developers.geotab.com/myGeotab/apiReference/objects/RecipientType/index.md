**Introduction**

The type of notification message that is generated for a[Recipient](../Recipient/index.md).

**Properties**

## AssignToGroup

The vehicle associate with the[ExceptionEvent](../ExceptionEvent/index.md)will be assigned to the designated group (removed from sibling groups). A[Group](../Group/index.md)is required.

## BeepTenTimesRapidly

Beep ten times rapidly using the GO device buzzer.

## BeepThreeTimes

Beep three times using the GO device buzzer.

## BeepThreeTimesRapidly

Beep three times rapidly using the GO device buzzer.

## Email

Recipient will be notified via either a simple email. A[User](../User/index.md)or valid Address is required. Optionally includes an EmailTemplate (NotificationBinaryFile).

## HosDisabled

Hos will be disabled.

## HosEnabled

Hos will be enabled.

## LogOnly

Recipient will be notified via a normal priority log that will appear in their Notifications. A[User](../User/index.md)is required.

## LogPopup

Recipient will be notified with a popup notification in the MyGeotab application that will also appear in their Notifications. A[User](../User/index.md)is required.

## LogUrgentPopup

Recipient will be notified with an urgent popup in the MyGeotab application that will also appear in their Notifications. A[User](../User/index.md)is required.

## PushNotification

Recipient will be notified with a mobile push notification, if they are using the MyGeotab mobile app. A[User](../User/index.md)is required.

## TextMessage

Recipient will be notified via a text message in the vehicle.

## TextToSpeech

Recipient will be notified via audio from a text to speech application connected to the[GoDevice](../GoDevice/index.md).

## WebRequest

Recipient will be notified via the related WebRequestTemplate (NotificationBinaryFile). A WebRequestTemplate is required.