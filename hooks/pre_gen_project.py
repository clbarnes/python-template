import re
import sys
import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

module_re = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

if not re.fullmatch(module_re, "{{ cookiecutter.package_name }}"):
    logger.error("{{ cookiecutter.package_name }} is not a valid Python module name")

    # exits with status 1 to indicate failure
    sys.exit(1)

if "{{ cookiecutter.url }}":
    path_re = r".+\..+"

    result = urlparse("{{ cookiecutter.url }}")
    if not result.scheme.startswith("http") or not re.fullmatch(path_re, result.netloc):
        logger.error("{{ cookiecutter.url }} is not a valid HTTP(S) URL")
        sys.exit(1)
