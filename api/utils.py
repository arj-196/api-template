import os

import toml

_current_dir = os.path.dirname(os.path.realpath(__file__))


def get_version():
    # get build version
    version = os.environ.get("BUILD_VERSION")
    if version:
        return version

    pyproject = toml.load(os.path.join(_current_dir, "../", "pyproject.toml"))
    return pyproject.get("tool", {}).get("poetry", {}).get("version", "0.0.0")
