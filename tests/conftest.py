import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from good_advice_backend.app import get_app


@pytest.fixture
def app():
    """Yields a new instance of FastAPI app."""
    yield get_app()


@pytest_asyncio.fixture
async def async_client(app):
    """Client fixture to make HTTP requests against to our app."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://testserver",
    ) as async_client:
        yield async_client
