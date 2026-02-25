import AppView from "@/components/pages/app-view/app-view";
import AppContextProvider from "@/provider/app-provider";
import QueryProvider from "@/provider/query-provider";
import "@geotab/zenith/dist/index.css";
import "./style.css";

interface AppProps {
  api: GeotabApi; // Type is defined globally in geotab.d.ts
  isLocalDevelopment: boolean;
}

const App = ({ api, isLocalDevelopment }: AppProps) => {
  return (
    <QueryProvider>
      <AppContextProvider>
        <AppView api={api} isLocalDevelopment={isLocalDevelopment} />
      </AppContextProvider>
    </QueryProvider>
  );
};

export default App;
