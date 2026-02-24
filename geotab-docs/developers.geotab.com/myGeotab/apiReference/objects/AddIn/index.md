**Introduction**

Add-Ins are used to extend the functionality provided by MyGeotab and Geotab Drive. An Add-In is JavaScript, HTML and CSS loaded into the MyGeotab or Geotab Drive portal and resides directly inside the user interface. This allows third-parties to create a seamless user experience and provide solutions that would otherwise require the user to visit a different website altogether.[More information on developing Add-Ins.](https://geotab.github.io/sdk/software/guides/developing-addins/)

**Properties**

## Configuration

The[AddInConfiguration](../AddInConfiguration/index.md).

## ErrorMessage

The error message if there was an issue with Add-In.

## Id

The unique identifier for the specific[Entity](../Entity/index.md)object in the Geotab system. See[Id](../Id/index.md).

## Url

The marketplace Add-In Url.

**Rate limits**

| Method | Description | Limit | Period | Status |
| --- | --- | --- | --- | --- |

| Get | Limit of 1000 Get requests per 1m. | 1000 | 1m | Active |
| Set | Limit of 10 Set requests per 1m. | 10 | 1m | Active |
| Add | Limit of 20 Add requests per 1m. | 20 | 1m | Active |
| Remove | Limit of 10 Remove requests per 1m. | 10 | 1m | Active |
| GetCountOf | Limit of 1000 GetCountOf requests per 1m. | 1000 | 1m | Active |