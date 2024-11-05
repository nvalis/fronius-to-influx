import time
from typing import Any, Dict, List, Type
import schedule

import pytz
from astral import LocationInfo
from influxdb_client import InfluxDBClient
from requests import get
from requests.exceptions import ConnectionError


class FroniusToInflux:
    def __init__(
            self, client: InfluxDBClient, inverter_address: str, endpoints: List[str]
    ) -> None:
        self.client = client
        self.inverter_address = inverter_address
        self.endpoints = endpoints

    def parse_data(self, data, endpoint) -> Dict:
        pd = {}
        if endpoint == "/solar_api/v1/GetMeterRealtimeData.cgi":
            pd = data["Body"]["Data"]["0"]
        return pd

    def job(self) -> None:
        collected_data = {}
        for endpoint in self.endpoints:
            response = get(f"http://{self.inverter_address}{endpoint}")
            data = response.json()
            parsed = self.parse_data(data, endpoint)
            collected_data[endpoint] = parsed
        print(collected_data)
        # write datapoints to influxdb

    def run(self) -> None:
        schedule.every(10).seconds.do(self.job)

        while True:
            schedule.run_pending()
            time.sleep(1)
