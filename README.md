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

### 🌐 [Click here to view the Live WikiScore](https://shehrbaano-ali.github.io/WikiScore-Lusofonia-Wish-8-/)

---
## 📸 Visual Overview

### 1. Visual representation of my prototype

![View](my-prototype.png)


---
## Table of Contents

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Technical Steps & Implementation](#technical-steps--implementation)
- [API & Retrieval (RAG Principles)](#api--retrieval-rag-principles)
- [Speed & Traffic Control (Parallel Processing)](#speed--traffic-control-parallel-processing)
- [The Professional Organizer Tools](#the-professional-organizer-tools)
- [Python & Django Logic](#python--django-logic)
- [AI Usage](#ai-usage)
---
## Introduction
I built WikiScore-Lusofonia to address a major gap in how the Portuguese-speaking community tracks Wikidata contributions. Current methods were less systematic; organizers needed a tool that was fast, precise, and focused on language-specific effort.

I built this prototype from scratch to be a full-stack answer. It features a real-time JavaScript terminal for organizers and a Python/Django backend for the official Wikimedia servers.


---
## Objectives
**1. Linguistic Precision:** Automatically identify and score Portuguese edits `(|pt)`.  
**2. Data Integrity:** Use a Bot-Shield and Revert-Validator to ensure only authentic work counts.  
**3. High Performance:** Use parallel processing to scan 100+ participants in seconds.  
**4. Permanent Storage:** Use SQL-based models so contest data is never lost.  
**5. Community Engagement:** Use a badge-based ranking system for healthy competition.

---
## Technical Steps & Implementation
**1. The SQL and Newcomers:**
In my code, this is handled by models.py. For people new to coding, data usually disappears when you refresh a page. I used Django Models to create a permanent SQL Database. This means when a new person joins a contest, their name and points are saved forever on the server, not just for one session.

**2. The Proxy:**
I used const PROXY = `*https://corsproxy.io/?*`;. Sometimes websites block outside code from talking to them. I used this CORS Proxy to act as a middleman so my app can talk to Wikidata smoothly without any blockages.

**3. Time/Dates:**
I didn't just hardcode a single date. I built a Time Machine feature using dateRange and updateDates(). Organizers can pick exactly when a contest starts and ends using the date inputs in the header, and the engine will only count edits from that specific time.

**4. The Point Breakdown:**
I broke down a user's work into 5 specific categories: `*Labels (L), Descriptions (D), Facts (F), References (R), and Images (I)*`. Every time a user makes an edit, the engine identifies exactly what they did and gives them the right amount of points based on my custom weights.

**5. Healthy Competition *(Badges):***
I used badgeRules and renderLegend to create a *Ranking System* from `Level 1 to Level 6`. These aren't just pictures; I created these badges to make editors feel like they are leveling up in a game. It turns a boring task into a fun, healthy competition.

---
## API & Retrieval (RAG Principles)
In my code, this lives in `harvestData` and `fetchScore`. I used the core principles of Data Retrieval that is the same logic used in RAG (Retrieval-Augmented Generation) systems to build a high performance API engine that pulls authentic data from Wikidata. My app *retrieves* raw, authentic data directly from the Wikidata API, behaving like a specialized search engine that only looks for contest data.

---
## Speed & Traffic Control (Parallel Processing)
Scanning 100 users one by one takes forever. I set the `CONCURRENCY_LIMIT = 20 `. This means the app scans 20 users at the same time. To prevent traffic jams (crashing the API), I added **throttling** so it only handles a safe amount of data at once. Every new edit found will show up in the frontend in real-time.


---
## The Professional Organizer Tools  

I added three critical tools that make this a professional system for organizers:

**1. Export to CSV:** A button that turns the leaderboard into a file so organizers can report results to the Wikimedia Foundation easily.  
**2. Bot-Shield:** A Security Guard that checks `e.hasOwnProperty('bot')` and ignores automated edits to keep the data authentic.  
**3. Organizer's Veto:** A *Disqualify* (🚫) button. If someone is cheating, the organizer can *gray them out* and remove their points with one click.  
**4. Transparency:** I added direct links to the raw data. If an organizer wants to check a score, they can touch the chain icon and see the user's actual Wikidata contributions instantly.

---

## Python & Django Logic

I provided two extra files to make sure this integrates into the real WikiScore environment:

`1. models.py:` The database architecture that creates the permanent table for scores.

`2. logic.py:` The Invisible Worker that runs on the server. It does the exact same math as my `app.js` but in Python, including my PT-Filter and point weights.

---

## Note
*Organizers can make the competition tough by changing the points on badges in the UI, because I made the system fully editable.*  
`I hope this prototype demonstrates my technical potential. I would appreciate more direct access to the Outreachy Dashboard systems in the future so I can build tools that run even smoother, without any API or caching blockages.`

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
├── my-prototype.png   # Full visual preview of the tool
└── style.css          # Terminal aesthetic, animations & neon styling
```

---
## AI Usage
I utilized Gemini for:
* **Documentation Structure:** Organizing this README to reflect the scratch to the end analysis.

All code, logic (PT vs GL split), and the Cache Buster fix were manually verified and implemented by me. I want to allow myself smooth reach to the Outreachy dashboard for my future work without any blockage.

---

*Here is the link to my _**[Blog]()**_*  
*This work is submitted for the Outreachy 2026 internship application for the Wikimedia Project.*  
*~Shehrbano Ali*
