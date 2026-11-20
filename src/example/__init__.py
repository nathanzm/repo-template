# Example package: a placeholder that shows the layout and keeps CI green.
# Replace it with the real package (rename src/example and pyproject's name).

import logging

log = logging.getLogger(__name__)


def greet(name: str) -> str:
    """Return a greeting for a non-blank name; raise ValueError otherwise."""
    if not name.strip():
        log.warning("Rejected blank name")
        raise ValueError("name must not be blank")
    return f"Hello, {name.strip()}!"
