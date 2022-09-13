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
    nr_select_sql = """
        SELECT
            atoll_mrat.xgcells5gnr.cell_id,
            atoll_mrat.xgtransmitters.azimut,
            atoll_mrat.xgtransmitters.height,
            atoll_mrat.sites.longitude,
            atoll_mrat.sites.latitude
        FROM
            atoll_mrat.xgtransmitters
        INNER JOIN atoll_mrat.xgcells5gnr
            ON atoll_mrat.xgcells5gnr.tx_id = atoll_mrat.xgtransmitters.tx_id
        INNER JOIN atoll_mrat.sites
            ON atoll_mrat.xgtransmitters.site_name = atoll_mrat.sites.name
    """
