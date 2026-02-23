import { Button, FormGroup, TextInput } from "@geotab/zenith";
import "./auth-dialog.css";

interface AuthDialogProps {
  open: boolean;
}

const AuthDialog = ({ open }: AuthDialogProps) => {
  if (!open) return null;

  return (
    <div className="dialog-container">
      <div className="dialog-window">
        <div className="dialog-content">
          <FormGroup>
            <TextInput
              id="name"
              value={"name"}
              onChange={() => {}}
              label="User name"
            />
          </FormGroup>
          <FormGroup>
            <TextInput
              id="db"
              value={"db"}
              onChange={() => {}}
              label="Database"
            />
          </FormGroup>
          <FormGroup>
            <TextInput
              id="password"
              value={"password"}
              onChange={() => {}}
              label="Password"
              type="password"
            />
          </FormGroup>
        </div>
        <div className="dialog-footer">
          <Button type="primary">Initialize</Button>
        </div>
      </div>
    </div>
  );
};

export default AuthDialog;
