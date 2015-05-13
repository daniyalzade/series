from influxdb import InfluxDBClient
import warnings
warnings.filterwarnings("ignore")

from env import CREDS

client = InfluxDBClient(**CREDS)

def get_client():
    return client
