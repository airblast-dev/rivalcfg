"""
This module generates rivalcfg's CLI.
"""


import sys
import types
import argparse

from . import handlers
from . import devices
from .version import VERSION


def normalize_cli_option_name(name):
    """Helper function to transform a setting name to a cli option.

    :param str name: The setting name.
    :rtype: str

    >>> normalize_cli_option_name("My_Test_Setting1")
    'my-test-setting1'
    """
    return name.lower().replace("_", "-")


class PrintSupportedDevicesAction(argparse.Action):
    """Print supported devices and exit."""

    def __call__(self, parser, namespace, value, option_string=None):
        for item in [getattr(devices, name) for name in dir(devices)]:
            if not isinstance(item, types.ModuleType):
                continue
            if not hasattr(item, "profile"):
                continue
            print("%s:" % item.profile["name"])
            print()
            for model in item.profile["models"]:
                print("  %04x:%04x | %s" % (
                    model["vendor_id"],
                    model["product_id"],
                    model["name"]))
            print()
        sys.exit(0)


def add_main_cli(cli_parser):
    """Adds the main CLI options.

    :param ArgumentParser cli_parser: An :class:`ArgumentParser` instance.
    """
    cli_parser.add_argument(
            "--no-save",
            help="Do not persist settings in the internal device memory",
            dest="SAVE",
            action="store_false",
            default=True)

    cli_parser.add_argument(
            "--list",
            help="List supported devices and exit",
            nargs=0,
            action=PrintSupportedDevicesAction)

    cli_parser.add_argument(
            "--version",
            action="version",
            version=VERSION)

    # TODO --print-info
    pass


def add_mouse_cli(cli_parser, mouse_profile):
    """Adds the CLI options for the given mouse profile.

    :param ArgumentParser cli_parser: An :class:`ArgumentParser` instance.
    :param mouse_profile: One of the rivalcfg mouse profile (provided by
                            :func:`rivalcfg.devices.get_profile`).
    """
    cli_group = cli_parser.add_argument_group(
            "%s Options" % mouse_profile["name"])

    for setting_name, setting_info in mouse_profile["settings"].items():
        handler = getattr(handlers, setting_info["value_type"])
        handler.add_cli_option(cli_group, setting_name, setting_info)
