// Geotab Add-In TypeScript declarations
// This file defines the global geotab object for add-in integration
// Import the GeotabApi type from mg-api-js
import GeotabApi from "mg-api-js";

// GeotabApi is the main API interface (both for mg-api-js and add-ins)
type GeotabApiInstance = GeotabApi;

interface GeotabState {
  device?: { id: string };
  language?: string;
  [key: string]: any;
}

interface GeotabAddin {
  initialize: (
    api: GeotabApiInstance,
    state: GeotabState,
    callback: () => void,
  ) => void;
  focus: (api: GeotabApiInstance, state: GeotabState) => void;
  blur: (api: GeotabApiInstance, state: GeotabState) => void;
}

declare global {
  const geotab: {
    addin: {
      [key: string]: () => GeotabAddin;
    };
  };

  // Export GeotabApi as a global type for use in components
  type GeotabApi = GeotabApiInstance;
}

export {};
