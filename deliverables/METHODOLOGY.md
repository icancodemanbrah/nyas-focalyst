# Scientific refinement and implementation assumptions

## Scientific scope
The supplied refinement package informed this revision. Human nucleus accumbens studies in other conditions provide context for individualized changes in low-frequency activity; ADHD behavioral variability provides context for repeated, event-labeled examples. These do not validate an ADHD task-initiation LFP signature. No actual experimental waveform files or annotated participant datasets were supplied, so every displayed sample is generated locally.

The proposed physical concept remains a bioresorbable receiver/electrode system powered by an external inductive transmitter. The software sends no hardware commands and provides no stimulation parameters. Battery/power gauges are omitted from the UI per the latest design request. Internal authorization still supports power-invalid checks in developer tests.

## One coherent, continuous stream
simulation.js exposes createStream(profile, seed). It maintains oscillator phases, deterministic noise and sample position across calls. The UI reads 16 new samples every 125 ms, giving a nominal 128 Hz simulation stream, and displays the newest 256 samples (two seconds). This is a software sampling clock, not measured acquisition timing.

Four components centered at 6, 12, 22 and 35 Hz, with jitter, slow amplitude modulation and uniform noise, form the combined signal. State changes smoothly adjust component amplitudes. The pale trace is the same low-frequency oscillator contribution used in the combined red trace. It is a generated component, not a separately recorded electrode or an independently drawn animation. The plot has fixed arbitrary-unit scales and clips large artifacts visually; features are computed from unclipped samples. Missing connections clear the plot. Reduced-motion settings reduce drawing frequency to once per second while data processing continues.

The first component illustrates a 2–8 Hz band discussed in the supplied research from another condition. The amplitude templates connecting rest, preparation, work, difficulty and interruption to particular bands remain invented demonstration assumptions. They have no validated interpretation for ADHD, mood, motivation or dopamine.

## Features, baseline and personalized calibration
For each complete window, remove its mean, apply a Hann window and compute a DFT over 0.5–50 Hz. Calculate normalized band-power shares for 2–8, 8–16, 16–30 and 30–45 Hz; compute RMS/peak quality checks. The same red-trace sample array drives the spectrum and classifier.

Calibration uses 48 labeled synthetic windows per individual: eight repeats of six defined states. An individual's mean resting feature vector is the baseline. Training centroids and incoming features are centered on that baseline before Euclidean-distance comparison. Baseline centering alone is a coordinate translation, so it does not establish improved classification; personalized templates and individualized component permutations produce the differences between model A and B. The System baseline-change readout is a percentage-point change in low-band share, not a clinical score or signal-strength measurement.

The model uses normalized exp(-10 × distance) weights; a difficulty threshold of 0.65, confidence cutoff of 0.58 and maximum nearest-centroid distance of 0.36 are provisional. Confidence is not a calibrated probability. Signal quality failures and ambiguous/unfamiliar features return uncertainty. The user interface loads Person A's mock calibration automatically. Both profiles remain available to developer evaluation. No calibration wizard or research screen is required to use the app.

## Behavioral definitions and task timing
The situation selector supplies defined synthetic behavioral evidence:
- Resting: no task attempt and no task action.
- Getting ready: task intent; a simulated first meaningful edit at six seconds, independent of mock authorization. Signal state changes to initiated, then working.
- Working: task-relevant action is continuing.
- Difficulty: reported difficulty and no meaningful task action.
- Interrupted: attempted task has paused.
- Unclear: artifact-contaminated samples with insufficient evidence.

These are scenario assumptions. Selecting a situation is not a clinical report or a measurement of intention. The six-second transition and four-second difficulty observation window are software timings with no clinical basis.

Task initiation is observed only when the simulated task action and an initiated/working pattern agree. A disagreement yields insufficient information. An event authorization cannot itself create task success. In the difficulty example, authorization leaves the task unstarted. Raw data, behavioral flags, features, predictions, configuration and outcome are logged separately.

## Authorization and live state
Work Mode is explicitly enabled by Start. Connected devices continue to show a signal while Work Mode is off. Analysis runs once per second. A difficulty episode needs a stable window, reported difficulty, no action, at least four seconds since selection and Start, and two consecutive difficulty estimates. It then passes through the common decision engine: Stop, communication, power, Work Mode, finite configuration, freshness, uncertainty, duplication, engagement, session/daily limits, lockout and score threshold.

One event is permitted per selected difficulty episode, with a five-second lockout and default caps of three per session/ten per local day. Choosing a new episode or explicitly restarting Work Mode still respects the caps and lockout. Disconnecting either simulated link, Stop or backgrounding the page disables authorization. A timer gap exceeding one second resets the signal buffer and pauses Work Mode. Reopening starts disconnected and off.

These mechanisms demonstrate software decisions. They do not provide independently validated implanted-device safeguards. Local clocks and browser storage are user-controlled.

## Reproducible evaluation, outside the UI
The original 17 deterministic model fixtures remain developer checks. They include intentional false-positive and false-negative examples and conditions with undefined ground truth. Calibration seeds and evaluation seeds are distinct, although both sets share the synthetic generator; generalization claims are unsupported.

The threshold benchmark uses 60 held-out examples with graded overlap and contradictory labels. Precision, recall, specificity, false-positive rate and balanced accuracy are reported; empty denominators yield null/Not available. Balanced accuracy is the mean of sensitivity and specificity when both are defined. Quality/uncertainty fixtures are tested explicitly. These artificial metrics cannot estimate clinical performance.

The new stream tests check deterministic continuity across different chunk sizes, live/static classifier agreement, artifact rejection/recovery, individual baselines and balanced-accuracy denominators. Browser tests exercise the actual simplified interface. Earlier multi-screen reviews are archived and do not constitute human usability evidence.

## Privacy and replay
The app processes data locally. Logs include raw samples for recorded events, feature vectors, model version, stream ID/sample position, fixed generator seed, scenario, task-action flags, decision and outcome. Raw event windows can therefore be inspected directly. History migration preserves older records when present. User-triggered CSV includes all fields across retained record types. History clearing and full-data deletion have explicit confirmations. There are no outbound app requests, trackers or external links.

## Research references supplied in the refinement package
1. Shivacharan et al. (2022): https://www.nature.com/articles/s41591-022-01941-w
2. Nucleus accumbens recordings/event detection: https://pmc.ncbi.nlm.nih.gov/articles/PMC8599841/
3. Kofler et al. (2013): https://pubmed.ncbi.nlm.nih.gov/23872284/
4. AAN diagnostic limitations (2016): https://pubmed.ncbi.nlm.nih.gov/27760867/
5. Hamid et al. (2016): https://www.nature.com/articles/nn.4173
6. Scangos et al. (2021): https://www.nature.com/articles/s41591-021-01480-w
7. Evaluation/class imbalance (2023): https://pubmed.ncbi.nlm.nih.gov/37385392/
8. Data leakage (2024): https://www.nature.com/articles/s41467-024-46150-w
9. Ahn et al. (2025): https://www.nature.com/articles/s41467-025-59835-7

These references and their descriptions were supplied by the user. Full texts were not independently verified during this revision; earlier source access was blocked by the environment's proxy. No published numeric detector or intervention parameter is imported as an ADHD threshold.

## Remaining scientific gap
Appropriately licensed raw regional LFP recordings with individual, task-event annotations would support replacing the invented signal templates and labels. Evidence connecting those signals to ADHD-related initiation difficulty, and evidence for any intervention's behavioral effect, remain unresolved. The app stays a synthetic architecture demonstration.
