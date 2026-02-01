<img src="git_leaks.png" />

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

# [DEMO]

* Simple project demo

<a href="03_gitleaks.md" >next >></a>