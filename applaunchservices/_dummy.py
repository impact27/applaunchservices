#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:16:20 2019

@author: quentinpeter
"""

name = "applaunchservices"

kLSRoles = {
    'none': 0,
    'viewer': 1,
    'editor': 2,
    'shell': 3,
    'all': 4
    }


def get_bundle_identifier(pid=None):
    """
    Get bundle identifier for the given process identifier.

    if pid is None, the current process pid is used.
    """
    return


def get_bundle_identifier_for_path(path):
    """
    Get bundle identifier for the given path.
    """
    return


def set_UTI_handler(uniform_type_identifier, role, bundle_identifier):
    """Set handler for given uniform type identifier and role."""
    return


def get_UTI_handler(uniform_type_identifier, role):
    """Get handler for given uniform type identifier and role."""
    return


def set_URL_scheme_handler(url_scheme, bundle_identifier):
    """Set handler for given URL scheme."""
    return


def get_URL_scheme_handler(url_scheme):
    """Get handler for given URL scheme."""
    return
