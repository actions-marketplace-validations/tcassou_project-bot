#!/usr/bin/env python3
import logging

from .github_api import GithubAPI
from .github_env import GithubEnv

logging.getLogger().setLevel(logging.INFO)


def run() -> None:
    """Run the Github action."""
    event_name = GithubEnv.get_event_name()
    if event_name != "issue":
        raise NotImplementedError("This Github Action only supports `issue` events!")

    logging.info("Reading Github webhook event from local files...")
    event = GithubEnv.get_event()
    logging.info("Reading Github action input from environment...")
    input = GithubEnv.get_input()
    logging.info("Getting Github Project ID based on URL...")
    project_id = GithubAPI.get_project_id(input["project_url"])
    logging.info("Adding issue to Project board...")
    GithubAPI.add_issue_to_project(event["issue"]["node_id"], project_id)
    logging.info("Done, exiting.")


if __name__ == "__main__":
    run()
