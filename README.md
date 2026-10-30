# Job Search Assistant (US Edition): a Claude skill

A free Claude skill that searches US job boards for recent postings, scores how well you fit each one, then tailors **your own resume** and writes a cover letter for every job you pick. It asks short multiple-choice questions about your gaps instead of inventing experience.

- Searches US boards and hiring systems: Greenhouse, Ashby, Lever, Workable, Built In, Y Combinator Work at a Startup, Wellfound, Welcome to the Jungle, Remote OK, We Work Remotely, Hacker News, Dice, and more.
- Shows only recent (last 30 days), live postings, with a fit score, what each job loses points on, and a link.
- Edits your uploaded Word resume (same design and length; only the words change).
- One folder per job, each with its own tailored resume and cover letter (.docx).
- Never adds a skill or number you didn't confirm.

## Install (Claude app)

1. Download **`job-search-usa.zip`** from the [latest release](../../releases/latest).
2. In the Claude app: **Settings → Capabilities**, turn on **Code execution and file creation**, then upload the zip under **Skills**.
3. Create a **Project** (e.g. "Job Search") and start a chat inside it.
4. Make sure web search is available (a toggle in some app versions, always on in others). Turn on extended thinking if your model picker offers it. Don't use Research mode.

## Use

- `/job-search-usa help`: what it does and the commands
- `/job-search-usa setup`: attach your resume (Word file works best) and answer a few clickable questions; choose the folder your job folders are saved in
- `/job-search-usa search`: find the 5 best-fitting recent jobs
- `/job-search-usa tailor 1 3` or `tailor all`: tailored resume + cover letter per job

## Limits

It doesn't apply for you. Postings can close after a search, so check the link and read every job before applying.
