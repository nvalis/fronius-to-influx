from fronius_to_influx import FroniusToInflux
from influxdb_client import InfluxDBClient
from astral import LocationInfo
import pytz

INFLUX_ADDR = "10.0.0.3"
INFLUX_TOKEN = "=="
INFLUX_ORG = "my-org"
INFLUX_BUCKET = "solar"
INVERTER_ADDR = "10.0.0.200"
USED_ENPOINTS = [
    #"/solar_api/v1/GetInverterRealtimeData.cgi",
    #"/solar_api/v1/GetInverterInfo.cgi",
    #"/solar_api/v1/GetActiveDeviceInfo.cgi",
    "/solar_api/v1/GetMeterRealtimeData.cgi",
    #"/solar_api/v1/GetStorageRealtimeData.cgi",
    #"/solar_api/v1/GetPowerFlowRealtimeData.fcgi",
]

z = FroniusToInflux(
    client = InfluxDBClient(url=INFLUX_ADDR, token=INFLUX_TOKEN, org=INFLUX_ORG),
    inverter_address = INVERTER_ADDR,
    endpoints = USED_ENPOINTS,
)
z.IGNORE_SUN_DOWN = True
z.run()
