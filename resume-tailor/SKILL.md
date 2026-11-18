---
name: "resume-tailor"
description: "Use when someone wants their existing resume tailored to one job posting or a job title (for example Forward Deployed Engineer): rewrites only the skills and bullet points in their own file, same layout and page count."
---

# Resume Tailor

Tailor an existing resume to one target: a pasted job posting, a job posting link, or just a job title. No job search, no new template. The user's own file comes back with only the Skills section and the work-experience bullet points rewritten.

If the user types `help`, say in 3 short lines what this does, what to attach (their resume as .docx, plus a posting or a job title), and that the original file is never changed.

## 1. Collect the inputs
- **Resume file.** A .docx is best because its layout carries over exactly. If they attach a PDF or Google Doc, ask once for a .docx export (Word: Save As .docx; Google Docs: File > Download > .docx). If they can't, say the layout may shift and continue from the PDF.
- **Target.** One of:
  - a pasted posting (best);
  - a link to one. Open it. If the page returns only a summary or loads poorly (common on Ashby, Workday and other JavaScript-heavy boards), stop and ask the user to paste the posting text. Don't substitute other listings for a specific posting;
  - a job title only. Then read 2 or 3 real current postings for that title if you can browse or search, and build the target from what they share. Tell the user plainly that the target is a blend of those postings and name them. If the postings are clearly different variants of the role (different industries or focus), say so and offer to use one real posting instead. If you can't look anything up, build it from what that role usually asks for and say so in one line.
- Don't ask for anything else up front.

## 2. Build the target (two layers)
Build the target from two layers, for any job:
- **Role layer: what this job title needs, whatever the company.** The 4 to 6 things anyone in this role does every week and gets hired for: the core work, the people they work with, the soft skills, the working conditions. Examples: a Forward Deployed Engineer works directly with customers, runs demos, scopes vague problems, and travels; a Product Manager writes specs, prioritizes, and aligns stakeholders; a Data Analyst builds dashboards and explains numbers to non-technical people. Work these out from the title and the postings, not from a fixed list.
- **Posting layer: what this specific posting asks for.** The 6 to 10 skills, tools, years of experience and phrases that matter most, in the posting's own wording. With a job title only, this layer comes from the 2 or 3 postings you read.

Show both layers to the user in one short block, labeled "What every [title] needs" and "What this posting asks for", before asking anything.

## 3. Ask about gaps (never invent)
Compare both layers with the resume and ask about every important item the resume doesn't clearly show. Resumes often undersell real experience, so these questions are where most of the tailoring comes from.

- **Role questions first.** One question per role-layer item the resume doesn't show, phrased around real situations, not keywords. For example: "Have you worked directly with customers or clients, like calls, onsite visits or support escalations?", "Have you run a demo or presented technical work to non-technical people?", "Have you taken a vague problem and turned it into a plan or a build?"
- **Posting questions next.** One question per posting-layer item missing from the resume: a tool, a language, a domain, years of experience.
- **Dig into hidden experience.** Where a resume bullet hints at a missing item, ask about it directly: "Your support role mentions escalations. Did you talk to customers yourself?"
- **Get the specifics for every yes.** For each "yes", ask one follow-up for where and what: which job, what they did, any real number. A vague yes can't become a bullet.
- **Format.** Use the multiple-choice question tool when it's available, up to 4 questions per round, in rounds, so nothing gets lost in chat. Options like "Yes, at [job from the resume]", "Yes, somewhere else", "A little", "No". Expect 2 or 3 rounds: usually 6 to 10 questions in total, fewer when the resume already covers most items. Don't pad with questions the resume already answers.
- Only add what they confirm, in their words. "No" and "A little" without specifics stay off the resume.

## 4. Edit the original file
- Change only two things: the Skills section and the bullet points under work experience.
- Leave everything else exactly as it is: header, contact details, job titles, companies, dates, education, section order, fonts, margins, spacing, styles.
- Don't add a summary, a new section, or any extra text.
- Never add a skill, tool, metric or experience the resume doesn't show or the user didn't confirm in step 3. You may reword, reorder and drop existing items to match the posting's wording, and lead each bullet with the part most relevant to the target.
- No stretches. A rewritten bullet claims no more than the original: don't upgrade verbs ("helped" does not become "drove" or "led"), don't widen scope, and don't merge two separate achievements into one bullet. A metric stays attached to the exact claim it measured in the original.
- Ask before dropping. If fitting the layout means removing a skill or a whole bullet, list what you'd drop and ask first (multiple-choice: drop this / drop that / let me shorten something else). Never drop silently.
- For a .docx: unzip it, change text in word/document.xml only, and rezip. Don't rebuild the resume from scratch.

## 5. Keep the page count
1. Before editing, render the original to PDF and note its page count and how full the last page is.
2. Measure first, don't guess. From the rendered original, record how many lines each bullet and the Skills line take and their character counts. Write each new bullet to fit the same number of lines, within about the original's character count. Aim to fit on the first pass instead of trial and error.
3. After editing, render again and look at the page images, not just extracted text. It must match the original page count and fill, with no bullet wrapping onto an extra line. If it grew, shorten bullets first; dropping a skill follows the ask-before-dropping rule.
4. Tell the user the check was done in LibreOffice, which can paginate slightly differently than Word, so they should confirm the page count when they open it.
5. If the resume uses text boxes, tables or multiple columns, say so before editing and take extra care that text stays inside its box.

## 6. Deliver
- Save as a new file beside the original, named with the target, for example `Resume_Forward-Deployed-Engineer.docx`. Never overwrite the original.
- Send the file.
- Under it, show a short before/after: the Skills line, and the 3 bullets that changed most, old and new.
- Flag for review: any bullet whose wording is stronger than the original, and anything removed (skills or bullets), each in one line.
- **Fit summary**, 3 short lines: what already matches the role and posting, what was added from their answers, and the real gaps they said no to. Present the gaps as what to work on next for this kind of role, not as a verdict.
- One line: "Check every bullet is true before you send it."

## Always
- The user reviews and submits. You tailor only.
- Facts come only from the resume and the user's answers.