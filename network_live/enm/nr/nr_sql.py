"""Sql commands for nrcells tabel."""


class NrSql(object):
    """Sql commands for nrcells tabel."""

    nr_delete_sql = 'TRUNCATE TABLE nrcells'

    nr_insert_sql = """
        INSERT
            INTO nrcells
        VALUES (
            :subnetwork,
            :gNBId,
            :site_name,
            :cell_name,
            :cellLocalId,
            :cellState,
            :nCI,
            :nRPCI,
            :nRTAC,
            :rachRootSequence,
            :qRxLevMin,
            :arfcnDL,
            :bSChannelBwDL,
            :configuredMaxTxPower,
            :ip_address,
            :vendor,
            :insert_date,
            :oss,
            :azimut,
            :height,
            :longitude,
            :latitude
        )
    """
