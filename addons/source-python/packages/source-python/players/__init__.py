# ../players/__init__.py

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python Imports
from _players import *
from loggers import _SPLogger


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
# Set all to an empty list
__all__ = [
    'PlayerInfo',
    'NetChannelInfo',
    'PlayerGenerator'
]


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Get the sp.players logger
PlayersLogger = _SPLogger.players
