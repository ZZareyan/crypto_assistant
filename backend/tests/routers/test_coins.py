import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_list_coins_returns_200(client: AsyncClient) -> None:
    response = await client.get("/api/v1/coins/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_list_coins_response_shape(client: AsyncClient) -> None:
    response = await client.get("/api/v1/coins/?page=1&per_page=10")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "page" in data
    assert "per_page" in data
    assert "total" in data


@pytest.mark.asyncio
async def test_get_coin_unknown_id_returns_404(client: AsyncClient) -> None:
    response = await client.get("/api/v1/coins/this-coin-does-not-exist-xyz")
    assert response.status_code == 404
