// Source: https://github.com/id-keenan/ibt-conversion
// Copyright (c) 2021 Ryan Keenan — ISC License (see LICENSE-ibt-conversion.txt)
// Modified by Rafaël HOCQUEL, 2026

require("regenerator-runtime/runtime");

const telemetryLib = require("ibt-telemetry");
const fs = require("fs");

let params = [];

var argv = require("minimist")(process.argv.slice(2));

const pathToIbt = argv._[0];
// Change this list manually (for now) if you want to change the params output in the CSV
const defaultParams = [
  "Speed",
  "Throttle",
  "Brake",
  "Clutch",
  "Gear",
  "RPM",
  "LapDistPct",
  "LapDist",
  "Lap",
  "LapBestLap",
  "LapBestLapTime",
  "TrackTemp",
  "Lat",
  "Lon",
  "SteeringWheelAngle",
  "FuelLevel",
];
params = defaultParams;

let csvString = params.toString() + "\n";
const telemetry = telemetryLib.Telemetry.fromFile(pathToIbt).then(
  (promisedData) => {
    let index = 0;
    for (sample of promisedData.samples()) {
      let current = [];
      for (paramIndex in params) {
        param = sample.getParam(params[paramIndex]);
        if (param !== null && typeof param !== undefined) {
          current.push(param.value);
        } else {
          current.push("");
        }
      }
      csvString += current.toString() + "\n";
      index++;
    }
    fs.writeFile("./output.csv", csvString, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      //file written successfully
    });
    console.log("CSV successfully created.");
  },
);
