# Scace Temperature Measurement

## Testing protocol

The measurement with a Scace is quite clearly defined (but leaves some latitude). The measuring process and the evaluation are defined here: [PROCEDURE FOR THE MEASUREMENT OF BREWING WATER TEMPERATURE IN ESPRESSO COFFEEMACHINES (2017)](https://www.worldcoffeeevents.org/wp-content/uploads/2017/01/2017-WCE-Procedure-for-Measuring-Brewing-Temperature-in-Espresso-Machines-2.pdf). For reference there is a decent collection of results here: [https://www.dieroester.at/kaffeetratsch/temperaturstabiliaet-bei-espressomaschinen](https://www.dieroester.at/kaffeetratsch/temperaturstabiliaet-bei-espressomaschinen).

## Reference values

This repository contains reference values in the directory `ref_values`. The reference values are measured with a Lelit Bianca v3. There are variations with flush, no flush, 10 sec flush and different offset values.

## Preparation

- Machine should be heated for 1 hour. This is a value at which every machine/brew group will really have reached its temperature
- Fill the water tank completely before taking the measurement and empty the drip tray, because you may not have time to make up for it later
- Place a small sponge under the Scace. Since the Scace produces a very fine and sharp jet, a sponge very well reduces the formation of a fine mist under the brew group, which can indeed have a cooling effect

- Optional: Decide wheter you want to use a flush. Stick to the exact timing of flushing for no longer than 5 seconds. You can use the 10s counter before the next cycle in this script to flush.

## Prerequisites

- Espresso machine
- Scace 2 device
- Amprobe TMD-56
- Micro USB to USB cable
- Python3 installation

## Setup

- Connect Scace 2 with Amprobe TMD-56 via T1
- Turn on the Amprobe TMD-56 (it is recommended to turn off the Auto Off functionality)
- Connect the Amprobe TMD-56 with your computer via Micro USB to USB cable
- Check if Python 3 is installed `python3 --version`

## Install dependencies

- `pip install -r requirements.txt`
- Note: it is recommended to use a virtual enviornment (further reading: [VirtualEnv and Pip Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/))

## Running the measurement

`python3 main.py`

## Output

Output is stored in CSV files for each cycle (e.g., `0.csv`, `1.csv`, `...`)
