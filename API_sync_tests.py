from typing import Generator
import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com/")
    # typing.Generator -> declare types of variables, parameters and return values of a function upfront.
    # Checks the code before compiling and running
    yield request_context
    # Discard all stored responses
    request_context.dispose()


def test_post_todo(api_request_context: APIRequestContext) -> None:
    json_data = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False,
    }
    response = api_request_context.post("/todos/1", data=json_data)
    # Check new response code
    assert response.ok

    todos_response = response.json()
    print("")
    print(f"todo Var: {response}")
    print(f"todo_response Var: {todos_response}")

