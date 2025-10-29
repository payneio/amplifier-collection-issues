"""
Amplifier Collection: Issue Management Integration

Provides Beads issue tracking integration for Amplifier sessions.
Enables AI agents to work with structured task management.
"""

__version__ = "0.1.0"

COLLECTION_METADATA = {
    "name": "issue-management",
    "version": __version__,
    "description": "Beads issue tracking integration for task-aware AI workflows",
    "provides": ["profiles", "context"],
    "dependencies": [],
}


def get_collection_info():
    """Return collection metadata."""
    return COLLECTION_METADATA
