# ../commands/__init__.py

"""Provides server, client, and say command functionality."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python Imports
#   Loggers
from loggers import _SPLogger


# =============================================================================
# >> FORWARD IMPORTS
# =============================================================================
# Source.Python Imports
#   Commands
from _commands import Command
from _commands import CommandReturn


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = ('Command',
           'CommandReturn',
           )


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Get the sp.commands logger
CommandsLogger = _SPLogger.commands
