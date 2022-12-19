# Welcome to the contribution section

Thank you for investing your time in contributing to our project!

Read our [Code of Conduct](./CODE_OF_CONDUCT.md) to keep our community approachable and respectable.

## Standard

Code contributions will only be accepted under the following conditions:

- code is formatted with [autopep8](https://pypi.org/project/autopep8/) using the defined [configuration](/backend/pyproject.toml)

```json
    "python.formatting.autopep8Path": "backend/venv/bin/autopep8",
    "python.formatting.provider": "autopep8",
```

- documented code with [doctstring generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

```python

class AnalyticsDashboardQuery(ObjectType):
    """_summary_

    Args:
       ObjectType (_type_): _description_
    """
```

- on save settings as such

```json
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": true,
      "source.organizeImports": true,
      "source.sortMembers": true
    },
```

You can use the settings defined in [.vscode/settings.json](/.vscode/settings.json) and install extensions using the [@recommended](/.vscode/extensions.json) tag.

## Workflow

Please use the [fork workflow](https://docs.github.com/en/get-started/quickstart/fork-a-repo) for contributions.

TL;DR

1. fork project
2. create branch with issue number and name: `#12 Example Issue -> 12_example_issue`
3. make changes
4. draft pull request
5. pass tests

### Issues

#### Create a new issue

If you spot a problem using the app, [search if an issue already exists](https://github.com/quantumfate/moneyjar/issues). If a related issue doesn't exist, you can open a new issue using a relevant [issue form](https://github.com/quantumfate/moneyjar/issues/new/choose).

#### Solve an issue

Scan through our [existing issues](https://github.com/quantumfate/moneyjar/issues) to find one that interests you. You can narrow down the search using `labels` as filters. As a general rule, we don’t assign issues to anyone. If you find an issue to work on, you are welcome to open a PR with a fix.
