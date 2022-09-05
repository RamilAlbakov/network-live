"""Get ENM data related to iot cells."""

from network_live.enm.enm_cli import execute_cli_command


def get_enm_iot_data():
    """
    Get ENM data related to iot cells.

    Returns:
        dict
    """
    iot_cell_parameters = [
        'cellId',
        'administrativeState',
        'cellBarred',
        'freqBand',
        'earfcndl',
        'nbIotCellType',
        'ceLevelNumber',
        'cmcIndex',
        'dlAnchPrbIndex',
        'ulAnchPrbIndex',
        'maxRrcConnectedUsers',
        'physicalLayerCellId',
        'tac',
        'qRxLevMin',
        'cellRange',
        'eutranCellRef',
        'plmnReservedList',
    ]

    iot_cell_cli_command = 'cmedit get * NbIotCell.({parameters})'.format(
        parameters=','.join(iot_cell_parameters),
    )

    return {
        'iot_data': execute_cli_command(iot_cell_cli_command),
        'last_parameter': sorted(iot_cell_parameters)[-1],
    }
