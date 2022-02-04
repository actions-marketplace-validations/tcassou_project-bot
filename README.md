# Project Bot Github Actoin

This action automated the the addition of issues to a given Github Project.
It is compatible with [the recently revamped projects](https://docs.github.com/en/issues/trying-out-the-new-projects-experience/about-projects).

## Setup
This action uses the Github graphql under the hood, and will need to authenticate to get access to your projects.
For this, [create a Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and store it as a Github secret in the repository where your actions are going to run. In the example further down, we use a secret called `GITHUB_API_TOKEN`.

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
  GITHUB_API_TOKEN: ${{ secrets.GITHUB_API_TOKEN }}

jobs:
  add_to_project:
    runs-on: ubuntu-latest
    steps:
    - name: Assign new issues to the project
      uses: tcassou/project-bot@1.0.0
      with:
        project_url: 'https://github.com/orgs/foo/projects/123'
```
