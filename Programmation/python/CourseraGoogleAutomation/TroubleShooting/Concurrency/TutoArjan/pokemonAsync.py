import asyncio
from random import randint
from req_http import http_get, http_get_sync
from typing import AsyncIterable
import time
# The highest Pokemon id 
MAX_POKEMON = 898

def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])

async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name



async def main() -> None:
    async for name in next_pokemon(20):
        print(name)
if __name__ == "__main__":
    startTime = time.time()
    asyncio.run(main())
    endTime = time.time() - startTime
    print("it's took : ", endTime, "seconds")