import { useEffect, useState } from "react";
import { getDatabase } from "@/api/database";
import AuthDialog from "@/components/auth-dialog/auth-dialog";
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
  const [openModal, setOpenModal] = useState(false);
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
      if (response.status === 200) {
        setIsAuth(true);
        return;
      }
      setOpenModal(true);
    });
  }, [session]);

  return (
    <QueryProvider>
      <GeotabMap />
      <AuthDialog open={openModal} />
    </QueryProvider>
  );
};

export default App;
