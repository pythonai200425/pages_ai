# Gitleaks

## What is Gitleaks

Gitleaks is an open-source **secret scanning** tool
It looks for things that should *never* be committed into code, like passwords, API keys, tokens, private keys, and other credentials

You can run it on:

* Git repositories (including commit history)
* Files / folders
* Input from stdin (so you can pipe content into it)  
  ```git diff --cached | gitleaks detect --stdin --redact```

## Who made it ?

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

* **TruffleHog** – Open-source secret scanner that searches git history and current files using regex and entropy analysis

* **GitGuardian** – Commercial security platform with open-source tools, focused on real-time secret detection and remediation

* **detect-secrets (Yelp)** – Lightweight open-source tool designed to prevent secrets from being committed, commonly used in pre-commit hooks

* **GitHub Advanced Security secret scanning** – GitHub’s native secret scanning for repos, integrated into the platform and mostly available on paid plans

* **GitLab Secret Detection** – Built-in GitLab CI feature that scans repositories for leaked credentials during pipelines

## Why people pick Gitleaks (and when it’s “better”)

Gitleaks tends to win when you want something that’s:

* **Fast and lightweight** (good for CI and local runs)
* **Easy to adopt** (CLI-first, simple workflows)
* **Runs locally/offline** (you don’t need to send code to a third party)
* **Highly configurable** (custom rules, allowlists/baselines)
* **Portable** (single binary feel, plus Docker / GitHub Action options)

## Gitleaks – Installation (Windows & macOS)

Simplest way to install Gitleaks on **Windows** and **macOS**

### Docker

```
docker run --rm -v C:\projects\my-app:/repo zricethezav/gitleaks:latest detect --source=/repo
```
-v C:\projects\my-app:/repo share my folder with Docker

--rm remove the docker container after the scan

❌ Can Docker scan a GitHub repo without cloning? No

❌ Can we run Gitleaks on a GitHub folder without cloning it ? No

## macOS

### Option 1: Homebrew (recommended)

```bash
brew install gitleaks
```

Verify installation:

```bash
gitleaks version
```

### Option 2: Prebuilt binary

1. Download the latest macOS release from GitHub
2. Extract the archive
3. Move the binary to a directory in your PATH

```bash
sudo mv gitleaks /usr/local/bin/
```

Verify:

```bash
gitleaks version
```

## Windows

### Option 1: Prebuilt binary (recommended)

1. Download the latest Windows release from GitHub (`gitleaks_windows_x64.zip`)

2. Extract the ZIP file

3. Move `gitleaks.exe` to a directory such as:

   * `C:\Program Files\Gitleaks\`

4. Add that directory to your **PATH** environment variable

Verify in PowerShell or CMD:

```powershell
gitleaks version
```

### Option 2: Chocolatey [Chocolatey is a package manager for Windows]

If you use Chocolatey:

```powershell
choco install gitleaks
```

Verify:

```powershell
gitleaks version
```

## After installation

Run your first scan:

```bash
gitleaks detect --source .
```

If the command runs, Gitleaks is installed correctly


Commonly used flags:

* `--report-format`
  Controls the output format
  Common values:

  * `json`
  * `sarif` SARIF (Static Analysis Results Interchange Format) representing the output of static analysis tools  
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

**What does "redacted" mean**

"Redacted" means the **actual secret value is intentionally hidden** in the output

Instead of showing the real password, token, or API key, Gitleaks masks it so the secret does not leak again through:

* CI logs
* Security reports
* Stored artifacts

**When you might skip it**

* Local debugging on your own machine
* Temporary scans where output is not saved

# GitHub Actions + Gitleaks Secret Scan

## What is GitHub Actions

GitHub Actions is GitHub’s built-in CI/CD system. It runs **workflows** (automations) when events happen in your repo, like:

* `push` to a branch
* `pull_request` opened/updated
* `workflow_dispatch` (manual run)
* on a schedule (`cron`)

A workflow is a YAML file stored here:

* `.github/workflows/<workflow-name>.yml`

It contains:

* **Triggers** (`on:`)
* **Jobs** (a job runs on a runner like `ubuntu-latest`)
* **Steps** (each step runs a command or uses an action)

### Demo ✅ In a few steps 

#### 1️⃣ Open your GitHub repo

Public or private — both work

#### 2️⃣ Create this file in the repo

**Path:**

```
.github/workflows/gitleaks.yml
```

You can do this directly in GitHub:

* **Add file** → **Create new file**
* Paste the path above

#### 3️⃣ Paste this content

```yaml
name: Gitleaks Scan

on:
  push:
  pull_request:

jobs:
  gitleaks:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Run Gitleaks
        run: |
          docker run --rm \
            -v ${{ github.workspace }}:/repo \
            zricethezav/gitleaks:latest \
            detect --source=/repo
```

**uses: actions/checkout@v4**  
Run an existing action (not a shell command)  
@v4 means: “Use version 4 of this action”  

#### 4️⃣ Commit the file

That’s it ✅
No settings, no secrets, no Docker install on your side

## What happens after that

* Every **push** → Gitleaks runs
* Every **pull request** → Gitleaks runs
* If a secret is found → ❌ build fails
* If clean → ✅ green check

You’ll see results under:

```
Repo → Actions → Gitleaks Scan
```

## Example: a secret leak Gitleaks will catch

```js
const API_KEY = "sk_live_1234567890abcdef1234567890abcdef"
console.log("app started")
```

If this code is committed:

* Gitleaks detects the API key
* The GitHub Action fails
* You see the leak details in the Actions log

# Gitleaks Configuration, Bypass, and Commit History

## The `.gitleaks.toml` File

The `.gitleaks.toml` file controls how Gitleaks behaves in your repository. It lets you fine‑tune secret detection so the scan is strict **but not noisy**.

It is typically placed at the root of the repository:

* `.gitleaks.toml`

### What it is used for

* Allowlisting known safe files or folders (docs, examples, fixtures)
* Allowlisting specific patterns that look like secrets but are fake
* Ignoring specific historical commits that cannot be changed
* Customizing or adding detection rules

### Common allowlist patterns

Ignore entire directories:

```toml
[allowlist]
paths = [
  "docs/",
  "examples/",
  "tests/fixtures/"
]
```

Ignore known fake secrets using regex:

```toml
[allowlist]
regexes = [
  "FAKE_[A-Z0-9_]+",
  "TEST_TOKEN_[0-9]+"
]
```

These rules reduce false positives while keeping real secret detection active

## Commit History Scanning

By default, Gitleaks scans **git history**, not just the files in the working tree

That means:

* A secret committed **years ago** can still fail today’s CI
* Removing a secret from the file is not enough if it exists in history

This is why CI workflows often use:

```yml
fetch-depth: 0
```

It allows Gitleaks to inspect all commits instead of only the latest one

## Ignoring Historical Commits

Sometimes you cannot rewrite history (forks, long‑lived repos, compliance reasons). In that case, you can allowlist specific commits

Example:

```toml
[allowlist]
commits = [
  "a1b2c3d4e5f6g7h8i9j0"
]
```

Use this only when:

* The secret is already revoked
* History rewriting is not possible
* The risk is fully understood

## Best Practice Summary

* Use `.gitleaks.toml` instead of disabling scans
* Prefer path and regex allowlists over commit allowlists
* Rotate secrets immediately if Gitleaks detects them
* Keep history scanning enabled for real security value

This keeps secret scanning strict, auditable, and CI‑friendly
