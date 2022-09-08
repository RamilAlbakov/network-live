"""Parse sector parameters and site data."""

from network_live.enm.parser_utils import parse_ips, parse_mo_value, parse_parameter


def parse_sector_parameters(enm_sector_data):
    """
    Parse parameters related to NRSectorCarrier mo.

    Args:
        enm_sector_data: ElementGroup

    Returns:
        dict
    """
    sectors = {}
    for element in enm_sector_data:
        element_value = element.value()
        if 'FDN' in element_value:
            sector = parse_mo_value(element_value, 'NRSectorCarrier')
            sectors[sector] = {}
        elif ' : ' in element_value:
            parameter_name, parameter_value = parse_parameter(element_value)
            sectors[sector][parameter_name] = parameter_value
    return sectors


def parse_ids(enm_id_data):
    """
    Parse site ids.

    Args:
        enm_id_data: ElementGroup

    Returns:
        dict
    """
    site_ids = {}
    for element in enm_id_data:
        element_value = element.value()
        if 'FDN' in element_value:
            site_name = parse_mo_value(element_value, 'MeContext')
        elif ' : ' in element_value:
            site_id = parse_parameter(element_value)[-1]
            site_ids[site_name] = site_id
    return site_ids


def add_non_cell_parameters(cell, enm_sectors, enm_site_ids, enm_ips):
    """
    Add to cell parameters object parameters related to non NRCellDU mo.

    Args:
        cell: dict
        enm_sectors: ElementGroup
        enm_site_ids: ElementGroup
        enm_ips: ElementGroup

    Returns:
        dict
    """
    common_data = {
        'oss': 'ENM',
        'vendor': 'Ericsson',
        'insert_date': '060922',
        'azimut': None,
        'height': None,
        'longitude': None,
        'latitude': None,
    }
    sectors = parse_sector_parameters(enm_sectors)
    site_ids = parse_ids(enm_site_ids)
    site_ips = parse_ips(enm_ips)
    site_name = cell['site_name']

    if not cell['nCI'].isnumeric():
        cell['nCI'] = None

    return {
        'gNBId': site_ids[site_name],
        'ip_address': site_ips[site_name],
        **cell,
        **sectors[cell['cell_name']],
        **common_data,
    }
