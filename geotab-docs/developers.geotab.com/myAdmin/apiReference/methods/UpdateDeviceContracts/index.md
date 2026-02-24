**Introduction**

Updates the comment and/or user contact (eg. assigned customer) for one or more Device Contracts.

**Parameters**

## activeTrackingDisallowed

This parameter is obsolete.

## apiKey

The active Api Key.

## comments

New comment if updateComments is true.

## groupId

GroupId setting for these devices. If updateGroupId is false or not specified, this parameter has no effect. The group ID may be used by the API user to group or categorize devices for the user's convenience.

## promoCode

PromoCode setting for these devices. If updatePromoCode is false or not specified, this parameter has no effect. Apply a valid promo code to the device(s).

## serialNos

Serial numbers of the Device Contracts to update.

## sessionId

The active session ID.

## updateActiveTracking

This parameter is obsolete.

## updateComments

True if comments are to be updated.

## updateCustomer

updateUserContact

## updateGroupId

True if the GroupId for these devices should be changed as per groupId parameter, false to not update GroupId.

## updatePromoCode

True if the PromoCode for these devices should be changed as per promoCode parameter, false to not update PromoCode.

## updateUserContact

True if assigned User Contact is to be updated.

## userCompanyId

userContactId.

## userContactId

ID of the[ApiUserContact](../../objects/ApiUserContact/index.md)to assign to the Device Contracts if updateUserContact is true. See[GetUserContacts](../GetUserContacts/index.md)to obtain a list of User Contacts.

**Return value**

**Code samples**