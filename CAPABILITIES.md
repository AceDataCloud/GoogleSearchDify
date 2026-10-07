# Google Search capability mapping

Compared with [MCPs at f0eed10abf31](https://github.com/AceDataCloud/MCPs/tree/f0eed10abf310824cb4c33d4944c63d3654ac95b/serp) and the public API contract at PlatformBackend `fa94598267a82545fb1afed6ee26bafd6cbb9ca7`.

The table maps service operations to Dify tools. Different MCP helper functions may use the same action selector or structured JSON input.

| MCP function | Dify equivalent | Notes |
|---|---|---|
| `serp_google_search` | `serp_google` | Select the corresponding type; time_range maps to range. |
| `serp_google_images` | `serp_google` | Select the corresponding type; time_range maps to range. |
| `serp_google_news` | `serp_google` | Select the corresponding type; time_range maps to range. |
| `serp_google_videos` | `serp_google` | Select the corresponding type; time_range maps to range. |
| `serp_google_places` | `serp_google` | Select the corresponding type; time_range maps to range. |
| `serp_google_maps` | `serp_google` | Select the corresponding type; time_range maps to range. |
| `serp_list_search_types` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `serp_list_countries` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `serp_list_languages` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `serp_list_time_ranges` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `serp_get_usage_guide` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |

## Parameter equivalents

- `serp_google_search`: `search_type` → type, `time_range` → range.
- `serp_google_news`: `time_range` → range.

## Verification boundary

Contract examples and regression tests cover request validation, transport and task handling. Actual Dify browser cases are recorded separately in `tests/e2e-results.json` and `tests/e2e-audit.json` when available. A schema test is not a successful paid generation. Unsupported service availability and untested advanced combinations must not be described as passed.
