import pytest


@pytest.mark.asyncio
async def test_hello_world(async_client):
    """Test that the hello world handle works."""
    response = await async_client.get("/")
    assert response.is_success
    assert response.json() == {"message": "Hello World"}
