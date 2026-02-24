Add-Ins are used to extend the functionality provided by MyGeotab and Geotab Drive. An Add-In is JavaScript, HTML and CSS loaded into the MyGeotab or Geotab Drive portal and resides directly inside the user interface. This allows third-parties to create a seamless user experience and provide solutions that would otherwise require the user to visit a different website altogether.  [Click here](https://github.com/Geotab/sdk-addin-samples)  to find the sample Add-Ins.

The Add-In generator is a great developer tool that allows integrators to create scaffolded Add-In projects. You can learn more about the generator and all of its features by going into the  [generator-addin repository](https://github.com/Geotab/generator-addin).


**Geotab Add-Ins can be of two types**

## Pages

A custom page Add-In can be thought of as a complete web application inside your Geotab account. A custom page Add-In has access to the MyGeotab API and the current page state. With custom pages you can develop business-aware Add-Ins by combining MyGeotab data with your own APIs.


## Buttons

Custom button Add-Ins can be included to perform different functions. Additional navigational buttons can be dynamically inserted inside certain areas of the MyGeotab user interface. This allows custom button Add-Ins to provide a simple way for users to reach your custom page Add-In (see Image 1). Buttons can also be placed on pages to execute functions for automation of routine tasks, such as report generation (see Image 3).

**Use cases**

Consider a manager who regularly performs similar tasks each day. Their workflow may consist of comparing fleet metrics with local data from your software. By creating a custom page Add-In, you can combine both of these tasks into one easy-to-use page where all the information is readily available.

Another example is to quickly navigate between different areas of Geotab. A simple-to-use one-click button Add-In can be made for most pages. The button will guide the user between areas, and can optionally use the page state to automatically fill in URL parameters to run reports with a single click.

**Requirements**

The Add-Ins created must have their source code stored externally using your own hosting provider or your own servers.

Referenced files must be publicly accessible via HTTPS and all hosted resources must be on a server that supports TLS 1.2 or higher.

**Accessibility**

Add-ins must comply with  [WCAG 2.2](https://www.w3.org/TR/WCAG22)  Level AA accessibility. Automated tools like  [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)  can test the majority of these requirements. To cover any remaining requirements, Lighthouse provides a list of  [manual test steps](https://developer.chrome.com/docs/lighthouse/accessibility/custom-control-roles)  that can be done using a screen reader such as  [VoiceOver](https://support.apple.com/en-ca/guide/voiceover/welcome/mac).

**Add-In configuration files**

Each Add-In created will have one configuration file. The configuration file is a JSON file ([http://www.json.org](http://www.json.org)) of keys and values which describes the Add-In, who is responsible for it, what source code it contains, and a digital security signature.


## Table 1 - Add-In configuration file keys/values

| Property | Description | Type | Required version |
| --- | --- | --- | --- |

| name | The name of this Add-In | String |  |
| supportEmail | Email address for support related to this Add-In | String |  |
| items | Array of custom pages and/or buttons (External references) | Array |  |
| files | Custom pages and/or buttons (Embedded code) | Object |  |
| key | Unique MyGeotab Marketplace Add-In key assigned by Geotab. If there's no plan to get your Add-In to the Marketplace, you can leave out the key/value pair from the Configuration File | String |  |
| signature | Digital signature of the Add-In | String |  |
| version | The version of the Add-In | String |  |
| enableViewSecurityId | If true, a"View{ADDIN_NAME}add-in"security clearance feature is created that must be enabled for users to be able to view the Add-In | Boolean | MyGeotab v9.0+ |
| securityIds | An array of custom security IDs that are added to the list of features available when editing clearances. These definitions can support multiple languages. e.g."securityIds": [{"name": "ExampleSecurityIdentifier1", "en": "Example Security Identifier 1"}, 
{"name": "ExampleSecurityIdentifier2", "en": "Example Security Identifier 2"}] | Array | MyGeotab v9.0+ |

If you do not know your MyGeotab Add-In key, please contact your authorized Geotab reseller for support.

The Add-In configuration file can specify the contents using either the Items, Files property, or a combination of both. It is recommended to use Items and externally referencing the source code to make development and debugging easier. When ready, the code can be embedded directly on Geotab ' s servers.

**Example Add-In configuration file**

The Add-In configuration file below demonstrates how to define a simple Add-In which references an HTML page specified by its URL. Any CSS or JavaScript which is required by the Add-In would be specified in the referenced HTML.


## Listing 1 - A simple Add-In configuration JSON file

Test the example above by navigating to Administration → System → System Settings → Add-Ins. Select New Add-In and paste the example in the configuration tab. Be sure to select save then refresh the page.

**Page Add-In navigation menu location**

Each Add-In can create a navigation entry in the left hand side menu. This allows quick and easy access to all of the Add-Ins. The placement of the navigation entry for the Add-In is specified in the configuration file, relative to another built-in navigation entry. In the section below, a navigation entry is placed directly after the Activity entry. A user with English as their interface language will see  " English Menu Text "  as the label. Note that we show only two properties for brevity.

Image 1 - Modified left-hand-side menuThe Add-In navigation entry can be placed after any of the following built-in values:


- `GettingStartedLink`
- `ActivityLink`
- `EngineMaintenanceLink`
- `ZoneAndMessagesLink`
- `RuleAndGroupsLink`
- `AdministrationLink`

To place the navigation entry as a sub-menu entry in one of the main entries, place a slash (`/`) character after the name. The custom entry will be the first item inside the sub-menu.

For example, by changing  `" ZoneAndMessagesLink/ "`  as the value for the  `" path "`  key:

`" path " :  " ZoneAndMessagesLink/ " ,`This will insert the custom navigation entry as follows:

Image 4 - Navigation entry after ZoneAndMessagesLinkNavigation entries cannot be set at the third level (sub-sub-menu) and below. If done so by the steps outlined above, the entry will simply appear as a non-formatted bullet point in the menu.

A user may not have access to some entries of the left hand side menu. The custom navigation entry will be shown after the nearest entry which is accessible to them.

**Redesigned left-hand navigation menu**

There ' s a new navigation menu that ' s currently accessible via **Feature Preview**, this new navigation menu requires the new `category` menu item property for page Add-In items.

Possible category IDs:


- `ProductivityId`
- `ComplianceId`
- `SafetyId`
- `MaintenanceId`
- `SustainabilityId`
- `PeopleId`
- `AddIns`
- `GroupsAndRulesId`
- `ReportsId`
- `GettingStartedLinkId`
- `SystemSettingsId`

If you would like to place it inside a sub menu, then fill in the sub menu ' s name as the  ' category '  value. The values can be found below:


- `PublicWorksId`
- `HOSId`
- `DiagnosticsId`
- `RoutesId`
- `AdvancedRoutingId`
- `BasicRoutingId`
- `TachographId`
- `InstallationId`
- `ReportSetupId`
- `ZonesId`

[MyGeotab Add-Ins: Introducing the Redesigned Left-hand Navigation Menu](https://docs.google.com/document/d/1zWboQArdttoMrVwNILe4vTh0hEKiBgI8Ch2vEcshlYE/edit?usp=sharing): This document goes into more details about the new menu.


## Table 2 - Menu item

| Name | Description | Type |
| --- | --- | --- |

| URL | A URL to the HTML page to load when clicking on this menu item | String |
| path | Specifies where in the menu hierarchy this menu item should reside. It will follow the menuId specified or become a child item if a trailing slash is provided, such as"ActivityLink/". | String |
| menuName | An object containing key value pairs for the text that appears on the menu item. The key is the language and the value is the text, for example:{"EN", "New menu item"}. | Object |
| icon | (To be deprecated June 04, 2021) A URL to the image (svg, png, jpg, etc.) that is placed in front of the menu item. Note that the current image size is 32x32 but it is recommended that SVG icons are used to allow for scaling. This property is to be deprecated and replaced by svgIcon for versions 2102 onward. During the transition period, if both icon and svgIcon exist, svgIcon will have higher priority (details here). | String |
| svgIcon | A URL to the svg image that is placed in front of the menu item. Since the image file type is a vector, you only need to submit one file in any color. The icon file will be updated to the appropriate colors (details here). A validator is availablehere. | String |


## Table 3 - Parent menu item

| Name | Description | Type |
| --- | --- | --- |

| menuId | A unique identifier for this menu. This string value of your choice but should be unique. See built-in ones above"GettingStartedLink","ActivityLink", etc. | String |
| path | Specifies where in the menu hierarchy this menu item should reside. It will follow the menuId specified or become a child item if a trailing slash is provided, such as"ActivityLink/". | String |
| menuName | An object containing key-value pairs for the text that appears on the menu item. The key is the language and the value is the text, for example:{"EN", "New menu item"}. | Object |
| icon | (To be deprecated June 04, 2021) A URL to the image (svg, png, jpg, etc.) that is placed in front of the menu item. Note that the current image size is 32x32 but it is recommended that SVG icons are used to allow for scaling. This property is to be deprecated and replaced by svgIcon for versions 2102 onward. During the transition period, if both icon and svgIcon exist, svgIcon will have higher priority (details here) . | String |
| svgIcon | A URL to the svg image that is placed in front of the menu item. Since the image file type is a vector, you only need to submit one file in any color. The icon file will be updated to the appropriate colors (details here). A validator is availablehere. | String |

**Listing 2 - Creating submenu items**

To create a sub-menu, add to the items array a special JSON object that looks nearly identical to the page item - with the exception of the URL property.

The process consists in creating a  [parent menu item](../../../index.md#geotab-add-in-table-3--parent-menu-item)  with the menuName for the submenu item, a menuId, icon, and a path for one of the build-in path navigation values (*GettingStartedLink*, *ActivityLink*, *EngineMaintenanceLink*, *ZoneAndMessagesLink*,  *RuleAndGroupsLink*, *AdministrationLink*).

To place a  [menu item](../../../index.md#geotab-add-in-table-2--menu-item)  under a parent menu item you will use the unique ID of the submenu as a path for the item. This is illustrated in the sample configuration below:


## Referencing source items

Each Add-In can define zero or more *items* as part of its configuration file. An item is a collection of keys and values which represent a page or a button.


## Table 4 - Button item

| Name | Description | Type |
| --- | --- | --- |

| page | Which built-in page to place the button on. Possible values:'map','tripsHistory','devices','device','zones','users','user','rules','rule','exceptions','customReports','customReport','engineFaults','speedProfile','hosLogs','hosLog','groupsTree','routes','fuelUsage',and'engineMeasurements'. | String |
| click | A URL to a JavaScript file which is executed when the button is clicked. | String |
| buttonName | An object containing key value pairs for the text that appears on the button. The key is the language, and the value is the text, for example{"EN", "New menu item"}. | Object |
| icon | (To be deprecated June 04, 2021) for placing it in the button label. This property is to be deprecated and replaced by svgIcon for versions 2102 onward. During the transition period, if both icon and svgIcon exist, svgIcon will have higher priority (details here). | String |
| svgIcon | A URL Reference to the svg image for placing it in the button label. Since the image file type is a vector, you only need to submit one file in any color. The icon file will be updated to the appropriate colors (details here). A validator is availablehere. | String |

At least one language is required in each item definition. The following language options are currently supported in MyGeotab: English (`" en "`), French Canada (`" fr "`), German (`" de "`), Spanish (`" es "`), Japanese (`" ja "`), Polish (`" pl "`), Brazilian Portuguese (`" pt-BR "`), Dutch (`" nl "`), Italian (`" it "`), Simplified Chinese (`" zh-Hans "`), Thai (`" th "`), Indonesian (`" id "`), Czech (`" cs "`), Swedish (`" sv "`), Turkish (`" tr "`), Malay (`" ms "`), French France (`" fr-FR "`), and Korean (`" ko-KR "`).

Reference to the image can be an external URL such as: `https://mysite.com/images/icon.png;` or a link to the image from the images folder of your Add-In.

When using the items property to include your source code exclusively, you can set the files property an empty object using  `{ }` as seen in Listing 1.

Every Add-In has a JavaScript object which is set in your main.js file. For example, the Add-In class name  " myaddin "  is provided by the following JavaScript entry point:

The name you provide should be unique for each Add-In and should take care to avoid including invalid characters in the name. Additionally, when referencing Add-Ins hosted externally, the absolute path to the Add-In should not include the following characters anywhere in their URL:


- " - "  The dash symbol
- " @ "  The  " at "  symbol
- " # "  The hash symbol

For example, the following is an invalid absolute URL due to its dashes and will not be loaded correctly by MyGeotab:

`https://my-web-server.com/pathToAddIn/index.html`
## Embedding source code

When developing a custom page or button Add-In, you have the option to embed the source code for your project in the JSON configuration file. When using this method, there is no requirement to host your own HTML, CSS, or JavaScript files as they will be converted into strings and written inside the configuration file itself.


## Listing 3 - Add-In configuration file using embedded source code

Please be aware that some characters may need to use HTML escape characters ([HTML ISO-8859-1 Reference](http://www.w3schools.com/charsets/ref_html_8859.asp)) and  [Character Reference](http://dev.w3.org/html5/html-author/charref)  for the overall JSON object to be validated.

By reproducing the previous example, there would be two folders, one named  " js "  and the other  " css " . Inside the folders are two JavaScript files and one CSS stylesheet; respectively.

The user experience of your custom Add-In can be enhanced by including images in the configuration file. This can be performed in two ways; see Listings 4, 5, and 6 below.


## Listing 4 - Absolute path to image in HTML

Referencing an external image using an absolute URL in the HTML or CSS.


## Listing 5 - Absolute path to image in CSS


## Listing 6 - Add-In configuration file with Base64 encoded image

The other method is to embed the images along with the rest of the source code in the markup. First, the images will need to be encoded using  [Base64 encoding](http://en.wikipedia.org/wiki/Base64), then the references to the image files replaced with the encoded version directly in the HTML or CSS.

**Using third-party libraries**

Add-Ins can include references to external libraries that have been custom developed or to existing libraries such as jQuery. This is performed in the traditional way by including a  `< script >`  tag to the URL of the file.


## Listing 7 - Referencing jQuery from an Add-In

Keep in mind that the end-user using the Add-In will be viewing your Add-In from a Geotab server. The files referenced must be publicly available on the Internet. Firewalls cannot be configured with a specific IP address for the Geotab server as the address may change in the future.

References to external source files can either be absolute URLs such as the example in Listing 7 or can be relative references to local files as demonstrated in Listing 3.


## Listing 8 - Avoiding CSS naming conflicts

When referencing the CSS files, keep in mind that naming conflicts are possible. Geotab ' s outer framework defines a number of CSS styles for common HTML tags which the custom Add-In may inherit. When designing HTML tags, it is recommended to prefix the HTML tags with a common name when they are stylized with the CSS.

**Page lifecycle**

When designing a custom page Add-In, it is important to understand the JavaScript events that take place on Geotab ' s servers. The user-defined JavaScript code must supply an entry point object which will be created with a predefined parameter signature. From these parameters, a signed-in Geotab API object will be received, along with the page state and a callback synchronization function.

Every page on Geotab ' s servers, including custom page Add-Ins, have the following three methods called during their lifecycle:

Table 5 - Add-In lifecycle methods

| Method | Description | Signature |
| --- | --- | --- |

| initialize | Called only once when your custom page is first accessed. Use this method to initialize variables required by your Add-In. | function(api, state, callback){... } |
| focus | This method is called after the user interface has loaded or the state of the organization filter is changed. Use this method for initial interactions with the user or elements on the page. | function(api, state){... } |
| blur | This method is called when the user is navigating away from your page. Use this method to save any required state. | function(api, state){... } |


## Visual diagram

Understanding the workflow and methods called will help you design a responsive custom page Add-In. Keep in mind that your initialize method will only be called once, unless the user explicitly refreshes their web browser. When the user interface is ready, the  `focus` method will be called. Finally, when the user is navigating away from your custom page Add-In, the `blur`  method will be called, completing the Add-In lifecycle.

It ' s important to call the `callback` passed into `initialize` *after* all work is complete. Keep in mind the asynchronous nature of JavaScript.

Image 2 - Add-In lifecycle workflow diagram

## Lifecycle implementation

The following code can be used as a starting point for a custom page Add-In. All of the lifecycle methods are defined, and the optional  `focus` and `blur` methods will be called due to the `callback` method being called in the  `initialize` method.

Use the commented area to define and then assign variables in the scope of the Add-In. Each of the Add-Ins will need to define its own unique namespace with the prefix `geotab.addin` (note that the namespace is not hyphenated). In the example below, the full namespace is `geotab.addin.myCustomPage1`.


## Listing 9 - HTML and JavaScript entry point example

**Custom button Add-Ins**

Custom button Add-Ins allow you to extend the capabilities of a built-in Geotab page by appending a new button to the top menu of the page. When a user clicks the custom button Add-In, the JavaScript method that has been defined will be called. This JavaScript method has access to the event which was generated by the click, the Geotab API under the credentials of the current user, and the page state variables.


## Button Add-In configuration file

The following example adds a custom button Add-In to the live map page. When clicked, the button will redirect the user to the vehicles page. Use this example as a starting point for creating your own custom button Add-Ins.

The exact position of the custom button Add-In within a built-in page is defined by the developer. For instance, in Image 3, a new button labeled *Perform Action* is added to the toolbar of the live map page.

This example uses external references to the source code. Similar to custom page Add-Ins, the Files property of the configuration file can be used to embed the source code on the Geotab servers.

Image 3 - Custom button Add-In on the live map page

## Use cases

The action your custom button Add-In performs is decided by your specific business requirement. The following are example actions that can be implemented:


- One-click navigation between maps and reports
- Call an API to alert for driver proximity
- Create a new zone at the current location
- Automated execution of a sequence of actions

## Listing 10 - Custom button Add-In configuration file

Almost any page is available to have a custom button Add-In added to it. Use a web browser ' s address bar to find the correct value for the Page property. Geotab pages will have a trailing hash (“#”) symbol followed by the page name. Determine the page name and then set the “page” value of your custom button Add-In configuration file to that value.

**JavaScript button action**

When a custom button Add-In is clicked by a user, it will execute a predefined method from the JavaScript file referenced. This method provides the button action with access to the generated event, the Geotab API as the signed-in user, and the page state.

To avoid conflicts with multiple Add-Ins enabled on an account, be certain to create unique namespaces for each Add-In.


## Listing 12 - Custom button click method

The state object is a powerful tool for creating navigational components by changing the current page state. The state object has access to a number of methods as follows:


## Table 6 - Geotab page state methods

| Method | Description | Parameters | Return type |
| --- | --- | --- | --- |

| getState | Gets an object that represents the current URL state | None | Object |
| setState | Sets the current URL state. The object parameter is a modified state retrieved fromgetState | Object | Void |
| gotoPage | Redirects the user to another page with optional parameters. Example:state.gotoPage("map",{someParameter1: true, someParameter2: 5 }); | String, [Object] | Void |
| hasAccessToPage | Checks whether the current user has the security clearance to view a page by its#(hash) value. Example:var result = state.hasAccessToPage("map"); | String | Boolean |
| getGroupFilter | Gets an array with ids of the selected groups in the organization filter. Example:var result = state.getGroupFilter(); | None | Array |
| getAdvancedGroupFilter | Gets an object with arelationproperty and agroupFilterConditionsarray of the selected groups in the organization filter. Example:var result = state.getAdvancedGroupFilter(); | None | Object |

The second parameter to the `gotoPage` method is optional and is used for query string parameters.

**Complete integration example**

Using all the concepts outlined in this document, the following is a complete integration example which creates a custom page Add-In with real-world functionality. In this example, the custom page has JavaScript methods that make requests using the Geotab API to retrieve the current vehicles on your account. The result of the API request is shown on the custom page in a list. Finally, when the user leaves the page, the custom page performs cleanup during the lifecycle methods.

For the purpose of this example, the integrationExample.css and integrationExample.js are empty files.


## Source code


## Listing 13 - HTML and JavaScript code for integration example


## Listing 14 - Configuration file for integration example

**Troubleshooting and debugging**

When developing Add-Ins, the use of Google Chrome and its Developer Tools window is recommended. To open the Chrome Developer Tools on Windows, press CTRL + SHIFT + I; on a Mac, press CMD + OPTION + I.

The contents of  `console.log( " ... " )`  statements can be examined using the Developer Tools, the timeline of XML HTTP requests can be viewed, and breakpoints to step through the JavaScript source code can be created.

It is also recommended to read Google ' s extensive learning resources available on using  [Chrome Developer Tools](https://developers.google.com/chrome-developer-tools/)  to get started debugging or learn about the advanced features they have available.

**Note:** Add-Ins that were locally added to a database in the past (recommended approach is to host on a server externally) might throw the error message  **" Add-In threw an error. Please contact your administrator. "**  To further confirm, the following error will appear in the browser console (found by hitting CTRL+SHIFT+I):  **Error: Add-In files:  < add-in file name >  couldn ' t be loaded. Probably they were moved to another location or removed.**  This could be linked to a server maintenance/migration event. The workaround would be to re-upload the files for the Add-Ins back to the database, while the resolution would be to externally host the source code as per the requirements listed  [here](../../../index.md#geotab-add-in-requirements).

**Add-In icon validator**

The Add-In Icon Validator tests uploaded SVG files against  [Geotab ' s requirements](https://www.geotab.com/blog/mygeotab-add-in-icons-specs/)  and displays them in the reformatted colors and style that will be displayed in MyGeotab.