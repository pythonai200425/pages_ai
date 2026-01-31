# Gitleaks

## What is Gitleaks

Gitleaks is an open-source **secret scanning** tool
It looks for things that should *never* be committed into code, like passwords, API keys, tokens, private keys, and other credentials

You can run it on:

* Git repositories (including commit history)
* Files / folders
* Input from stdin (so you can pipe content into it)

## Who made it

Gitleaks was created by **Zachary (Zach) Rice**
It’s maintained by the Gitleaks project/community (the project is still actively updated)

## Free or not

Free ✅
Gitleaks is open-source and **MIT licensed**, so you can use it in personal and commercial projects

## Which language

Gitleaks is written in **Go**

## What year it started

Work on Gitleaks started in **early 2018** (it began as a hobby project)

## What does it find

Gitleaks detects **hardcoded secrets**, for example:

* API keys (cloud providers, SaaS tools)
* Access tokens (GitHub, GitLab, Slack, etc.)
* Passwords and credentials in config files
* Private keys / key material
* Generic “this looks like a secret” patterns

How it finds them (high level):

* Mostly pattern matching rules (commonly regex-based)
* Built-in rules + custom rules you can add

Where it’s especially useful:

* Pre-commit checks (catch secrets before they ever land)
* CI/CD pipelines (block builds if secrets are detected)
* Auditing existing repos (including scanning history)

## Similar tools

A few common alternatives (same problem space):

* **TruffleHog**
* **GitGuardian** (commercial + open-source components)
* **detect-secrets** (Yelp)
* **GitHub Advanced Security** secret scanning
* **GitLab Secret Detection**

## Why people pick Gitleaks (and when it’s “better”)

Gitleaks tends to win when you want something that’s:

* **Fast and lightweight** (good for CI and local runs)
* **Easy to adopt** (CLI-first, simple workflows)
* **Runs locally/offline** (you don’t need to send code to a third party)
* **Highly configurable** (custom rules, allowlists/baselines)
* **Portable** (single binary feel, plus Docker / GitHub Action options)

Tradeoff to be aware of:

* Like many scanners, pattern-based detection can create false positives if rules aren’t tuned
* Some other tools may offer stronger “verification” and enterprise workflows (depending on product)

Commonly used flags:

* `--report-format`
  Controls the output format
  Common values:

  * `json`
  * `sarif`
  * `csv`
  * `junit`

* `--report-path`
  Where the output file is written

* `--redact`
  Redacts secrets in the output (recommended for CI logs)

* `--verbose`
  More detailed output while scanning

* `--no-git`
  Scan files without treating the target as a git repository

* `--config`
  Use a custom configuration file (rules, allowlists, etc.)

* `--baseline-path`
  Ignore already-known findings (useful for legacy repos)

Example (JSON output):

```bash
gitleaks detect \
  --source . \
  --report-format json \
  --report-path gitleaks-report.json \
  --redact
```


# Gitleaks – Example Run

## Example code with a leaked secret

`app.js`

```js
// Demo example – do NOT do this in real code
const API_KEY = "sk_live_1234567890abcdef1234567890abcdef"
console.log("app started")
```

This file contains a hardcoded API key, which is exactly the kind of issue Gitleaks is designed to detect

---

## Running Gitleaks

Run Gitleaks against the current directory and output the results as JSON:

```bash
gitleaks detect \
  --source . \
  --report-format json \
  --report-path gitleaks-report.json \
  --redact
```

What this command does:

* Scans the source directory
* Looks for hardcoded secrets
* Outputs findings in JSON format
* Writes results to a file
* Redacts secret values from the output

---

## Example finding (output)

`gitleaks-report.json` (simplified example):

```json
[
  {
    "Description": "Generic API Key",
    "File": "app.js",
    "StartLine": 2,
    "EndLine": 2,
    "RuleID": "generic-api-key",
    "Match": "sk_live_**********************",
    "Secret": "REDACTED"
  }
]
```

The finding tells you:

* What was detected
* Where it was detected (file + line)
* Which rule matched

But the real secret value is not exposed

---

## What does "redacted" mean

"Redacted" means the **actual secret value is intentionally hidden** in the output

Instead of showing the real password, token, or API key, Gitleaks masks it so the secret does not leak again through:

* CI logs
* Security reports
* Stored artifacts

### Example

Original secret in code:

```text
sk_live_1234567890abcdef1234567890abcdef
```

Redacted output:

```text
sk_live_**********************
```

or:

```text
REDACTED
```

### Why redaction is important

* Prevents secondary leaks caused by reports themselves
* Safe to store and share reports
* Recommended best practice for CI/CD pipelines

### When to use `--redact`

* Always in CI/CD
* When reports are uploaded, archived, or shared

### When you might skip it

* Local debugging on your own machine
* Temporary scans where output is not saved
