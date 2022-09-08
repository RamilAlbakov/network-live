"""Some functions which help to parse needed data."""

import re


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


def get_ip(ip_string):
    """
    Parse ip address from string.

    Args:
        ip_string: string

    Returns:
        string
    """
    ip_re_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    try:
        ip_address = re.search(ip_re_pattern, ip_string).group()
    except AttributeError:
        ip_address = None
    return ip_address


def parse_ips(enm_ip_data):
    """
    Parse ip addresses for nodes in enm data.

    Args:
        enm_ip_data: enmscripting ElementGroup

    Returns:
        dict
    """
    node_ips = {}
    oam = False
    for element in enm_ip_data:
        element_value = element.value()
        if 'FDN' in element_value and 'oam' in element_value.lower():
            name = parse_mo_value(element_value, 'MeContext')
            oam = True
        elif ' : ' in element_value and oam:
            node_ips[name] = get_ip(element_value)
            oam = False
    return node_ips
