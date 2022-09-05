"""Update network live with enm iot cells."""

from dotenv import load_dotenv
from network_live.enm.iot.iot_main import iot_main

load_dotenv('.env')


def main():
    """Update network live with enm iot cells."""
    print(iot_main())
