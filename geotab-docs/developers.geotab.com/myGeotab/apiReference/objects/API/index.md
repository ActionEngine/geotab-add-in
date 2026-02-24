**Introduction**

Used to make API calls against a MyGeotab web server. This object is typically used when using the API from a Microsoft .Net language, like C#, VB.Net or managed C++. It makes it easy to invoke the various methods and receive the results. It also automates of some tasks such as handling a database that was moved from one server to another or credentials expiring. This class is thread safe.

**Properties**

## Database

The specific database on the server to which the API call is being made.

## LoginResult

The result of the login request.

## Password

Sets the user's password.

## Server

The name of the server that the API call is being made to.

## SessionId

The token generated from the authentication call which can be used to make the API call instead of the password.

## Timeout

The timeout for the requests in milliseconds.

## UserName

The username (typically an email address) that identifies the user being authenticated.