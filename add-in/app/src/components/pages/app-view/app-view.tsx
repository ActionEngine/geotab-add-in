import { useCallback, useContext, useEffect, useState } from "react";
import { databaseInit, getDatabase } from "@/api/database";
import AuthDialog from "@/components/auth-dialog/auth-dialog";
import GeotabMap from "@/components/geotab-map/geotab-map";
import DataQuality from "@/components/pages/data-quality/data-quality";
import AspenGis from "@/components/ui/aspen-gis/aspen-gis";
import { AppContext } from "@/provider/app-provider";
import { AuthInitialState } from "@/types/auth";
import { DATABASE_STATUS } from "@/types/schemas/database";
import { getSessionAsync } from "@/utils/geotabApi";
import { geotabSessionParse } from "@/utils/sessionParse";
import "@geotab/zenith/dist/index.css";
import { GeotabSession } from "mg-api-js";

interface AppViewProps {
  api: GeotabApi; // Type is defined globally in geotab.d.ts
}

const AppView = ({ api }: AppViewProps) => {
  const {
    session,
    databaseInfo,
    updateSession,
    updateDatabaseInfo,
    updateIsLoading,
  } = useContext(AppContext);

  const [openModal, setOpenModal] = useState(false);
  const [databaseInitialized, setDatabaseInitialized] = useState(true);

  const fetchSession = async () => {
    try {
      const sessionRes = await getSessionAsync(api);
      updateSession(geotabSessionParse(sessionRes as GeotabSession));
    } catch (error) {
      console.error("Error fetching session:", error);
    }
  };

  const fetchDatabase = useCallback(async () => {
    if (session === null) return;
    try {
      const database = await getDatabase(session);
      setDatabaseInitialized(true);
      if (!database) {
        setOpenModal(true);
        setDatabaseInitialized(false);
        return;
      }
      updateDatabaseInfo(database);
    } finally {
      updateIsLoading(false);
    }
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

    let timeoutId: number | null = null;
    let isCancelled = false;

    const pollDatabase = async () => {
      await fetchDatabase();

      if (isCancelled) {
        return;
      }

      timeoutId = window.setTimeout(pollDatabase, 15000);
    };

    timeoutId = window.setTimeout(pollDatabase, 15000);

    return () => {
      isCancelled = true;
      if (timeoutId !== null) {
        window.clearTimeout(timeoutId);
      }
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
      {databaseInfo?.ingestion_status === DATABASE_STATUS.DONE && (
        <DataQuality api={api} />
      )}
      {(!databaseInitialized ||
        (databaseInfo &&
          databaseInfo.ingestion_status !== DATABASE_STATUS.DONE)) && (
        <GeotabMap api={api} isAuthPage />
      )}
      <AuthDialog open={openModal} onSubmit={handleAuthSubmit} />
      <AspenGis />
    </>
  );
};

export default AppView;
