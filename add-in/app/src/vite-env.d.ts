/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_BASE_URL: string;
  readonly VITE_GEOTAB_EMAIL: string;
  readonly VITE_GEOTAB_PASSWORD: string;
  readonly VITE_GEOTAB_DATABASE: string;
  readonly VITE_GEOTAB_SERVER: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
