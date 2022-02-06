import os

import pytest

from app.github_env import GithubEnv


@pytest.mark.parametrize(
    "event_name",
    [
        ("issue"),
        ("push"),
    ],
)
def test_get_event_name(event_name):
    os.environ["GITHUB_EVENT_NAME"] = event_name
    assert GithubEnv.get_event_name() == event_name


@pytest.mark.parametrize(
    "project_url",
    [
        ("abc"),
        ("https://github.com/orgs/foo/projects/123"),
    ],
)
def test_get_input(project_url):
    os.environ["INPUT_PROJECT_URL"] = project_url
    assert GithubEnv.get_input() == {"project_url": project_url}
