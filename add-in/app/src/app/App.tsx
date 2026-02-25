import { useCallback, useEffect, useState } from "react";
import { databaseInit, getDatabase } from "@/api/database";
import AuthDialog from "@/components/auth-dialog/auth-dialog";
import DataQuality from "@/components/data-quality/data-quality";
import GeotabMap from "@/components/geotab-map/geotab-map";
import Loader from "@/components/loader/loader";
import BannerUI from "@/components/ui/banner/banner";
import QueryProvider from "@/provider/query-provider";
import { AuthInitialState } from "@/types/auth";
import { DATABASE_STATUS, DatabaseResponse } from "@/types/shemas/database";
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

  const fetchDatabase = useCallback(() => {
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
  }, [session]);

  useEffect(() => {
    fetchSession();
  }, []);

  useEffect(() => {
    if (session === null) return;

    // eslint-disable-next-line no-console
    console.log(session);

    fetchDatabase();
  }, [session, fetchDatabase]);

  useEffect(() => {
    if (
      databaseInfo === null ||
      databaseInfo.ingestion_status === DATABASE_STATUS.DONE
    ) {
      return;
    }

    const intervalId = window.setInterval(() => {
      fetchDatabase();
    }, 5000);

    return () => {
      window.clearInterval(intervalId);
    };
  }, [databaseInfo, fetchDatabase]);

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
      .catch(() => setLoading(false));
  };

  return (
    <QueryProvider>
      {databaseInfo?.ingestion_status === DATABASE_STATUS.DONE ? (
        <DataQuality />
      ) : (
        <GeotabMap api={api} />
      )}
      <AuthDialog
        open={openModal}
        onSubmit={handleAuthSubmit}
        session={session}
      />
      <Loader loading={loading} />
      <BannerUI
        isOpen={
          databaseInfo !== null &&
          databaseInfo?.ingestion_status !== DATABASE_STATUS.DONE
        }
        type="info"
      >
        Aspen is being initialized
      </BannerUI>
    </QueryProvider>
  );
};

export default App;
