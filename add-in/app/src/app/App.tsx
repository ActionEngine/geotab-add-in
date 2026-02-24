import { useEffect, useState } from "react";
import { databaseInit, getDatabase } from "@/api/database";
import AuthDialog from "@/components/auth-dialog/auth-dialog";
import GeotabMap from "@/components/geotab-map/geotab-map";
import Loader from "@/components/loader/loader";
import SideBar from "@/components/side-bar/side-bar";
import QueryProvider from "@/provider/query-provider";
import { AuthInitialState } from "@/types/auth";
import { DatabaseResponse } from "@/types/shemas/database";
import { getSessionAsync } from "@/utils/geotabApi";
import { geotabSessionParse } from "@/utils/sessionParse";
import "@geotab/zenith/dist/index.css";
import { GeotabCredentials, GeotabSession } from "mg-api-js";
import "./style.css";

interface AppProps {
  api: GeotabApi; // Type is defined globally in geotab.d.ts
  isLocalDevelopment: boolean;
}

const App = ({ api, isLocalDevelopment }: AppProps) => {
  const [databaseInfo, setDatabaseInfo] = useState<DatabaseResponse | null>(
    null,
  );
  const [openModal, setOpenModal] = useState(false);
  const [loading, setLoading] = useState(true);
  const [session, setSession] = useState<GeotabCredentials | null>(null);
  const fetchSession = async () => {
    try {
      const sessionRes = await getSessionAsync(api);
      if (isLocalDevelopment) {
        setSession(geotabSessionParse(sessionRes as GeotabSession));
        return;
      }
      setSession(sessionRes as GeotabCredentials);
    } catch (error) {
      console.error("Error fetching session:", error);
    }
  };

  const fetchDatabase = () => {
    if (session === null) return;
    getDatabase(session)
      .then((response) => {
        if (!response) {
          setOpenModal(true);
          return;
        }
        setDatabaseInfo(response);
      })
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    fetchSession();
  }, []);

  useEffect(() => {
    if (session === null) return;

    // eslint-disable-next-line no-console
    console.log(session);

    fetchDatabase();
  }, [session]);

  const handleAuthSubmit = (data: AuthInitialState) => {
    if (session === null) return;
    setLoading(true);
    databaseInit(session, data)
      .then((response) => {
        if (response.status === 200) {
          setOpenModal(false);
          fetchDatabase();
        }
      })
      .finally(() => setLoading(false));
  };

  return (
    <QueryProvider>
      <SideBar databaseInfo={databaseInfo} />
      <GeotabMap api={api} />
      <AuthDialog
        open={openModal}
        onSubmit={handleAuthSubmit}
        session={session}
      />
      <Loader loading={loading} />
    </QueryProvider>
  );
};

export default App;
