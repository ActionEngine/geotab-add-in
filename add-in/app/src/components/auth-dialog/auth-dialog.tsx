import { useState } from "react";
import { AuthInitialState } from "@/types/auth";
import { Button, FormGroup, TextInput } from "@geotab/zenith";
import "./auth-dialog.css";

interface AuthDialogProps {
  open: boolean;
  onSubmit?: (initState: AuthInitialState) => void;
}

const AuthDialog = ({ open, onSubmit }: AuthDialogProps) => {
  const [userName, setUserName] = useState("");
  const [database, setDatabase] = useState("");
  const [password, setPassword] = useState("");
  if (!open) return null;

  const handleSubmit = () => {
    onSubmit?.({
      user_name: userName,
      database_name: database,
      password,
    });
  };

  return (
    <div className="dialog-container">
      <div className="dialog-window">
        <div className="dialog-content">
          <FormGroup>
            <TextInput
              value={userName}
              onChange={(e) => setUserName(e.target.value)}
              label="User name"
            />
          </FormGroup>
          <FormGroup>
            <TextInput
              value={database}
              onChange={(e) => setDatabase(e.target.value)}
              label="Database"
            />
          </FormGroup>
          <FormGroup>
            <TextInput
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              label="Password"
              type="password"
            />
          </FormGroup>
        </div>
        <div className="dialog-footer">
          <Button
            disabled={!userName || !database || !password}
            type="primary"
            onClick={handleSubmit}
          >
            Initialize
          </Button>
        </div>
      </div>
    </div>
  );
};

export default AuthDialog;
