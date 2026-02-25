import { useCallback, useContext, useEffect, useState } from "react";
import { databaseInit, getDatabase } from "@/api/database";
import AuthDialog from "@/components/auth-dialog/auth-dialog";
import GeotabMap from "@/components/geotab-map/geotab-map";
import DataQuality from "@/components/pages/data-quality/data-quality";
import { AppContext } from "@/provider/app-provider";
import { AuthInitialState } from "@/types/auth";
import { DATABASE_STATUS } from "@/types/shemas/database";
import { getSessionAsync } from "@/utils/geotabApi";
import { geotabSessionParse } from "@/utils/sessionParse";
import "@geotab/zenith/dist/index.css";
import { GeotabCredentials, GeotabSession } from "mg-api-js";

interface AppViewProps {
  api: GeotabApi; // Type is defined globally in geotab.d.ts
  isLocalDevelopment: boolean;
}

const AppView = ({ api, isLocalDevelopment }: AppViewProps) => {
  const {
    session,
    databaseInfo,
    updateSession,
    updateDatabaseInfo,
    updateIsLoading,
  } = useContext(AppContext);

  const [openModal, setOpenModal] = useState(false);

  const fetchSession = async () => {
    try {
      const sessionRes = await getSessionAsync(api);
      if (isLocalDevelopment) {
        updateSession(geotabSessionParse(sessionRes as GeotabSession));
        return;
      }
      updateSession(sessionRes as GeotabCredentials);
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
        updateDatabaseInfo(response);
      })
      .finally(() => updateIsLoading(false));
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
    }, 10000);

    return () => {
      window.clearInterval(intervalId);
    };
  }, [databaseInfo, fetchDatabase]);

  const handleAuthSubmit = (data: AuthInitialState) => {
    if (session === null) return;
    updateIsLoading(true);
    databaseInit(session, data)
      .then((response) => {
        if (response.status === 200) {
          setOpenModal(false);
          fetchDatabase();
        }
      })
      .catch(() => updateIsLoading(false));
  };

  return (
    <>
      {databaseInfo?.ingestion_status === DATABASE_STATUS.DONE ? (
        <DataQuality />
      ) : (
        <GeotabMap api={api} />
      )}
      <AuthDialog open={openModal} onSubmit={handleAuthSubmit} />
    </>
  );
};

export default AppView;
