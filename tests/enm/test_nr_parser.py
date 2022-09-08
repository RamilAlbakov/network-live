"""Test functions from nr_parser mofule."""

from network_live.enm.nr.nr_parser import parse_sector_parameters, parse_ids


def test_parse_sector_parameters(enm_nr_sector_data):
    """Test parse_sector_parameters function."""
    nr_sectors = parse_sector_parameters(enm_nr_sector_data)
    first_sector = {
        'arfcnDL': '646666',
        'bSChannelBwDL': '100',
        'configuredMaxTxPower': '200000',
    }
    second_sector = {
        'arfcnDL': '646666',
        'bSChannelBwDL': '100',
        'configuredMaxTxPower': '200000',
    }
    assert nr_sectors['642039-152'] == first_sector
    assert nr_sectors['642476-150'] == second_sector


def test_parse_ids(enm_site_ids):
    """Test parse_ids function."""
    site_ids = parse_ids(enm_site_ids)
    assert site_ids['gRBS_00484_TEXOFFICE_K'] == '600484'
    assert site_ids['GRBS_99999_TEXOFFICE_TEST'] == '699999'
