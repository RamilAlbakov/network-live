import pytest


class ElementGroup(object):
    def __init__(self, element):
        self.element = element

    def value(self):
        return self.element


@pytest.fixture()
def enm_nr_sector_data():
    sector_data_values = (
        'FDN : SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE_Turkestan,MeContext=gRBS_42039_ALPAMYS,ManagedElement=gRBS_42039_ALPAMYS,GNBDUFunction=1,NRSectorCarrier=642039-152',
        'arfcnDL : 646666',
        'bSChannelBwDL : 100',
        'configuredMaxTxPower : 200000',
        'FDN : SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE_Turkestan,MeContext=gRBS_42476_TURRIXOS,ManagedElement=gRBS_42476_TURRIXOS,GNBDUFunction=1,NRSectorCarrier=642476-150',
        'arfcnDL : 646666',
        'bSChannelBwDL : 100',
        'configuredMaxTxPower : 200000',
        '2 instance(s)',
    )
    return (
        ElementGroup(sector_data) for sector_data in sector_data_values
    )


@pytest.fixture()
def enm_site_ids():
    site_ids_values = (
        'FDN : SubNetwork=ONRM_ROOT_MO,SubNetwork=NR_Almaty,MeContext=gRBS_00484_TEXOFFICE_K,ManagedElement=gRBS_00484_TEXOFFICE_K,GNBDUFunction=1',
        'gNBId : 600484',
        'FDN : SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE_Almaty,MeContext=GRBS_99999_TEXOFFICE_TEST,ManagedElement=GRBS_99999_TEXOFFICE_TEST,GNBDUFunction=1',
        'gNBId : 699999',
        '2 instance(s)',
    )
    return (
        ElementGroup(site_id_data) for site_id_data in site_ids_values
    )

@pytest.fixture()
def enm_cell_data():
    enm_cells_values = (
        'FDN : SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE_Turkestan,MeContext=gRBS_42952_TURVOKZAL,ManagedElement=gRBS_42952_TURVOKZAL,GNBDUFunction=1,NRCellDU=642952-150',
        'cellLocalId : 150',
        'cellState : ACTIVE',
        'nCI : 10534125718',
        'nRPCI : 21',
        'nRTAC : 17266',
        'qRxLevMin : -128',
        'rachRootSequence : 2',
        'FDN : SubNetwork=ONRM_ROOT_MO,SubNetwork=LTE_Turkestan,MeContext=gRBS_42952_TURVOKZAL,ManagedElement=gRBS_42952_TURVOKZAL,GNBDUFunction=1,NRCellDU=642952-154',
        'cellLocalId : 154',
        'cellState : ACTIVE',
        'nCI : 10534125722',
        'nRPCI : 23',
        'nRTAC : 17266',
        'qRxLevMin : -128',
        'rachRootSequence : 109 ',
        '2 instance(s)',
    )
    return (
        ElementGroup(enm_cell) for enm_cell in enm_cells_values
    )


def add_func(cell, non_cell_data):
    return {**cell, **non_cell_data}

@pytest.fixture()
def add_non_cell_data():
    return add_func
