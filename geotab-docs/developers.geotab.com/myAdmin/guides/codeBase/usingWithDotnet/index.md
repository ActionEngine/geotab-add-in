**Overview**

The .NET SDK tools facilitate the integration of MyAdmin with your own .NET software. All communication to MyGeotab services occurs through HTTPS and the data is serialized in  [JSON](http://www.json.org/)  format. The provided .NET library automatically handles both serialization and deserialization of JSON into MyAdmin objects.


## Packages

The inclusion of the Geotab.Internal.MyAdmin.APILib and Geotab.Checkmate.ObjectModel packages allows you to interact with the API. The nuget packages include tools to assist with serialization and deserialization of JSON and provide definitions for MyAdmin object classes. The packages can be found on the NuGet website:

[Geotab.Internal.MyAdmin.APILib](https://www.nuget.org/packages/Geotab.Internal.MyAdmin.APILib)

[Geotab.Checkmate.ObjectModel](https://www.nuget.org/packages/Geotab.Checkmate.ObjectModel)

**Step 1: Initialization & authentication**

The MyAdminInvoker class contains methods that facilitate calls to API functions. To access the invoker and object classes, include the following references in your code:

Then, create an instance of the API invoker in your code:

The parameters required by each method are passed using a Dictionary  <string, object> . For example, to authenticate with the API, pass a valid username and password to call the Authenticate method using the code below:

The Authenticate method authenticates with the MyAdmin API and, if successful, returns an ApiUser object. The ApiUser object contains the SessionId and UserId - used as the API key for all other methods.

**Step 2: Making calls**

Once authenticated, you can call other methods by passing the API key, Session ID, and any parameters required by the method.

**Step 3: Pagination (V3 APIs)**

Version 3 of the MyAdmin API (`/v3/MyAdminApi.ashx`) introduces root-level pagination for methods returning arrays. The .NET SDK facilitates this through a root-level pagination property in the JSON-RPC request. To ensure requests are serialized correctly, use the following patterns provided by the Geotab.Internal.MyAdmin.APILib library.


### Option A: Using the Invocation Builder (Recommended)

The InvocationBuilder provides a fluent interface to configure pagination parameters. This approach automatically structures the JSON payload to place the pagination object at the root, ensuring compatibility with V3 endpoints like GetDeviceContracts.


#### Offset-Based Pagination


### Option B: Using InvokeWithPaginationAsync

Alternatively, you can use the `InvokeWithPaginationAsync` method by passing an `IPaginationRequest` object (such as `OffsetPaginationRequest`).

**More information**

For more information, see [.NET examples](../../../codeSamples/dotNetExamples/index.md).