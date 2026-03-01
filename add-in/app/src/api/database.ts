import { AuthInitialState } from "@/types/auth";
import { DatabaseResponse } from "@/types/schemas/database";
import { GeotabCredentials } from "mg-api-js";
import { getHeaders } from "./helper";

const BASE_URL = import.meta.env.VITE_BASE_URL;

const DATABASE_ENDPOINT = `${BASE_URL}/database`;

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
