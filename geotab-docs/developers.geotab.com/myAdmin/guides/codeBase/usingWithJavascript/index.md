**Overview**

All communication with our services is done over HTTPS with data serialized in JSON format. A request consists of three properties:

Before calling any API methods, a call must be made to the Authenticate method to obtain the user ' s API key and session ID. All method calls require a `params` object which contains the values for the parameters required by the methods. The following sections describe how to build the `params` object to authenticate and call an API method. The myAdminApi.js utility is provided to help with calling MyAdmin API methods. It can be downloaded   .

**Step 1: initialization & authentication**

The call to Authenticate is made as follows:

In the above example, the code passes the user name and password in the `logonParams` object and provides a callback function to be executed following a successful login. The callback function receives an ApiUser object which contains, among other properties, the user ' s API key (userId) and session ID. See the reference documentation for more information on the  [Authenticate](../../../apiReference/methods/index.md) method and the [ApiUser](../../../apiReference/objects/index.md)  object.

**Step 2: making calls to other methods**

Once authenticated, all other API methods can be called using the API key and Session ID obtained in the previous example. For example, the following code will return a list of available device plans:

The result object in the above code contains an array of ApiDevicePlan.

**More information**

For more information, see the [JavaScript Examples](../../../codeSamples/javascriptExamples/index.md) section.