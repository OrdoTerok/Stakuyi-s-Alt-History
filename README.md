# Stakuyi's Alt History  HOI4 Mod

A Hearts of Iron IV mod for YouTuber **Stakuyi** that lets him explore alternate history paths voted on by his community. 
**Current Version:** 0.6.3

---

## Mod Framework

This mod is built on a robust, heavily automated framework designed to handle deep alt-history configurations and maintain performance over long campaigns without breaking the Clausewitz engine.

### Python Automation Pipeline
Managing over 150 political paths across 50 nations manually is impossible. We use a suite of Python scripts to automate mod generation:
*   **scenario_automator.py & inject_all_nations.py**: These scripts generate the 50-nation arrays and write the output payloads directly into the Custom Game Rules files, initialization events, and localisation grids. This is what populates the massive Pre-Game Lobby.
*   **inject_bypasses.py**: This script reads the generated focus logic, utilizes an AST bracket-matcher, and dynamically injects bypass blocks precisely into the correct focus nodes across vanilla and modded focus trees.
*   **mod_validator.py**: An offline syntax checker that ensures no brackets or scopes are left opened or unclosed after the automated injections.

### Dynamic Day-1 Bypasses
Rather than relying on the AI to slowly stumble its way down an alternate history path over months or years, the Python automation ensures that **Day 1 bypasses are dynamically injected** into focus trees. When the game loads, the chosen paths are instantly pre-completed, seamlessly pushing nations into their new ideological states on exactly January 1, 1936.

### Custom Game Rules Lobby Generation
The Custom Game Rules lobby is automatically populated with 50-nation arrays by the automation scripts. Every major and minor nation has its specific political and diplomatic starting conditions mapped into the lobby, allowing perfectly tailored scenarios.

### Structural Modding & Performance
To keep the game running smoothly in the late game:
*   **on_actions over Weekly Pulses**: We have completely replaced constant, lag-inducing weekly pulses with optimized on_actions triggers for events and state checks.
*   **Performance Guardrails**: Aggressive late-game unit limits are enforced to prevent division spam.
*   **AI Strategy Plans**: Custom AI strategy plans (SAH_major_custom.txt, etc.) prioritize functional, coherent gameplay over spamming minor generic divisions into eternity.

---

## Mod Features

Once the framework spins up the scenario, players experience a completely reinvented alternate history playground right from Day 1.

### The 50-Nation Automated Pre-Game Lobby
Before you even unpause the game, the Custom Game Rules lobby features over **150 political paths** across **50 Major and Minor nations**. You can select exact political starts (e.g., American Caesar, Trotskyist USSR, French Legitimist) and watch the world instantly conform to your chosen scenario.

### The "Rebuilding State" Tier System
When forcing alternative regimes on Day 1, vanilla HOI4 would normally plunge 10+ nations into immediate Civil Wars. To preserve sanity and lore, the mod **suppresses Day-1 Civil Wars** entirely. Instead, nations diverging from their historical paths begin 1936 burdened by the **Rebuilding State** mechanic:
*   **Tier 1 (Devastating Recovery):** Massive economic, political power, and military training debuffs. Used for regimes that violently changed just prior to 1936.
*   **Tier 2 (Prolonged Rebuilding):** Medium debuffs for nations that experienced upheaval 3-6 years ago.
*   **Tier 3 (Stabilized Regime):** Minor political gridlock for nations that flipped 10+ years ago (e.g., Trotsky taking power in 1924).
*   **Decision Sinks:** Players and AI must actively spend Political Power and time to transition their nations through these tiers and fully stabilize their regimes.

### "Global Escalation" Tension & Imperial Collapse
The mod introduces advanced, dynamic threat and reaction systems:
*   **Global Escalation System:** Dynamic threat and tension checks that react to global events, ideological shifts, and wars in real-time.
*   **Imperial Collapse:** Empires won't hold onto vast swathes of resistant territory post-capitulation. Peace treaties and the survival of empires are constantly re-evaluated, shattering massive unsustainable empires into more manageable, fractured states.

---

## Roadmap

### Phase 1: Foundation (Completed)
*   **Python Automation Pipeline**: Infrastructure for generating Custom Game Rules and injecting code dynamically.
*   **Dynamic Day-1 Bypasses**: Bypassing vanilla focus tree limitations seamlessly on January 1, 1936.
*   **50-Nation Automated Pre-Game Lobby**: Pre-game configuration across a massive amount of paths.
*   **"Rebuilding State" Tier System**: Suppressing civil wars and managing Tiers 1-3 with extensive PP decision sinks.
*   **Performance Enhancements**: Optimized on_actions and late-game unit limits.

### Phase 2: Refinement & Expansion (Current Focus)
*   **Alternate 1939 Start Work**: Generating custom OOBs and automating unit spawning for alternate history 1939 start scenarios (via generate_1939_units.py and SAH_1939_units.txt).
*   **AI Strategy Overhauls**: Expanding custom AI strategy plans for all 50 nations so they navigate alt-history scenarios logically.
*   **Balancing the Rebuilding State**: Fine-tuning the political power sinks and modifier debuffs across different tiers and ideologies.
*   **"Global Escalation" Tension & Imperial Collapse**: Active development of dynamic threat mechanics and post-capitulation empire shattering.
*   **DLC Compatibility Updates**: Ensuring bypass injections work flawlessly with the latest vanilla DLC focus tree additions.

### Phase 3: Future Horizons (Planned)
*   **Custom Interface Integration**: Designing dedicated GUIs for the Global Escalation system and Rebuilding states.
*   **Dynamic Focus Tree Generation**: Moving beyond bypasses to modularly assemble focus trees based on Lobby selections.
*   **Expanded Minor Nation Content**: Deeper alt-history paths for Central and South American nations.

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

If you modify or expand focus trees in common/national_focus/, you must re-run the Python automation scripts to ensure the Lobby Rules and Bypasses stay perfectly synced with the Framework.

1. **python inject_all_nations.py / python scenario_automator.py**: Regenerates the 50-nation arrays and writes the output payload into the custom rules files, init events, and localisation.
2. **python inject_bypasses.py**: Reads the generated focus logic and uses the AST bracket-matcher to carefully sneak bypass blocks into the target files.
3. **python mod_validator.py**: Run this to ensure no brackets or scopes are left unclosed after your changes.

---

## Credits

- **Mod design & scripting**: OrdoTerok
- **HOI4 version target**: 1.14.x
