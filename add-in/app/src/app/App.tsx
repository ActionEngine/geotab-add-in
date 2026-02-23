import { useEffect, useState } from "react";
import { getDatabase } from "@/api/database";
import GeotabMap from "@/components/geotab-map/geotab-map";
import QueryProvider from "@/provider/query-provider";
import { getSessionAsync } from "@/utils/geotabApi";
import "@geotab/zenith/dist/index.css";
import { GeotabSession } from "mg-api-js";
import "./style.css";

interface AppProps {
  api: GeotabApi; // Type is defined globally in geotab.d.ts
}

const App = ({ api }: AppProps) => {
  const [isAuth, setIsAuth] = useState(false);
  const [session, setSession] = useState<GeotabSession | null>(null);

  const fetchSession = async () => {
    try {
      const sessionRes = await getSessionAsync(api);
      setSession(sessionRes);
    } catch (error) {
      console.error("Error fetching session:", error);
    }
  };

  useEffect(() => {
    fetchSession();
  }, []);

  useEffect(() => {
    if (session === null) return;

    getDatabase(session as GeotabSession).then((response) => {
      console.log(response);
    });
  }, [session]);

  return (
    <QueryProvider>
      <GeotabMap />
    </QueryProvider>
  );
};

export default App;
