# fronius-to-influx
Collect Fronius inverter data and save in Influxdb for Grafana. This tool collects the most basic Fronius inverter data for a most basic fotovoltaic setup. If your installation is more sophisticated, then probably some extra work will be reqired. 

# fronius endpoints
This tool collects data from one or many of the three endpoints below. Endpoints that can be used (adjust DeviceId accordingly): 

    http://<fronius_ip>/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=3PInverterData&DeviceId=1
    http://<fronius_ip>/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=CommonInverterData&DeviceId=1
    http://<fronius_ip>/solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DataCollection=MinMaxInverterData&DeviceId=1

# install requirements
To install requirements:

    pip install -r requirements.txt

# run
To run this tool adjust configuration (IP addresses, port numbers, user names and passwords, list of endpoints) in `src/main.py`:

    vim src/main.py 

Then run:

    python src/main.py

# grafana dashboards
I put my dashboards in `grafana_dashboards` directory. Feel free to use them.
