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
