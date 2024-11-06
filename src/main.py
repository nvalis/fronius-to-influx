from fronius_to_influx import FroniusToInflux
import os
from influxdb_client import InfluxDBClient

INFLUX_ADDR = os.environ["INFLUX_ADDR"]
INFLUX_TOKEN = open(os.environ["INFLUX_TOKEN_FILE"]).read().strip()
INFLUX_ORG = os.environ["INFLUX_ORG"]
INFLUX_BUCKET = os.environ["INFLUX_BUCKET"]
INVERTER_ADDR = os.environ["INVERTER_ADDR"]
USED_ENPOINTS = [
    "/solar_api/v1/GetInverterRealtimeData.cgi",
    #"/solar_api/v1/GetInverterInfo.cgi",
    #"/solar_api/v1/GetActiveDeviceInfo.cgi",
    "/solar_api/v1/GetMeterRealtimeData.cgi",
    "/solar_api/v1/GetStorageRealtimeData.cgi",
    "/solar_api/v1/GetPowerFlowRealtimeData.fcgi",
]

z = FroniusToInflux(
    client = InfluxDBClient(url=INFLUX_ADDR, token=INFLUX_TOKEN, org=INFLUX_ORG),
    bucket = INFLUX_BUCKET,
    org = INFLUX_ORG,
    inverter_address = INVERTER_ADDR,
    endpoints = USED_ENPOINTS,
)
z.IGNORE_SUN_DOWN = True
z.run()
