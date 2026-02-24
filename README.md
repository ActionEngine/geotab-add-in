# FAQ

## Setting up vscode

Q: How do i configure vscode to use different python interpreters (virtual environments) for different sub-folders?

A:
There is `projects.code-workspace` at the root of this repository. It is structured like this
```json
{
  "folders": [
    {"name": "REPO ROOT", "path": "."},
    {"name": "subproject-A", "path": "path-A"},
    {"name": "subproject-B", "path": "path-B"}
  ],
  "settings": {
    // those are comon for the whole repository
  }
}
```

Add your subproject there.

After that, in your subroject folder, create `.vscode/settings.json` file, and set up path to the python interpreter you need:
```json
{"python.defaultInterpreterPath": "./.venv/bin/python"}
```

Note that path is relative to the root of sub-project, not to the root of git repository. For `subproject-A` from example above, path will be relative to `path-A`.

To avoid your subproject appearing twice in side-panel, you add it to `settings.files.exclue` in `projects.code-workspace` file:
```json
{
  "folders": [
    {"name": "REPO ROOT", "path": "."},
    {"name": "subproject-A", "path": "path-A"},
    {"name": "subproject-B", "path": "path-B"}
  ],
  "settings": {
    "files.exclude": {
      "path-A": true,
      "path-B": true
    }
  }
}
```

After that, select `File -> Open Workspace from file` and choose `projects.code-workspace` file you just edited
