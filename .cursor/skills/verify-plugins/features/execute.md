# Discover and execute

## Sub-features

Run main.py with its plugins directory present. Both concrete classes are discovered, their actual execute methods print their distinct greeting, then the app finishes.

## How to get to it (user POV)

Use a terminal in the app root and run `python3 main.py`.

## Driving it with Python child processes

Run `python3 .cursor/skills/verify-plugins/helpers/drive.py`. It checks actual CLI text/status in an isolated source copy, records evidence, then removes scratch state.

## Gotchas

Discovery order follows filesystem enumeration; assert both messages, not order. Unknown third-party plugins may have effects and are not covered.
