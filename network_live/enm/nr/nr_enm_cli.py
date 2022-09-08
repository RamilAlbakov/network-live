"""Get ENM data related to nr5g cells."""

from network_live.enm.enm_cli import create_cli_command, execute_cli_command


def get_enm_nr_data():
    """
    Get all neccessary nr5g data from enm.

    Returns:
        dict
    """
    nr_cell_params = [
        'cellLocalId',
        'cellState',
        'nCI',
        'nRPCI',
        'nRTAC',
        'qRxLevMin',
        'rachRootSequence',
    ]

    nr_sector_params = [
        'arfcnDL',
        'bSChannelBwDL',
        'configuredMaxTxPower',
    ]

    nr_id_parameters = [
        'gNBId',
    ]

    nr_mos = {
        'cell': 'NRCellDU',
        'sector': 'NRSectorCarrier',
        'id': 'GNBDUFunction',
    }

    return {
        'enm_nr_cells': execute_cli_command(
            create_cli_command(nr_mos['cell'], nr_cell_params),
        ),
        'enm_nr_sectors': execute_cli_command(
            create_cli_command(nr_mos['sector'], nr_sector_params),
        ),
        'enm_site_ids': execute_cli_command(
            create_cli_command(nr_mos['id'], nr_id_parameters),
        ),
        'last_parameter': sorted(nr_cell_params)[-1],
    }
