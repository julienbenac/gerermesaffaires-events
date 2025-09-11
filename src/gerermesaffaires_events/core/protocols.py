from typing import Protocol


class EventEmitterProtocol(Protocol):
    """Protocol defining the interface for event emission.

    This protocol establishes the contract for objects that can emit events,
    ensuring compatibility with different event emitter implementations.
    """

    def emit(self, event: str, *args: object, **kwargs: object) -> bool:
        """Emit an event with the given name and arguments."""


class ServerProtocol(Protocol):
    """Protocols defining the interface for the server.

    This protocol establishes the contract for server implementations,
    ensuring they provide the necessary application interface for
    ASGI compatibility and deployment.
    """

    @property
    def app(self) -> "ServerProtocol":
        """Return the server application instance."""
