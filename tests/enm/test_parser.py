"""Test functions from enm.parser module."""

from network_live.enm.parser import parse_fdn, parse_enm_cells
from network_live.enm.parser_utils import parse_mo_value, parse_parameter

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


def test_parse_enm_cells(enm_cell_data, add_non_cell_data):
    """Test parse_enm_cells function."""
    common_data = {
        'non_cell_data': {'oss': 'ENM', 'vendor': 'Ericsson'},
    }
    cells = parse_enm_cells(
        enm_cell_data,
        'rachRootSequence',
        'nr',
        common_data,
        add_non_cell_data,
    )

    cell2 = cells.pop()
    cell1 = cells.pop()

    assert cell1['site_name'] == 'gRBS_42952_TURVOKZAL'
    assert cell1['cellState'] == 'ACTIVE'
    assert cell2['cell_name'] == '642952-154'
    assert cell2['oss'] == 'ENM'