import re

completions = {
    'USA_continue_the_new_deal': '''
            add_political_power = 150
            add_popularity = { ideology = democratic popularity = 0.1 }
            custom_effect_tooltip = "Sets us firmly on the historical New Deal path."''',
    
    'USA_reestablish_the_gold_standard': '''
            add_political_power = 120
            add_popularity = { ideology = neutrality popularity = 0.1 }
            custom_effect_tooltip = "Sets us on the Conservative / Alt-History path."''',
            
    'USA_america_first': '''
            add_political_power = 120
            add_popularity = { ideology = fascism popularity = 0.1 }
            custom_effect_tooltip = "Initiates the Silver Shirt mobilization."''',
            
    'USA_suspend_the_persecution': '''
            add_political_power = 120
            add_popularity = { ideology = communism popularity = 0.1 }
            custom_effect_tooltip = "Embraces Communist ideologies."''',
            
    'USA_wpa': '''
            add_political_power = 50
            random_owned_controlled_state = {
                limit = { free_building_slots = { building = industrial_complex size > 0 } }
                add_building_construction = { type = industrial_complex level = 2 instant_build = yes }
            }''',
            
    'USA_war_department_expansion': '''
            add_political_power = 50
            add_army_experience = 20
            random_owned_controlled_state = {
                limit = { free_building_slots = { building = arms_factory size > 0 } }
                add_building_construction = { type = arms_factory level = 2 instant_build = yes }
            }''',
            
    'USA_neutrality_act': '''
            add_political_power = 120
            add_ideas = neutrality_idea
            custom_effect_tooltip = "Strengthens our neutrality."''',
            
    'USA_limited_intervention': '''
            add_political_power = 120
            add_named_threat = { threat = 5 name = USA_limited_intervention }
            custom_effect_tooltip = "We will intervene where necessary."''',
            
    'USA_war_production_board': '''
            add_political_power = 50
            add_ideas = USA_war_production_board
            custom_effect_tooltip = "Greatly increases production efficiency."''',
            
    'USA_selective_service_act': '''
            add_political_power = 50
            add_ideas = USA_selective_service_idea
            custom_effect_tooltip = "Increases our available manpower."''',
            
    'USA_arsenal_of_democracy': '''
            add_political_power = 150
            add_ideas = USA_arsenal_of_democracy
            custom_effect_tooltip = "We are the Arsenal of Democracy!"''',
            
    'USA_the_giant_wakes': '''
            add_political_power = 150
            remove_ideas = USA_great_depression
            custom_effect_tooltip = "The Great Depression is finally over."''',
            
    'USA_destroyers_for_bases': '''
            add_political_power = 50
            if = {
                limit = { ENG = { exists = yes } }
                ENG = { add_equipment_to_stockpile = { type = convoy amount = 50 } }
            }
            custom_effect_tooltip = "We send older ships in exchange for base rights."''',
            
    'USA_lend_lease_act': '''
            add_political_power = 100
            custom_effect_tooltip = "Unlocks major lend-lease decisions."''',
            
    'USA_war_plan_black': '''
            add_political_power = 50
            create_wargoal = { type = puppet_wargoal target = GER }
            custom_effect_tooltip = "Prepare for war against Germany."''',
            
    'USA_war_plan_orange': '''
            add_political_power = 50
            create_wargoal = { type = puppet_wargoal target = JAP }
            custom_effect_tooltip = "Prepare for war against Japan."''',
            
    'USA_the_united_nations': '''
            add_political_power = 200
            custom_effect_tooltip = "Spearheads the creation of the United Nations."''',
            
    'USA_america_first_committee': '''
            add_political_power = 100
            add_popularity = { ideology = neutrality popularity = 0.1 }''',
            
    'USA_deregulate_industry': '''
            random_owned_controlled_state = {
                limit = { free_building_slots = { building = industrial_complex size > 0 } }
                add_building_construction = { type = industrial_complex level = 3 instant_build = yes }
            }''',
            
    'USA_expand_the_national_guard': '''
            add_army_experience = 50
            custom_effect_tooltip = "Expands stateside defense forces."''',
            
    'USA_the_american_caesar': '''
            add_political_power = 150
            set_politics = { ruling_party = neutrality elections_allowed = no }
            custom_effect_tooltip = "MacArthur becomes the strongman of America."''',
            
    'USA_the_macarthur_dictatorship': '''
            add_political_power = 200
            add_popularity = { ideology = neutrality popularity = 0.2 }
            custom_effect_tooltip = "Full dictatorial powers to MacArthur."''',
            
    'USA_military_governorates': '''
            add_political_power = 100
            add_ideas = USA_military_governorates
            custom_effect_tooltip = "Enforces stability through military rule."''',
            
    'USA_imperial_presidency': '''
            add_political_power = 150
            custom_effect_tooltip = "Solidifies the Imperial Presidency."''',
            
    'USA_the_new_american_empire': '''
            add_political_power = 200
            custom_effect_tooltip = "A new empire rises in the Americas."''',
            
    'USA_subjugate_canada': '''
            create_wargoal = { type = puppet_wargoal target = CAN }''',
            
    'USA_secure_the_pacific': '''
            create_wargoal = { type = puppet_wargoal target = JAP }''',
            
    'USA_an_american_cincinnatus': '''
            add_political_power = 150
            set_politics = { ruling_party = democratic elections_allowed = yes }
            custom_effect_tooltip = "MacArthur steps down, restoring democracy."''',
            
    'USA_neutrality_to_the_end': '''
            add_political_power = 150
            add_ideas = USA_strict_neutrality
            custom_effect_tooltip = "We shall remain isolated permanently."''',
            
    'USA_fortify_the_coasts': '''
            random_owned_controlled_state = {
                limit = { is_coastal = yes }
                add_building_construction = { type = coastal_bunker level = 2 instant_build = yes }
            }''',
            
    'USA_hemispheric_defense': '''
            add_political_power = 100
            custom_effect_tooltip = "Guarantees all neutral nations in the Americas."''',
            
    'USA_the_monroe_doctrine_enforced': '''
            create_wargoal = { type = puppet_wargoal target = MEX }
            custom_effect_tooltip = "Enforce the Monroe Doctrine by force if needed."''',
            
    'USA_intervene_in_mexico': '''
            create_wargoal = { type = puppet_wargoal target = MEX }''',
            
    'USA_fortress_america': '''
            add_political_power = 150
            add_ideas = USA_fortress_america''',
            
    'USA_paramilitary_training': '''
            add_army_experience = 50
            add_popularity = { ideology = fascism popularity = 0.1 }''',
            
    'USA_corporate_statism': '''
            random_owned_controlled_state = {
                limit = { free_building_slots = { building = industrial_complex size > 0 } }
                add_building_construction = { type = industrial_complex level = 3 instant_build = yes }
            }''',
            
    'USA_ally_with_the_silver_shirts': '''
            add_political_power = 100
            add_popularity = { ideology = fascism popularity = 0.15 }''',
            
    'USA_honor_the_confederacy': '''
            add_political_power = 120
            custom_effect_tooltip = "We look to our past for strength."''',
            
    'USA_the_national_defense_state': '''
            set_rule = { can_declare_war_without_wargoal_when_in_war = yes }
            custom_effect_tooltip = "The State is organized completely around national defense."''',
            
    'USA_voter_registration_act': '''
            add_political_power = 100
            add_popularity = { ideology = fascism popularity = 0.2 }''',
            
    'USA_the_fascist_menace': '''
            set_politics = { ruling_party = fascism elections_allowed = no }
            custom_effect_tooltip = "Fascism officially takes control of the US."''',
            
    'USA_manifest_destiny_realized': '''
            add_political_power = 200
            create_wargoal = { type = annex_everything target = MEX }
            create_wargoal = { type = annex_everything target = CAN }''',
            
    'USA_the_asian_threat': '''
            create_wargoal = { type = puppet_wargoal target = JAP }''',
            
    'USA_the_european_allies': '''
            add_political_power = 100
            custom_effect_tooltip = "Allying with the old empires of Europe."''',
            
    'USA_worker_cooperatives': '''
            add_political_power = 50
            add_popularity = { ideology = communism popularity = 0.1 }
            random_owned_controlled_state = {
                limit = { free_building_slots = { building = industrial_complex size > 0 } }
                add_building_construction = { type = industrial_complex level = 2 instant_build = yes }
            }''',
            
    'USA_the_red_army_of_america': '''
            add_army_experience = 50
            add_popularity = { ideology = communism popularity = 0.1 }''',
            
    'USA_unholy_alliance': '''
            add_political_power = 100
            add_popularity = { ideology = communism popularity = 0.15 }''',
            
    'USA_democratic_socialism': '''
            add_political_power = 150
            add_popularity = { ideology = communism popularity = 0.2 }''',
            
    'USA_the_dictatorship_of_the_proletariat': '''
            set_politics = { ruling_party = communism elections_allowed = no }
            custom_effect_tooltip = "The Proletariat assumes full control."''',
            
    'USA_marxist_leninism': '''
            add_political_power = 100
            add_popularity = { ideology = communism popularity = 0.15 }
            custom_effect_tooltip = "Align ourselves fully with Moscow."''',
            
    'USA_the_peoples_republic': '''
            set_politics = { ruling_party = communism elections_allowed = no }
            custom_effect_tooltip = "The Republic falls, the People's Republic rises."''',
            
    'USA_american_socialism': '''
            add_political_power = 100
            add_popularity = { ideology = communism popularity = 0.15 }
            custom_effect_tooltip = "Develop socialism suited for American realities."''',
            
    'USA_shatter_the_empires': '''
            create_wargoal = { type = puppet_wargoal target = ENG }
            create_wargoal = { type = puppet_wargoal target = FRA }''',
            
    'USA_liberate_the_americas': '''
            custom_effect_tooltip = "Brings revolution to all American nations."''',
            
    'USA_the_grand_revolution': '''
            add_political_power = 300
            custom_effect_tooltip = "A global communist revolution!"'''
}

file_path = "c:/Users/Sean/Documents/Code_Projects/Hoi4 Mods/Stakuyi's Alt History/common/national_focus/usa.txt"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

def inject_rewards(c: str, d: dict[str, str]) -> str:
    parts: list[str] = c.split("focus = {")
    new_parts: list[str] = [parts[0]] # header
    
    count = 0
    for part in parts[1:]:
        m_id = re.search(r"^\s*id\s*=\s*(USA_[a_zA-Z0-9_]+)", part, re.MULTILINE)
        if m_id:
            fid = m_id.group(1)
            if fid in d:
                def repl(m_reward: re.Match[str]) -> str:
                    return "completion_reward = {" + d[fid] + "\n        }"
                part = re.sub(r"completion_reward\s*=\s*\{.*?\}", repl, part, count=1, flags=re.DOTALL)
                count += 1
        new_parts.append(part)
        
    print(f"Modified {count} focuses.")
    return "focus = {".join(new_parts)

new_content = inject_rewards(content, completions)
with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)
