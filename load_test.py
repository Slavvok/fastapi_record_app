import asyncio
import time

import aiohttp


async def test_get_record():
    async with aiohttp.ClientSession() as session:

        url = 'http://127.0.0.1:8080/records/2'
        async with session.get(url) as resp:
            response = await resp.json()
            # print(response)


async def test_get_record_list():
    async with aiohttp.ClientSession() as session:

        url = 'http://127.0.0.1:8080/records/?f=1&l=5'
        async with session.get(url) as resp:
            response = await resp.json()
            # print(response)


async def test_add_record():
    async with aiohttp.ClientSession() as session:

        url = 'http://127.0.0.1:8080/records/?data=aegaweg'
        async with session.post(url) as resp:
            response = await resp.json()
            # print(response)


async def main():
    start = time.time()
    print("Testing get record")
    await asyncio.gather(*[test_get_record() for _ in range(1000)])
    print("Testing get record list")
    await asyncio.gather(*[test_get_record_list() for _ in range(1000)])
    print("Testing add record")
    await asyncio.gather(*[test_add_record() for _ in range(1000)])
    print(time.time() - start)


if __name__ == '__main__':
    asyncio.run(main())
