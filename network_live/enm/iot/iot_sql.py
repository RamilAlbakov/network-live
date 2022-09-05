"""Present sql commands for iot cells."""


class IotSqls(object):
    """Present sql commands for iot cells."""

    iot_delete_sql = 'TRUNCATE TABLE iotcells'

    iot_insert_sql = """
        INSERT
            INTO iotcells
        VALUES (
            :subnetwork,
            :site_name,
            :cell_name,
            :cellId,
            :administrativeState,
            :cellBarred,
            :freqBand,
            :earfcndl,
            :nbIotCellType,
            :ceLevelNumber,
            :cmcIndex,
            :dlAnchPrbIndex,
            :ulAnchPrbIndex,
            :maxRrcConnectedUsers,
            :physicalLayerCellId,
            :tac,
            :qRxLevMin,
            :cellRange,
            :eutranCellRef,
            :plmnReservedList,
            :oss,
            :vendor,
            :insert_date
        )
    """
