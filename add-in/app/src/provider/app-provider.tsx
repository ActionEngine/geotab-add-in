import { createContext, useState } from "react";
import Loader from "@/components/loader/loader";
import BannerUI from "@/components/ui/banner/banner";
import { DATABASE_STATUS, DatabaseResponse } from "@/types/shemas/database";
import { GeotabCredentials } from "mg-api-js";

type AppContextType = {
  isLoading: boolean;
  session: GeotabCredentials | null;
  databaseInfo: DatabaseResponse | null;
  updateIsLoading: (loading: boolean) => void;
  updateDatabaseInfo: (info: DatabaseResponse) => void;
  updateSession: (session: GeotabCredentials) => void;
};

const initialState: AppContextType = {
  isLoading: false,
  session: null,
  databaseInfo: null,
  updateIsLoading: () => {},
  updateDatabaseInfo: () => {},
  updateSession: () => {},
};

export const AppContext = createContext(initialState);

const AppContextProvider = ({ children }: { children: React.ReactNode }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [session, setSession] = useState<GeotabCredentials | null>(null);
  const [databaseInfo, setDatabaseInfo] = useState<DatabaseResponse | null>(
    null,
  );

  const updateIsLoading = (loading: boolean) => {
    setIsLoading((prev) => {
      if (prev === loading) return prev;
      return loading;
    });
  };

  const updateDatabaseInfo = (info: DatabaseResponse | null) => {
    setDatabaseInfo(info);
  };

  const updateSession = (session: GeotabCredentials | null) => {
    setSession(session);
  };

  const value = {
    isLoading,
    session,
    databaseInfo,
    updateIsLoading,
    updateDatabaseInfo,
    updateSession,
  };

  return (
    <AppContext.Provider value={value}>
      {children}
      <Loader loading={isLoading} />
      <BannerUI
        isOpen={
          databaseInfo !== null &&
          databaseInfo?.ingestion_status !== DATABASE_STATUS.DONE
        }
        type="info"
      >
        Aspen is being initialized
      </BannerUI>
    </AppContext.Provider>
  );
};

export default AppContextProvider;
