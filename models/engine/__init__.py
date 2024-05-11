#!/usr/bin/python3
# creation of a unique FileStorage instance and call reload()

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()
# Call reload() method to load data from JSON file
storage.reload()
