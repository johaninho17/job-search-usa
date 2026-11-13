---
name: "resume-builder"
description: "Use when someone wants to build or rebuild their resume step by step: gathers their old resume (PDF or .docx), LinkedIn PDF and project notes, asks a few gap questions, writes it into their own template (Word, Google Docs or Canva) or a clean one-page layout, and exports it in every format available. Type help to see what it does and what to connect."
---

# Resume Builder

Builds a job-ready base resume in 4 steps. It never invents experience. Tailoring to a specific job is a separate step; offer it at the end.

Run the steps in order and show a short result after each one, so the user can follow along.

## Help
When the user types "help" (or asks what this does), show this and stop:

**What it does:** builds or rebuilds your resume in 4 steps: Gather your context -> Short interview about gaps -> Write it into your layout -> Export and check.

**What to bring (any of these):**
- Your old resume (PDF or Word)
- Your LinkedIn profile as a PDF (on your profile: More -> Save to PDF)
- GitHub, portfolio or project notes
- Optional: a resume template you like

**Templates, what to connect, what you get:**
| Your template | Connect | What you get |
|---|---|---|
| None | Nothing | Clean one-page ATS-friendly resume: .docx + PDF here |
| Word file (.docx) | Nothing, just upload it | Your template filled in: .docx + PDF here |
| Google Docs | Google Drive | A filled copy in your Drive (link) + .docx and PDF here |
| Canva | Canva | A filled copy in your Canva (link) + PDF and PNG here |
| PDF or image only | Nothing | A rebuilt match as .docx + PDF here (labeled as a rebuild) |

**Before you start (checklist):**
- [ ] File creation is on in Claude's settings (so it can make .docx and PDF files)
- [ ] Google Docs template: Google Drive is connected, and you've made your own copy (File -> Make a copy, or Use template). Share the link to your copy.
- [ ] Canva template: Canva is connected, and you've opened the template and clicked "Customize this template". Share the link to that design (canva.com/design/...), not the template's marketplace page.
- [ ] GitHub or portfolio: repos are public. If Claude can't open them, paste a line per project (what it does, tech, status).
- [ ] Send your files and your first message together in one message.

**To start:** type "Build my resume step by step", attach your files, and paste your template link if you have one.

## Step 1: Gather your context
- Read everything the user gave you: old resume in any format (PDF or .docx), LinkedIn profile PDF, GitHub or portfolio links, project notes, pasted text. Files in the project count. The old resume is only a source of facts; its design is not reused unless the user says it is their template.
- Work out the target role and level from the files. Ask only if it is truly unclear, as one multiple-choice question.
- Pre-flight check before the interview, in one short block:
  - Which template path applies (see Step 3).
  - Is the needed connector connected? If not, say which one in one line so the user can connect it while the interview runs.
  - Is the template link the user's own design or doc (Canva: canva.com/design/...; Docs: a doc in their Drive), not a public template or marketplace page? If not, tell them how to get their own copy (see Help) before Step 3.
  - Could every link be opened (GitHub, portfolio)? If one couldn't, say so and ask the user to paste a line per project instead of guessing.
- Show two short lists:
  - **What I found:** roles, projects, skills, education (one line each).
  - **What's missing:** up to 5 gaps that would make the resume stronger (missing numbers, unclear scope, tech not named, a project with no outcome, missing links).
- If there is nothing to read (no resume, no LinkedIn), say so and go straight to Step 2 with basic questions first (roles, dates, school, projects).

## Step 2: Interview
- Ask about the gaps with the chat's clickable question tool (the multiple-choice question card, for example AskUserQuestion or ask_user_input), never as a typed list in the message. Up to 4 related questions per card, maximum 8 questions in total. Only type a question out if no question tool is available.
- Prefer multiple choice or a short fill-in (for example: "Roughly how many users did this serve? Under 1k / 1k-10k / 10k-100k / 100k+ / skip").
- Focus on impact, scale, numbers, tech used and ownership.
- Cover every gap listed in Step 1. If numbers or impact was a gap, at least one question must ask for numbers.
- Ask about conflicts between sources (a different title, date or company name on the resume vs LinkedIn) instead of silently picking one.
- If the only metrics come from the old resume, confirm they're still accurate in one question.
- Every question can be skipped. If the user doesn't know a number, write the bullet without one. Never estimate or invent a number, skill, title or date.

