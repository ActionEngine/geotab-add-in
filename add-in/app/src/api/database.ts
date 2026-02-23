import { GeotabSession } from "mg-api-js";

const BASE_URL = import.meta.env.VITE_BASE_URL;

const DATABASE_ENDPOINT = `${BASE_URL}/database`;
const DATABASE_GET_ENDPOINT = `${DATABASE_ENDPOINT}/get_database`;
// const DATABASE_INIT_ENDPOINT = `${DATABASE_ENDPOINT}/init`;

export const getDatabase = (session: GeotabSession) => {
  return fetch(`${DATABASE_GET_ENDPOINT}`, {
    method: "GET",
    headers: {
      "geotab-session-id": session.credentials.sessionId || "",
      "geotab-database": session.credentials.database,
      "geotab-username": session.credentials.userName,
    },
  });
};
