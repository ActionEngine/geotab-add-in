import { useEffect, useState } from "react";
import { databaseInit, getDatabase } from "@/api/database";
import AuthDialog from "@/components/auth-dialog/auth-dialog";
import GeotabMap from "@/components/geotab-map/geotab-map";
import SideBar from "@/components/side-bar/side-bar";
import QueryProvider from "@/provider/query-provider";
import { AuthInitialState } from "@/types/auth";
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

    // eslint-disable-next-line no-console
    console.log(session);

    getDatabase(session).then((response) => {
      if (response.status === 200) {
        setIsAuth(true);
        return;
      }
      setOpenModal(true);
    });
  }, [session]);

  const handleAuthSubmit = (data: AuthInitialState) => {
    if (session === null) return;
    databaseInit(session, data).then((response) => {
      if (response.status === 200) {
        setIsAuth(true);
        setOpenModal(false);
      }
    });
  };

  return (
    <QueryProvider>
      {isAuth && <SideBar />}
      <GeotabMap api={api} />
      <AuthDialog open={openModal} onSubmit={handleAuthSubmit} />
    </QueryProvider>
  );
};

export default App;
