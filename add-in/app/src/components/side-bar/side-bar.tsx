import { DatabaseResponse } from "@/types/shemas/database";
import "./side-bar.css";

interface SideBarProps {
  databaseInfo: DatabaseResponse | null;
}

const SideBar = ({ databaseInfo }: SideBarProps) => {
  if (!databaseInfo) return null;
  return <div className="side-bar">Aspen is being initialized</div>;
};

export default SideBar;
