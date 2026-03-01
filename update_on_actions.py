new_on_actions = """

# ============================================================
# Diplomatic Reactive Scripting Hub
# ============================================================

# Fires when a country changes its ruling party/ideology.
on_ruling_party_change = {
    effect = {
        # ROOT = the country changing ideology
        SAH_reactive_ideology_change = yes
    }
}

# Fires when war is declared.
on_declare_war = {
    effect = {
        # ROOT = attacker
        # FROM = defender
        SAH_reactive_war_declaration = yes
    }
}

# Fires when a nation is puppeted
on_puppet_country = {
    effect = {
        # ROOT = The overlord.
        # FROM = The subject.
        SAH_reactive_puppeting = yes
    }
}

# Fires when a nation joins a faction
on_faction_joined = {
    effect = {
        # ROOT = country joining
        # FROM = faction leader
        SAH_reactive_faction_change = yes
    }
}
"""

with open("common/on_actions/SAH_on_actions.txt", "a", encoding="utf-8") as f:
    f.write(new_on_actions)

print("Updated SAH_on_actions.txt with Diplomatic hooks.")
