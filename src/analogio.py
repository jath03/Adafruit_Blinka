"""
`analogio` - Analog input and output control
============================================
See `CircuitPython:analogio` in CircuitPython for more details.
Not supported by all boards.

* Author(s): Carter Nelson, Melissa LeBlanc-Williams
"""

from adafruit_blinka.agnostic import detector
import sys

# pylint: disable=ungrouped-imports,wrong-import-position,unused-import

if detector.board.microchip_mcp2221:
    from adafruit_blinka.microcontroller.mcp2221.analogio import AnalogIn
    from adafruit_blinka.microcontroller.mcp2221.analogio import AnalogOut
elif detector.board.greatfet_one:
    from adafruit_blinka.microcontroller.nxp_lpc4330.analogio import AnalogIn
    from adafruit_blinka.microcontroller.nxp_lpc4330.analogio import AnalogOut
elif detector.chip.RK3308:
    from adafruit_blinka.microcontroller.generic_linux.sysfs_analogin import AnalogIn
elif "sphinx" in sys.modules:
    pass
else:
    raise NotImplementedError("analogio not supported for this board.")
