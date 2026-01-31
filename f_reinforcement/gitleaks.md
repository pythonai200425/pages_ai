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

---

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

## “Verbs” you can use for Gitleaks (for docs / resumes / README)

* Scan
* Detect
* Prevent
* Audit
* Identify
* Flag
* Block
* Enforce
* Monitor
* Validate (as a pipeline gate)
* Remediate (when paired with rotation + cleanup workflows)

## Tags (keywords)

Use these as repo topics, blog tags, or documentation labels:

* #gitleaks
* #secret-scanning
* #secrets
* #credentials
* #apikeys
* #devsecops
* #security
* #sast
* #git
* #cicd
* #precommit
* #shiftleft
* #supplychain-security
* #leak-prevention
* #compliance

## Output formats / flags ("tags" as in CLI flags)

When people say "tags" in the context of Gitleaks, they often mean **output formats and flags** you pass to the CLI

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

Example (SARIF for GitHub / security tools):

```bash
gitleaks detect \
  --source . \
  --report-format sarif \
  --report-path gitleaks.sarif
```

These formats are what you typically "tag" into:

* CI systems
* GitHub Security tab
* Code scanning dashboards
* Compliance reports

---

If you want, I can add a short section mapping **which format to use where** (GitHub, GitLab, Jenkins, Azure DevOps)


---

If you want, I can also add a tiny “How to use” section (local scan + CI example)
