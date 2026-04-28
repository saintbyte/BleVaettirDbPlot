#!/bin/bash
set -x
.venv/bin/python chart.py --db data.db --sensor-name "Thermometer" --width 4000 --type humidity --output thermometer_humidity_chart.png
.venv/bin/python chart.py --db data.db --sensor-name "Indoor Hall Thermometer" --width 4000  --type humidity --output indoor_thermometer_humidity_chart.png
