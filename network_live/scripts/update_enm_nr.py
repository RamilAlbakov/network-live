"""Update network live with enm nr5g cells."""

from dotenv import load_dotenv
from network_live.enm.nr.nr_main import nr_main

load_dotenv('.env')


def main():
    """Update network live with enm nr5g cells."""
    print(nr_main())
