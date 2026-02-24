import { GeotabCredentials, GeotabSession } from "mg-api-js";

export const geotabSessionParse = (
  session: GeotabSession,
): GeotabCredentials => {
  return {
    sessionId: session.credentials.sessionId,
    database: session.credentials.database,
    userName: session.credentials.userName,
  };
};
