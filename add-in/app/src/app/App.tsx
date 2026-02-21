import { Button } from "@geotab/zenith";
import "@geotab/zenith/dist/index.css";
import "./style.css";

interface AppProps {
  api: GeotabApi; // Type is defined globally in geotab.d.ts
}

const App = ({ api }: AppProps) => {
  console.log("App component initialized with API:", api);
  // Example: Using the Geotab API
  // const handleFetchDevices = () => {
  //   api.call("Get", { typeName: "Device" }, (devices) => {
  //     console.warn("Devices:", devices);
  //   }, (message, error) => {
  //     console.error("Error fetching devices:", message, error);
  //   });
  // };
  //
  // Or using promises:
  // const handleFetchDevices = async () => {
  //   try {
  //     const devices = await api.call("Get", { typeName: "Device" });
  //     console.warn("Devices:", devices);
  //   } catch (error) {
  //     console.error("Error fetching devices:", error);
  //   }
  // };

  return (
    <>
      App
      <Button>Button</Button>
    </>
  );
};

export default App;
