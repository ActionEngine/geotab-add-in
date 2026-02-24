This page provides an overview of the storage (AddInData) API and describes its use within Add-Ins.

For a sample Add-In that uses the storage API go to this  [link](https://github.com/Geotab/sdk-addin-samples/tree/master/storage-api-sample).


**What is the storage API?**

The Storage API allows an Add-In or integration to store records which contain generic data to a customer database. The  `AddInData` object allows storage of structured JSON which can be searched for and retrieved using the API.


## Sample JSON

Following sections will refer to this example JSON:

**AddInId**

An AddInId must be created before the Storage API methods can be used within your Add-In. This encoded GUID is used to register and identify which Add-In some data is associated. AddInId is a mandatory parameter when calling AddInData methods to Add and Get data. This allows each Add-In ' s data to be isolated from the data used by other Add-Ins. This allows multiple solutions to each have their own collection of AddInData objects in the same database without the collections mixing. To generate your own AddInId, please use the following  [example](../../runner/index.md@script=JTIydmFyJTIwZ2VuZXJhdGVHdWlkJTIwJTNEJTIwZnVuY3Rpb24lMjBndWlkKCklMjAlN0IlNUNuJTIwJTIwZnVuY3Rpb24lMjBzNCgpJTIwJTdCJTVDbiUyMCUyMCUyMCUyMHJldHVybiUyME1hdGguZmxvb3IoKDElMjAlMkIlMjBNYXRoLnJhbmRvbSgpKSUyMColMjAweDEwMDAwKSU1Q2.md).

**Creating an AddInData object**

An AddInData object must first be created in a database. The properties of AddInData are as follows:

| Property | Description |
| --- | --- |

| Id | The standard Id for any Entity. |
| AddInId |
| Groups |
| Details | The JSON data. May be whole or partial depending on the action (Addvs.Set) or the filtering provided when callingGet. |

As an example, you can use the [API Runner tool](../../runner/index.md) to create an AddInData object that ' s not limited to any groups using the following operation:

The same example with the addition of the **Groups** parameter would result in limiting the data to the specified groups, in this case the driver activity group:


## Important notes

Each invocation of the Add operation will create a new AddInData object with a unique Id bound to the entered AddInId. The Id of the AddInData object is required to remove the object with the `Remove` method. See below for an example.


## Example 1

This method call will correctly save the sample JSON and associate it to the Add-In with the AddInId of  `a2C4ABQuLFkepPVf6-4OKAQ`.

**Request**

**Response**

**Retrieving stored AddInData content**

AddInData uses a search object to query specific data using an object ' s path in the JSON.

The AddInDataSearch properties are as follows:

| Property | Description |
| --- | --- |

| Id | The standard Id for any Entity. |
| AddInId | Can be optionally provided when searching for AddInData that belongs to a specific AddInData. |
| Groups | Used to define the scope of a row of Add-In data. Works the same as any other ObjectModel Entity. |
| SelectClause (String) | Used to filter the resulting rows based on the JSON content of the row. Works with the object path notation described in usage. Independent of WhereClause. |
| WhereClause (String) | Used to filter the resulting rows based on the JSON content of the row. Works with the object path and operator notation described in usage. Independent of SelectClause. |

As an example, you can use the [API Runner tool](../../runner/index.md) to perform GET operations that return one or more AddInData objects:


## Example 2

Get the emails of all customers who have an item with a price less than 15. This method call will return an array with a single AddInData object.

**Request:**

**Response:**


## Example 3

Get all item names for a user with the email **joe@smith.com**. This method call will return an array with multiple AddInData objects that satisfy both the select and where clauses.

**Request:**

**Response:**

**Note**: Both returned AddInData objects will have the same Id because they come from the same object in the database.


## Example 4

Get all data

**Request:**

**Response:**


## Object path notation

The `SELECT` and `WHERE` clauses of the AddInDataSearch object use a special notation to describe an object path. If we wanted to modify the call in Example 4 to retrieve just the customer name from the AddInData object, we would add the following path notation to the `SELECT` clause of the AddInDataSearch object:

`customer.name`

The returned AddInData object will contain a value of  " joesmith "  in its data property.

If you have an array in the path, it must be indicated by a [] after the name of the array property.

For example, if you wanted to modify Example 4 to select all item names, we would add the following to the `SELECT` clause of the AddInDataSearch object:

`items.[].name`

The same notation is used for the `WHERE` clause. This notation can be used to drill down to as many objects as you want.


## Operators and arguments

The `WHERE` clause of the AddInDataSearch object supports the following operators:

| Operator | Description |
| --- | --- |

| = | Equal to |
| < | Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to |

These can be used with the object path notation explained above.

For example, if you want to get all items with a price less than 20, the appropriate `WHERE` clause will be:

`items.[].price < 20`**Note**: The data type of the value on the right side of the operator is important. String values will need to be enclosed in quotation marks and properly escaped.

To get all customers with the name  " joesmith " , the appropriate `WHERE` clause will be:

`customer.name =  " joesmith "`
## Important operation notes for using Get


- The `SELECT` clause must be included if the `WHERE` clause is specified, otherwise the entire data object will be returned.
- The `GET` operation always returns an Array of AddInData objects, each with a unique value in the data property.
- Search matching is case-sensitive. In the examples above, searching for  `customer.name =  " JoeSmith "`  will not return any results.
- Results returned by the `SELECT` and `WHERE` clauses will be in the scope of the entire AddInData object. To have a search return separate matches, the independent pieces of content must be added to separate AddInData objects using the  `ADD` operation.

**Updating stored AddInData content**

To update stored content, use the `SET` method on an AddInData object while specifying its AddInId ID. The return value is always `null`.

As an example, use the [API Runner tool](../../runner/index.md) to perform the following operation:

**Deleting an AddInData object**

An AddInData object is deleted when you specify its ID. The return value is always `null`.


## AddInData JSON restrictions

The following are the only restrictions on the JSON stored within AddInData objects:


- The JSON data for an AddInData object must be 10,000 characters or less.
- No property in the JSON data can have the format  " geotabXYZ " . This naming format is reserved for Geotab use.

**Additional notes And limitations**

## Legacy property  ' data '

The AddInData object has been available as a beta feature through several releases and as such, we ' ve made improvements through time. Now that we are officially releasing this feature in 2101, a legacy property we are looking to get rid of is the  ' Data '   property. This is a string property that is not deserialized as an object when sent over JSON. The newer property,  ' Details ' , deserializes as an object and should be used instead (you do not need to call JSON.parse() on this property).  **Partners that have designed their applications to work with the  ' Data '  property should transition to using  ' Details ' . In a future release, the  ' Data '  property will be completely removed.**


## Cannot delete properties of objects

All objects properties stored in the JSON can be modified but not deleted.

Example (Replacing):

With

Results in a merged dataset instead of a deletion of the previous content

Workarounds to this issue would be to either:


- Use arrays as a property of an object as they can be modified and resized without issue.
- Make two calls: first to change the  " customer "  value to an empty string, then a second call to set new data.

## No LIKE statement

Currently there is no support for fuzzy string matching.


## No AND/OR statements

The `WHERE` clause cannot perform conjunctions or disjunctions.


## Security clearance matters

Security Clearance limitations allow the following API methods:


- **Administrator, Supervisor, Default User, Drive App User**  =>   " Add/Set/Get/Remove "
- **ViewOnly**  =>   " Get "
- **Nothing**  =>  None

## Small vs large

While it ' s possible to create a single AddInData object with an array of details, this approach is less scalable. First is contending with the mandatory limit of 10,000 characters. Second is that it can cause unduly large objects to deal with which can be less memory efficient. Third is that if there is an array of entries and you need to remove one, you will have to remove the whole object and add a new one with the updated list of details. In general, we have found it more useful to treat the AddInData as a simple object which there can be many of.

**Additional resources**

[Storage API Add-In Sample](https://github.com/Geotab/sdk-addin-samples/tree/master/storage-api-sample)