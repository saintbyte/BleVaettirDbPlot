#!/bin/bash
set -x
.venv/bin/python chart.py --db data.db --sensor-name "Thermometer" --width 4000 --type temperature --output thermometer_temp_chart.png
.venv/bin/python chart.py --db data.db --sensor-name "Indoor Hall Thermometer" --width 4000  --type temperature --output indoor_thermometer_temp_chart.png
