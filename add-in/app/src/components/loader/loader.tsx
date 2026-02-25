import "./loader.css";

interface LoaderProps {
  loading: boolean;
}

const Loader = ({ loading }: LoaderProps) => {
  if (!loading) return null;
  return (
    <div className="overlay">
      <div className="loader" />
    </div>
  );
};

export default Loader;
