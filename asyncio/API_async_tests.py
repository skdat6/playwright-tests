import asyncio, logging, pytest
from playwright.async_api import async_playwright, Playwright

@pytest.mark.asyncio
async def test():
    async with async_playwright() as playwright:
        logging.basicConfig(level=logging.DEBUG)
        api_request_context = await playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
        data = {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False,
        }

        response = await api_request_context.post("/todos", data=data)

        assert response.ok
        print(f"toDo var: {response}")


async def main():
    await asyncio.gather(test())
    asyncio.run(main())
        # await run(playwright)

