# Playtesting Guide: Stakuyi's Alt History Mod

Thank you for playtesting! This mod completely rebuilds the AI weights, tension curves, and late-game performance guardrails of Hearts of Iron IV to create highly dynamic alternate history campaigns.

Because the mod heavily relies on invisible event-driven architecture, we need you to look for specific "Engine Failures" rather than general balance issues. Please read the guidelines below before booting up your test campaign.

---

## 🔍 What to Keep an Eye On

### 1. "Ping-Ponging" AI
**The Issue:** We tied AI focus tree weights to dynamic triggers (neighbor ideologies, world tension). The engine might struggle to calculate these.
**What to look for:** Does the AI start a 70-day focus, cancel it halfway through, and immediately start a different one, only to restart the first one a week later? If AI nations are forever stuck at 0 political power because they keep swapping focuses, note down the specific nation and the year.

### 2. "Forever Wars" and Faction Bloat
**The Issue:** Vanilla HOI4 lets minor nations join major wars by simply creating a faction. 
**What to look for:** Please check the peace conference menus. Does a massive war finish in 1941, but the peace conference *never* fires because a completely unreachable minor nation (e.g., El Salvador or Tibet) joined the opposing faction across the globe?

### 3. State-Lock Errors (Missing Bypasses)
**The Issue:** The new custom focus trees rely heavily on state-control prerequisites. 
**What to look for:** If you manually conquer a state (e.g., taking Ottawa in the new Fascist US tree), does the focus tree physically lock you out of progressing because an event broke, or does the focus safely allow you to "Bypass" it?

### 4. The 1942 Performance Wall
**The Issue:** We built a custom "Late Game Performance Caps" toggle in the Game Setup Rules that lobotomizes AI minor states from spamming divisions.
**What to look for:** Please enable the Performance Rule in the lobby and play your campaign until at least **1942**. Report the hourly stutter rate. If it's still lagging terribly, we will need to increase the Soft-Cap penalties.

---

## 📋 The Standardized Bug Report Template
If you encounter a bug, **do not just describe it broadly in chat**. Use the exact template below. 

*We cannot track down nested logic loops without a Save File and the game's Error Log!*

***
### 🐛 Bug Report

**Short Title:** [e.g., USA AI stuck on missing focus / Imperial Collapse broke the conference]

**Bug Category:** 
- [ ] Focus Tree Logic
- [ ] AI Diplomatic Behavior
- [ ] World-Song Tension System
- [ ] Game Rules / Shattered Timeline
- [ ] Crash to Desktop (CTD) 

**Context:**
- **Nation Played:** 
- **In-Game Date when bug occurred:** 
- **Relevant Custom Game Rules Set:** *(e.g., Set UK to Communist, Forced Historical)*
- **Other Mods Enabled:** *(Please test with ONLY this mod enabled!)*

**Description of the Issue:**
*[Example: "I capitulated France in 1940. The 45-day delay event fired, but instead of releasing West Africa as a single puppet, it released them as independent and instantly put them in a war against me."]*

**Steps to Reproduce:**
1. [e.g., Start game as GER]
2. [e.g., Defeat FRA but do not annex WAF in the conference]
3. [e.g., Wait 45 days for Event ID SAH_timeline.2 to fire]
4. [e.g., Observe the error]

**Mandatory Attachments:**
- [ ] Screenshot of the issue
- [ ] **Save File** *(from right before the bug happens)*
- [ ] **Error.log** *(Found in Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log)*
***
