Requests made to the MyAdmin API are performed using HTTPS. The URL your web application will send its requests to is:

API request parameters and the results are transported in the lightweight  [JSON](https://www.json.org/)  format. The [Reference](../../apiReference/methods/index.md) contains a listing of the methods that can be invoked, the parameters they expect, and the results they return. Requests to the API can be invoked using HTTP POST. HTTP POST requests use the JSON-RPC standard. The following sections explain how to construct HTTP POST requests to the MyAdmin API.


**HTTP POST request**

When using HTTP POST request to invoke an API method, the following endpoint is used:

However, instead of encoding the method name and parameters in the query string, it is passed in the HTTP body using the JSON-RPC format.The MyAdmin API supports  [JSON-RPC](https://en.wikipedia.org/wiki/JSON-RPC)  version 1.0. The following is a JavaScript example that shows how HTTP POST can be used to invoke a method.

**Note**: This can be done from any language that has support for HTTP, for example the java.net.HttpUrlConnection class in Java or System.Net.HttpWebRequest in Microsoft .NET.

**Results & errors**

A successful call to the server will result in an object with property  " result " , like this:

However, when the call is incorrect or an error is triggered on the server, the error will be returned as an object with property  " error " :

The properties of the error object are:

| Property | Description |
| --- | --- |

| name | For all JSON-RPC errors, this is always “JSONRPCError”. |
| message | The description of the likely root cause of the error. |
| errors | An array of individual errors that were caught. Usually, there is at least one error in this array. |

The properties for objects in the “errors” array are:

| Property | Description |
| --- | --- |

| name | The name of the server exception. For example, “SecurityException”, “NullReferenceException”, etc. |
| message | The description associated with the server exception. |

Session expiry is an example of a case where it is useful to catch and handle errors.

**Working with dates**

When exchanging dates as parameters to API methods, you must ensure that they are formatted properly as an  [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)  string. In addition, all dates will have to first be converted to  [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)  in order to ensure timezone information and daylight savings times are accounted for correctly.

**Pagination**

Version 3 of the API, e.g., `/v3/MyAdminApi.ashx`, introduces Pagination. Any method returning an array will be paginated, i.e., a limited number of results will be returned, along with other pagination information.

v3 versions of endpoints/methods that do not yet support pagination **will return an error when called**. Pagination support will be indicated in the method ' s docs, for those methods that support it. Please use the v1 version of those endpoints until they can be updated to support pagination. Please contact your account manager to indicate the endpoint for which you would like pagination supported, and they will queue the work with our development team.

Two kinds of pagination are supported:


- Offset-based pagination. This is the default method.
- Keyset-based pagination. Supported on some endpoints. This is faster and more efficient than offset-based pagination, and as such is recommended, where available.

## Offset-based pagination

This type of pagination breaks the result set into indexed pages, starting at 1. Specify the desired page and results per page by passing them in the request object, like so:

Default page size is **20**. Maximum page size is **500**.

For `GET` requests, use the query parameters `page` and `per_page`.

The result object will include pagination information, where `total` is the total number of records matched by the query:

For `GET` requests, these values will be returned in the HTTP headers `Page`, `PerPage` and  `Total`. Also for `GET` requests, a `Link` header will be returned that can be used to access the next page.


## Keyset-based pagination

Keyset-pagination allows for more efficient retrieval of pages, and runtime is independent of the size of the collection, in contrast to offset-based pagination. Use keyset pagination, on the methods that support it, like so:

For `GET` requests, use the query parameter `pagination` set to `keyset` to enable keyset pagination (on those methods that support it).

The result object will include keyset pagination information:

For `GET` requests, these values will be returned in the HTTP headers `PerPage` and `NextCursor`. Also for `GET` requests, a `Link` header will be returned that can be used to access the next page.

Note that no information about total records or total pages will be returned for keyset pagination.

To get the next page, pass in the cursor returned in the result object of the previous page:

For `GET` requests, use the query parameter `cursor`.

**Maximum number of results**

Most unpaginated endpoints (see Pagination above) will be limited to 100,000 results (as of early 2024). However, some endpoints that already return more than 100,000 results (prior to 2024) will be grandfathered-in, to preserve API backwards-compatibility. Geotab may work with integrators in the future to work towards applying record limits to these grandfathered-in endpoints as well. So, integrators are encouraged to move to paginated versions of endpoints, ideally, or to generally avoid making requests that return large numbers of results.

The goal of pagination and these record limits is to improve the stability/performance of the API for all.