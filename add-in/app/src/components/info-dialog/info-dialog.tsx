import {
  IconClose,
  IconPlusCircle,
  IconQuestion,
  IconWarning,
  TextIconButton,
} from "@geotab/zenith";
import "./auth-dialog.css";

interface InfoDialogProps {
  open: boolean;
  onClose?: () => void;
}

const InfoDialog = ({ open, onClose }: InfoDialogProps) => {
  if (!open) return null;

  const handleClose = () => {
    onClose?.();
  };

  return (
    <div className="overlay">
      <div className="dialog-info">
        <div className="dialog-info-header">
          Hardware Status Descriptions & Metrics
          <TextIconButton
            type="tertiary"
            icon={IconClose}
            onClick={handleClose}
          />
        </div>
        <div className="dialog-info-content">
          <div className="info-block">
            <h3 className="dialog-info-content-title">Distance to Road</h3>
            <div>
              This metric evaluates the positioning accuracy of Geotab GO
              devices by analyzing the variance between the reported GPS
              coordinates and known road networks.
            </div>
            <div>
              <b>Hardware Measurement:</b> It identifies GPS Drift, where
              environmental factors or antenna degradation cause the device to
              report coordinates that physically deviate from the drivable path.
              A lower score suggests the device may be experiencing signal
              multipath issues or requires a clear view of the sky.
            </div>
            <b>Status Description:</b>
            <div className="info-block-item">
              <IconPlusCircle className="pass" size="huge" />
              <div>
                <span className="pass">Healthy Status (90-100%):</span> High
                percentage indicates minimal GPS drift and optimal antenna
                performance.
              </div>
            </div>
            <div className="info-block-item">
              <IconQuestion className="warning" size="huge" />
              <div>
                <span className="warning">Moderate Status (60-90%):</span>{" "}
                Occasional GPS "shadowing" detected. Some devices may have
                obstructed views of the sky or are experiencing minor signal
                multipath issues.
              </div>
            </div>
            <div className="info-block-item">
              <IconWarning className="fall" size="huge" />
              <div>
                <span className="fall">Unhealthy Status (0-60%):</span>{" "}
                Significant GPS drift. Multiple devices are reporting
                coordinates physically off-road, suggesting damaged antennas or
                severe environmental interference.
              </div>
            </div>
          </div>
          <div className="info-block">
            <h3 className="dialog-info-content-title">Teleportation</h3>
            <div>
              This check monitors for impossible or illogical jumps in
              geographical coordinates between consecutive data pings.
            </div>
            <div>
              <b>Hardware Measurement:</b> It assesses Telemetry Integrity. If a
              device reports "teleporting" (moving between two points faster
              than physically possible), it indicates hardware-level data
              corruption, severe signal lag, or internal clock synchronization
              errors. This is a primary indicator that a device may require a
              firmware update or replacement.
            </div>
            <b>Status Description:</b>
            <div className="info-block-item">
              <IconPlusCircle className="pass" size="huge" />
              <div>
                <span className="pass">Healthy Status (90-100%):</span>{" "}
                Excellent data integrity. Coordinates follow a logical, linear
                path with no "teleportation" or impossible jumps between pings.
              </div>
            </div>
            <div className="info-block-item">
              <IconQuestion className="warning" size="huge" />
              <div>
                <span className="warning">Moderate Status (60-90%):</span> Minor
                data gaps or latency issues. Some devices are experiencing
                desynchronization or lag in reporting.
              </div>
            </div>
            <div className="info-block-item">
              <IconWarning className="fall" size="huge" />
              <div>
                <span className="fall">Unhealthy Status (0-60%):</span> Severe
                telemetry corruption. Devices are frequently "jumping" across
                the map, indicating potential firmware failures or
                hardware-level packet loss.
              </div>
            </div>
          </div>
          <div className="info-block">
            <h3 className="dialog-info-content-title">Idle Outlier</h3>
            <div>
              This metric identifies vehicles that report excessive or unusual
              stationary durations that do not align with standard operational
              profiles.
            </div>
            <div>
              <b>Hardware Measurement:</b> It evaluates the reliability of the
              Accelerometer and Ignition Sense hardware. Persistent "Idle
              Outliers" often signal a faulty connection to the vehicle's engine
              bus or a miscalibrated internal accelerometer that fails to
              trigger "Trip Start" or "Trip Stop" events accurately, leading to
              "ghost" idling data.
            </div>
            <b>Status Description:</b>
            <div className="info-block-item">
              <IconPlusCircle className="pass" size="huge" />
              <div>
                <span className="pass">Healthy Status (90-100%):</span> Reliable
                sensor calibration. The accelerometer and ignition sense
                hardware are correctly identifying active trips versus
                stationary idling.
              </div>
            </div>
            <div className="info-block-item">
              <IconQuestion className="warning" size="huge" />
              <div>
                <span className="warning">Moderate Status (60-90%):</span>{" "}
                Periodic sensor misalignment. Some devices are reporting "ghost"
                idle events or failing to trigger trip starts immediately upon
                movement.
              </div>
            </div>
            <div className="info-block-item">
              <IconWarning className="fall" size="huge" />
              <div>
                <span className="fall">Unhealthy Status (0-60%):</span> Faulty
                hardware sensing. High rates of incorrect idling data suggest a
                loose connection to the vehicle engine bus or a failing internal
                accelerometer.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InfoDialog;
