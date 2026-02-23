import { AuthInitialState } from "@/types/auth";
import { GeotabSession } from "mg-api-js";

const BASE_URL = import.meta.env.VITE_BASE_URL;

const DATABASE_ENDPOINT = `${BASE_URL}/database`;

const getHeaders = (session: GeotabSession) => {
  return {
    "geotab-session-id": session.credentials.sessionId || "",
    "geotab-database": session.credentials.database,
    "geotab-username": session.credentials.userName,
  };
};

export const getDatabase = (session: GeotabSession) => {
  const headers = getHeaders(session);
  return fetch(`${DATABASE_ENDPOINT}`, {
    method: "GET",
    headers,
  });
};

export const databaseInit = (
  session: GeotabSession,
  data: AuthInitialState,
) => {
  const headers = getHeaders(session);
  return fetch(`${DATABASE_ENDPOINT}`, {
    method: "POST",
    headers: {
      ...headers,
      "content-type": "application/json",
    },
    body: JSON.stringify(data),
  });
};
