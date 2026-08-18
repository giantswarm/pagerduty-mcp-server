# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project's packages adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

This changelog covers the Giant Swarm fork only. For upstream changes,
see [`PagerDuty/pagerduty-mcp-server`](https://github.com/PagerDuty/pagerduty-mcp-server).

## [Unreleased]

### Added

* `unit-tests` CircleCI job running `pytest` on every branch and tag. Nothing in CI ran the Python test suite before.
* `tests/test_entrypoint.py`, importing `pagerduty_mcp.server` and `pagerduty_mcp.__main__` so a moved dependency API fails the test suite instead of the container.

### Fixed

* `mcp[cli]` pinned to `~=1.29`. Under `mcp` 2.0 the server crashed on startup with `ModuleNotFoundError: No module named 'mcp.server.fastmcp'`, affecting releases v1.0.23 through v1.0.29.
* Team ownership: team ownership aligned to the canonical `io.giantswarm.application.team: atlas` annotation (was key `application.giantswarm.io/team`, value `team-honeybadger`).

## [1.0.0] - 2026-06-05

### Added

- HTTP / SSE / streamable-http transport support via new `--transport`,
  `--host`, `--port` CLI flags on `pagerduty-mcp run`. Enables in-cluster
  deployment behind the muster MCP gateway.
- Giant Swarm Helm chart `mcp-pagerduty` (read-only by default, opt-in
  `enableWriteTools` flag, optional Cilium NetworkPolicy).
- CircleCI release pipeline (`architect/push-to-registries` +
  `architect/push-to-app-catalog`) publishing image and chart to the public
  `gsoci.azurecr.io` registry.
- `CHANGELOG.md` (this file).

[Unreleased]: https://github.com/giantswarm/pagerduty-mcp-server/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/giantswarm/pagerduty-mcp-server/releases/tag/v1.0.0
