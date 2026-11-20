# Tests for the example package; each test names the requirement it covers.

import pytest

from example import greet


def test_greets_name() -> None:
    """REQ-001: a non-blank name gets a greeting, trimmed."""
    assert greet("  Ada ") == "Hello, Ada!"


@pytest.mark.parametrize("blank", ["", "   ", "\t\n"])
def test_rejects_blank_name(blank: str) -> None:
    """REQ-002: a blank name is rejected."""
    with pytest.raises(ValueError, match="blank"):
        greet(blank)
