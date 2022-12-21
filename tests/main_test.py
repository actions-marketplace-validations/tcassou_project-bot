import os

import pytest
from expectise import Expect
from expectise import Expectations

from .helpers import github_event
from app.main import run


def test_run():
    with Expectations():
        Expect("GithubEnv").to_receive("get_event").and_return(github_event(issue_number=1, issue_id="rejgk"))
        response = {"data": {"organization": {"projectV2": {"id": "abc"}}}}
        Expect("GithubAPI").to_receive("_post").and_return(response)  # 1st _post in `get_project_id`
        Expect("GithubAPI").to_receive("_post").and_return(None)  # 2nd _post in `add_issue_to_project`
        run()


def test_unsupported_event():
    os.environ["GITHUB_EVENT_NAME"] = "push"
    with pytest.raises(NotImplementedError):
        run()


def test_invalid_project_url():
    os.environ["INPUT_PROJECT_URL"] = "https://github.com/projects/12"
    with Expectations():
        Expect("GithubEnv").to_receive("get_event").and_return(github_event(issue_number=1, issue_id="rejgk"))
        with pytest.raises(ValueError):
            run()
