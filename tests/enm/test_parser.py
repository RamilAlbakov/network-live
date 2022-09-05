"""Test functions from enm.parser module."""

from network_live.enm.parser import parse_mo_value, parse_parameter, parse_fdn

fdn = 'FDN : SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE_Turkestan,MeContext=ERBS_42036_TURKELEVAT_KB,ManagedElement=ERBS_42036_TURKELEVAT_KB,ENodeBFunction=1,NbIotCell=542036-204'


def test_parse_mo_value():
    """Test parse_fdn function."""
    subnetwork = parse_mo_value(fdn, 'SubNetwork')
    site_name = parse_mo_value(fdn, 'MeContext')
    cell_name = parse_mo_value(fdn, 'NbIotCell')

    assert subnetwork == 'LTE_Turkestan'
    assert site_name == 'ERBS_42036_TURKELEVAT_KB'
    assert cell_name == '542036-204'


def test_parse_parameter():
    """Test parse_parameter function."""
    parameter_strings = [
        'earfcndl : 6200',
        'eutranCellRef : SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE_Turkestan,MeContext=ERBS_42036_TURKELEVAT_KB,ManagedElement=ERBS_42036_TURKELEVAT_KB,ENodeBFunction=1,EUtranCellFDD=542036-104',
    ]
    parameters = [parse_parameter(parameter_string) for parameter_string in parameter_strings]

    assert parameters == [['earfcndl', '6200'], ['eutranCellRef', '542036-104']]


def test_parse_fdn():
    """Test parse_fdn function."""
    cell = parse_fdn(fdn, 'iot')
    expected = {
        'subnetwork': 'LTE_Turkestan',
        'site_name': 'ERBS_42036_TURKELEVAT_KB',
        'cell_name': '542036-204',
    }
    assert cell == expected
