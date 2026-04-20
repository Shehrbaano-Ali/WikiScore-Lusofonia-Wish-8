# Shehrbano Ali - WikiScore-Lusofonia (Wish #8)

**Name:** Shehrbano Ali  
**Email:** shehrbanoali2230@gmail.com  
**Github:** [Shehrbaano-Ali](https://github.com/Shehrbaano-Ali/)  
**Program:** Outreachy 2026 Cohort  
**Project:** Addressing the Lusophone technological wishlist proposals  
**Date:** April 19th, 2026  
**Wish #8:** [Proposta para a Lista de Desejos nº 8 - Criar uma ferramenta para contar as edições do Wikidata em português](https://meta.wikimedia.org/wiki/Lista_de_desejos_tecnol%C3%B3gicos_da_lusofonia/2025/Propostas/Ferramenta_de_pontua%C3%A7%C3%A3o_para_edi%C3%A7%C3%B5es_no_Wikidata)


---
## LINK

### 🌐 [Click here to view the Live WikiScore](https://shehrbaano-ali.github.io/WikiScore-Lusofonia-Wish-8/)

---
## 📸 Visual Overview

### 1. Visual representation of Wikiscore (Laptop View 💻)

![View](my-prototype.png)


### 2. Phone View 📱
![View](my-prototype-mobile.png)


---
## Table of Contents

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Three Super Visual Features](#three-super-visual-features)
- [Technical Steps & Implementation](#technical-steps--implementation)
- [📱Mobile Adaptation & UX Polishing](#mobile-adaptation--ux-polishing)
- [API & Retrieval (RAG Principles)](#api--retrieval-rag-principles)
- [Speed & Traffic Control (Parallel Processing)](#speed--traffic-control-parallel-processing)
- [The Professional Organizer Tools](#the-professional-organizer-tools)
- [Python & Django Logic](#python--django-logic)
- [Note](#note)
- [Repository Structure](#repository-structure)
- [AI Usage](#ai-usage)
---
## Introduction
I built WikiScore-Lusofonia to address a major gap in how the Portuguese-speaking community tracks Wikidata contributions. Current methods were less systematic; organizers needed a tool that was fast, precise, and focused on language-specific effort.

I built this prototype from scratch to be a full-stack answer. It features a real-time JavaScript terminal for organizers and a Python/Django backend for the official Wikimedia servers.


---
## Objectives
1. The *Precision model* automatically identifies and scores Portuguese edits `(|pt)`.  
2. Use a `Bot-Shield` and `Revert-Validator` to ensure only authentic work counts.  
3. For *High Performance* use parallel processing to scan 100+ participants in seconds.  
4. For *Permanent Storage* use SQL-based models so contest data is never lost.  
5. For the *Healthy Competition* use a badge-based ranking system.
6. I didn’t just look for Portuguese. I made sure the engine catches Brazilian editors too `(pt-br)`.
   No one in the Lusophone family gets left behind.
7. Built a *Strict Mode* that only counts edits on the official contest list. If participant is editing random stuff just to farm points, the engine ignores it.
8. By using Infinite Pagination, my engine keeps flipping the page until it fetches every single edit, even if a user has thousands of contributions.

---

## Three Super Visual Features  
1. The terminal identifies Continental vs. Brazilian edits instantly. It’s not just a counter; it’s culturally aware.
2. The Strict-Mode 🔴 is enabled that is a real-time visual Anti-Cheat indicator, ensuring only mission critical items are being processed by the engine.
3. I added a *LAST_TRACKED QID* for every participant. Organizers shouldn't have to guess where points come from;
   they can now tap the specific Item ID `(like Q1622272)` to see the exact Wikidata page being improved. 

---
## Technical Steps & Implementation

To ensure the engine is both fair and precise, I have implemented a weighted scoring algorithm:  

### $$\text{Total Score} = \sum (\text{Labels} \times w_L) + (\text{Desc} \times w_D) + (\text{Facts} \times w_F) + (\text{Ref} \times w_R) + (\text{Img} \times w_I)$$  

This allows the community to prioritize high-value edits (like References, labels, images etc) while still rewarding all forms of contribution.

**1. The SQL and Newcomers:**  
**i.** In my code, this is handled by models.py. For people new to coding, data usually disappears when you refresh a page. I used Django Models to create a permanent SQL Database. This means when a new person joins a contest, their name and points are saved forever on the server, not just for one session.  

**ii.** I used BigIntegerField for IDs. Wikidata is massive, and using normal numbers eventually crashes the database.

**2. The Proxy:**  
I used const PROXY = `*https://corsproxy.io/?*`;. Sometimes websites block outside code from talking to them. I used this CORS Proxy to act as a middleman so my app can talk to Wikidata smoothly without any blockages.

**3. Time/Dates:**  
I didn't just hardcode a single date. I built a Time Machine feature using dateRange and updateDates(). Organizers can pick exactly when a contest starts and ends using the date inputs in the header, and the engine will only count edits from that specific time.

**4. The Point Breakdown:**  
I broke down a user's work into 5 specific categories: `*Labels (L), Descriptions (D), Facts (F), References (R), and Images (I)*`. Every time a user makes an edit, the engine identifies exactly what they did and gives them the right amount of points based on my custom weights.  

**5. Healthy Competition *(Badges):***  
I used badgeRules and renderLegend to create a *Ranking System* from `Level 1 to Level 6`. These aren't just pictures; I created these badges to make editors feel like they are leveling up in a game. It turns a boring task into a fun, healthy competition.  
A contributor can edit 1,000 global items, but you only *Level Up* their badges by doing Portuguese-specific work. It keeps the focus on the mission.


---

## 📱Mobile Adaptation & UX Polishing
A professional tool must be accessible. I implemented specific mobile-first logic to ensure the terminal remains functional on small screens:  

1. Implemented a swipeable table logic that keeps the data-heavy leaderboard readable on mobile without squishing columns.
2. I created a *Swipe to see scores* hint that only appears on mobile.
3. Since mobile devices lack hover states, I built a custom `showNameTooltip` function. When a truncated username is tapped, a subtle terminal-style popup appears to show the full ID before fading away.
4. Utilized Tailwind md: prefixes to ensure the layout snaps from a tight mobile view to a wide, balanced desktop sequence automatically.

---
## API & Retrieval (RAG Principles)
In my code, this lives in `harvestData` and `fetchScore`. I used the core principles of Data Retrieval that is the same logic used in RAG (Retrieval-Augmented Generation) systems to build a high performance API engine that pulls authentic data from Wikidata.  
My app *retrieves* raw, authentic data directly from the Wikidata API, behaving like a specialized search engine that only looks for contest data.

---
## Speed & Traffic Control (Parallel Processing)
Scanning 100 users one by one takes forever. I set the `CONCURRENCY_LIMIT = 20 `. This means the app scans 20 users at the same time. To prevent traffic jams (crashing the API), I added **throttling** so it only handles a safe amount of data at once.  
Every new edit found will show up in the frontend in real-time.


---
## The Professional Organizer Tools  

I added three critical tools that make this a professional system for organizers:

**1.** A button *Export to CSV* turns the leaderboard into a file so organizers can report results to the Wikimedia Foundation easily.  
**2.** A *Bot-Shield* is a security guard that checks `e.hasOwnProperty('bot')` and ignores automated edits to keep the data authentic.  
**3.** A *Disqualify* (🚫) button. If someone is cheating, the organizer can *gray them out* and remove their points with one click.  
**4.** I added direct links to the raw data. If an organizer wants to check a score, they can touch the chain icon and see the user's actual Wikidata contributions instantly.

---

## Python & Django Logic

I designed the backend logic to integrate seamlessly into the existing WikiScore environment without requiring structural rewrites.

1. **`models.py`:** Unlike generic implementations, I used `BigIntegerField` for revision IDs to prevent system crashes as Wikidata grows.
   It includes an **Audit Trail** (storing the raw `comment`) and **Item Tracking** (storing the specific `QID`), ensuring 100% transparency if a score is disputed.
3. **`logic.py`:** Packaged as a standard **Django Management Command**. It can be added to the existing `update.py` pipeline with a single line. 
4. Specifically for Wish #8, my regex engine `r'\|pt(-br)?'` is designed to detect both **Portuguese (pt)** and **Brazilian Portuguese (pt-br)** edits. This ensures no Lusophone editor is left behind.
5. I implemented a `WikidataPointRule` model and contest-level switches (`wikidata_enabled`, `wikidata_exclude_bots`, `wikidata_linked_only`) so organizers can customize the strictness of the contest from the Django Admin panel.
6. Once stored, points are added to the grand total via a one-line update to the `CounterHandler` method:
   `wikidata_points = sum(edit.points for edit in WikidataContribution.objects.filter(participant=user, is_portuguese=True))`
7. My regex `r'\|pt(-br)?'` is specifically tuned for **Wish #8**. It’s the difference between a generic tool and a community tool.
8. I added a `timeout=10` and `on_delete` protection. The engine is designed to be stable, resilient, and won't hang the server if the API is slow.
9. I have optimized the scoring logic so it can be called directly by the existing CounterHandler.get_points() method.
   This ensures that the new Wikidata points are injected into the leaderboard calculation without requiring any structural changes to the existing frontend

```
Question:
How do we integrate this into the existing system?

Answer:
1. Because `logic.py` is built as a standard Django Management Command,
   maintainers can plug it directly into the current update pipeline.

2. Maintainers can simply add `load_wikidata` to the existing steps list in the `update.py` pipeline
   (running alongside load_edits and load_reverts).
3. The engine will automatically detect active contests, filter out bot traffic, and log the scores into the `WikidataContribution` vault.
4. This setup allows the system to wake up, sync, and update the database in the background without affecting user experience.

```
---

## Note
*Organizers can make the competition tough by changing the points on badges in the UI, because I made the system fully editable.*  

`This system is ready for live use. I designed the code to fit directly into the WikiScore main branch to provide a reliable base for all future Portuguese Wikidata contests.  
In the future, I would appreciate more direct access to the Outreachy Dashboard systems so I can build tools that run even smoother.`

---

## Repository Structure
```
WikiScore-Lusofonia-Wish-8/
│
├── django-logic/      # Backend Python & Django files
    ├── models.py      # SQL Database Structure
│   └── logic.py       # Python Scoring Engine
├── LICENSE            # MIT License 
├── README.md          # Technical documentation (this file)
├── app.js             # Core scoring engine & API integration
├── badge_50.jpg       # Achievement asset: Level 1 
├── badge_200.jpg      # Achievement asset: Level 2
├── badge_500.jpg      # Achievement asset: Level 3 
├── badge_1000.png     # Achievement asset: Level 4  
├── badge_2000.png     # Achievement asset: Level 5 
├── badge_3000.png     # Achievement asset: Level 6
├── index.html         # Terminal UI structure & Organizer dashboard
├── my-prototype.png   # Full visual preview of the tool on laptop
├── my-prototype-mobile.png   # Full visual preview of the tool on Phone
└── style.css          # Terminal aesthetic, animations & neon styling
```

---
## AI Usage
I utilized Gemini for:
* Organizing this README to reflect my scratch to the end analysis.
* Working through responsive CSS edge cases to ensure the sequence remained perfect on both laptop and mobile.

All code, logic (PT vs GL split), and the Cache Buster fix were manually verified and implemented by me. I want to allow myself smooth reach to the Outreachy dashboard for my future work without any blockage.

---

*Here is the link to my _**[Blog](https://shehrbanoali66.hashnode.dev/post-contribution-task-creating-a-live-data-safe-tool-for-the-lusophone-wishlist-8)**_*  
*This work is submitted for the Outreachy 2026 internship application for the Wikimedia Project.*  
*~Shehrbano Ali*
