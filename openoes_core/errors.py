"""
OpenOES Error Handling Module

This module provides standardized error classes for the OpenOES SDK.
"""

import logging

# Configure logging
logger = logging.getLogger(__name__)


class OpenOESError(Exception):
    """Base exception class for all OpenOES errors."""
    
    def __init__(self, message: str, *args, **kwargs):
        self.message = message
        logger.error(f"{self.__class__.__name__}: {message}")
        super().__init__(message, *args, **kwargs)


class ConnectionError(OpenOESError):
    """Exception raised for Redis connection errors."""
    
    def __init__(self, message: str, host: str = None, port: int = None, *args, **kwargs):
        self.host = host
        self.port = port
        if host and port:
            message = f"{message} (host={host}, port={port})"
        super().__init__(message, *args, **kwargs)


class ACLError(OpenOESError):
    """Exception raised for Redis ACL errors."""
    
    def __init__(self, message: str, username: str = None, *args, **kwargs):
        self.username = username
        if username:
            message = f"{message} (username={username})"
        super().__init__(message, *args, **kwargs)


class StreamError(OpenOESError):
    """Exception raised for Redis Stream errors."""
    
    def __init__(self, message: str, stream_name: str = None, *args, **kwargs):
        self.stream_name = stream_name
        if stream_name:
            message = f"{message} (stream={stream_name})"
        super().__init__(message, *args, **kwargs)


class KeyError(OpenOESError):
    """Exception raised for Redis key errors."""
    
    def __init__(self, message: str, key: str = None, *args, **kwargs):
        self.key = key
        if key:
            message = f"{message} (key={key})"
        super().__init__(message, *args, **kwargs)


class ValidationError(OpenOESError):
    """Exception raised for validation errors."""
    
    def __init__(self, message: str, field: str = None, value: str = None, *args, **kwargs):
        self.field = field
        self.value = value
        if field and value:
            message = f"{message} (field={field}, value={value})"
        elif field:
            message = f"{message} (field={field})"
        super().__init__(message, *args, **kwargs)


class CreditRequestError(OpenOESError):
    """Exception raised for credit request errors."""
    
    def __init__(self, message: str, request_id: str = None, user_id: str = None, 
                 asset: str = None, *args, **kwargs):
        self.request_id = request_id
        self.user_id = user_id
        self.asset = asset
        
        details = []
        if request_id:
            details.append(f"request_id={request_id}")
        if user_id:
            details.append(f"user_id={user_id}")
        if asset:
            details.append(f"asset={asset}")
            
        if details:
            message = f"{message} ({', '.join(details)})"
            
        super().__init__(message, *args, **kwargs)


class SettlementError(OpenOESError):
    """Exception raised for settlement errors."""
    
    def __init__(self, message: str, settlement_id: str = None, user_id: str = None, 
                 *args, **kwargs):
        self.settlement_id = settlement_id
        self.user_id = user_id
        
        details = []
        if settlement_id:
            details.append(f"settlement_id={settlement_id}")
        if user_id:
            details.append(f"user_id={user_id}")
            
        if details:
            message = f"{message} ({', '.join(details)})"
            
        super().__init__(message, *args, **kwargs)


class ConfigurationError(OpenOESError):
    """Exception raised for configuration errors."""
    
    def __init__(self, message: str, parameter: str = None, *args, **kwargs):
        self.parameter = parameter
        if parameter:
            message = f"{message} (parameter={parameter})"
        super().__init__(message, *args, **kwargs)


class TimeoutError(OpenOESError):
    """Exception raised for timeout errors."""
    
    def __init__(self, message: str, operation: str = None, timeout: float = None, 
                 *args, **kwargs):
        self.operation = operation
        self.timeout = timeout
        
        details = []
        if operation:
            details.append(f"operation={operation}")
        if timeout:
            details.append(f"timeout={timeout}s")
            
        if details:
            message = f"{message} ({', '.join(details)})"
            
        super().__init__(message, *args, **kwargs)


def handle_redis_error(func):
    """
    Decorator to handle Redis errors and convert them to OpenOES errors.
    
    Args:
        func: The function to decorate
        
    Returns:
        Decorated function that handles Redis errors
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionError as e:
            # Already an OpenOES error, re-raise
            raise
        except ACLError as e:
            # Already an OpenOES error, re-raise
            raise
        except StreamError as e:
            # Already an OpenOES error, re-raise
            raise
        except KeyError as e:
            # Already an OpenOES error, re-raise
            raise
        except ValidationError as e:
            # Already an OpenOES error, re-raise
            raise
        except CreditRequestError as e:
            # Already an OpenOES error, re-raise
            raise
        except SettlementError as e:
            # Already an OpenOES error, re-raise
            raise
        except ConfigurationError as e:
            # Already an OpenOES error, re-raise
            raise
        except TimeoutError as e:
            # Already an OpenOES error, re-raise
            raise
        except OpenOESError as e:
            # Already an OpenOES error, re-raise
            raise
        except Exception as e:
            # Convert other exceptions to OpenOES errors
            logger.exception(f"Unhandled exception in {func.__name__}")
            raise OpenOESError(f"Unhandled exception: {str(e)}")
    
    return wrapper