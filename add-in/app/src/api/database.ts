import { AuthInitialState } from "@/types/auth";
import { DatabaseResponse } from "@/types/shemas/database";
import { GeotabCredentials } from "mg-api-js";

const BASE_URL = import.meta.env.VITE_BASE_URL;

const DATABASE_ENDPOINT = `${BASE_URL}/database`;

const getHeaders = (session: GeotabCredentials) => {
  return {
    "geotab-session-id": session.sessionId || "",
    "geotab-database": session.database,
    "geotab-username": session.userName,
  };
};

export const getDatabase = async (
  session: GeotabCredentials,
): Promise<DatabaseResponse | null> => {
  const headers = getHeaders(session);
  const response = await fetch(`${DATABASE_ENDPOINT}`, {
    method: "GET",
    headers,
  });
  if (response.status !== 200) {
    return null;
  }

  const result = await response.json();

  return result;
};

export const databaseInit = async (
  session: GeotabCredentials,
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
