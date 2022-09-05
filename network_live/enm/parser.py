"""Parse enm cell data."""

import re
from collections import deque


def parse_mo_value(fdn, mo_type):
    """
    Parse MO value from FDN for related MO type.

    Args:
        fdn: string
        mo_type: string

    Returns:
        strings
    """
    mo_re_patterns = {
        'MeContext': 'MeContext=[^,]*',
        'SubNetwork': ',SubNetwork=[^,]*',
        'EUtranCellFDD': 'EUtranCellFDD=.*',
        'UtranCell': 'UtranCell=.*',
        'IubLink': 'IubLink=.*',
        'GeranCell': 'GeranCell=.*',
        'ChannelGroupCell': 'GeranCell=[^,]*',
        'NRSectorCarrier': 'NRSectorCarrier=.*',
        'NRCellDU': 'NRCellDU=.*',
        'NbIotCell': 'NbIotCell=.*',
    }
    mo = re.search(mo_re_patterns[mo_type], fdn).group()
    return mo.split('=')[-1]


def parse_parameter(parameter_string):
    """
    Parse parameter name and parameter value from enm cli string.

    Args:
        parameter_string: string

    Returns:
        list
    """
    parameter_name, parameter_value = parameter_string.split(' : ')
    if parameter_name.endswith('Ref'):
        actual_parameter = parameter_value.split(',')[-1]
        parameter_value = actual_parameter.split('=')[-1]
    return [parameter_name, parameter_value]


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
    }

    network_live_fields = {
        'iot': ['subnetwork', 'site_name', 'cell_name'],
    }

    return {
        field: parse_mo_value(fdn, mo_type) for field, mo_type in zip(
            network_live_fields[technology],
            enm_mo_types[technology],
        )
    }


def parse_enm_cells(enm_cells, last_parameter, technology, add_site_data):
    """
    Parse enm cells parameters from enmscripting ElementGroup.

    Args:
        enm_cells: ElementGroup
        last_parameter: string
        technology: string
        add_site_data: function

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
                    add_site_data(cell),
                )
    return cells
