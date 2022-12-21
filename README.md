# Issues to Project Github Action
[![Lint and Test](https://github.com/tcassou/project-bot/actions/workflows/lint_test.yaml/badge.svg)](https://github.com/tcassou/project-bot/actions)

This Github Action automated the the addition of issues to a given Github Project.
It uses the Github GraphQL API under the hood, and is compatible with [the recently revamped projects](https://docs.github.com/en/issues/trying-out-the-new-projects-experience/about-projects).

## Setup
This action will need to authenticate to get access to your repositories and projects via the Github API.
For this, [create a Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and store it as a Github secret in the repository where your actions are going to run.
The script expects a `GITHUB_API_TOKEN` environment variable containing your token, regardless of the name you choose for your secret (see example below).

## Inputs

### `project_url`
**Required** URL of the Github project that issues should be added to.
Examples:
* For an organization project, https://github.com/orgs/foo/projects/123"
* For a user project, https://github.com/users/bar/projects/456"

## Example usage
In your workflow file under `./.github/workflows`:
```yaml
name: Add Issues to Project

on:
  issues:
    types: [opened]
env:
  GITHUB_API_TOKEN: ${{ secrets.MY_API_TOKEN }}

jobs:
  add_to_project:
    runs-on: ubuntu-latest
    steps:
    - name: Assign new issues to the project
      uses: tcassou/project-bot@2.0.0
      with:
        project_url: 'https://github.com/orgs/foo/projects/123'
```
