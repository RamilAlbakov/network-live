"""Update network live with enm nr5g cells."""

import cx_Oracle
from network_live.enm.enm_cli import get_enm_ip_data
from network_live.enm.nr.nr_enm_cli import get_enm_nr_data
from network_live.enm.nr.nr_parser import add_non_cell_parameters
from network_live.enm.nr.nr_sql import NrSql
from network_live.enm.parser import parse_enm_cells
from network_live.sql import Atoll


def nr_main():
    """
    Update network live with enm nr5g cells.

    Returns:
        string
    """
    nr_atoll = Atoll(NrSql.nr_delete_sql, NrSql.nr_insert_sql, NrSql.nr_select_sql)
    enm_data = get_enm_nr_data()
    non_cell_data = {
        'enm_sectors': enm_data['enm_nr_sectors'],
        'enm_site_ids': enm_data['enm_site_ids'],
        'enm_ips': get_enm_ip_data()['enm_bbu_ip_data'],
        'atoll_data': nr_atoll.select_physical_parameters(),
    }
    cells = parse_enm_cells(
        enm_data['enm_nr_cells'],
        enm_data['last_parameter'],
        'nr',
        non_cell_data,
        add_non_cell_parameters,
    )
    try:
        nr_atoll.delete_data()
    except cx_Oracle.Error:
        return 'NR ENM Fail'

    try:
        nr_atoll.update_network_live(list(cells))
    except cx_Oracle.Error:
        return 'NR ENM Fail'

    return 'NR ENM Success'
