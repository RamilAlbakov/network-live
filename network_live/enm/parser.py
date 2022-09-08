"""Parse enm cell data."""

from collections import deque

from network_live.enm.parser_utils import parse_mo_value, parse_parameter


def parse_fdn(fdn, technology):
    """
    Parse all neccessary mo values from fdn according to technology.

    Args:
        fdn: string
        technology: string

    Returns:
        dict
    """
    enm_mo_types = {
        'iot': ['SubNetwork', 'MeContext', 'NbIotCell'],
        'nr': ['SubNetwork', 'MeContext', 'NRCellDU'],
    }

    network_live_fields = {
        'iot': ['subnetwork', 'site_name', 'cell_name'],
        'nr': ['subnetwork', 'site_name', 'cell_name'],
    }

    return {
        field: parse_mo_value(fdn, mo_type) for field, mo_type in zip(
            network_live_fields[technology],
            enm_mo_types[technology],
        )
    }


def parse_enm_cells(enm_cells, last_parameter, technology, non_cell_data, add_non_cell_data):
    """
    Parse enm cells parameters from enmscripting ElementGroup.

    Args:
        enm_cells: ElementGroup
        last_parameter: string
        technology: string
        non_cell_data: dict
        add_non_cell_data: function

    Returns:
        deque object
    """
    cells = deque()
    for element in enm_cells:
        element_value = element.value()
        if 'FDN' in element_value:
            cell = parse_fdn(element_value, technology)
        elif ' : ' in element_value:
            parameter_name, parameter_value = parse_parameter(element_value)
            cell[parameter_name] = parameter_value
            if parameter_name == last_parameter:
                cells.append(
                    add_non_cell_data(cell, **non_cell_data),
                )
    return cells
