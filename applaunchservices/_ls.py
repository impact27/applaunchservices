#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:15:45 2019

@author: quentinpeter
"""

import os
from CoreServices.LaunchServices import (LSCopyDefaultRoleHandlerForContentType,
                            LSSetDefaultRoleHandlerForContentType,
                            LSCopyDefaultHandlerForURLScheme,
                            LSSetDefaultHandlerForURLScheme,
                            LSOpenCFURLRef,
                            kLSRolesNone,
                            kLSRolesViewer,
                            kLSRolesEditor,
                            kLSRolesShell,
                            kLSRolesAll)

from AppKit import NSRunningApplication, NSBundle, NSURL


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


def get_bundle_identifier_for_path(path):
    """
    Get bundle identifier for the given path.
    """
    bundle_url = 'file://' + os.path.abspath(path)
    return NSBundle.bundleWithURL_(
        NSURL.URLWithString_(bundle_url)).bundleIdentifier()


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


def open_URL(url):
    """Open the url with launchservices."""
    URL = NSURL.URLWithString_(url)
    LSOpenCFURLRef(URL, None)


def open_path(path):
    """Open the path with launchservices."""
    open_URL('file://' + os.path.abspath(path))
