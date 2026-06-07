import os

base_dir = 'd:/INDIA'

files = {
    'README.md': '''# Incredible India Explorer 🇮🇳

![Hero Image](assets/hero_banner.png)

Welcome to the **Incredible India Explorer**—an immersive, interactive digital experience designed to showcase the rich culture, history, geography, and wildlife of India.

## 💡 The Idea Behind This
The Incredible India Explorer was born out of a desire to move beyond static encyclopedias and dry historical texts. India's culture, history, and geography are dynamic and alive. This project aims to build an immersive, interactive digital experience—using modern web technologies, gamification, and interactive storytelling—to let users truly *experience* India from their screens.

## ✨ Features
*   **Interactive Freedom Story:** A 'Choose Your Own Adventure' style historical narrative allowing you to explore the Independence Movement through different philosophies.
*   **Dynamic Storylines:** Vertical scrolling timelines that tell a narrative journey (e.g., traveling from the Himalayas down to Kanyakumari).
*   **Bharat AI Guide:** A simulated, highly intelligent chatbot that can answer your questions about Indian food, culture, and travel destinations.
*   **Interactive Map:** A beautifully animated SVG map of India allowing users to click and learn about specific states.
*   **Global Theme Toggle:** Seamlessly switch between an elegant Frosted Glass Dark Mode and a crisp, clean Light Mode.
*   **Premium UI/UX:** Built entirely with Vanilla HTML, CSS, and JS, featuring CSS Grid, Flexbox, glassmorphism, and scroll-triggered IntersectionObserver animations.

## 🚀 Getting Started

This project uses no complex build tools or backend frameworks. It runs purely in the browser!

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/incredible-india-explorer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd incredible-india-explorer
   ```
3. Open `index.html` in your favorite web browser!

## 🤝 Contributing
We welcome contributions! Please see our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and use the provided Issue and PR templates.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
''',

    'LICENSE': '''MIT License

Copyright (c) 2026 Incredible India Explorer Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''',

    'CODE_OF_CONDUCT.md': '''# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting
''',

    '.github/ISSUE_TEMPLATE/bug_report.md': '''---
name: Bug report
about: Create a report to help us improve
title: "[BUG] "
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. iOS]
 - Browser [e.g. chrome, safari]
 - Version [e.g. 22]
''',

    '.github/ISSUE_TEMPLATE/feature_request.md': '''---
name: Feature request
about: Suggest an idea for this project
title: "[FEATURE] "
labels: enhancement
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
''',

    '.github/PULL_REQUEST_TEMPLATE.md': '''## Description
Please include a summary of the change and which issue is fixed. Please also include relevant motivation and context.

Fixes # (issue)

## Type of change
Please delete options that are not relevant.
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] This change requires a documentation update

## Checklist:
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] My changes generate no new warnings
''',

    '.github/workflows/deploy-pages.yml': '''name: Deploy to GitHub Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v4
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
'''
}

for rel_path, content in files.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
