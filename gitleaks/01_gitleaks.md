<img src="git_leaks.png" />

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

## Secret Scanning Tools – Comparison Table

| Tool                                           | Type                          | Open Source                   | Where it Runs                     | What it’s Best At                                                 | Typical Use Case                                   |
| ---------------------------------------------- | ----------------------------- | ----------------------------- | --------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------- |
| **Gitleaks**                                   | Static secret scanning (SAST) | ✅ Yes                         | Local, CI, Docker, GitHub Actions | Fast scanning of repos, git history, and files for leaked secrets | CI pipelines, pre-commit checks, org-wide scanning |
| **TruffleHog**                                 | Static secret scanning (SAST) | ✅ Yes                         | Local, CI                         | Deep scanning with regex + entropy to catch high-risk secrets     | Security audits, historical repo scans             |
| **GitGuardian**                                | Secret scanning platform      | ⚠️ Partially (core tools OSS) | SaaS + local hooks                | Real-time detection, alerts, remediation workflows                | Teams & orgs needing monitoring + dashboards       |
| **detect-secrets (Yelp)**                      | Static secret scanning (SAST) | ✅ Yes                         | Local, pre-commit, CI             | Preventing secrets before they are committed                      | Developer laptops, pre-commit hooks                |
| **GitHub Advanced Security – Secret Scanning** | Native platform feature       | ❌ No (commercial)             | GitHub only                       | Automatic detection of known secret patterns                      | Enterprises fully on GitHub                        |
| **GitLab Secret Detection**                    | Native CI feature             | ❌ No (platform feature)       | GitLab CI                         | Built-in secret detection during pipelines                        | Teams using GitLab CI/CD                           |

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
  How it works ?
  * You run Gitleaks once to find all current leaks  
  * You save those findings as a baseline file  
  * Future scans compare against that baseline  
  * Only new findings are reported  

Example (JSON output):

```bash
gitleaks detect \
  --source . \
  --report-format json \
  --report-path gitleaks-report.json \
  --redact
```


