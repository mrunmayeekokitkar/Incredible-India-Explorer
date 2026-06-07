import os
import shutil

base_dir = 'd:/INDIA'

# Remove deploy-pages.yml
deploy_file = os.path.join(base_dir, '.github/workflows/deploy-pages.yml')
if os.path.exists(deploy_file):
    os.remove(deploy_file)

files = {
    # WORKFLOWS
    '.github/workflows/auto-assign.yml': '''name: Auto Assign PRs
on:
  pull_request:
    types: [opened, ready_for_review]

jobs:
  assign:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.addAssignees({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              assignees: [context.payload.pull_request.user.login]
            })
''',

    '.github/workflows/labeler.yml': '''name: Auto Label PRs
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v4
        with:
          repo-token: "${{ secrets.GITHUB_TOKEN }}"
          configuration-path: .github/labeler.yml
''',

    '.github/workflows/duplicate-issues.yml': '''name: Check Duplicate Issues
on:
  issues:
    types: [opened, edited]

jobs:
  find_duplicates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions-cool/issues-similarity-analysis@v1
        with:
          filter-threshold: 0.8
          title-excludes: 'bug, feature'
          comment-title: '### 🔎 Potential duplicate issues found'
          comment-body: 'Please check if these issues have already addressed your problem.'
''',

    '.github/labeler.yml': '''# Labeler configuration
ui-ux:
  - '**/*.css'
  - '**/*.html'

javascript:
  - '**/*.js'

documentation:
  - '**/*.md'
''',

    # ISSUE TEMPLATES
    '.github/ISSUE_TEMPLATE/enhancement.md': '''---
name: Enhancement
about: Suggest an enhancement to an existing feature
title: "[ENHANCEMENT] "
labels: enhancement
assignees: ''

---

**Is your enhancement related to a specific page or feature?**
Please describe.

**Describe the enhancement you'd like**
A clear and concise description of the enhancement.

**Additional context**
Add any other context or screenshots here.
''',

    '.github/ISSUE_TEMPLATE/ui_ux_issue.md': '''---
name: UI/UX Issue
about: Report a visual, responsive, or design problem
title: "[UI/UX] "
labels: ui-ux, design
assignees: ''

---

**Describe the UI/UX issue**
A clear and concise description of the design or responsive layout issue.

**Where does this happen?**
- Page URL: 
- Specific component (e.g. Navbar, Timeline, Card):

**Expected design/behavior**
A clear description of what the UI should look like.

**Screenshots**
If applicable, add screenshots.

**Device Information:**
 - Device: [e.g. iPhone 13, Desktop]
 - Screen Resolution: [e.g. 1920x1080]
 - Browser: [e.g. chrome, safari]
''',

    '.github/ISSUE_TEMPLATE/blank.md': '''---
name: Blank Issue
about: Create an issue that doesn't fit the other templates
title: ''
labels: ''
assignees: ''

---

**Description**
Provide a clear description of the issue or topic you want to discuss.
''',
    
    # CONFIG.YML to enable blank issues explicitly in some GH versions
    '.github/ISSUE_TEMPLATE/config.yml': '''blank_issues_enabled: true
contact_links:
  - name: Community Discussions
    url: https://github.com/yourusername/yourrepo/discussions
    about: Ask questions and discuss features here.
'''
}

for rel_path, content in files.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
