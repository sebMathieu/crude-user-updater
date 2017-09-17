
""" List of common filters. """
COMMON_FILTERS = ["\.DS_Store$", "\.git", "\.pyc$"]

""" Name of the file with the list of files to remove. """
TO_REMOVE_FILE = ".to_remove"

""" Name of the file with the list of regex pattern of files to ignore. """
IGNORE_LIST_FILE = ".to_ignore"

""" List of reserved files to ignore when updates are applied."""
RESERVED_FILES = [TO_REMOVE_FILE, IGNORE_LIST_FILE]
