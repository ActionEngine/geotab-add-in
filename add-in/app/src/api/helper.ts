import { GeotabCredentials } from "mg-api-js";

export const getHeaders = (session: GeotabCredentials) => {
  return {
    "geotab-session-id": session.sessionId || "",
    "geotab-database": session.database,
    "geotab-username": session.userName,
  };
};
