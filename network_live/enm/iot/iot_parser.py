"""Add some common informations to iot cells."""


def add_site_data(cell):
    """
    Add some site data to cells.

    Args:
        cell: dict

    Returns:
        dict
    """
    site_data = {
        'oss': 'ENM',
        'vendor': 'Ericsson',
        'insert_date': '080922',
    }
    return {**cell, **site_data}
