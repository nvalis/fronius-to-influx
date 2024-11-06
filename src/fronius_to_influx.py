import time
from typing import Any, Dict, List, Type
import schedule
from pprint import pprint
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import requests

class FroniusToInflux:
    def __init__(
            self, client: InfluxDBClient, bucket: str, org: str, inverter_address: str, endpoints: List[str]
    ) -> None:
        self.client = client
        self.bucket = bucket
        self.org = org
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.inverter_address = inverter_address
        self.endpoints = endpoints

    def parse_data(self, data, endpoint) -> Dict:
        dp = data["Body"]["Data"]
        points = []

        if endpoint == "/solar_api/v1/GetInverterRealtimeData.cgi":
            for k,v in dp.items():
                points.append(Point("InverterRealtimeData").field(k, v["Values"]["1"]))
        elif endpoint == "/solar_api/v1/GetInverterInfo.cgi":
            pass
        elif endpoint == "/solar_api/v1/GetActiveDeviceInfo.cgi":
            pass
        elif endpoint == "/solar_api/v1/GetMeterRealtimeData.cgi":
            dp = dp["0"]
            for k in ["Details", "Enable", "Visible", "TimeStamp"]:
                dp.pop(k)
            for k,v in dp.items():
                points.append(Point("MeterRealtimeData").field(k, v))
        elif endpoint == "/solar_api/v1/GetStorageRealtimeData.cgi":
            dp = dp["0"]["Controller"]
            dp.pop("Details")
            for k,v in dp.items():
                points.append(Point("StorageRealtimeData").field(k, v))
        elif endpoint == "/solar_api/v1/GetPowerFlowRealtimeData.fcgi":
            for k in ["P_Akku", "P_Grid", "P_Load", "P_PV", "rel_Autonomy", "E_Total"]:
                points.append(Point("PowerFlowRealtimeData").field(k, dp["Site"][k]))
        else:
            pass

        return points

    def job(self) -> None:
        for endpoint in self.endpoints:
            response = requests.get(f"http://{self.inverter_address}{endpoint}").json()
            data_points = self.parse_data(response, endpoint)
            self.write_api.write(bucket=self.bucket, org=self.org, record=data_points)

    def run(self) -> None:
        schedule.every(10).seconds.do(self.job)

        while True:
            schedule.run_pending()
            time.sleep(1)
