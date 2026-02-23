import GeotabMap from "@/components/geotab-map/geotab-map";
import QueryProvider from "@/provider/query-provider";
import "@geotab/zenith/dist/index.css";
import "./style.css";

const App = () => {
  return (
    <QueryProvider>
      <GeotabMap />
    </QueryProvider>
  );
};

export default App;
