<img src="git_leaks.png" />

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

# [DEMO]

<a href="04_gitleaks.md" >next >></a>

