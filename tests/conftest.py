import os

import pytest

from app.github_api import GithubAPI


ENVIRONMENT = {
    "GITHUB_GRAPHQL_URL": "https://api.foo.com/graphql",
    "GITHUB_API_TOKEN": "secret_token_nobody_should_ever_see",
    "GITHUB_EVENT_NAME": "issues",
    "GITHUB_EVENT_PATH": "/github/workflow/event.json",
    "INPUT_PROJECT_URL": "https://github.com/orgs/foo/projects/123",
}


@pytest.fixture(scope="function", autouse=True)
def _set_up(request):
    print(f"ENV set to `{os.environ['ENV']}`.\n")
    os.environ.update(ENVIRONMENT)

    def _tear_down():
        GithubAPI.URL = None
        GithubAPI.TOKEN = None

    request.addfinalizer(_tear_down)
