# Validation of the simplified Focalyst revision

The latest executable results are stored in test-results.json. The app was reviewed and tested in a browser; no human usability study is claimed.

## Interface requirements
- Only Live, History and System navigation.
- One native situation picker on Live, beside continuous signals and Start/Stop.
- Simulated implant and wireless-patch connections, with visible linked/offline states.
- No battery/power gauges, 3D model, external links, research screen or calibration wizard.
- Continuous coherent traces while connected, including while Work Mode is off.
- Automatic permission decisions while Work Mode is on; no separate Send/Evaluate action.
- History, explicit CSV export, session reset, connection management and local-data erasure.

## Executed checks
- 12 engine test groups: deterministic signals, feature-based calibration/classification, both profiles, uncertainty/quality, all 17 research fixtures, physical/permission gates, repeated events/lockout, long sessions, thresholds, outcomes, confusion metrics and invalid configuration.
- 5 stream test groups: deterministic continuity across chunk sizes, calibration agreement with live windows, noisy-data rejection/recovery, individual baseline centering, balanced-accuracy denominators.
- Browser workflow: exactly three tabs and no links; connect; resting stream visibly changes; difficulty autorizes one event; repeated monitoring preserves that count; working and paused-task behavior; noisy-signal block; Stop from another tab; connection loss/recovery; CSV; history deletion; session reset; reload; all tabs at 320/390/768 pixels.
- Browser edge cases: session cap; daily count retained after reset; task-action evidence in the getting-ready scenario; rapid Start/Stop; all-data deletion; offline use; App Inventor CSV bridge stub; local-midnight reset; 200% zoom.

Initial enlarged-text testing found horizontal overflow in the header and navigation. Container-responsive sizing corrected it, and the test passed on rerun. The native Playwright video recorder was unavailable; the supplied 16-second MP4 uses screenshots of the actual browser app at four frames per simulated second with a controlled clock.

## Packaging checks
The App Inventor asset must match Focalyst.html byte-for-byte. The AIA ZIP's integrity, project entries, and local WebViewer asset path are checked when delivering. The source ZIP includes current source, tests, packaging script and documentation. Prior screenshots/review scripts remain archived separately and do not describe the new interface.

## Scope of evidence
The browser checks verify software behavior and visible state transitions. Synthetic examples do not establish ADHD detection accuracy or clinical effects. Full scientific sources were not independently reviewed during this revision; methodology references come from the supplied refinement package.

MIT App Inventor import, APK compilation, physical Android execution, native CSV file saving and real screen-reader use remain unverified. The CSV bridge check uses a JavaScript stub. CSS zoom does not establish all Android OS text-scaling behavior. There is no real implant, patch or neural-data connection.

## Reproduce
Start a local server from the source root: `python3 -m http.server 8765 --bind 127.0.0.1`.

With Node, Playwright and Chromium available, run `python3 tests/run-validation.py`. This executes all four suites and writes the exact results to deliverables/test-results.json. Use `node tests/evaluate.cjs --threshold=0.65` for developer research metrics. The application itself has no runtime package dependencies.
