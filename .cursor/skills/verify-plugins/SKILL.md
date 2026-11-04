---
name: verify-plugins
description: Verify ChatClientCpp's actual Python plugin-loader CLI after loader, interface or example-plugin changes.
---
# Verify plugin CLI

## Launch

Despite the repository name, the current app is Python main.py with AppPlugin and two example plugins. Requires Python3 only. From root run `python3 .cursor/skills/verify-plugins/helpers/drive.py`. It copies source/plugins/tests, excluding bytecode, into its own temporary working directory. No C++ build, server, ports, external account, migrations or network.

## Doctor

The helper parses all copied Python sources with ast without importing/executing them first. It then starts the real copied main.py. Readiness means it discovers two actual plugins and reaches execution, not merely successful import.

## Drive

Normal journey: real CLI discovers PluginOne and PluginTwo, invokes their actual execute methods, prints each greeting and finishes with exit0/no stderr. Failure-state journey: remove the copied plugins directory, invoke main.py again, verify the missing-folder message and no-loaded-plugins result without crashing. Finally run the existing unittest suite in the isolated copy; this suite uses mocks and is reported separately, not as real-plugin proof. Read features/README.md.

## Evidence

`artifacts/verification/plugins.json` records source hashes, doctor, actual CLI stdout/stderr/exit, missing-folder result and existing unit-test output. Real CLI paths are not mocked. This proves shipped example-plugin execution and graceful absence; arbitrary third-party plugins, malicious-plugin containment and dependency compatibility are not certified.

## Cleanup

Each child has a15second timeout. Proof is written before the helper removes only its own scratch tree. Existing tests' temporary plugin is checked gone. Evidence survives and is checked. No original source/data is deleted.

## Helpers

`python3 .cursor/skills/verify-plugins/helpers/drive.py` is the full verification command. Run after loader/plugin changes; use `/maintain-verification-skill` to map new behaviors rather than counting existing source-only tests as execution.
