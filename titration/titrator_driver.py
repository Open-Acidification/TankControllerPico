"""
The file for the Alkalinity Titrator driver
"""

import threading

from titration import mock_config
from titration.gui import GUI
from titration.titrator import Titrator


def run():
    """
    The function that sets up threading for the Titrator and GUI
    """
    titrator = Titrator()

    # Always run titrator loop in a background thread
    thread = threading.Thread(
        target=titrator_loop_forever, args=(titrator,), daemon=True
    )
    thread.start()

    # Run GUI on main thread if mock mode is enabled
    if mock_config.MOCK_ENABLED:
        run_gui(titrator)


def run_gui(titrator):
    """
    The function that drives the Alkalinity Titrator's GUI
    """
    GUI(titrator)


def titrator_loop_forever(titrator):
    """
    The function that runs the Titrator loop forever
    """
    while True:
        titrator.loop()
