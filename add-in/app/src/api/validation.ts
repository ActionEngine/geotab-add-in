import {
  ValidationDeviceResponse,
  ValidationResponse,
} from "@/types/shemas/validaton";
import { GeotabCredentials } from "mg-api-js";
import { getHeaders } from "./helper";

const BASE_URL = import.meta.env.VITE_BASE_URL;

const VALIDATION_ENDPOINT = `${BASE_URL}/validation`;
const VALIDATION_BY_DEVICE_ENDPOINT = `${VALIDATION_ENDPOINT}/by-device`;

export const getValidation = async (
  session: GeotabCredentials,
): Promise<ValidationResponse[] | []> => {
  const headers = getHeaders(session);
  const response = await fetch(`${VALIDATION_ENDPOINT}`, {
    method: "GET",
    headers,
  });
  if (response.status !== 200) {
    return [];
  }

  const result = await response.json();

  return result;
};

export const getValidationByDevice = async (
  session: GeotabCredentials,
): Promise<ValidationDeviceResponse[] | []> => {
  const headers = getHeaders(session);
  const response = await fetch(`${VALIDATION_BY_DEVICE_ENDPOINT}`, {
    method: "GET",
    headers,
  });
  if (response.status !== 200) {
    return [];
  }

  const result = await response.json();

  return result;
};
