#!/usr/bin/python3
"""Create new ``models`` package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
