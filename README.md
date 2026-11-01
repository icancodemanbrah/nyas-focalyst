# Focalyst — simplified live demo

Download [Focalyst.html](deliverables/Focalyst.html) and open it in a browser.

For MIT App Inventor, download [Focalyst.aia](deliverables/Focalyst.aia) using GitHub’s **Download raw file** button, then import it through **Projects → Import project (.aia)**.

[Video walkthrough](deliverables/Focalyst-walkthrough.mp4) · [Methodology](deliverables/METHODOLOGY.md) · [Validation](deliverables/VALIDATION.md)

1. Tap **Connect devices**. The simulated implant and patch link, and a resting signal begins moving.
2. Pick a situation on **Live**. The same selector changes the stream before or during a session.
3. Tap **Start** to enable Work Mode. The button becomes **Stop**.

The three tabs are Live, History and System. System manages connections, session resets and local data. No 3D model, external links, calibration steps, research tests or separate simulation page appear in the app.

## What to try
- Resting: continuous resting signal; no response.
- Getting ready to start: a simulated meaningful task action occurs after six seconds. Signal evidence catches up as the two-second window updates.
- Working steadily: task activity suppresses mock events.
- Finding it hard to start: consistent synthetic difficulty plus a reported difficulty and no task action can authorize one mock event after an observation window.
- Paused after an interruption: no new response until the situation changes.
- Unclear / noisy signal: authorization is blocked.

A situation is a controllable synthetic input. It is not an ADHD diagnostic label. The app has no real device connection. All research assumptions are described in METHODOLOGY.md.

## Waveform
The red trace is the combined synthetic LFP-like signal. The pale trace is its generated 2–8 Hz component. Both scroll continuously from the same sample stream. The classifier and optional System spectrum use the last two seconds of red-trace samples. With reduced-motion enabled, the visible chart refreshes once per second.

Stop disables Work Mode immediately while the connected signal continues. Disconnecting either device stops Work Mode and removes the stale trace. Returning from the background requires an explicit restart. Session and daily caps remain in effect; each difficulty episode permits at most one event.

## Files
- Focalyst.html: standalone app with embedded CSS and JavaScript.
- Focalyst.aia: App Inventor project containing the same HTML.
- Focalyst-source.zip: current source, tests, packaging script and docs.
- Focalyst-walkthrough.mp4: short capture of the real browser demo, using a controlled simulation clock.

## Build and test
No runtime dependencies are needed. From the source directory, run `python3 package-demo.py` to regenerate HTML and AIA. Serve it with `python3 -m http.server 8765 --bind 127.0.0.1`.

Run `node tests/engine.cjs` and `node tests/stream.cjs` for the pure model checks. With Playwright and Chromium installed, run `node tests/simple-browser.cjs` and `node tests/simple-edge-browser.cjs`. FOCALYST_PLAYWRIGHT_PATH and FOCALYST_BROWSER_PATH can select your test tools. The browser tests use the server on port 8765.

Developer evaluation remains available with `node tests/evaluate.cjs --threshold=0.65`. This reports reproducible detection metrics, including balanced accuracy, for both synthetic profiles. It is separate from the user interface.

## App Inventor
Projects → Import project (.aia) from my computer → choose Focalyst.aia. The WebViewer loads http://localhost/Focalyst.html from bundled assets. Try AI Companion or build an APK.

MIT import/build and physical Android operation remain unverified. CSV is displayed as selectable text and passed to WebViewString in App Inventor; native file-saving blocks are not implemented. Desktop browsers download CSV normally.

## Local data
History and counters stay on the device. The app imports prior Focalyst history when available. Clear history retains counts; Reset session retains the daily count; Erase saved demo data removes history, counters and prior-version data. New sessions never reconnect or resume automatically after reload. No analytics or uploads are present.
