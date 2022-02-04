import requests
import re
import os
import json


ENTITIES = {
    "orgs": "organization",
    "users": "user",
}


def run_query(query):
    response = requests.post(
        os.environ["GITHUB_GRAPHQL_URL"],
        json={"query": query},
        headers={"Authorization": "token " + os.environ["GITHUB_API_TOKEN"]},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":

    print(os.environ["GITHUB_EVENT_PATH"])
    with open(os.environ["GITHUB_EVENT_PATH"], "rb") as event_file:
        event = json.loads(event_file)

    project_url = os.environ["INPUT_PROJECT_URL"]
    pattern = r"^https:\/\/github.com\/(orgs|users)\/(.+)\/projects\/([0-9]+)"
    entity_path, entity_name, project_number = re.search(pattern, project_url).groups()
    entity_type = ENTITIES[entity_path]

    # Getting the project ID from the owner type, owner name and project number
    project_query = f"""
        {{
            {entity_type}(login: "{entity_name}") {{
                projectNext(number: {project_number}) {{
                    id
                }}
            }}
        }}
    """
    project_id = run_query(project_query)["data"][entity_type]["projectNext"]["id"]
    print(project_id)

    # Getting the issue ID from repository name, owner and issue number
    # issue_query = f"""
    #     {{
    #         repository(name: "{event['repository']['name']}", owner: "{event['repository']['owner']['login']}") {{
    #             issue(number: {event['issue']['number']}) {{
    #                 id
    #             }}
    #         }}
    #     }}
    # """
    # issue_id = run_query(issue_query)["data"]["repository"]["issue"]["id"]
    # print(issue_id)

    attach_query = f"""
        mutation {{
            addProjectNextItem(input: {{projectId: "{project_id}" contentId: "{event['issue']['node_id']}"}}) {{
                projectNextItem {{
                    id
                }}
            }}
        }}
    """
    print(run_query(attach_query))