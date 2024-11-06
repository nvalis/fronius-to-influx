# fronius-to-influx
Collect Fronius inverter data and save in Influxdb for Grafana. This tool collects the most basic Fronius inverter data for a most basic fotovoltaic setup. If your installation is more sophisticated, then probably some extra work will be reqired. 

# fronius endpoints
This tool collects data from the following endpoints: 

    http://<fronius_ip>/solar_api/v1/GetInverterRealtimeData.cgi
    http://<fronius_ip>/solar_api/v1/GetMeterRealtimeData.cgi
    http://<fronius_ip>/solar_api/v1/GetStorageRealtimeData.cgi
    http://<fronius_ip>/solar_api/v1/GetPowerFlowRealtimeData.fcgi

# run
To run this tool adjust configuration (IP addresses, port numbers, user names and passwords, list of endpoints) in `compose.yaml` and create a :

    vim compose.yaml
    echo "==my-token" > influx_token.txt

Then run:

    docker compose build && docker compose up -d