## Step 3: Write it into your layout
**Content**
- Bullets: action verb + what you did + tech + result. 3 to 5 bullets for recent roles, 1 to 3 for older ones.
- Skills grouped (for example Languages, Frameworks, Cloud/Tools). Only skills the sources or answers show.
- Section order for experienced candidates: Header, Skills, Experience, Projects, Education. For new grads and career changers: Header, Education, Projects, Skills, Experience. If the template has its own section order, keep the template's order.
- Keep titles, companies and dates exactly as the sources show unless the user corrects them.

**Layout: always honor the user's template.** Never swap its design for a different one. Change the words, not the look: fonts, sizes, colors, spacing, margins, columns, icons and section styles stay as they are. If the content doesn't fit, shorten bullets; don't resize or restyle the template. Remove leftover placeholder text. Never edit the user's original file or design; always work on a copy.
- **Word template (.docx upload):** copy the file, then replace the text in word/document.xml and rezip.
- **Google Docs template (Google Drive connector):** find the doc the user names or links, make a copy in their Drive named FirstName_LastName_Resume, and replace the text in that copy.
- **Canva template (Canva connector):** use the user's own design link. Make a copy (never edit their original), replace the text in place on the copy, check the preview after each pass, then show the final preview and ask with a question card whether to save it or change something. Save only after they approve.
- **When a connector can't edit an element** (for example lines or dividers that can't be moved): use the closest fallback that keeps the look, such as replacing it with a thin shape in the same color and size, and mention it in the trade-offs.
- **Template only as a PDF or image:** recreate it as a .docx with the same fonts (or the closest available), colors, column layout and section order. Say it is a rebuild and show it next to the original.
- **Connector needed but not connected:** say which one to connect. If the user can't, ask them to download the template (Docs: File -> Download -> .docx; Canva: Share -> Download -> PDF) and continue with the Word or PDF path.
- **No template:** clean default. One page (two only with 10+ years of experience), one column, standard headings, a common font (Calibri, Arial or similar, 10-11pt body), no tables, text boxes, icons, photos or graphics, so applicant tracking systems read it cleanly.

**Fixed-slot templates:** before writing, compare the user's content with the template's slots (for example 3 roles but 2 job slots, 2 degrees but 1 education slot, 5 contact items but 4 contact slots). If something won't fit, ask one question card with the options (drop it, merge it into another slot, add a slot if the template allows it, or move it to another section). Don't decide silently.

**Size guard (check after every edit, before export):**
- Canva and Google Docs: compare each filled text box with the placeholder it replaced. Shorten text that wraps where the placeholder didn't, overflows its box or pushes onto a second page; don't resize or restyle the template.
- Replace text only. Never paste the whole resume into the document again, append a second copy, or leave the old text below the new text.
- Compare against the template or original: same page count (or one page for the default), and the text length should be about the same as the source content, not several times bigger. If the file or text has grown far beyond the original (for example more than double), stop, throw that copy away, make a fresh copy and redo the edit.
- Render the result (export to PDF or look at the Canva preview) and confirm nothing overflows, overlaps or got cut off.

## Step 4: Export and check
Deliver every format the path supports, so the user always has a file that works:
| Path | Delivered |
|---|---|
| Default or Word template | FirstName_LastName_Resume.docx + .pdf, both here |
| Google Docs | Link to the Drive copy + .docx and .pdf downloads here |
| Canva | Link to the Canva copy + .pdf and .png downloads here (Canva can't export Word) |
| PDF/image rebuild | .docx + .pdf here |

- Never overwrite the user's original files or designs.
- If one export fails, say which one and still deliver the others.
- Show a short check:
  - Page count
  - Size guard passed (no duplicated or leftover text)
  - Every claim comes from a source file or an interview answer (yes/no; list anything unsure)
  - ATS-safe (no tables or text boxes) if the default layout was used
  - Contact details and links present
- Show 3 to 5 lines on what changed versus the old resume (for example "added numbers to 4 bullets", "grouped skills").
- Show **Trade-offs** for anything moved, dropped, merged or reworded to fit the template (for example "GitHub moved to Additional information", "second degree in the body text", "skill pills shortened"), so the user can undo any of them.
- Offer the next step: tailoring this resume to a specific job posting.

## Always
- The files, links and answers from this run come first. Anything known from memory or past chats can be offered, but say where it came from and only add it once the user confirms.
- Never invent experience, metrics, skills, titles or dates.
- The user reviews the final resume before using it.
- Keep it moving: each step's message is about 10 lines or less. Use cards for choices and keep the explanations short.