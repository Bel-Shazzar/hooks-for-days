# Hooks for days

Assortment of pre commit hooks.

## List of hooks

### copied-lines-at-file-end

Removes duplicate lines at the end of files, ignoring a single empty line.

This Issue can come from using vscode with both isort and the black formatter, I believe. This hook should prevent accidental commits.