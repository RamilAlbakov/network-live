"""Connect to ENM and execute ENM CLI commands."""

import os

import enmscripting


def execute_cli_command(cli_command):
    """
    Execute ENM CLI commands.

    Args:
        cli_command: string

    Returns:
        enmscripting ElementGroup
    """
    session = enmscripting.open(os.getenv('ENM_SERVER')).with_credentials(
        enmscripting.UsernameAndPassword(
            os.getenv('ENM_LOGIN'),
            os.getenv('ENM_PASSWORD'),
        ),
    )
    enm_cmd = session.command()
    response = enm_cmd.execute(cli_command)
    enmscripting.close(session)
    return response.get_output()


def create_cli_command(mo_type, mo_parameters):
    """
    Create enm cli command.

    Args:
        mo_type: string
        mo_parameters: list

    Returns:
        string
    """
    return 'cmedit get * {mo_type}.({parameters})'.format(
        mo_type=mo_type,
        parameters=','.join(mo_parameters),
    )


def get_enm_ip_data():
    """
    Get ip data for every site from enm.

    Returns:
        dict
    """
    dus_ip_cli_command = 'cmedit get * Ip.(nodeIpAddress)'
    bbu_ip_cli_command = 'cmedit get * AddressIPv4.(address)'
    return {
        'enm_dus_ip_data': execute_cli_command(dus_ip_cli_command),
        'enm_bbu_ip_data': execute_cli_command(bbu_ip_cli_command),
    }
