import { useState } from "react";
import { AuthInitialState } from "@/types/auth";
import { Button, FormGroup, TextInput } from "@geotab/zenith";
import { GeotabSession } from "mg-api-js";
import "./auth-dialog.css";

interface AuthDialogProps {
  open: boolean;
  session: GeotabSession | null;
  onSubmit?: (initState: AuthInitialState) => void;
}

const AuthDialog = ({ open, session, onSubmit }: AuthDialogProps) => {
  const userName = session?.credentials.userName || "";
  const database = session?.credentials.database || "";
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
              label="User name"
              readOnlyValue
              disabled
            />
          </FormGroup>
          <FormGroup>
            <TextInput
              value={database}
              label="Database"
              readOnlyValue
              disabled
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
