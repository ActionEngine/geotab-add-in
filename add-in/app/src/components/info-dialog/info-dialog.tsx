import {
  IconClose,
  IconPlusCircle,
  IconQuestion,
  IconWarning,
  Popup,
  TextIconButton,
} from "@geotab/zenith";
import "./auth-dialog.css";

interface InfoDialogProps {
  open: boolean;
  onClose?: () => void;
}

const SegmentPopupContent = () => (
  <div
    style={{
      maxWidth: 380,
      padding: "0.75rem",
      fontSize: "0.82rem",
      lineHeight: 1.55,
      display: "flex",
      flexDirection: "column",
      gap: "0.6rem",
    }}
  >
    <div>
      <strong>What is a Road Segment?</strong>
      <p style={{ margin: "0.25rem 0 0" }}>
        A Road Segment is a specific, standardized section of a roadway defined
        by the Overture Maps global infrastructure dataset. Instead of looking
        at a vehicle's performance over an entire trip, Aspen breaks every route
        into these precise segments to create a localized baseline.
      </p>
    </div>
    <div>
      <strong>Why Segments Matter</strong>
      <p style={{ margin: "0.25rem 0 0" }}>
        By analyzing data at the segment level, Aspen can account for variables
        that normally trick standard diagnostics:
      </p>
      <ul style={{ margin: "0.25rem 0 0", paddingLeft: "1.1rem" }}>
        <li>
          <strong>Terrain &amp; Elevation:</strong> A truck will naturally use
          more fuel and run hotter while climbing a 6% grade. By comparing it
          only to other vehicles on that specific hill, Aspen knows if the
          increased load is normal or an anomaly.
        </li>
        <li>
          <strong>Traffic Patterns:</strong> Stop-and-go city blocks have
          different "normal" battery discharge rates than open highways.
        </li>
        <li>
          <strong>Contextual Benchmarking:</strong> Every time a vehicle in the
          Aspen network traverses a segment, it contributes to a "living
          average." Your vehicle's health is measured against the collective
          performance of every fleet vehicle that has driven that exact stretch
          of road.
        </li>
      </ul>
    </div>
    <div>
      <strong>The Benefit to You</strong>
      <p style={{ margin: "0.25rem 0 0" }}>
        This Segment Intelligence filters out the noise. When you see an
        Unhealthy Status, it means your vehicle is performing significantly
        worse than the average vehicle under the exact same road conditions,
        allowing you to identify mechanical issues or data quality issues that
        would otherwise be hidden by the environment.
      </p>
    </div>
  </div>
);

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
            <h3 className="dialog-info-content-title dialog-info-text-bold">
              Distance to Road
            </h3>
            <div>
              This metric evaluates the positioning accuracy of Geotab GO
              devices by analyzing the variance between the reported GPS
              coordinates and known road networks.
            </div>
            <div>
              Hardware Measurement: It identifies GPS Drift, where environmental
              factors or antenna degradation cause the device to report
              coordinates that physically deviate from the drivable path. A
              lower score suggests the device may be experiencing signal
              multipath issues or requires a clear view of the sky.
            </div>
            <span className="dialog-info-text-bold">Status Description:</span>
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
            <h3 className="dialog-info-content-title dialog-info-text-bold">
              Teleportation
            </h3>
            <div>
              This check monitors for impossible or illogical jumps in
              geographical coordinates between consecutive data pings.
            </div>
            <div>
              Hardware Measurement: It assesses Telemetry Integrity. If a device
              reports "teleporting" (moving between two points faster than
              physically possible), it indicates hardware-level data corruption,
              severe signal lag, or internal clock synchronization errors. This
              is a primary indicator that a device may require a firmware update
              or replacement.
            </div>
            <span className="dialog-info-text-bold">Status Description:</span>
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
            <h3 className="dialog-info-content-title dialog-info-text-bold">
              Idle Outlier
            </h3>
            <div>
              This metric identifies vehicles that report excessive or unusual
              stationary durations that do not align with standard operational
              profiles.
            </div>
            <div>
              Hardware Measurement: It evaluates the reliability of the
              Accelerometer and Ignition Sense hardware. Persistent "Idle
              Outliers" often signal a faulty connection to the vehicle's engine
              bus or a miscalibrated internal accelerometer that fails to
              trigger "Trip Start" or "Trip Stop" events accurately, leading to
              "ghost" idling data.
            </div>
            <span className="dialog-info-text-bold">Status Description:</span>
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
          <div className="info-block">
            <h3 className="dialog-info-content-title dialog-info-text-bold">
              Fuel Consumption (Anomaly Detection)
            </h3>
            <div>
              This metric evaluates the fuel efficiency of a vehicle by
              comparing its consumption against the historical average of all
              vehicles traversing the same{" "}
              <Popup
                alignment="top"
                triggerBy="click"
                trigger={
                  <span
                    style={{
                      textDecoration: "underline",
                      cursor: "pointer",
                      color: "#0078D4",
                    }}
                  >
                    road segment
                  </span>
                }
              >
                <SegmentPopupContent />
              </Popup>
              .
            </div>
            <div>
              Performance Measurement: It identifies data deviations by
              analyzing each vehicle's fuel consumption diagnostics in the
              segment they are driving in relative to the segment baseline. A
              lower score indicates the vehicle is consuming significantly more
              fuel than the average for that specific terrain or traffic
              pattern, flagging potential engine degradation, fuel leaks, or
              data collection issues.
            </div>
            <span className="dialog-info-text-bold">Status Description:</span>
            <div className="info-block-item">
              <IconPlusCircle className="pass" size="huge" />
              <div>
                <span className="pass">Healthy Status (90-100%):</span> Optimal
                efficiency. The vehicle's fuel consumption aligns perfectly with
                the established segment average for this road.
              </div>
            </div>
            <div className="info-block-item">
              <IconQuestion className="warning" size="huge" />
              <div>
                <span className="warning">Moderate Status (60-90%):</span> Minor
                efficiency variance. The vehicle is consuming more fuel than the
                segment baseline, potentially due to low tire pressure,
                early-stage engine wear, or data collection issues.
              </div>
            </div>
            <div className="info-block-item">
              <IconWarning className="fall" size="huge" />
              <div>
                <span className="fall">Unhealthy Status (0-60%):</span>{" "}
                Significant efficiency loss. Drastic deviation from the segment
                average suggests a mechanical fault, fuel system breach, or
                major data collection issues.
              </div>
            </div>
          </div>
          <div className="info-block">
            <h3 className="dialog-info-content-title dialog-info-text-bold">
              Coolant Temperature (Anomaly Detection)
            </h3>
            <div>
              This metric monitors engine operating temperatures by comparing
              them to the average thermal profile of all vehicles on the current{" "}
              <Popup
                alignment="top"
                triggerBy="click"
                trigger={
                  <span
                    style={{
                      textDecoration: "underline",
                      cursor: "pointer",
                      color: "#0078D4",
                    }}
                  >
                    road segment
                  </span>
                }
              >
                <SegmentPopupContent />
              </Popup>
              .
            </div>
            <div>
              Performance Measurement: It evaluates data deviations using each
              vehicle's cooling temperature diagnostics. By benchmarking against
              the segment average, it filters out normal temperature increases
              caused by steep inclines or heavy traffic. A lower score
              identifies a vehicle running hotter than the "norm" for that
              specific road segment or a data collection issue.
            </div>
            <span className="dialog-info-text-bold">Status Description:</span>
            <div className="info-block-item">
              <IconPlusCircle className="pass" size="huge" />
              <div>
                <span className="pass">Healthy Status (90-100%):</span> Stable
                thermal profile. The engine temperature is consistent with the
                established average for this road segment.
              </div>
            </div>
            <div className="info-block-item">
              <IconQuestion className="warning" size="huge" />
              <div>
                <span className="warning">Moderate Status (60-90%):</span>{" "}
                Thermal fluctuation detected. The engine is running warmer than
                the segment benchmark, indicating potential cooling system
                inefficiency, thermostat issues, or data collection issues.
              </div>
            </div>
            <div className="info-block-item">
              <IconWarning className="fall" size="huge" />
              <div>
                <span className="fall">Unhealthy Status (0-60%):</span> Critical
                thermal deviation. Operating temperatures are significantly
                higher than the segment average, signaling a high risk of
                radiator blockage, coolant loss, or major data collection
                issues.
              </div>
            </div>
          </div>
          <div className="info-block">
            <h3 className="dialog-info-content-title dialog-info-text-bold">
              EV Battery Discharge Rate (Anomaly Detection)
            </h3>
            <div>
              This metric measures the rate of energy depletion by benchmarking
              a vehicle's discharge against the average energy output of all EVs
              on the same{" "}
              <Popup
                alignment="top"
                triggerBy="click"
                trigger={
                  <span
                    style={{
                      textDecoration: "underline",
                      cursor: "pointer",
                      color: "#0078D4",
                    }}
                  >
                    road segment
                  </span>
                }
              >
                <SegmentPopupContent />
              </Popup>
              .
            </div>
            <div>
              Performance Measurement: It evaluates data deviations by
              monitoring battery depletion against the segment baseline. A lower
              score flags "Energy Outliers" where a vehicle is losing charge
              faster than other vehicles on the same path, identifying battery
              degradation, excessive power draw, or data collection issues.
            </div>
            <span className="dialog-info-text-bold">Status Description:</span>
            <div className="info-block-item">
              <IconPlusCircle className="pass" size="huge" />
              <div>
                <span className="pass">Healthy Status (90-100%):</span>{" "}
                Consistent energy output. The battery discharge rate matches the
                established average for this specific road segment.
              </div>
            </div>
            <div className="info-block-item">
              <IconQuestion className="warning" size="huge" />
              <div>
                <span className="warning">Moderate Status (60-90%):</span> Minor
                discharge anomaly. The vehicle is losing charge faster than the
                segment average, likely due to HVAC overuse, early-stage battery
                wear, or data collection issues.
              </div>
            </div>
            <div className="info-block-item">
              <IconWarning className="fall" size="huge" />
              <div>
                <span className="fall">Unhealthy Status (0-60%):</span> Major
                energy deviation. Rapid discharge compared to the segment
                baseline suggests significant battery cell degradation, high
                electrical load, or major data collection issues.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InfoDialog;
