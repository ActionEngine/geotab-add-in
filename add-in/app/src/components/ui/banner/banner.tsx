import { Banner, IBanner } from "@geotab/zenith/esm/banner/banner";
import "./style.css";

interface BannerProps extends IBanner {
  isOpen?: boolean;
}

const BannerUI = ({ isOpen, children, ...props }: BannerProps) => {
  if (!isOpen) return null;
  return (
    <Banner className="banner-ui" {...props}>
      {children}
    </Banner>
  );
};

export default BannerUI;
