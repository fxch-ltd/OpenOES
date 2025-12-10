"""
OpenOES Community Edition SDK - Testing Module

This module provides tools for testing integrations with the OpenOES
Community Edition system, including mock Valkey/Redis clients, data generators,
test scenarios, and response validators using Valkey/Redis-compatible backends.
"""

__version__ = '0.1.0'

# Import components for easier access
from .mock_redis import MockRedisClient
from .generators import (
    DataGenerator,
    CreditRequestGenerator,
    SettlementGenerator,
    EventGenerator,
    AccountGenerator
)
from .scenarios import (
    TestScenario,
    CreditRequestScenario,
    SettlementScenario,
    EventHandlingScenario,
    IntegrationScenario
)
from .validators import (
    Validator,
    CreditRequestValidator,
    SettlementValidator,
    EventValidator,
    AccountValidator
)