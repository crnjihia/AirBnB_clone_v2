#!/usr/bin/python3
"""Test cases for the AirBnb clone modules.
"""
import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    """Clears the content of a specified stream.

    Args:
        stream (TextIO): The stream to clear.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)


def delete_file(file_path: str):
    """Deletes a file if it exists.

    Args:
        file_path (str): The path of the file to delete.
    """
    if os.path.isfile(file_path):
        os.unlink(file_path)


def reset_store(store: FileStorage, file_path='file.json'):
    """Resets the items in the specified storage.

    Args:
        store (FileStorage): The FileStorage instance to reset.
        file_path (str): The path to the storage file.
    """
    with open(file_path, mode='w') as file:
        file.write('{}')
    if store is not None:
        store.reload()


def read_text_file(file_name):
    """Retrieves the contents of a specified file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


def write_text_file(file_name, text):
    """Writes text to a specified file.

    Args:
        file_name (str): The name of the file to write to.
        text (str): The content to write to the file.
    """
    with open(file_name, mode='w') as file:
        file.write(text)
