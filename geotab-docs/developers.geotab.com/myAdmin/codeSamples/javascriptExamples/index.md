The example below demonstrates a simple JavaScript application that authenticates with the MyAdmin API, then calls  `GetDevicePlans` and `LookupDevice`.
**Example 1**

The `call` method uses the following parameters:


- Method name;
- Parameters;
- Success callback; and
- Error callback (optional).

**Note**: The Success callback receives the object returned by the API as a parameter. The  [Reference](../../apiReference/methods/index.md) page provides details about the objects returned by each method. In the example above, the error callback is called if the login fails. The error callback receives two parameters: an error message and an " errors "  object that contains an array of individual errors that occurred. In the example above, the `devicePlans`  object — returned by`GetDevicePlans` — is an array of `ApiDevicePlans`. The device object, returned by `LookupDevice`, is an  `ApiDeviceInstallResult`. For more information, see [Reference](../../apiReference/methods/index.md).