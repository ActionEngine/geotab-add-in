// Geotab Add-In entry point
import ReactDOM from "react-dom/client";
import App from "@/app/App";
import "@geotab/zenith/dist/index.css";
import GeotabApi from "mg-api-js";

// Local development mode - create API instance from env variables
const isLocalDevelopment = typeof geotab === "undefined";

if (isLocalDevelopment) {
  const container = document.getElementById("root");
  if (container) {
    const root = ReactDOM.createRoot(container);

    // Create Geotab API client using the official mg-api-js library
    const localApi = new GeotabApi({
      credentials: {
        database: import.meta.env.VITE_GEOTAB_DATABASE,
        userName: import.meta.env.VITE_GEOTAB_EMAIL,
        password: import.meta.env.VITE_GEOTAB_PASSWORD,
      },
      path: import.meta.env.VITE_GEOTAB_SERVER || "my.geotab.com",
    });

    // Authenticate immediately to catch credential errors early
    localApi.authenticate().catch((error) => {
      console.error("Geotab authentication failed:", error);
    });

    root.render(<App api={localApi} />);
  }
} else {
  // Production mode - use Geotab add-in pattern
  geotab.addin.aspenDQ = function () {
    let root: ReactDOM.Root | null = null;

    return {
      initialize: function (_api: any, _state: any, callback: () => void) {
        callback();
      },

      // eslint-disable-next-line @typescript-eslint/no-unused-vars
      focus: function (api: any, _state: any) {
        const container = document.getElementById("root");
        if (container) {
          root = ReactDOM.createRoot(container);
          root.render(<App api={api} />);
        }
      },

      blur: function () {
        if (root) {
          root.unmount();
          root = null;
        }
      },
    };
  };
}
