# Claude Job Search Skills

Free Claude skills for your job search: build a strong base resume, find jobs that fit you, rank them, and tailor your own resume and cover letter for each one. None of them invent experience, and none of them apply for you.

| Skill | What it does | Best for |
|---|---|---|
| [**resume-builder**](resume-builder/SKILL.md) | Builds or rebuilds your resume in 4 steps from your old resume, LinkedIn PDF and projects: a few clickable gap questions, then it writes it into your own template (Word, Google Docs or Canva) or a clean one-page layout and exports every format. | Starting or refreshing your base resume |
| [**browser-job-scout**](browser-job-scout/SKILL.md) | Works in your own Chrome with the Claude in Chrome extension. Type `scout this page` on LinkedIn Jobs (or a Greenhouse, Ashby, Lever or Workable board) to rank every posting by fit, then `tailor #N` for a tailored resume and cover letter. | LinkedIn and job boards you already have open |
| [**job-search-usa**](job-search-usa/SKILL.md) | Searches US job boards for recent postings, scores your fit, then tailors your resume and writes a cover letter, asking short questions about gaps. | Finding new jobs across many boards |

## Install (Claude app)

1. Download the zip for the skill you want: [resume-builder.zip](../../raw/main/downloads/resume-builder.zip), [browser-job-scout.zip](../../raw/main/downloads/browser-job-scout.zip) or [job-search-usa.zip](../../raw/main/downloads/job-search-usa.zip).
2. In the Claude app: **Settings → Capabilities**, turn on **Code execution and file creation**, then upload the zip under **Skills**.
3. For **resume-builder** with a template, connect **Google Drive** (Google Docs templates) or **Canva** (Canva templates) under Connectors.
4. For **browser-job-scout**, also install the [Claude in Chrome](https://claude.com/chrome) extension and sign in.

## resume-builder

1. Type `/resume-builder help` to see the steps, templates and what to connect.
2. In one message, attach your old resume (PDF or Word) and your LinkedIn profile PDF (profile → More → Save to PDF), paste your GitHub or portfolio link, and type `Build my resume step by step`.
3. Using a template? Google Docs: share the link to your own copy. Canva: open the template, click **Customize this template**, and share that design link.
4. Answer the clickable gap questions (skip any you don't know; it never makes up numbers), approve the preview, and download your files.

It always works on a copy, keeps your template's look, and lists any trade-offs it made to fit. You get a .docx and PDF (default, Word or Google Docs) or a PDF and PNG plus your Canva copy (Canva).

## browser-job-scout

1. Open your own LinkedIn profile in Chrome and attach your resume (.docx) in the Claude panel. Type `help` to see the steps.
2. Go to LinkedIn Jobs and set your filters (role, location or remote, date posted, Easy Apply).
3. Type `scout this page` (add a page count if you want more than 1).
4. Type `tailor #N` for any job in the table, then download the resume and cover letter from the chat.

It reads your resume and LinkedIn profile together, changes only your skills and work-experience bullets, keeps the same layout and page count, and flags any cover-letter sentence your resume doesn't back up. Tip: pair it with [Simplify.jobs](https://simplify.jobs) to autofill the application form.

## job-search-usa

Searches Greenhouse, Ashby, Lever, Workable, Built In, Y Combinator Work at a Startup, Wellfound, Welcome to the Jungle, Remote OK, We Work Remotely, Hacker News, Dice and more. It shows only recent (last 30 days), live postings with a fit score and a link, then edits your Word resume (same design and length) and writes a cover letter per job, one folder per job.

Create a **Project** (for example "Job Search") and start a chat inside it. Make sure web search is available, and turn on extended thinking if your model picker offers it. Don't use Research mode.

- `/job-search-usa help`: what it does and the commands
- `/job-search-usa setup`: attach your resume (a Word file works best) and answer a few clickable questions
- `/job-search-usa search`: find the 5 best-fitting recent jobs
- `/job-search-usa tailor 1 3` or `tailor all`: a tailored resume and cover letter per job

## Limits

These skills don't apply for you. Postings can close after a search, so check the link and read every job before applying.
