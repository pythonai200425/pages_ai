<img src="git_leaks.png" />

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

## Customizing or Adding Detection Rules – Examples

This shows **practical examples** of how you customize or add your own detection rules (using Gitleaks-style config).

## 1️⃣ Add a custom rule for a company-specific API key

Example: your company uses keys like:

```
ACME_API_KEY=acme_live_xxxxxxxxxxxxxxxxx
```

### Custom rule

```toml
[[rules]]
id = "acme-api-key"
description = "ACME internal API key"
regex = "acme_live_[a-zA-Z0-9]{20,}"
entropy = 3.5
keywords = ["acme", "api", "key"]
```

What this does:

* Matches only your internal key format
* Avoids generic false positives
* Uses entropy to confirm randomness

## 2️⃣ Detect hardcoded JWT secrets

Example leak:

```js
const JWT_SECRET = "super_random_secret_value_here"
```

### Custom rule

```toml
[[rules]]
id = "jwt-secret"
description = "Hardcoded JWT secret"
regex = "JWT_SECRET\s*=\s*[\"'][^\"']{16,}[\"']"
entropy = 2.5
keywords = ["jwt", "secret"]
```

This flags:

* Hardcoded secrets
* Even if they are not well-known providers

## 3️⃣ Add a rule without entropy (pattern-only)

Useful when format is strict.

Example:

```text
INTERNAL_TOKEN=INT-1234-5678-ABCD
```

### Custom rule

```toml
[[rules]]
id = "internal-token"
description = "Internal non-random token"
regex = "INT-[0-9]{4}-[0-9]{4}-[A-Z]{4}"
entropy = 0
keywords = ["internal", "token"]
```

Why entropy is 0:

* Token is structured, not random
* Regex alone is enough

## 4️⃣ Override an existing rule (reduce false positives)

Example: UUIDs are being flagged incorrectly.

### Custom allow rule

```toml
[[allowlist]]
description = "Ignore UUID-like values"
regex = "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
```

This tells Gitleaks:

* Yes, it looks random
* But it is safe

## 5️⃣ Add a rule limited to certain file types

Only scan `.env` files:

```toml
[[rules]]
id = "env-secret"
description = "Secrets inside env files"
regex = "(SECRET|TOKEN|KEY)=[^\n]+"
path = "\\.env$"
entropy = 2.0
```

This avoids scanning:

* docs
* markdown
* examples

## 6️⃣ Enable the custom config

Run Gitleaks with your config:

```bash
gitleaks detect --config .gitleaks.toml
```

Or in Docker:

```bash
docker run --rm -v .:/repo zricethezav/gitleaks:latest \
  detect --source=/repo --config=/repo/.gitleaks.toml
```

## One-sentence takeaway

Custom rules let you catch **your real secrets**, reduce noise, and adapt secret scanning to how *your* organization actually works


## Best Practice Summary

* Use `.gitleaks.toml` instead of disabling scans
* Prefer path and regex allowlists over commit allowlists
* Rotate secrets immediately if Gitleaks detects them
* Keep history scanning enabled for real security value

This keeps secret scanning strict, auditable, and CI‑friendly
