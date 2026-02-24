**Introduction**

The class contains the collection of object property names. The fields are matched on case-insensitive basis and included or excluded from the result, depending on isIncluded flag.

**Properties**

## Fields

The collection containing the[Entity](../Entity/index.md)field names. The system matches those on case-insensitive basis and excludes from the result. Check specific[Entity](../Entity/index.md)for the fields that can be included or excluded. Undefined or empty collection results in default API behavior: a completely populated object.

## IsIncluded

A value indicating whether the specified fields are to be included or excluded. [Default true]