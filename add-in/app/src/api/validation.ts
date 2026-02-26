import {
  ValidationDeviceResponse,
  ValidationDistanceToRoadResponse,
  ValidationResponse,
  ValidationTeleportationResponse,
} from "@/types/shemas/validaton";
import { GeotabCredentials } from "mg-api-js";
import { getHeaders } from "./helper";

const BASE_URL = import.meta.env.VITE_BASE_URL;

const VALIDATION_ENDPOINT = `${BASE_URL}/validation`;
const VALIDATION_BY_DEVICE_ENDPOINT = `${VALIDATION_ENDPOINT}/by-device`;
const GET_VALIDATION_TELEPORTATION_ENDPOINT = (device_id: string) =>
  `${VALIDATION_ENDPOINT}/teleportation/?deviceId=${device_id}`;
const GET_VALIDATION_DISTANCE_TO_ROAD_ENDPOINT = (device_id: string) =>
  `${VALIDATION_ENDPOINT}/distance-to-road/?deviceId=${device_id}`;

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

export const getValidationTeleportation = async (
  session: GeotabCredentials,
  devaceId: string,
): Promise<ValidationTeleportationResponse[] | []> => {
  const headers = getHeaders(session);
  const response = await fetch(
    GET_VALIDATION_TELEPORTATION_ENDPOINT(devaceId),
    {
      method: "GET",
      headers,
    },
  );
  if (response.status !== 200) {
    return [];
  }
  const result = await response.json();

  return result;
};

export const getValidationDistanceToRoad = async (
  session: GeotabCredentials,
  devaceId: string,
): Promise<ValidationDistanceToRoadResponse[] | []> => {
  const headers = getHeaders(session);
  const response = await fetch(
    GET_VALIDATION_DISTANCE_TO_ROAD_ENDPOINT(devaceId),
    {
      method: "GET",
      headers,
    },
  );
  if (response.status !== 200) {
    return [];
  }

  const result = await response.json();

  return result;
};
