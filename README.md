# Claude Job Search Skills

Free Claude skills for your job search: find jobs that fit you, rank them, and tailor your own resume and cover letter for each one. None of them invent experience, and none of them apply for you.

| Skill | What it does | Best for |
|---|---|---|
| [**browser-job-scout**](browser-job-scout/SKILL.md) | Works in your own Chrome with the Claude in Chrome extension. Type `scout this page` on LinkedIn Jobs (or a Greenhouse, Ashby, Lever or Workable board) to rank every posting by fit, then `tailor #N` for a tailored resume and cover letter. | LinkedIn and job boards you already have open |
| [**job-search-usa**](job-search-usa/SKILL.md) | Searches US job boards for recent postings, scores your fit, then tailors your resume and writes a cover letter, asking short questions about gaps. | Finding new jobs across many boards |

## Install (Claude app)

1. Download the zip for the skill you want: [browser-job-scout.zip](../../raw/main/downloads/browser-job-scout.zip) or [job-search-usa.zip](../../raw/main/downloads/job-search-usa.zip).
2. In the Claude app: **Settings → Capabilities**, turn on **Code execution and file creation**, then upload the zip under **Skills**.
3. For **browser-job-scout**, also install the [Claude in Chrome](https://claude.com/chrome) extension and sign in.

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
