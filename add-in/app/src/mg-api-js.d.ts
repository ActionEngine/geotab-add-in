// Type declarations for mg-api-js

declare module "mg-api-js" {
  interface GeotabCredentials {
    database: string;
    userName: string;
    password?: string;
    sessionId?: string;
  }

  interface GeotabAuthentication {
    credentials: GeotabCredentials;
    path?: string;
  }

  interface GeotabOptions {
    rememberMe?: boolean;
    timeout?: number;
    newCredentialStore?: any;
    fullResponse?: boolean;
  }

  interface GeotabSession {
    credentials: GeotabCredentials;
    path: string;
  }

  class GeotabApi {
    constructor(authentication: GeotabAuthentication, options?: GeotabOptions);

    // Authenticate method
    authenticate(): Promise<void>;
    authenticate(
      successCallback: () => void,
      errorCallback: (message: string, error: any) => void,
    ): void;

    // Call method
    call(method: string, params: any): Promise<any>;
    call(
      method: string,
      params: any,
      successCallback: (result: any) => void,
      errorCallback?: (message: string, error: any) => void,
    ): void;

    // MultiCall method
    multiCall(calls: Array<[string, any]>): Promise<any[]>;
    multiCall(
      calls: Array<[string, any]>,
      successCallback: (results: any[]) => void,
      errorCallback?: (message: string, error: any) => void,
    ): void;

    // GetSession method
    getSession(): Promise<GeotabSession>;
    getSession(successCallback: (session: GeotabSession) => void): void;

    // Forget method
    forget(): Promise<GeotabCredentials>;
  }

  export = GeotabApi;
}
