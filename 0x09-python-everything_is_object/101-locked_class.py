#!/usr/bin/python3
"""Defines a class which is locked"""


class LockedClass:
    """
    Prevent making new attribute for my LockedClass class
    """
    __slots__ = ["first_name"]
