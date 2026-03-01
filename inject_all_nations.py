from typing import Dict, Any

extra_scenarios: Dict[str, Dict[str, Any]] = {
    'ARG': {
        'rule_name': 'SAH_arg_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'infamous_decade': {'target_focus': 'ARG_the_concordancia_government', 'name': 'Historical Argentina', 'desc': 'Provides the historical setup for Argentina.'},
            'radical_civic': {'target_focus': 'ARG_the_radical_civic_union', 'name': 'Radical Civic Union', 'desc': 'Brings the Radical Civic Union back to power.'},
            'peronist': {'target_focus': 'ARG_the_peronist_movement', 'name': 'Peronist Movement', 'desc': 'Sparks the Peronist movement.'}
        }
    },
    'AUS': {
        'rule_name': 'SAH_aus_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'fatherland_front': {'target_focus': 'AUS_the_fatherland_front', 'name': 'Historical Austria', 'desc': 'Austria maintains the Fatherland Front.'},
            'austrofascism': {'target_focus': 'AUS_austrofascism', 'name': 'Austrofascism', 'desc': 'Austria fully embraces Fascism.'},
            'social_democrats': {'target_focus': 'AUS_the_social_democrats', 'name': 'Social Democrats', 'desc': 'Austria aligns with democratic socialism.'}
        }
    },
    'BEL': {
        'rule_name': 'SAH_bel_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 1,
        'starts': {
            'catholic_bloc': {'target_focus': 'BEL_the_catholic_bloc', 'name': 'Historical Belgium', 'desc': 'Belgium continues with the Catholic Bloc.'},
            'liberal_party': {'target_focus': 'BEL_the_liberal_party', 'name': 'Liberal Party', 'desc': 'The Liberal Party takes control.'},
            'rexist_party': {'target_focus': 'BEL_the_rexist_party', 'name': 'Rexist Party (Fascist)', 'desc': 'Degrelle and the Rexists seize power.'}
        }
    },
    'BUL': {
        'rule_name': 'SAH_bul_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'tsars_dictatorship': {'target_focus': 'BUL_the_tsars_dictatorship', 'name': 'Historical Tsar', 'desc': 'The Tsar maintains his royal dictatorship.'},
            'zveno': {'target_focus': 'BUL_zveno', 'name': 'Zveno (Fascist)', 'desc': 'The militarist Zveno takes control.'},
            'fatherland_front': {'target_focus': 'BUL_the_fatherland_front', 'name': 'Fatherland Front (Communist)', 'desc': 'Bulgaria turns Communist.'}
        }
    },
    'CHI': {
        'rule_name': 'SAH_chi_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'historical': {'target_focus': 'CHI_three_principles_of_the_people', 'name': 'Historical China', 'desc': 'China follows the Three Principles.'},
            'welfare': {'target_focus': 'CHI_welfare', 'name': 'Welfare State', 'desc': 'China commits to social welfare.'}
        }
    },
    'CHL': {
        'rule_name': 'SAH_chl_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'popular_front': {'target_focus': 'CHL_the_popular_front', 'name': 'Popular Front (History)', 'desc': 'Chile follows the Popular Front.'},
            'nacistas': {'target_focus': 'CHL_the_nacistas', 'name': 'Nacistas (Fascist)', 'desc': 'The Nacistas assume control.'}
        }
    },
    'COG': {
        'rule_name': 'SAH_cog_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'force_publique': {'target_focus': 'COG_the_force_publique', 'name': 'Force Publique', 'desc': 'Congo relies on the Force Publique.'},
            'evolues': {'target_focus': 'COG_the_evolues', 'name': 'The Evolues', 'desc': 'Congo empowers the Evolues.'}
        }
    },
    'CZE': {
        'rule_name': 'SAH_cze_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'political_direction': {'target_focus': 'CZE_political_direction', 'name': 'Historical Czechoslovakia', 'desc': 'Czechoslovakia maneuvers politics.'},
            'fascist_direction': {'target_focus': 'CZE_fascist_direction', 'name': 'Fascist Direction', 'desc': 'Czechoslovakia turns fascist.'},
            'communist_direction': {'target_focus': 'CZE_communist_direction', 'name': 'Communist Direction', 'desc': 'Czechoslovakia turns communist.'}
        }
    },
    'DEN': {
        'rule_name': 'SAH_den_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'social_democrats': {'target_focus': 'DEN_the_social_democrats', 'name': 'Historical Denmark', 'desc': 'Denmark retains the Social Democrats.'},
            'conservative': {'target_focus': 'DEN_the_conservative_peoples_party', 'name': 'Conservative Party', 'desc': 'The Conservative party rules.'}
        }
    },
    'EGY': {
        'rule_name': 'SAH_egy_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'anglo_treaty': {'target_focus': 'EGY_the_anglo_egyptian_treaty', 'name': 'Historical Egypt', 'desc': 'Egypt proceeds with the Anglo-Egyptian treaty.'},
            'wafd_party': {'target_focus': 'EGY_the_wafd_party', 'name': 'Wafd Party', 'desc': 'Egypt embraces the Wafd Party.'}
        }
    },
    'EST': {
        'rule_name': 'SAH_est_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'era_of_silence': {'target_focus': 'EST_the_era_of_silence', 'name': 'Era of Silence', 'desc': 'Estonia maintains the Era of Silence.'},
            'vaps_movement': {'target_focus': 'EST_the_vaps_movement', 'name': 'Vaps Movement', 'desc': 'The Vaps Movement takes over.'}
        }
    },
    'ETH': {
        'rule_name': 'SAH_eth_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'emperor': {'target_focus': 'ETH_the_emperor', 'name': 'The Emperor', 'desc': 'Ethiopia rallies behind the Emperor.'}
        }
    },
    'FIN': {
        'rule_name': 'SAH_fin_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'finnish_model': {'target_focus': 'FIN_the_finnish_model', 'name': 'Historical Finland', 'desc': 'Finland uses the Finnish Model.'},
            'lapua_movement': {'target_focus': 'FIN_the_lapua_movement', 'name': 'Lapua Movement (Fascist)', 'desc': 'The Lapua Movement succeeds.'},
            'red_guards': {'target_focus': 'FIN_the_red_guards', 'name': 'Red Guards (Communist)', 'desc': 'The Red Guards launch a revolution.'}
        }
    },
    'HUN': {
        'rule_name': 'SAH_hun_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'renounce_trianon': {'target_focus': 'HUN_renounce_the_treaty_of_trianon', 'name': 'Historical Hungary', 'desc': 'Hungary renounces Trianon.'},
            'king': {'target_focus': 'HUN_a_king_for_our_people', 'name': 'Monarchist Hungary', 'desc': 'Hungary invites a King.'},
            'communist': {'target_focus': 'HUN_the_communist_party', 'name': 'Communist Hungary', 'desc': 'Hungary turns Communist.'},
            'habsburg': {'target_focus': 'HUN_invite_the_habsburg_prince', 'name': 'Habsburg Prince', 'desc': 'Hungary restores Austria-Hungary.'}
        }
    },
    'IRQ': {
        'rule_name': 'SAH_irq_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'hashemite': {'target_focus': 'IRQ_the_hashemite_kingdom', 'name': 'Hashemite Kingdom', 'desc': 'Iraq stays a Hashemite Kingdom.'},
            'golden_square': {'target_focus': 'IRQ_the_golden_square', 'name': 'Golden Square (Fascist)', 'desc': 'The Golden Square executes a coup.'}
        }
    },
    'LAT': {
        'rule_name': 'SAH_lat_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'ulmainis': {'target_focus': 'LAT_the_ulmanis_dictatorship', 'name': 'Ulmanis Dictatorship', 'desc': 'Latvia under Ulmanis.'},
            'perkonkrusts': {'target_focus': 'LAT_the_perkonkrusts', 'name': 'Perkonkrusts', 'desc': 'The Perkonkrusts take power.'}
        }
    },
    'LIT': {
        'rule_name': 'SAH_lit_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'smetona': {'target_focus': 'LIT_the_smetona_dictatorship', 'name': 'Smetona Dictatorship', 'desc': 'Lithuania under Smetona.'},
            'iron_wolf': {'target_focus': 'LIT_the_iron_wolf', 'name': 'Iron Wolf', 'desc': 'The Iron Wolf ascends.'}
        }
    },
    'MAN': {
        'rule_name': 'SAH_man_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'obedience': {'target_focus': 'MAN_obedience', 'name': 'Obedience', 'desc': 'Manchukuo remains obedient to Japan.'},
            'assertiveness': {'target_focus': 'MAN_assertiveness', 'name': 'Assertiveness', 'desc': 'Manchukuo asserts its independence.'},
            'democratic': {'target_focus': 'MAN_the_democratic_party', 'name': 'Democratic Party', 'desc': 'Manchu transition to democracy.'},
            'communist': {'target_focus': 'MAN_the_communist_party', 'name': 'Communist Party', 'desc': 'Manchu communist revolution.'}
        }
    },
    'NOR': {
        'rule_name': 'SAH_nor_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'nygaardsvold': {'target_focus': 'NOR_the_nygaardsvold_cabinet', 'name': 'Nygaardsvold Cabinet', 'desc': 'Norway under Nygaardsvold.'},
            'quisling': {'target_focus': 'NOR_quisling_government', 'name': 'Quisling Government (Fascist)', 'desc': 'Quisling seizes control.'},
            'communist': {'target_focus': 'NOR_the_communist_party', 'name': 'Communist Party', 'desc': 'Norway adopts communism.'}
        }
    },
    'NZL': {
        'rule_name': 'SAH_nzl_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'labour': {'target_focus': 'NZL_the_labour_party', 'name': 'Labour Party', 'desc': 'New Zealand under the Labour Party.'}
        }
    },
    'PAR': {
        'rule_name': 'SAH_par_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'febrerista': {'target_focus': 'PAR_the_febrerista_revolution', 'name': 'Febrerista Revolution', 'desc': 'Paraguay proceeds post-revolution.'}
        }
    },
    'PER': {
        'rule_name': 'SAH_per_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'pahlavi': {'target_focus': 'PER_the_pahlavi_dynasty', 'name': 'Pahlavi Dynasty', 'desc': 'Iran empowers the Pahlavi Dynasty.'},
            'tudeh': {'target_focus': 'PER_the_tudeh_party', 'name': 'Tudeh Party (Communist)', 'desc': 'The Tudeh party incites revolution.'}
        }
    },
    'PHI': {
        'rule_name': 'SAH_phi_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'commonwealth': {'target_focus': 'PHI_the_commonwealth', 'name': 'The Commonwealth', 'desc': 'The Philippines remains a Commonwealth.'},
            'ganap': {'target_focus': 'PHI_the_ganap_party', 'name': 'Ganap Party (Fascist)', 'desc': 'The Ganap party asserts control.'},
            'hukbalahap': {'target_focus': 'PHI_the_hukbalahap', 'name': 'Hukbalahap (Communist)', 'desc': 'The Hukbalahap rebel.'}
        }
    },
    'POR': {
        'rule_name': 'SAH_por_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'estado_novo': {'target_focus': 'POR_the_estado_novo', 'name': 'Estado Novo', 'desc': 'Portugal proceeds with the Estado Novo.'},
            'popular_front': {'target_focus': 'POR_the_popular_front', 'name': 'Popular Front', 'desc': 'The Popular Front sweeps the government.'}
        }
    },
    'PRC': {
        'rule_name': 'SAH_prc_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'maoism': {'target_focus': 'PRC_maoism', 'name': 'Maoism', 'desc': 'Communist China under Mao.'},
            'orthodox_marxism': {'target_focus': 'PRC_orthodox_marxism', 'name': 'Orthodox Marxism', 'desc': 'Communist China under Orthodox Marxism.'},
            'social_democracy': {'target_focus': 'PRC_social_democracy', 'name': 'Social Democracy', 'desc': 'A transition towards Social Democracy.'}
        }
    },
    'SWI': {
        'rule_name': 'SAH_swi_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'federal_council': {'target_focus': 'SWI_the_federal_council', 'name': 'Federal Council', 'desc': 'Switzerland under the Federal Council.'}
        }
    },
    'URU': {
        'rule_name': 'SAH_uru_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'colorado': {'target_focus': 'URU_the_colorado_party', 'name': 'Colorado Party', 'desc': 'Uruguay relies on the Colorado Party.'}
        }
    },
    'WRL': {
        'rule_name': 'SAH_wrl_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'nationalists': {'target_focus': 'WRL_cooperate_with_the_nationalists', 'name': 'Cooperate with Nationalists', 'desc': 'Warlord aligns with Nationalists.'},
            'communists': {'target_focus': 'WRL_cooperate_with_the_communists', 'name': 'Cooperate with Communists', 'desc': 'Warlord aligns with Communists.'}
        }
    },
    'AFG': {
        'rule_name': 'SAH_afg_scenario_start_rule', 'group_name': 'SAH_GAME_RULES_GROUP', 'tier': 2,
        'starts': {
            'barakzai': {'target_focus': 'AFG_the_barakzai_dynasty', 'name': 'Barakzai Dynasty', 'desc': 'Afghanistan supports the Barakzai Dynasty.'}
        }
    }
}

with open('scenario_automator.py', 'r', encoding='utf-8') as f:
    orig = f.read()

import json
output_lines: list[str] = []
for tag, data in extra_scenarios.items():
    formatted = json.dumps(data, indent=4)
    formatted = formatted.replace('\"', '\'')
    formatted = formatted.replace('null', 'None').replace('true', 'True').replace('false', 'False')
    
    # We need to preserve the dict formatting to append
    # Strip the outermost { and }
    inner_lines = formatted.split('\n')[1:-1]
    inner = '\n'.join(inner_lines)
    output_lines.append(f"    '{tag}': {{\n{inner}\n    }},")

all_new_dicts = '\n'.join(output_lines)

# Insert before the last }
lines = orig.split('\n')
for i in range(len(lines)-1, -1, -1):
    if lines[i].startswith('}'):
        lines.insert(i, all_new_dicts)
        break

with open('scenario_automator.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Successfully injected all additional nations!")
