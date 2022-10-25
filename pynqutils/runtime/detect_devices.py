# Copyright (C) 2022 Xilinx, Inc
# SPDX-License-Identifier: BSD-3-Clause

#import pynq

from ..setup_utils import get_board

def detect_devices(active_only=False):
    """Return a list containing all the detected devices names."""
    dev_list = []
    dev_list.append(get_board())
    return dev_list
    #devices = pynq.Device.devices
    #if not devices:
    #    raise RuntimeError("No device found in the system")
    #if active_only:
    #    return pynq.Device.active_device.name
    #return [d.name for d in devices]
