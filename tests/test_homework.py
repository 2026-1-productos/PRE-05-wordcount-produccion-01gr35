"""Autograding script for student homework."""

import os


def test_word_count():
    """Test Word Count"""


for path in [
    "Dockerfile",
    ".Dockerignore",
]:
    if not os.path.exists(path):
        raise Exception(f"'{path}' directory does not exist")
