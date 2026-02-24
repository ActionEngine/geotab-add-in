import { useState } from "react";
import { AuthInitialState } from "@/types/auth";
import { Button, FormGroup, TextInput } from "@geotab/zenith";
import { GeotabCredentials } from "mg-api-js";
import "./auth-dialog.css";

interface AuthDialogProps {
  open: boolean;
  session: GeotabCredentials | null;
  onSubmit?: (initState: AuthInitialState) => void;
}

const AuthDialog = ({ open, session, onSubmit }: AuthDialogProps) => {
  const userName = session?.userName || "";
  const database = session?.database || "";
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
    <div className="overlay">
      <div className="dialog">
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
