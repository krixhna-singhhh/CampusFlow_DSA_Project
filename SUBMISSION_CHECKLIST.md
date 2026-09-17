# VITyarthi Submission Checklist

Before triggering evaluation, check every item once.

## GitHub
- [ ] Create a new GitHub repository.
- [ ] Keep the repository root exactly as the contents of this folder (do not upload an extra parent folder if avoidable).
- [ ] Set repository visibility to **Public**.
- [ ] Confirm `README.md` opens on the repository home page.
- [ ] Confirm `statement.md`, `campusflow/`, `tests/`, `docs/`, `data/`, and `PROJECT_REPORT.pdf` are visible.
- [ ] Use the root URL only: `https://github.com/YOUR-USERNAME/YOUR-REPO-NAME`
- [ ] Do **not** submit a URL containing `/tree/`, `/blob/`, or a file path.

## Quick Git workflow (recommended for version-control marks)
From inside this folder:

```bash
git init
git add README.md statement.md requirements.txt .gitignore LICENSE
git commit -m "docs: initialize CampusFlow project"

git add campusflow config data
git commit -m "feat: implement CampusFlow DSA modules"

git add tests
git commit -m "test: add automated unit tests"

git add docs PROJECT_REPORT.pdf SUBMISSION_CHECKLIST.md
git commit -m "docs: add diagrams results and project report"

git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git push -u origin main
```

If Git asks for identity first:

```bash
git config user.name "Krishnapal Rajput"
git config user.email "YOUR-GITHUB-EMAIL"
```

## Run Check
From repository root:

```bash
python -m unittest discover -s tests -v
python -m campusflow seed
python -m campusflow task-list
python -m campusflow task-plan
python -m campusflow course-plan
python -m campusflow analytics
```

## VITyarthi Portal
- [ ] Upload `PROJECT_REPORT.pdf` as the project report.
- [ ] Paste only the public GitHub repository root URL.
- [ ] Open that URL in an incognito/private browser window to confirm it is publicly accessible.
- [ ] Review everything before triggering evaluation because re-submission is not permitted after evaluation starts.
