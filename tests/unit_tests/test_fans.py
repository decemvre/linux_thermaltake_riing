"""
linux_thermaltake_rgb
Software to control your thermaltake hardware
Copyright (C) 2018  Max Chesterfield (chestm007@hotmail.com)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
import unittest

from mock import patch

from linux_thermaltake_rgb.fan_manager import FanModel, TempTargetModel, CurveModel

TempTargetModel._get_temp = (lambda self: 50)
CurveModel._get_temp = (lambda self: 50)


class FanTest(unittest.TestCase):

    @patch('linux_thermaltake_rgb.drivers.ThermaltakeControllerDriver._initialize_device', autospec=True)
    def test_fan_factory(self, init_dev):

        for clazz in FanModel.inheritors():
            if clazz.model is None:
                continue

            fan = FanModel.factory({'model': clazz.model,
                                    'points': [[50, 50]],  # curve
                                    'speed': 50,  # locked_speed
                                    'target': 50,  # temp_target
                                    'multiplier': 10
                                    })
            fan.main()
            self.assertIsInstance(fan, FanModel)
