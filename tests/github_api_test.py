import os

from app.github_api import GithubAPI
from app.github_api import GithubEntities


def test_entities():
    assert len(GithubEntities) == 2
    assert GithubEntities.orgs.value == "organization"
    assert GithubEntities.users.value == "user"


def test_set_up():
    assert GithubAPI.URL is None
    assert GithubAPI.TOKEN is None
    os.environ["GITHUB_GRAPHQL_URL"] = "https://foo.bar"
    os.environ["GITHUB_API_TOKEN"] = "top_secret"
    GithubAPI._set_up()
    assert GithubAPI.URL == "https://foo.bar"
    assert GithubAPI.TOKEN == "top_secret"
