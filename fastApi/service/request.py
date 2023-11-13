import httpx


# Static method
async def fetch(full_url: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(full_url)
        return response.json()
    except:
        print(f"Error during fetching url {full_url}")


class Requests:
    base_url: str = "https://pokeapi.co/api/v2/"

    async def pokemon_details(self, id: int):
        full_url: str = f"{self.base_url}pokemon/{id}"
        return await fetch(full_url)

    async def ability_details(self, full_url: str):
        return await fetch(full_url)


request = Requests()
