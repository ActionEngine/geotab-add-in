import { GeotabCredentials, GeotabSession } from "mg-api-js";

export const geotabSessionParse = (
  session: GeotabCredentials | GeotabSession,
): GeotabCredentials => {
  if ("credentials" in session) {
    return {
      sessionId: session.credentials.sessionId,
      database: session.credentials.database,
      userName: session.credentials.userName,
    };
  }
  return session;
};
