/**
 * Utility functions to promisify Geotab API methods
 * The Geotab add-in API uses callbacks, but we prefer promises for modern async/await
 */
import { GeotabCredentials } from "mg-api-js";

interface GeotabSession {
  credentials: {
    database: string;
    userName: string;
    sessionId?: string;
  };
  path: string;
}

/**
 * Promisify getSession method from Geotab API
 */
export function getSessionAsync(
  api: GeotabApi,
): Promise<GeotabSession | GeotabCredentials> {
  return new Promise((resolve, reject) => {
    try {
      // Try promise-based first (mg-api-js)
      const result = api.getSession();
      if (result && typeof result.then === "function") {
        result.then(resolve).catch(reject);
      } else {
        // Fallback to callback-based (Geotab add-in API)
        api.getSession((session: GeotabSession) => {
          resolve(session);
        });
      }
    } catch (error) {
      reject(error);
    }
  });
}

/**
 * Promisify call method from Geotab API
 */
export function callAsync(
  api: GeotabApi,
  method: string,
  params: any,
): Promise<any> {
  return new Promise((resolve, reject) => {
    try {
      // Try promise-based first (mg-api-js)
      const result = api.call(method, params);
      if (result && typeof result.then === "function") {
        result.then(resolve).catch(reject);
      } else {
        // Fallback to callback-based (Geotab add-in API)
        api.call(
          method,
          params,
          (result: any) => {
            resolve(result);
          },
          (message: string, error: any) => {
            reject(new Error(`${message}: ${error}`));
          },
        );
      }
    } catch (error) {
      reject(error);
    }
  });
}

/**
 * Promisify multiCall method from Geotab API
 */
export function multiCallAsync(
  api: GeotabApi,
  calls: Array<[string, any]>,
): Promise<any[]> {
  return new Promise((resolve, reject) => {
    try {
      // Try promise-based first (mg-api-js)
      const result = api.multiCall(calls);
      if (result && typeof result.then === "function") {
        result.then(resolve).catch(reject);
      } else {
        // Fallback to callback-based (Geotab add-in API)
        api.multiCall(
          calls,
          (results: any[]) => {
            resolve(results);
          },
          (message: string, error: any) => {
            reject(new Error(`${message}: ${error}`));
          },
        );
      }
    } catch (error) {
      reject(error);
    }
  });
}
