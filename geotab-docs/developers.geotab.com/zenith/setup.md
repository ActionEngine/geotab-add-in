By using Zenith, you consent to all terms of use. Full terms of use can be seen  [here](https://docs.google.com/document/d/17DJX3BAIgVq0APHiENi3dN2KFEN9BqgiSahsDGpQaCo/edit?tab=t.0).


**React**

Zenith library is a set of React components. To learn more, visit the React documentation  [Quick Start](https://react.dev/learn)  page.

**Project Installation and setup**

Zenith is distributed as an npm package on  [npmjs.com](https://www.npmjs.com/).

Go to the root of your project and run the following command:

**Importing styles**

Styles in Zenith library are located in the css file`@geotab/zenith/dist/index.css`, which should be included in your project. The following is an example of how to include them if your builder handles css imports:

It can also be imported in your less/sass file.

**Usage**

If you have followed the installation process correctly, you can now import components from the package:

Components are now ready for use

**Available components**

The Zenith component library, based on the Zenith Design System, provides a wide range of UI elements for building consistent and engaging interfaces. These elements include:
- **Foundational element:**Colors, icons, and font presets.
- **Atomic components:**Basic building blocks like buttons, checkboxes, and input fields.
- **Higher-order components:**Complex components such as headers, tables, and filter bars.

A complete list of available components and usage examples can be found in  [Storybook](../zenith-storybook/index.md)  .

**Colors**

Zenith provides a defined color palette, where each color has a specific name, purpose, and value. This palette ensures consistency and accessibility across all applications. Colors are defined as CSS custom properties, offering flexibility and maintainability. They can be used within Zenith components and throughout any application for a unified style.

Explore the full color palette and usage guidelines in  [Storybook](../zenith-storybook/index.md@path=%252Fdocs%252Fglobal-styles-colors--docs.md)  .

The following is an example of how Zenith colors can be used:

**Typography**

Zenith defines typography presents for various use cases. These styles can be applied to your components, assigned class names to your HTML elements, or integrated into your classes (if you are using CSS-preprocessors such as less or sass.

Explore the full range of typography presets in  [Storybook](../zenith-storybook/index.md@path=%252Fdocs%252Fglobal-styles-typography--docs.md).

Components are now ready for use.

**Caption**

Caption is a set of CSS class names which enables positioning two or three elements with default padding. The helper aligns elements vertically and sets default spacing between them. It consists of the following classes:
- zen-caption — the parent element
- zen-caption__pre-content — the first element (usually an icon)
- zen-caption__content — the main content element (usually a text)
- zen-caption__post-content — an additional element at the end (usually an icon)

The most popular use case is  " Icon + Text " . It consists of the following CSS classes:

**Link**

Link is a class name used to apply Zenith styles to a link. It also uses the following modifications:
- zen-link zen-link—disabled — disable the style of a link
- zen-link zen-link—inline — remove paddings/margins (This is useful when a link is embedded in text)
- zen-link zen-link—hidden — applies  " display:none "  and makes the link invisible
- zen-link zen-link—light — displays the link without an underline

**UI components**

Zenith provides a comprehensive set of UI components which can be combined like building blocks to create complex user interfaces. All components are fully independent and can be used in any combination. A full list of components can be found in  [Storybook](../zenith-storybook/index.md).

Components should be imported from the npm package prior to use:

Some components are not available in the index file of the npm package and must be imported directly from the file as below:

**Containers**

Zenith offers versatile container components like Card and Summary tiles. These provide features like titles, tooltips, and menus, while allowing you to customize the content within. For example, a Card can display anything from page summary information to line charts, all with consistent styling for borders, titles, and interactive elements.

**User language and date format**

Zenith includes components such as DateRange, which relies on date and time format. Use UserFormatProvider to wrap your application and set date formats as below:

Use the properties dateFormat and language to configure both date and time format and language in the current user object. FiltersBar.PeriodPicker will format dates according to your settings:

Zenith only provides translation for built-in strings. In the example above, only the beta pill will be translated by Zenith; Page name must be translated prior to using it in the component.

**Troubleshooting**

Please visit our Zenith  [community page](https://community.geotab.com/s/group/0F9Pd0000003b33KAA/geotab-zenith)  or contact  [zenith@geotab.com](mailto:zenith@geotab.com)  if you have any questions or feedback.