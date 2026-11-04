# Missing plugin folder

## Sub-features

Run main.py without a plugins directory. It reports the missing folder, reports no plugins loaded and finishes with exit0.

## How to get to it (user POV)

Use a terminal in the app root and run `python3 main.py`.

## Driving it with Python child processes

Run `python3 .cursor/skills/verify-plugins/helpers/drive.py`. It checks actual CLI text/status in an isolated source copy, records evidence, then removes scratch state.

## Gotchas

The harness renames only the copied scratch plugins directory. Never rename or delete original user content for this test.
