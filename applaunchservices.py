#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:47:20 2019

@author: quentinpeter
"""

import os
from LaunchServices import (LSCopyDefaultRoleHandlerForContentType,
                            LSSetDefaultRoleHandlerForContentType,
                            LSCopyDefaultHandlerForURLScheme,
                            LSSetDefaultHandlerForURLScheme,
                            kLSRolesNone,
                            kLSRolesViewer,
                            kLSRolesEditor,
                            kLSRolesShell,
                            kLSRolesAll)

from AppKit import NSRunningApplication


name = "applaunchservices"

kLSRoles = {
    'none': kLSRolesNone,
    'viewer': kLSRolesViewer,
    'editor': kLSRolesEditor,
    'shell': kLSRolesShell,
    'all': kLSRolesAll
    }


def get_bundle_identifier(pid=None):
    """
    Get bundle identifier for the given process identifier.

    if pid is None, the current process pid is used.
    """
    if pid is None:
        pid = os.getpid()
    app = NSRunningApplication.runningApplicationWithProcessIdentifier_(pid)
    if app is None:
        return
    return app.bundleIdentifier()


def set_UTI_handler(uniform_type_identifier, role, bundle_identifier):
    """Set handler for given uniform type identifier and role."""
    LSSetDefaultRoleHandlerForContentType(
        uniform_type_identifier, kLSRoles[role], bundle_identifier)


def get_UTI_handler(uniform_type_identifier, role):
    """Get handler for given uniform type identifier and role."""
    return LSCopyDefaultRoleHandlerForContentType(
        uniform_type_identifier, kLSRoles[role])


def set_URL_scheme_handler(url_scheme, bundle_identifier):
    """Set handler for given URL scheme."""
    LSSetDefaultHandlerForURLScheme(url_scheme, bundle_identifier)


def get_URL_scheme_handler(url_scheme):
    """Get handler for given URL scheme."""
    return LSCopyDefaultHandlerForURLScheme(url_scheme)
