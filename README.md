# Stakuyi's Alt History  HOI4 Mod

A Hearts of Iron IV mod for YouTuber **Stakuyi** that lets him explore alternate history paths voted on by his community. 
**Current Version:** 0.1.0

---

## Mod Features & Framework

This mod completely reinvents how Alternate History playthroughs are configured by allowing players (and the AI) to start down deep alt-history focus branches right from **Day 1**, without relying on the AI to slowly stumble its way there.

### 1. The 50-Nation Automated Pre-Game Lobby
We mapped out over **150 political paths** across **50 Major and Minor nations** directly into the Custom Game Rules lobby. 
*   **What it does:** You can select exact political starts (e.g., American Caesar, Trotskyist USSR, French Legitimist) before the game even begins.
*   **Day 1 Bypasses:** The mod uses a Python compiler to automatically scan vanilla and modded focus trees and dynamically injects bypass blocks. When the game loads, the chosen paths are instantly pre-completed, seamlessly pushing nations into their new ideological states without breaking the Clausewitz engine.

### 2. The "Rebuilding State" Tier System
When forcing alternative regimes on Day 1, vanilla HOI4 would instantly plunge 10+ nations into immediate Civil Wars on January 1st. 
To preserve sanity and lore, the mod **suppresses Day-1 Civil Wars** entirely. Instead, if a nation diverges from its historical path, it begins the game burdened by the **Rebuilding State** mechanic. 
*   **Tier 1 (Devastating Recovery):** Massive economic, political power, and military training debuffs. Used for regimes that violently changed just prior to 1936.
*   **Tier 2 (Prolonged Rebuilding):** Medium debuffs for nations that experienced upheaval 3-6 years ago.
*   **Tier 3 (Stabilized Regime):** Minor political gridlock for nations that flipped 10+ years ago (e.g., Trotsky taking power in 1924).
*   **Decision Sinks:** Players and AI must spend Political Power and time to actively transition their nations through these tiers to fully stabilize their regime.

### 3. "World-Song" Tension & Imperial Collapse
*   **World-Song System:** Dynamic threat and tension checks that react to global events and wars via customized on_actions.
*   **Imperial Collapse Events:** Re-evaluating peace treaties and the survival of empires. Empires will shatter into more manageable states rather than holding onto vast swathes of resistant territory post-capitulation.

### 4. Performance Guardrails
*   Aggressive late-game unit limits. 
*   Custom AI strategy plans prioritize functional gameplay over spamming minor generic divisions into eternity. Replaced constant weekly pulses with optimized on_actions.

---

## Installation

1. Copy (or symlink) this entire folder into your HOI4 mod directory:
   \\\
   Documents\Paradox Interactive\Hearts of Iron IV\mod\
   \\\
2. Create a **launcher .mod file** alongside it (same mod\ folder, **not** inside this folder) with the following content, adjusting the path to match your system:
   \\\
   name="Stakuyi's Alt History"
   path="mod/Stakuyi's Alt History"
   \\\
3. Launch HOI4, open the **Mods** tab in the launcher, and enable **Stakuyi's Alt History**.

---

## Automation Scripts (For Contributors)

If you modify or expand focus trees in common/national_focus/, you must re-run the Python automation scripts to ensure the Lobby Rules and Bypasses stay perfectly synced.

1. **python inject_all_nations.py / scenario_automator.py:** Regenerates the 50-nation arrays and writes the output payload into the custom rules files, init events, and localisation.
2. **python inject_bypasses.py:** Reads the generated focus logic and uses an AST bracket-matcher to carefully sneak bypass blocks precisely into the correct focus nodes across all target files.
3. **python mod_validator.py:** An offline syntax checker to ensure no brackets or scopes are left opened/unclosed.

---

## Credits

- **Mod design & scripting**: OrdoTerok
- **HOI4 version target**: 1.14.x
