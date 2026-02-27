import AppView from "@/components/pages/app-view/app-view";
import AppContextProvider from "@/provider/app-provider";
import QueryProvider from "@/provider/query-provider";
import "@geotab/zenith/dist/index.css";
import "./style.css";

interface AppProps {
  api: GeotabApi; // Type is defined globally in geotab.d.ts
}

const App = ({ api }: AppProps) => {
  return (
    <QueryProvider>
      <AppContextProvider>
        <AppView api={api} />
      </AppContextProvider>
    </QueryProvider>
  );
};

export default App;
