#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is distributed under the following licence:

this project is licensed under 2-clause BSD

Copyright (c) 2013, Min Ragan-Kelley

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
__version__ = '0.3.0'

import sys
import platform
from distutils.version import LooseVersion as V

try:
    import CoreServices.LaunchServices
    import AppKit
    HAS_LS = True
except ImportError:
    HAS_LS = False


if (not HAS_LS
      or sys.platform != "darwin"
      or V(platform.mac_ver()[0]) < V("10.4")):
    from ._dummy import *
else:
    from ._ls import *

if HAS_LS:
    del CoreServices.LaunchServices, AppKit
del sys, platform, V