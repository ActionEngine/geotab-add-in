import { createContext, useState } from "react";
import { LngLatLike } from "react-map-gl/mapbox-legacy";
import Loader from "@/components/loader/loader";
import BannerUI from "@/components/ui/banner/banner";
import { DATABASE_STATUS, DatabaseResponse } from "@/types/schemas/database";
import { GeotabCredentials } from "mg-api-js";

interface ViewMapState {
  longitude: LngLatLike;
  latitude: LngLatLike;
  zoom: number;
}

type AppContextType = {
  isLoading: boolean;
  session: GeotabCredentials | null;
  globalBbox: readonly [number, number, number, number] | null;
  mapStateMain: ViewMapState | null;
  mapStateChecks: ViewMapState | null;
  databaseInfo: DatabaseResponse | null;
  updateIsLoading: (loading: boolean) => void;
  updateDatabaseInfo: (info: DatabaseResponse) => void;
  updateSession: (session: GeotabCredentials) => void;
  updateMapStateMain: (mapState: ViewMapState) => void;
  updateMapStateChecks: (mapState: ViewMapState) => void;
  updateGlobalBbox: (
    bbox: readonly [number, number, number, number] | null,
  ) => void;
};

const initialState: AppContextType = {
  isLoading: false,
  session: null,
  globalBbox: null,
  mapStateMain: null,
  mapStateChecks: null,
  databaseInfo: null,
  updateIsLoading: () => {},
  updateDatabaseInfo: () => {},
  updateSession: () => {},
  updateMapStateMain: () => {},
  updateMapStateChecks: () => {},
  updateGlobalBbox: () => {},
};

export const AppContext = createContext(initialState);

const AppContextProvider = ({ children }: { children: React.ReactNode }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [mapStateMain, setMapStateMain] = useState<ViewMapState | null>(null);
  const [mapStateChecks, setMapStateChecks] = useState<ViewMapState | null>(
    null,
  );
  const [session, setSession] = useState<GeotabCredentials | null>(null);
  const [databaseInfo, setDatabaseInfo] = useState<DatabaseResponse | null>(
    null,
  );
  const [globalBbox, setGlobalBbox] = useState<
    readonly [number, number, number, number] | null
  >(null);

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

  const updateMapStateMain = (mapState: ViewMapState | null) => {
    setMapStateMain(mapState);
  };

  const updateMapStateChecks = (mapState: ViewMapState | null) => {
    setMapStateChecks(mapState);
  };

  const updateGlobalBbox = (
    bbox: readonly [number, number, number, number] | null,
  ) => {
    setGlobalBbox(bbox);
  };

  const value = {
    isLoading,
    session,
    databaseInfo,
    globalBbox,
    mapStateMain,
    mapStateChecks,
    updateGlobalBbox,
    updateMapStateMain,
    updateMapStateChecks,
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
