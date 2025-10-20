"""
The file for the Tank Controller driver
"""

import threading

from tank_controller import mock_config
from tank_controller.gui import GUI
from tank_controller.tank_controller import TankController


def run():
    """
    The function that sets up threading for the Tank Controller and GUI
    """
    tank_controller = TankController()

    # Always run tank controller loop in a background thread
    thread = threading.Thread(
        target=tank_controller_loop_forever, args=(tank_controller,), daemon=True
    )
    thread.start()

    # Run GUI on main thread if mock mode is enabled
    if mock_config.MOCK_ENABLED:
        run_gui(tank_controller)


def run_gui(tank_controller):
    """
    The function that drives the Tank Controller's GUI
    """
    GUI(tank_controller)


def tank_controller_loop_forever(tank_controller):
    """
    The function that runs the Tank Controller loop forever
    """
    while True:
        tank_controller.loop()
