"""
This module provides functions to work with csv files.
"""

import subprocess
import os
import codecs
import warnings
import os


def day_is_already_written(todays_date, filepath):
    warnings.warn(
        "WARNING: This function is deprecated, use the "
        "function is_date_in_last_line instead!"
    )
    return is_date_in_last_line(todays_date, filepath)


def is_date_in_last_line(todays_date, filepath):
    """
    Checks if the specified date is already written in the last line
    of a csv file.

    :param todays_date: Date as string like "2018-01-01"
    :param filepath: Filename to check
    :return: True if Date is present in the last line of the file
    """
    line = subprocess.check_output(["tail", "-1", filepath])
    last_line = line.decode("utf-8")

    return todays_date in last_line


def delete_last_line(filepath):
    """
    Deletes the last line of the specified file.
    If the file has only one line, it is left.
    :param filepath: Filename to delete the last line from
    :return: None
    """
    with open(filepath, "r+", encoding="utf-8") as filehandle:
        # Move the pointer (similar to a cursor in a text editor) to the end of the file
        filehandle.seek(0, os.SEEK_END)
        # This code means the following code skips the very last character in the file -
        # i.e. in the case the last line is null we delete the last line
        # and the penultimate one
        pos = filehandle.tell() - 1
        # Read each character in the file one at a time from the penultimate
        # character going backwards, searching for a newline character
        # If we find a new line, exit the search
        while pos > 0 and filehandle.read(1) != "\n":
            pos -= 1
            filehandle.seek(pos, os.SEEK_SET)
        # So long as we're not at the start of the file, delete all the characters ahead
        # of this position
        if pos > 0:
            filehandle.seek(pos, os.SEEK_SET)
            filehandle.truncate()


def create_headers(filepath, header_row):
    """
    Creates a csv header row if the specified file is empty
    or doesn't exist.

    :param filepath: The filepath
    :param header_row: String for the header row
    :return True if file was empty and header is written

    Example usage:

    >>> create_headers("data.csv", "date,time,temperature,humidity")
    """
    with open(filepath, "a") as filehandle:
        # Check if file is empty and write row
        if os.stat(filepath).st_size == 0:
            filehandle.write(header_row + "\n")
            return True
        return False


def count_lines(filepath):
    """
    Counts the number of lines of a given file.

    :param file: The filepath
    :return: Number of lines contained in the file.
    """
    with codecs.open(filepath, encoding="utf-8", errors="ignore") as filehandle:
        if os.stat(filepath).st_size == 0:
            return 0
        else:
            return len(filehandle.read().splitlines())


def delete_file(filepath):
    """
    Deletes the specified file if the file exists.

    :param filepath: Path of the file to be deleted
    :return: True if the file was deleted, else False
    """
    if os.path.isfile(filepath):
        os.remove(filepath)
        return True
    else:
        print("Error: %s file not found" % filepath)
        return False
