import { useEffect } from "react";
import { Button } from "@geotab/zenith";
import "@geotab/zenith/dist/index.css";
import { getSessionAsync } from "../utils/geotabApi";
import "./style.css";

interface AppProps {
  api: GeotabApi; // Type is defined globally in geotab.d.ts
}

const App = ({ api }: AppProps) => {
  useEffect(() => {
    // eslint-disable-next-line no-console
    getSessionAsync(api).then((session) => console.log(session));
  });

  // Example: Using the Geotab API with promisified wrapper
  // import { callAsync } from "../utils/geotabApi";
  // const handleFetchDevices = async () => {
  //   try {
  //     const devices = await callAsync(api, "Get", { typeName: "Device" });
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
