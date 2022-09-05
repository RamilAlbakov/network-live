"""Update network live with enm iot cells."""

import cx_Oracle
from network_live.enm.iot.iot_enm_cli import get_enm_iot_data
from network_live.enm.iot.iot_parser import add_site_data
from network_live.enm.iot.iot_sql import IotSqls
from network_live.enm.parser import parse_enm_cells
from network_live.sql import Atoll


def iot_main():
    """
    Update network live with enm iot cells.

    Returns:
        string
    """
    enm_iot_data = get_enm_iot_data()
    iot_cells = parse_enm_cells(
        enm_iot_data['iot_data'],
        enm_iot_data['last_parameter'],
        'iot',
        add_site_data,
    )

    iot_atoll = Atoll(IotSqls.iot_delete_sql, IotSqls.iot_insert_sql)

    iot_atoll.delete_data()
    try:
        iot_atoll.update_network_live(list(iot_cells))
    except cx_Oracle.Error:
        return 'IOT ENM Fail'
    return 'IOT ENM Success'
