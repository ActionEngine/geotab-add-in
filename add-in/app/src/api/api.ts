import GeotabApi from "mg-api-js";

const user = import.meta.env.VITE_GEOTAB_EMAIL as string;
const database = import.meta.env.VITE_GEOTAB_DATABASE as string;
const password = import.meta.env.VITE_GEOTAB_PASSWORD as string;

const authentication = {
  credentials: {
    database: database,
    userName: user,
    password: password,
  },
};

const api = new GeotabApi(authentication);

export const apiGet = async <T>(typeName: string): Promise<T> => {
  return (await api.call("Get", {
    typeName: typeName,
  })) as T;
};
