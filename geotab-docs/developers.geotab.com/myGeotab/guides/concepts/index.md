Requests made to the Geotab API are performed over HTTPS. The current API is version 1. The version number is appended to the API endpoint URL, where the web application sends requests:

`https://[myserver]/apiv1`

NOTE: Sample text inside `[`and`]`(e.g `[myserver]`) are placeholders to indicate where the user enters information unique to their requirements.

API request parameters and their results are transported using the lightweight  [JSON](http://www.json.org)  format. The [API Reference](../../apiReference/methods/index.md) contains a list of methods that can be invoked, including the parameters they expect, and the results they return. Examples are provided below to demonstrate what the Geotab API can do.

Requests to the Geotab API are invoked using HTTP GET or HTTP POST. HTTP POST requests use the JSON-RPC standard. When making requests that contain MyGeotab credentials, use the POST request only. This helps to minimize potential leaks into browser histories, or web server logs.

The following sections explain how to construct HTTP GET and POST requests to the Geotab API.


**Security**

MyGeotab API requests can only be made over secure connections (HTTPS). The minimum SSL/TLS version supported by the MyGeotab API is TLS v1.2.

Geotab recommends that all users of Geotab APIs adhere to modern cryptography best practices. When using our libraries, we recommend that developers use algorithms and ciphers that provide the most forward secrecy and the greatest adherence to modern compliance requirements.

At the time of writing this document, best practices implies that we use AES-256 (or stronger) cipher suites and algorithms with a modern cipher mode, such as GCM or CCM. We recommend utilizing modern key exchange algorithms such as DHE or ECDHE. RSA3072 or the equivalent elliptic cryptographic algorithm should be use for asymmetric cryptography. We recommend SHA3 for all hashing operations. When using modern network communications software, the latest version of TLS (TLS1.3 at the time of writing) should be used.

**Make your first API call**

While both GET and POST requests are supported, we strongly recommend that only POST requests are used for requests that include MyGeotab credentials as parameters.

The endpoint shown below is used to invoke an API method when an HTTP POST request is used. The example that follows illustrates a POST request that returns all devices (vehicles) and their properties.

`https://[myserver]/apiv1`

The method ' s name and parameters are passed in the HTTP body using the  [JSON-RPC](https://en.wikipedia.org/wiki/JSON-RPC)  format. Geotab API version 1 supports JSON-RPC version 2.0. The full set of API methods and objects returned can be viewed in the  [API reference](../../apiReference/methods/index.md).

To understand which parameters must be passed, consider the following JSON object:

To understand how HTTP POST can be used to invoke a method, consider the following JavaScript example. This can be achieved from any language that supports HTTP, such as the java.net.HttpUrlConnection class in Java, or System.Net.Http.HttpClient in .Net.

**Results and errors**

Using the example above, a successful request to the server results in an object with the property  " result” in the following format:

Generic:

Specific:

However, if the request is incorrect, or an error is triggered on the server, the error is returned as an object with the property  " error”. For example:

The properties of the error object are [JsonRpcError](../../apiReference/objects/index.md#JsonRpcError), and  [JsonRpcErrorData](../../apiReference/objects/index.md#JsonRpcErrorData). Objects are documented in the API Reference.

**Authentication**

Authentication is performed to obtain a session token (credentials). A new token will only be generated from an  [Authenticate](../../apiReference/methods/Authenticate/index.md) call if no valid session ID is passed in to the  [API](../../apiReference/objects/API/index.md) object. This token then confirms your identity for subsequent API operations. If the session expires, a new authentication request must be made to get a new token.

A session will expire if:
- The session exceeds its 14 day lifetime from generation The length of the session lifetime may increase in the future as we address new authentication technologies.
- The user ' s password is changed. In this case, all active sessions will expire.
- For a given user account, a maximum of 100 concurrent sessions is exceeded. Upon exceeding the limit of 100 sessions, the oldest sessions will begin expiring. For instance, when the 101st authentication occurs, the session from the first call will expire.

This approach encourages efficient use of authentication requests, as shown in the authentication example below:

Database, user and password must be set for successful authentication.


## Example 1: Authenticate with valid credentials

In this example, an authentication request is made to my.geotab.com to log in to the database named *database*.


- The `Authenticate` method is requested using the credentials provided.
- The response from the server contains two important properties — `path` and `credentials`.

The path will either contain the URL of a server, or the string value `ThisServer`. Since the *database* is on my.geotab.com, it returns *ThisServer*. This means that the path is correct.

The `credentials` object contains the username, database and session ID. This object is required for all subsequent requests to the server.


- Since the authentication method confirmed the path is correct, other methods can be used as well. For example, you can mak a request to `Get` devices from my.geotab.com. Pass the `credentials` object with the call to `Get` Device.
- The `Get` result is returned with one device.

## Example 2: Requests with missing databases or with expiring credentials

The examples above demonstrate how to authenticate to get a token and make a call to Get devices. However, there are two additional scenarios to consider:


- The credentials provided to `Authenticate` method are invalid.
- The token has eventually expired.

In these scenarios, the API request will fail returning the JSON-RPC error similar to below:

If the error contains an object with type `InvalidUserException`, the authentication failed or the authentication process must be repeated to obtain a fresh token.


## Example 3: Requests with invalid/expired sessionId

For a given user account, a maximum of 100 concurrent sessions is allowed. Each authentication generates a new session. Upon exceeding the limit of 100 sessions, the oldest sessions will begin expiring. For instance, when the 101st authentication occurs, the session from the first call will expire.

Any API call made with an expired sessionId will result in an `Invalid session @ ...` error:

**HTTP compression**

The MyGeotab API supports *brotli*, *gzip* and *deflate* compression. To use either of these compression methods, include the HTTP header for  " Accept-Encoding”. For example:

`Accept-Encoding: brotli, gzip, deflate`

If you are using an API client (.Net, JavaScript, Nodejs, etc.), the header is enabled automatically.

**Pagination**

In `Get` calls to entities that support pagination, you can pass a resultsLimit along with a sort object to page through your data, enabling more efficient data retrieval. The resultsLimit parameter specifies the number of records to return per page, and the sort object specifies the sorting criteria for the data and facilitates the retrieval of subsequent pages. For detailed information on sorting, refer to the [sorting](index.md#sorting) section. When implementing paging, it is recommended to continue requesting new pages until a page with no results is returned.

Below are the entities that support pagination. Maximum page sizes (resultsLimit) and the available sorting options for these entities can be found in their respective documentation.


- [Audit](../../apiReference/objects/Audit/index.md)
- [DebugData](../../apiReference/objects/DebugData/index.md)
- [Device](../../apiReference/objects/Device/index.md)
- [Diagnostic](../../apiReference/objects/Diagnostic/index.md)
- [DriverChange](../../apiReference/objects/DriverChange/index.md)
- [DutyStatusLog](../../apiReference/objects/DutyStatusLog/index.md)
- [ExceptionEvent](../../apiReference/objects/ExceptionEvent/index.md)
- [FaultData](../../apiReference/objects/FaultData/index.md)
- [FuelTaxDetail](../../apiReference/objects/FuelTaxDetail/index.md)
- [LogRecord](../../apiReference/objects/LogRecord/index.md)
- [Route](../../apiReference/objects/Route/index.md)
- [ShipmentLog](../../apiReference/objects/ShipmentLog/index.md)
- [StatusData](../../apiReference/objects/StatusData/index.md)
- [TextMessage](../../apiReference/objects/TextMessage/index.md)
- [Trip](../../apiReference/objects/Trip/index.md)
- [Zone](../../apiReference/objects/Zone/index.md)

To begin paging, the request for an entity with pagination support can be structured as follows:

To request subsequent pages, you must populate the `offset` field in the sort object. To achieve this, take the value of the property by which you are sorting from the last record returned and use it as the `offset`. If you are sorting by a non-unique property, such as `name` in this example, it is strongly recommended to include the ID of the last record returned in the  `lastId` field as well. A request for the next page would then be constructed as follows:

You can continue this process until zero records are returned, indicating that you have reached the end of your data.

JS Example:

**Sorting**

To appropriately [page](index.md#pagination) through your data, you must pass a sort object and a resultsLimit as as parameters in a `Get` call to an entity that supports pagination. The properties of a sort object are described as follows:

| Sort properties | Description |
| --- | --- |

| sortBy | Required. Possible values includeid,name,date,version,start, andstop. This property specifies the field by which to sort the data. Refer to the table in thepagingsection to see whichsortByoptions are available for each supported entity. |
| sortDirection | Optional. Possible values areascfor ascending ordescfor descending order. This property determines the sort order of the specified field. The default value isasc. |
| offset | Theoffsetmay be set tonullfor the initial page request. For subsequent page requests, theoffsetshould be the last known value of thesortByproperty from the previous page. Theoffsettype must correspond to that of thesortByproperty. |
| lastId | Similar tooffset, this field can benullfor the initial page request. For subsequent pages,lastIdshould be populated with the ID of the last record returned. This field is essential when sorting by non-unique fields, such asnameordate, to prevent data loss at the page boundary. |

Below are the required `lastId` and `offset` combinations for the various sort options:

| Sorting by | LastId required | Offset |
| --- | --- | --- |

| id | * | Type: IdJSON Example:"b14C3EE" |
| version |  | Type: VersionJSON Example:"000000000014c3ee" |
| date |  | Type: DateTimeJSON Example:"2024-01-01T00:00:00.000Z" |
| name |  | Type: StringJSON Example:"Delivery Truck 12" |
| start |  | Type: DateTimeJSON Example:"2024-01-01T00:00:00.000Z" |
| stop |  | Type: DateTimeJSON Example:"2024-01-01T00:00:00.000Z" |

* ArgumentException thrown if passed.

When [paging](index.md#pagination) in C#, you should use the Sort object which corresponds to your  `sortBy` field. The recommended Sort implementations are:


- [SortById](../../apiReference/objects/SortById/index.md)
- [SortByVersion](../../apiReference/objects/SortByVersion/index.md)
- [SortByDate](../../apiReference/objects/SortByDate/index.md)
- [SortByName](../../apiReference/objects/SortByName/index.md)
- [SortByStart](../../apiReference/objects/SortByStart/index.md)
- [SortByStop](../../apiReference/objects/SortByStop/index.md)

C# Example:

**Working with dates**

When exchanging dates as parameters to API methods, you must ensure that they are formatted properly as an  [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)  string (format `yyyy-MM-ddTHH:mm:ss.fffZ`). In addition, all dates will have to first be converted to  [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)  in order to ensure time zone information and daylight savings times are accounted for correctly.

**Unit of measure**

As a general rule, MyGeotab uses the metric system for values such as speed (km/h) and distance (m). For example, if you queried the odometer reading for a vehicle, the value would be returned in meters or if you retrieved the current speed of a vehicle it would be in km/h. It does not matter in which region in the world the vehicle or user of MyGeotab system is located — we always return the values in metric.A simple conversion can be applied to these values should you wish to work in imperial units or other customized units instead.

Please note that MyGeotab also records various other status data (e.g. engine data) from the vehicle and these values can be in various units of measure. The units of measure are not provided by Geotab in all cases. Refer to the applicable  [SAE](https://www.sae.org/standards/)  standard of the specific code for the associated unit of measure.

**Entities**

All objects in the MyGeotab system are called entities. Entities have an ID property that is used to uniquely identify that object in the database. The ID is an opaque string value that uniquely identifies the entity and no assumption about the format or length of this ID value should be made when comparing or storing the values.

**ID**

An ID is used to uniquely reference entities in the API. IDs are represented by opaque strings. Generally the contents of the IDs are not significant for the user. Building logic around the value of the string should be avoided — unless it is a system ID (see the examples below).


## Example 3

In this example, a vehicle in the system and its ID value will be examined. Here is a partial JSON representation of a device object:

Note the  " id” property with value  " b0a46”. This is the unique identifier for the device (vehicle) with description  " 007 - Aston Martin”.

To find Trips for this vehicle all of the properties of the device do not have to be passed to the Get method. Instead, only the ID property of the device object is required. Below is an example of a valid parameter object (TripSearch) for passing into Get method. The deviceSearch with the ID property set to the value  " b0a46” (as indicated in the example above) is passed.

Calling the Get method with the parameter defined above will return all trips for the vehicle  " 007 - Aston Martin”.


## Example 4

There are certain IDs that are predefined for system entities. For example the group that has been defined as the root group of all user groups, and called the CompanyGroup, will have an ID of  " CompanyGroupId” rather than other characters (such as  " b0a46” above). For example:

If the system entities do not have any properties then they are specified as strings with their ID ' s name. For example the source   " Obd” will be identified as  " SourceObdId”.

**Building block approach**

The results of a call to our API will only contain literal values and the identities of contained objects — not the actual fully populated child objects. This provides a predictable system that efficiently serializes objects to JSON and back. Additional lookups of the nested objects will be required to retrieve additional properties of the objects.

For example, an engine status data record has a device property. If 1000 engine status data records are retrieved for a device, the status data ' s device property will only contain the ID of the device. An additional retrieval for the devices object will be required to obtain the status data records. This approach has several benefits:


- Saves bytes over the wire
- Reduces request time
- Avoids redundant copies of entities
- More flexible since the child objects may not always be required

In the example below it can be seen how, by creating a dictionary of devices where the key is the device ID and the value is the device object, devices can be easily  " stitched” into the status data records:

statusDatas[i].device = deviceLookup[statusDatas[i].device.id];

Depending on the process, for some entities like diagnostics, it may be desirable to maintain a local cache from which the status/fault data can be populated. In this case it will be necessary to refresh the cache when the cache is missing the required entity making an API call. This will allow the API to get the required entity and add it to the local cache. An example of maintaining a diagnostic cache would occur when consuming a feed of data from the API. An example of this process is included in both the  [.Net](https://github.com/Geotab/sdk-dotnet-samples/tree/master/DataFeed)  and  [JavaScript DataFeed](https://geotab.github.io/sdk/software/js-samples/dataFeed.html)  examples.

**Property Selector**

`PropertySelector` is a new optional parameter that can be used with the  [Get](../../apiReference/methods/index.md#Get) and [GetFeed](../../apiReference/methods/index.md#GetFeed) methods to selectively include or exclude specific properties for entity type requested. This provides a mechanism to reduce the amount of data sent over the wire and can significantly reduce call times.


## Supported types

A limited set of objects have support for use with property selector in the beta version. These objects tend to have many properties and would provide the most benefit to reducing size over the wire.

| Property | Description |
| --- | --- |

| Fields | An array of string, consisting of the properties for a givenEntitytype for which we want to include/exclude in the entities of the result set. Refer to thereferencepage for all the properties supported for a givenEntity. Note that the properties of an inheriting class will also be supported. (For example,Go9is child ofDevice, so the properties defined forGo9can be supplied toFields.) |
| IsIncluded | A boolean, which iftrue, will include the properties of a givenEntitytype defined inFieldsfor the entities of the result set. Otherwise, if this boolean is false, the properties defined inFieldswill be excluded. |


## Examples

A simple  [example](../../runner/index.md@script=JTIyYXBpLmNhbGwoJTVDJTIyR2V0JTVDJTIyJTJDJTIwJTdCJTVDbiUyMCUyMCU1QyUyMnR5cGVOYW1lJTVDJTIyJTNBJTIwJTVDJTIyRGV2aWNlJTVDJTIyJTJDJTVDbiUyMCUyMCU1QyUyMnByb3BlcnR5U2VsZWN0b3IlNUMlMjIlM0ElNUNuJTIwJTIwJTdCJTVDbiUyMCUyMCUyMCUyMG.md)  of this can be illustrated by using the property selector with `Device`. The `Device` object can have many properties which may not be useful to all use-cases. For example, if I have an Add-In to display a list of 500 devices by name. We only want our `Device` objects to have the properties `Name` and `Id`, so we set our  `PropertySelector` object like so:


### Javascript


#### Request


#### Response

In our example, making this call using the property selector results in the total JSON size over the wire of 5.4 kB and time of 45 ms.

Making the same call, without property selector (returning all properties) results in 41.8 kB of JSON sent over the wire and a round trip time of 320 ms.

| Using property selector | Device count | Size | Time |
| --- | --- | --- | --- |

| false | 500 | 41.8 kB | 320 ms |
| true | 500 | 5.4 kB | 45 ms |
| Improvement |  | -36.4 kB | -275 ms |


### C# example


## List of supported entities

Below is a list of entities that support the PropertySelector functionality.

| Entity | Supported in release | Notes |
| --- | --- | --- |

| Device | 8.0 | The following properties are not supported:deviceFlags,isAuxInverted,deviceType,productId,autogroups,auxWarningSpeed,enableAuxWarning |
| User | 8.0 | isEULAAcceptedandacceptedEULAare tied to each other, so if either property is set to be returned based on thePropertySelectorlogic, both properties will be returned. |
| Group | 8.0 | N/A |
| Rule | 8.0 | N/A |
| LogRecord | 8.0 | dateTimemust be included. |
| Trip | 9.0 | N/A |
| TextMessage | 10.0 | N/A |
| IoxAddOn | 10.0 | N/A |
| IoxAddOnStatus | 10.0 | N/A |


## PropertySelector FAQ

**Can I combine property selector and search?**

Yes. PropertySelector and Search work independently of each other and can be used together in the same request.

**MultiCall**

A MultiCall is a way to make several API calls against a server with a single HTTP request. This eliminates potentially expensive round trip costs.

Why use a MultiCall?

Making an HTTP request over a network has overhead. This can be in the form of Network overhead, the round trip time to send and receive data over the network and HTTP overhead, the HTTP request and response headers. A MultiCall can be used to reduce amount of overhead in situations where many small requests need to be made to a server.

For example, if we make a request to get the count of devices. The request would be constructed in a format similar to:

Response:

Let ' s assume that it takes 100 milliseconds for this call round trip (the time from sending request to receiving the response), including 40 milliseconds to send the request, 20 ms to process the data on the server, and 40 ms for the response to be returned.  [Google ' s SPDY research project white paper](https://www.chromium.org/spdy/spdy-whitepaper/)  states that *" typical header sizes of 700-800 bytes is common”*. Based on this assumption, we pay a 750 byte cost when making a request. From the example, there would be 80 ms of network overhead and 750 bytes of HTTP overhead, this is accepted as the  " cost of doing business” when making a request over a network.

Taking the previous assumptions, what would the overhead be for making 1000 requests for road max speeds? When individual calls are made to the server for 1000 addresses; the base (minimum) HTTP and Network overhead is required for each of these calls. This would result in 80 seconds (80,000 milliseconds) of network overhead and 0.72 MB (750,000 bytes) in headers just going to and from the server. It can be clearly seen that a great deal of overhead can be generated by making small but repeated requests.

By using a MultiCall, the network and HTTP overhead remains at the cost of a single request. This brings the overhead back down to our original 80 milliseconds and 750 bytes. The server processes each request and returns an Array of results when complete.

The above illustration is an extreme example to demonstrate the benefits of using a MultiCall. A MultiCall can (and should) be used to make short running calls of 2 or more requests more efficient than individual calls.


## Basic Implementation

Making a MultiCall is simple, use the method  " ExecuteMultiCall” with the parameter  " calls” of JSON type Array. Each call should be formatted as an Object with property  " method” of type string with the method name as its value and a property  " params” of type Object with the method parameters as its properties. The parent  " params” object will also need to contain the user credentials if they are required for at least one of the child methods being called. It is not necessary to include credentials with each child call.

Response:


## Errors

In a MultiCall, each request is run on the server synchronously. If one fails, the error results are returned immediately and  **unreached calls are not run**. The error results includes the index of the call in the array that the exception occurred.

To illustrate, let ' s assume an array of calls (api.multicall([call-a, call-b, call-c])) where call-b is formatted incorrectly.

Below is an example of the error result. The `requestIndex` property contains the index of the call that failed.

Alternatively, a successful MultiCall would look similar to:


## API client support

All of the [API clients](../../apiClients/index.md) have native support for making multi-calls. Below are examples of making multi-calls using the Javascript and .Net wrappers:

JavaScript API multi-call example:

.Net nuget package multi-call example:


## MultiCall FAQ

**Can I use a search in a multicall?**

Yes, it is possible to use a search in a multicall.

**When shouldn ' t I use a multicall?**


- If you need to make a few requests that are long running and return a large amount of data, it may be preferable to make the requests singularly instead of running one multicall request that continues for a very long time before completion. When the connection is held open for a long period of time, you become increasingly susceptible to network interference that can terminate the request.
- Manipulating data (Add, Set, Remove) via a multicall is not recommended. A multicall is not transactional. Therefore, if call 1 of 3 to Add succeeds and call 2 of 3 fails, call 3 of 3 will not be executed and call 1 would not be rolled back.

**How many request can I put in a multicall?**

For optimal performance, we advise limiting to 100 nested requests.

This is relevant when processing requests large response sizes, for instance, Getover an extended period. Similarly, using chunking to manage high-volume requests improves process control and optimizes response management.

That being said, the system does not enforce a hard limit on the number of requests in a multicall at this point.

**What if the call doesn ' t return a result?**

The index in the array of results will have a **null** value.