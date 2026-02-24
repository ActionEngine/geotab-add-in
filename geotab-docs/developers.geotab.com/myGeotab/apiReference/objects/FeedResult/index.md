**Introduction**

An object containing the result of a feed method.

**Properties**

## Data

A list of data returned by the feed.

## ToVersion

The last version of the data returned by the feed call. If this parameter is passed back into the feed call, then returned data will be the changes that occurred after the last feed call was made. In this way the feed can return a continuous stream of data.