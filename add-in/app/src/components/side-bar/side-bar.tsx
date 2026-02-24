import { DatabaseResponse } from "@/types/shemas/database";
import "./side-bar.css";

interface SideBarProps {
  databaseInfo: DatabaseResponse | null;
}

const SideBar = ({ databaseInfo }: SideBarProps) => {
  if (!databaseInfo) return null;
  return (
    <div className="side-bar">
      <div>Aspen is being initialized</div>;
    </div>
  );
};

export default SideBar;
