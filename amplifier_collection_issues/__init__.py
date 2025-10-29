"""Amplifier Collection - Issues

Issue management collection with persistent queue and dependency tracking.
"""

__version__ = "0.1.0"


def get_collection_info():
    """Return collection metadata for Amplifier."""
    return {
        "name": "amplifier-collection-issues",
        "version": __version__,
        "description": "Issue management collection for Amplifier",
    }
