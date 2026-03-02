import os
import re
from typing import Dict, Any

# ====================================================================
# STAKUYI SCENARIO AUTOMATOR
# Defines the "Starts" you want to generate.
# ====================================================================
SCENARIOS: Dict[str, Dict[str, Any]] = {
    "USA": {
        "rule_name": "SAH_usa_scenario_start_rule",
        "group_name": "SAH_GAME_RULES_GROUP",
        "industrial_targets": ["USA_arsenal_of_democracy", "USA_war_plan_orange"],
        "starts": {
            "american_caesar": {
                "target_focus": "USA_the_american_caesar",
                "name": "American Caesar Start",
                "desc": "Starts the game heavily down the American Caesar path, skipping excessive PP gains."
            },
            "fascist_menace": {
                "target_focus": "USA_the_fascist_menace",
                "name": "America First Start",
                "desc": "Starts the game heavily down the Fascist path."
            },
            "communist": {
                "target_focus": "USA_the_peoples_republic",
                "name": "Communist America Start",
                "desc": "Starts the game heavily down the Communist path."
            },
            "giant_wakes": {
                "target_focus": "USA_the_giant_wakes",
                "name": "The Giant Wakes (Historical)",
                "desc": "Pre-completes the historical democratic recovery from the Great Depression."
            }
        }
    },
    "GER": {
        "rule_name": "SAH_ger_scenario_start_rule",
        "group_name": "SAH_GAME_RULES_GROUP",
        "industrial_targets": ["GER_kdf_wagen", "GER_army_innovations_2"],
        "starts": {
            "danzig_or_war": {
                "target_focus": "GER_danzig_or_war",
                "name": "Historical Fascist Start",
                "desc": "Germany has completed all pre-war historical focuses up to Danzig."
            },
            "return_of_kaiser": {
                "target_focus": "GER_return_of_the_kaiser",
                "name": "Return of the Kaiser",
                "desc": "Germany has opposed Hitler and revived the Kaiserreich."
            },
            "communist_uprising": {
                "target_focus": "GER_the_workers_republic",
                "name": "Communist Uprising",
                "desc": "Germany has staged a communist uprising and aligned left."
            },
            "anti_soviet_pact": {
                "target_focus": "GER_support_democracy_in_europe",
                "name": "Democratic Germany Start",
                "desc": "Germany has restored free elections and created a democratic bloc."
            }
        }
    },
    "SOV": {
        "rule_name": "SAH_sov_scenario_start_rule",
        "group_name": "SAH_GAME_RULES_GROUP",
        "industrial_targets": ["SOV_relocate_industry_to_the_urals"],
        "starts": {
            "historical_stalin": {
                "target_focus": "SOV_the_great_purge",
                "name": "Historical Stalin",
                "desc": "The USSR has completed the Great Purge."
            },
            "permanent_revolution": {
                "target_focus": "SOV_permanent_revolution",
                "name": "Trotskyist Start",
                "desc": "The USSR has followed the Left Opposition."
            },
            "new_economic_policy": {
                "target_focus": "SOV_the_new_economic_policy",
                "name": "Bukharin Start",
                "desc": "The USSR has followed the Right Opposition."
            },
            "tsarist_restored": {
                "target_focus": "SOV_the_romanovs_restored",
                "name": "Tsarist Start",
                "desc": "The Romanovs have been restored."
            },
            "republic": {
                "target_focus": "SOV_the_duma",
                "name": "Russian Republic Start",
                "desc": "The USSR has transitioned to a Democratic Republic."
            },
            "fascist_destiny": {
                "target_focus": "SOV_the_russian_fascist_party",
                "name": "Russian Fascist Party Start",
                "desc": "The USSR has fallen to the Russian Fascist Party."
            }
        }
    },
    "ENG": {
        "rule_name": "SAH_eng_scenario_start_rule",
        "group_name": "SAH_GAME_RULES_GROUP",
        "industrial_targets": ["ENG_general_rearmament"],
        "starts": {
            "churchill": {
                "target_focus": "ENG_churchill_government",
                "name": "Churchill Government",
                "desc": "Britain has secured Churchill's aggressive stance against dictators."
            },
            "kings_party": {
                "target_focus": "ENG_the_kings_party",
                "name": "The King's Party",
                "desc": "Edward VIII has established absolute monarchical rule."
            },
            "mosley_fascist": {
                "target_focus": "ENG_march_on_london",
                "name": "Blackshirt Start",
                "desc": "Mosley's Blackshirts have marched on London."
            },
            "communist_britain": {
                "target_focus": "ENG_the_communist_alternative",
                "name": "Communist Britain",
                "desc": "The Trade Unions have seized power in Britain."
            }
        }
    },
    "FRA": {
        "rule_name": "SAH_fra_scenario_start_rule",
        "group_name": "SAH_GAME_RULES_GROUP",
        "industrial_targets": ["FRA_widespread_rearmament", "FRA_extend_the_maginot_line"],
        "starts": {
            "french_commune": {
                "target_focus": "FRA_the_french_commune",
                "name": "French Commune Start",
                "desc": "France has completed the communist popular front."
            },
            "legitimist": {
                "target_focus": "FRA_legitimist_restoration",
                "name": "Legitimist Restoration",
                "desc": "France has restored the Legitimist monarchy."
            },
            "bonapartist": {
                "target_focus": "FRA_bonapartist_restoration",
                "name": "Bonapartist Restoration",
                "desc": "France has restored the Bonapartist empire."
            },
            "latin_entente": {
                "target_focus": "FRA_latin_entente",
                "name": "Latin Entente (Fascist)",
                "desc": "France has turned Fascist and formed the Latin Entente."
            }
        }
    },
    "JAP": {
        "rule_name": "SAH_jap_scenario_start_rule",
        "group_name": "SAH_GAME_RULES_GROUP",
        "industrial_targets": ["JAP_yamato_class_battleships", "JAP_spiritual_mobilization"],
        "starts": {
            "strike_south": {
                "target_focus": "JAP_strike_south_doctrine",
                "name": "Historical Strike South",
                "desc": "Japan has purged the Kodoha and looks South."
            },
            "showa_restoration": {
                "target_focus": "JAP_showa_restoration",
                "name": "Showa Restoration (Non-Aligned)",
                "desc": "Japan has executed the Showa Restoration."
            },
            "democratic_diet": {
                "target_focus": "JAP_restore_the_diet",
                "name": "Democratic Japan Start",
                "desc": "Japan has restored the Diet."
            },
            "communist_japan": {
                "target_focus": "JAP_the_japanese_communist_party",
                "name": "Communist Japan Start",
                "desc": "Japan has undergone a communist revolution."
            }
        }
    },
    "ITA": {
        "rule_name": "SAH_ita_scenario_start_rule",
        "group_name": "SAH_GAME_RULES_GROUP",
        "industrial_targets": ["ITA_expand_the_regia_marina", "ITA_expand_the_regia_aeronautica"],
        "starts": {
            "pact_of_steel": {
                "target_focus": "ITA_solidify_the_pact_of_steel",
                "name": "Pact of Steel (Historical)",
                "desc": "Italy is fully aligned with Germany in the Pact of Steel."
            },
            "latin_bloc": {
                "target_focus": "ITA_the_latin_bloc",
                "name": "Italy First / Latin Bloc",
                "desc": "Italy pursues its own independent Fascist faction."
            },
            "kingdom_of_god": {
                "target_focus": "ITA_kingdom_of_god",
                "name": "The Kingdom of God",
                "desc": "The Pope has seized control of Italy."
            },
            "republic_of_italy": {
                "target_focus": "ITA_the_republic_of_italy",
                "name": "Italian Republic Start",
                "desc": "The monarchy has been abolished and democracy restored."
            },
            "communist_italy": {
                "target_focus": "ITA_the_italian_communist_party",
                "name": "Communist Italy Start",
                "desc": "The Italian Communist Party has taken control."
            }
        }
    },
    "POL": {
        "rule_name": "SAH_pol_scenario_start_rule",
        "industrial_targets": ["POL_central_industrial_region"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "april_constitution": {
                "target_focus": "POL_april_constitution",
                "name": "Sanation Government (Historical)",
                "desc": "Poland has secured the Sanation government."
            },
            "falanga": {
                "target_focus": "POL_the_falanga",
                "name": "Falangist Poland Start",
                "desc": "The Fascist Falanga has seized control of Poland."
            },
            "comintern": {
                "target_focus": "POL_align_with_the_comintern",
                "name": "Communist Poland Start",
                "desc": "Poland has aligned with the Comintern."
            },
            "regency_council": {
                "target_focus": "POL_invite_the_king",
                "name": "Monarchist Poland Start",
                "desc": "Poland has established the Regency Council and invited a King."
            }
        }
    },
    "CAN": {
        "rule_name": "SAH_can_scenario_start_rule",
        "industrial_targets": ["CAN_defense_of_canada_regulations"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "zombies": {
                "target_focus": "CAN_send_in_the_zombies",
                "name": "Historical Canadian Effort",
                "desc": "Canada commits to the historical UK allegiance."
            },
            "fascist_canada": {
                "target_focus": "CAN_national_unity_party",
                "name": "National Unity Party (Fascist)",
                "desc": "The swastika clubs have formed the National Unity Party."
            },
            "communist_canada": {
                "target_focus": "CAN_communist_revolution",
                "name": "Communist Canada Start",
                "desc": "Canada has undergone a communist revolution."
            }
        }
    },
    "AST": {
        "rule_name": "SAH_ast_scenario_start_rule",
        "industrial_targets": ["AST_standardize_rail_gauge"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "never_gallipoli_again": {
                "target_focus": "AST_never_gallipoli_again",
                "name": "Historical Australia Start",
                "desc": "Australia historically commits to the defense of the Empire."
            },
            "australia_first": {
                "target_focus": "AST_the_australia_first_movement",
                "name": "Australia First (Fascist)",
                "desc": "Australia shifts right and focuses on itself."
            },
            "communist_australia": {
                "target_focus": "AST_workers_revolution",
                "name": "Communist Australia Start",
                "desc": "The Australian workers have rebelled."
            }
        }
    },
    "SAF": {
        "rule_name": "SAH_saf_scenario_start_rule",
        "industrial_targets": ["SAF_expand_the_gold_mining_industry"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "appeasement": {
                "target_focus": "SAF_support_the_policy_of_appeasement",
                "name": "Historical South Africa",
                "desc": "South Africa stands with the Allies."
            },
            "ossewabrandwag": {
                "target_focus": "SAF_support_the_ossewabrandwag",
                "name": "Ossewabrandwag (Fascist)",
                "desc": "South Africa embraces Fascism and abandons Westminster."
            },
            "anti_colonialist": {
                "target_focus": "SAF_anti_colonialist_crusade",
                "name": "Communist South Africa Start",
                "desc": "South Africa embraces Communism and begins an anti-colonial crusade."
            }
        }
    },
    "RAJ": {
        "rule_name": "SAH_raj_scenario_start_rule",
        "industrial_targets": ["RAJ_expand_the_railway_network"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "provincial_elections": {
                "target_focus": "RAJ_provincial_elections",
                "name": "Historical India Start",
                "desc": "India commits to supporting the crown."
            },
            "quit_india": {
                "target_focus": "RAJ_quit_india_movement",
                "name": "Quit India Movement",
                "desc": "India moves towards Democratic independence."
            },
            "indian_national_army": {
                "target_focus": "RAJ_indian_national_army",
                "name": "Indian National Army (Fascist)",
                "desc": "Bose's Indian National Army prepares to forcefully seize independence."
            }
        }
    },
    "ROM": {
        "rule_name": "SAH_rom_scenario_start_rule",
        "industrial_targets": ["ROM_expand_the_oil_industry"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "preserve_romania": {
                "target_focus": "ROM_preserve_greater_romania",
                "name": "Historical Romania",
                "desc": "Romania acts to preserve its current borders."
            },
            "align_axis": {
                "target_focus": "ROM_align_axis",
                "name": "Iron Guard (Fascist)",
                "desc": "Romania firmly aligns with Germany."
            },
            "balkan_dominance": {
                "target_focus": "ROM_the_balkan_dominance",
                "name": "Balkan Dominance (Non-Aligned)",
                "desc": "Romania forcefully establishes dominance over the Balkans."
            }
        }
    },
    "YUG": {
        "rule_name": "SAH_yug_scenario_start_rule",
        "industrial_targets": ["YUG_western_focus"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "regency_council": {
                "target_focus": "YUG_the_regency_council",
                "name": "Historical Yugoslavia",
                "desc": "Yugoslavia balances internal pressure under the regency."
            },
            "tripartite_pact": {
                "target_focus": "YUG_sign_the_tripartite_pact",
                "name": "Tripartite Pact (Fascist)",
                "desc": "Yugoslavia signs the Tripartite Pact and embraces Fascism."
            },
            "communist_partisans": {
                "target_focus": "YUG_the_communist_partisans",
                "name": "Communist Yugoslavia Start",
                "desc": "Tito's partisans have seized power."
            },
            "western_focus": {
                "target_focus": "YUG_western_focus",
                "name": "Democratic Yugoslavia Start",
                "desc": "Yugoslavia rejects the radical factions and commits to democracy."
            }
        }
    },
    "GRE": {
        "rule_name": "SAH_gre_scenario_start_rule",
        "industrial_targets": ["GRE_hellenic_armed_forces"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "metaxas": {
                "target_focus": "GRE_the_metaxas_dictatorship",
                "name": "Metaxas Dictatorship (Historical)",
                "desc": "Greece continues under Metaxas."
            },
            "megali_idea": {
                "target_focus": "GRE_revive_the_megali_idea",
                "name": "Megali Idea (Fascist)",
                "desc": "Greece moves right to revive Byzantine ambitions."
            },
            "venizelist": {
                "target_focus": "GRE_the_venizelist_movement",
                "name": "Venizelist Start (Democratic)",
                "desc": "The Venizelists establish a democratic Greece."
            }
        }
    },
    "TUR": {
        "rule_name": "SAH_tur_scenario_start_rule",
        "industrial_targets": ["TUR_the_saadabad_pact"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "peace_at_home": {
                "target_focus": "TUR_peace_at_home",
                "name": "Historical Turkey",
                "desc": "Turkey continues Kemalism and peace at home."
            },
            "multi_party": {
                "target_focus": "TUR_multi_party_system",
                "name": "Multi-Party Turkey Start",
                "desc": "Turkey embraces a full democratic system."
            }
        }
    },
    "MEX": {
        "rule_name": "SAH_mex_scenario_start_rule",
        "industrial_targets": ["MEX_hispanic_alliance"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "prm": {
                "target_focus": "MEX_the_prm",
                "name": "Historical Mexico Start",
                "desc": "Mexico proceeds down its historical timeline."
            },
            "gold_shirts": {
                "target_focus": "MEX_the_gold_shirts",
                "name": "Gold Shirts Start (Fascist)",
                "desc": "The Fascist Gold Shirts rise."
            },
            "hispanic_alliance": {
                "target_focus": "MEX_hispanic_alliance",
                "name": "Hispanic Alliance",
                "desc": "Mexico forms a Hispanic Alliance bloc."
            }
        }
    },
    "BRA": {
        "rule_name": "SAH_bra_scenario_start_rule",
        "industrial_targets": ["BRA_the_coffee_valorization_program"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "estado_novo": {
                "target_focus": "BRA_the_estado_novo",
                "name": "Estado Novo (Historical)",
                "desc": "Vargas installs the Estado Novo."
            },
            "integralist": {
                "target_focus": "BRA_integralist_uprising",
                "name": "Integralist Brazil Start (Fascist)",
                "desc": "The Integralists launch their uprising."
            },
            "aln_revolt": {
                "target_focus": "BRA_the_aln_revolt",
                "name": "Communist Brazil Start",
                "desc": "The ALN communists have revolted."
            }
        }
    },
    "SPR": {
        "rule_name": "SAH_spr_scenario_start_rule",
        "industrial_targets": ["SPR_rebuild_the_nation"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "popular_front": {
                "target_focus": "SPR_the_popular_front",
                "name": "Popular Front (Historical)",
                "desc": "The Republicans proceed historically into the Civil War."
            },
            "falange": {
                "target_focus": "SPR_the_falange",
                "name": "Nationalist Pre-Civil War",
                "desc": "The Nationalists prepare their uprising."
            },
            "anti_fascist_unity": {
                "target_focus": "SPR_anti_fascist_unity",
                "name": "Communist Spain Start",
                "desc": "The Communists consolidate power in Spain."
            }
        }
    },
    "HOL": {
        "rule_name": "SAH_hol_scenario_start_rule",
        "industrial_targets": ["HOL_invest_in_the_east_indies"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "gateway_to_europe": {
                "target_focus": "HOL_the_gateway_to_europe",
                "name": "Historical Netherlands",
                "desc": "The Netherlands prepare for European conflict."
            },
            "anton_mussert": {
                "target_focus": "HOL_anton_mussert",
                "name": "Mussert Start (Fascist)",
                "desc": "Mussert assumes control."
            }
        }
    },
    "SWE": {
        "rule_name": "SAH_swe_scenario_start_rule",
        "industrial_targets": ["SWE_the_nordic_defence_council"],
        "group_name": "SAH_GAME_RULES_GROUP",
        "starts": {
            "per_albin_bus": {
                "target_focus": "SWE_the_per_albin_bus",
                "name": "Historical Sweden Start",
                "desc": "Sweden prepares for neutrality."
            },
            "svea_rike": {
                "target_focus": "SWE_the_svea_rike",
                "name": "Svea Rike (Fascist)",
                "desc": "Sweden turns to the far right."
            },
            "socialist_republic": {
                "target_focus": "SWE_socialist_republic_of_sweden",
                "name": "Communist Sweden Start",
                "desc": "Sweden embraces socialism."
            }
        }
    },
    'ARG': {
    'rule_name': 'SAH_arg_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'infamous_decade': {
            'target_focus': 'ARG_the_concordancia_government',
            'name': 'Historical Argentina',
            'desc': 'Provides the historical setup for Argentina.'
        },
        'radical_civic': {
            'target_focus': 'ARG_the_radical_civic_union',
            'name': 'Radical Civic Union',
            'desc': 'Brings the Radical Civic Union back to power.'
        },
        'peronist': {
            'target_focus': 'ARG_the_peronist_movement',
            'name': 'Peronist Movement',
            'desc': 'Sparks the Peronist movement.'
        }
    }
    },
    'AUS': {
    'rule_name': 'SAH_aus_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'fatherland_front': {
            'target_focus': 'AUS_the_fatherland_front',
            'name': 'Historical Austria',
            'desc': 'Austria maintains the Fatherland Front.'
        },
        'austrofascism': {
            'target_focus': 'AUS_austrofascism',
            'name': 'Austrofascism',
            'desc': 'Austria fully embraces Fascism.'
        },
        'social_democrats': {
            'target_focus': 'AUS_the_social_democrats',
            'name': 'Social Democrats',
            'desc': 'Austria aligns with democratic socialism.'
        }
    }
    },
    'BEL': {
    'rule_name': 'SAH_bel_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 1,
    'starts': {
        'catholic_bloc': {
            'target_focus': 'BEL_the_catholic_bloc',
            'name': 'Historical Belgium',
            'desc': 'Belgium continues with the Catholic Bloc.'
        },
        'liberal_party': {
            'target_focus': 'BEL_the_liberal_party',
            'name': 'Liberal Party',
            'desc': 'The Liberal Party takes control.'
        },
        'rexist_party': {
            'target_focus': 'BEL_the_rexist_party',
            'name': 'Rexist Party (Fascist)',
            'desc': 'Degrelle and the Rexists seize power.'
        }
    }
    },
    'BUL': {
    'rule_name': 'SAH_bul_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'tsars_dictatorship': {
            'target_focus': 'BUL_the_tsars_dictatorship',
            'name': 'Historical Tsar',
            'desc': 'The Tsar maintains his royal dictatorship.'
        },
        'zveno': {
            'target_focus': 'BUL_zveno',
            'name': 'Zveno (Fascist)',
            'desc': 'The militarist Zveno takes control.'
        },
        'fatherland_front': {
            'target_focus': 'BUL_the_fatherland_front',
            'name': 'Fatherland Front (Communist)',
            'desc': 'Bulgaria turns Communist.'
        }
    }
    },
    'CHI': {
    'rule_name': 'SAH_chi_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'historical': {
            'target_focus': 'CHI_three_principles_of_the_people',
            'name': 'Historical China',
            'desc': 'China follows the Three Principles.'
        },
        'welfare': {
            'target_focus': 'CHI_welfare',
            'name': 'Welfare State',
            'desc': 'China commits to social welfare.'
        }
    }
    },
    'CHL': {
    'rule_name': 'SAH_chl_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'popular_front': {
            'target_focus': 'CHL_the_popular_front',
            'name': 'Popular Front (History)',
            'desc': 'Chile follows the Popular Front.'
        },
        'nacistas': {
            'target_focus': 'CHL_the_nacistas',
            'name': 'Nacistas (Fascist)',
            'desc': 'The Nacistas assume control.'
        }
    }
    },
    'COG': {
    'rule_name': 'SAH_cog_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'force_publique': {
            'target_focus': 'COG_the_force_publique',
            'name': 'Force Publique',
            'desc': 'Congo relies on the Force Publique.'
        },
        'evolues': {
            'target_focus': 'COG_the_evolues',
            'name': 'The Evolues',
            'desc': 'Congo empowers the Evolues.'
        }
    }
    },
    'CZE': {
    'rule_name': 'SAH_cze_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'political_direction': {
            'target_focus': 'CZE_political_direction',
            'name': 'Historical Czechoslovakia',
            'desc': 'Czechoslovakia maneuvers politics.'
        },
        'fascist_direction': {
            'target_focus': 'CZE_fascist_direction',
            'name': 'Fascist Direction',
            'desc': 'Czechoslovakia turns fascist.'
        },
        'communist_direction': {
            'target_focus': 'CZE_communist_direction',
            'name': 'Communist Direction',
            'desc': 'Czechoslovakia turns communist.'
        }
    }
    },
    'DEN': {
    'rule_name': 'SAH_den_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'social_democrats': {
            'target_focus': 'DEN_the_social_democrats',
            'name': 'Historical Denmark',
            'desc': 'Denmark retains the Social Democrats.'
        },
        'conservative': {
            'target_focus': 'DEN_the_conservative_peoples_party',
            'name': 'Conservative Party',
            'desc': 'The Conservative party rules.'
        }
    }
    },
    'EGY': {
    'rule_name': 'SAH_egy_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'anglo_treaty': {
            'target_focus': 'EGY_the_anglo_egyptian_treaty',
            'name': 'Historical Egypt',
            'desc': 'Egypt proceeds with the Anglo-Egyptian treaty.'
        },
        'wafd_party': {
            'target_focus': 'EGY_the_wafd_party',
            'name': 'Wafd Party',
            'desc': 'Egypt embraces the Wafd Party.'
        }
    }
    },
    'EST': {
    'rule_name': 'SAH_est_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'era_of_silence': {
            'target_focus': 'EST_the_era_of_silence',
            'name': 'Era of Silence',
            'desc': 'Estonia maintains the Era of Silence.'
        },
        'vaps_movement': {
            'target_focus': 'EST_the_vaps_movement',
            'name': 'Vaps Movement',
            'desc': 'The Vaps Movement takes over.'
        }
    }
    },
    'ETH': {
    'rule_name': 'SAH_eth_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'emperor': {
            'target_focus': 'ETH_the_emperor',
            'name': 'The Emperor',
            'desc': 'Ethiopia rallies behind the Emperor.'
        }
    }
    },
    'FIN': {
    'rule_name': 'SAH_fin_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'finnish_model': {
            'target_focus': 'FIN_the_finnish_model',
            'name': 'Historical Finland',
            'desc': 'Finland uses the Finnish Model.'
        },
        'lapua_movement': {
            'target_focus': 'FIN_the_lapua_movement',
            'name': 'Lapua Movement (Fascist)',
            'desc': 'The Lapua Movement succeeds.'
        },
        'red_guards': {
            'target_focus': 'FIN_the_red_guards',
            'name': 'Red Guards (Communist)',
            'desc': 'The Red Guards launch a revolution.'
        }
    }
    },
    'HUN': {
    'rule_name': 'SAH_hun_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'renounce_trianon': {
            'target_focus': 'HUN_renounce_the_treaty_of_trianon',
            'name': 'Historical Hungary',
            'desc': 'Hungary renounces Trianon.'
        },
        'king': {
            'target_focus': 'HUN_a_king_for_our_people',
            'name': 'Monarchist Hungary',
            'desc': 'Hungary invites a King.'
        },
        'communist': {
            'target_focus': 'HUN_the_communist_party',
            'name': 'Communist Hungary',
            'desc': 'Hungary turns Communist.'
        },
        'habsburg': {
            'target_focus': 'HUN_invite_the_habsburg_prince',
            'name': 'Habsburg Prince',
            'desc': 'Hungary restores Austria-Hungary.'
        }
    }
    },
    'IRQ': {
    'rule_name': 'SAH_irq_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'hashemite': {
            'target_focus': 'IRQ_the_hashemite_kingdom',
            'name': 'Hashemite Kingdom',
            'desc': 'Iraq stays a Hashemite Kingdom.'
        },
        'golden_square': {
            'target_focus': 'IRQ_the_golden_square',
            'name': 'Golden Square (Fascist)',
            'desc': 'The Golden Square executes a coup.'
        }
    }
    },
    'LAT': {
    'rule_name': 'SAH_lat_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'ulmainis': {
            'target_focus': 'LAT_the_ulmanis_dictatorship',
            'name': 'Ulmanis Dictatorship',
            'desc': 'Latvia under Ulmanis.'
        },
        'perkonkrusts': {
            'target_focus': 'LAT_the_perkonkrusts',
            'name': 'Perkonkrusts',
            'desc': 'The Perkonkrusts take power.'
        }
    }
    },
    'LIT': {
    'rule_name': 'SAH_lit_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'smetona': {
            'target_focus': 'LIT_the_smetona_dictatorship',
            'name': 'Smetona Dictatorship',
            'desc': 'Lithuania under Smetona.'
        },
        'iron_wolf': {
            'target_focus': 'LIT_the_iron_wolf',
            'name': 'Iron Wolf',
            'desc': 'The Iron Wolf ascends.'
        }
    }
    },
    'MAN': {
    'rule_name': 'SAH_man_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'obedience': {
            'target_focus': 'MAN_obedience',
            'name': 'Obedience',
            'desc': 'Manchukuo remains obedient to Japan.'
        },
        'assertiveness': {
            'target_focus': 'MAN_assertiveness',
            'name': 'Assertiveness',
            'desc': 'Manchukuo asserts its independence.'
        },
        'democratic': {
            'target_focus': 'MAN_the_democratic_party',
            'name': 'Democratic Party',
            'desc': 'Manchu transition to democracy.'
        },
        'communist': {
            'target_focus': 'MAN_the_communist_party',
            'name': 'Communist Party',
            'desc': 'Manchu communist revolution.'
        }
    }
    },
    'NOR': {
    'rule_name': 'SAH_nor_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'nygaardsvold': {
            'target_focus': 'NOR_the_nygaardsvold_cabinet',
            'name': 'Nygaardsvold Cabinet',
            'desc': 'Norway under Nygaardsvold.'
        },
        'quisling': {
            'target_focus': 'NOR_quisling_government',
            'name': 'Quisling Government (Fascist)',
            'desc': 'Quisling seizes control.'
        },
        'communist': {
            'target_focus': 'NOR_the_communist_party',
            'name': 'Communist Party',
            'desc': 'Norway adopts communism.'
        }
    }
    },
    'NZL': {
    'rule_name': 'SAH_nzl_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'labour': {
            'target_focus': 'NZL_the_labour_party',
            'name': 'Labour Party',
            'desc': 'New Zealand under the Labour Party.'
        }
    }
    },
    'PAR': {
    'rule_name': 'SAH_par_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'febrerista': {
            'target_focus': 'PAR_the_febrerista_revolution',
            'name': 'Febrerista Revolution',
            'desc': 'Paraguay proceeds post-revolution.'
        }
    }
    },
    'PER': {
    'rule_name': 'SAH_per_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'pahlavi': {
            'target_focus': 'PER_the_pahlavi_dynasty',
            'name': 'Pahlavi Dynasty',
            'desc': 'Iran empowers the Pahlavi Dynasty.'
        },
        'tudeh': {
            'target_focus': 'PER_the_tudeh_party',
            'name': 'Tudeh Party (Communist)',
            'desc': 'The Tudeh party incites revolution.'
        }
    }
    },
    'PHI': {
    'rule_name': 'SAH_phi_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'commonwealth': {
            'target_focus': 'PHI_the_commonwealth',
            'name': 'The Commonwealth',
            'desc': 'The Philippines remains a Commonwealth.'
        },
        'ganap': {
            'target_focus': 'PHI_the_ganap_party',
            'name': 'Ganap Party (Fascist)',
            'desc': 'The Ganap party asserts control.'
        },
        'hukbalahap': {
            'target_focus': 'PHI_the_hukbalahap',
            'name': 'Hukbalahap (Communist)',
            'desc': 'The Hukbalahap rebel.'
        }
    }
    },
    'POR': {
    'rule_name': 'SAH_por_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'estado_novo': {
            'target_focus': 'POR_the_estado_novo',
            'name': 'Estado Novo',
            'desc': 'Portugal proceeds with the Estado Novo.'
        },
        'popular_front': {
            'target_focus': 'POR_the_popular_front',
            'name': 'Popular Front',
            'desc': 'The Popular Front sweeps the government.'
        }
    }
    },
    'PRC': {
    'rule_name': 'SAH_prc_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'maoism': {
            'target_focus': 'PRC_maoism',
            'name': 'Maoism',
            'desc': 'Communist China under Mao.'
        },
        'orthodox_marxism': {
            'target_focus': 'PRC_orthodox_marxism',
            'name': 'Orthodox Marxism',
            'desc': 'Communist China under Orthodox Marxism.'
        },
        'social_democracy': {
            'target_focus': 'PRC_social_democracy',
            'name': 'Social Democracy',
            'desc': 'A transition towards Social Democracy.'
        }
    }
    },
    'SWI': {
    'rule_name': 'SAH_swi_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'federal_council': {
            'target_focus': 'SWI_the_federal_council',
            'name': 'Federal Council',
            'desc': 'Switzerland under the Federal Council.'
        }
    }
    },
    'URU': {
    'rule_name': 'SAH_uru_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'colorado': {
            'target_focus': 'URU_the_colorado_party',
            'name': 'Colorado Party',
            'desc': 'Uruguay relies on the Colorado Party.'
        }
    }
    },
    'WRL': {
    'rule_name': 'SAH_wrl_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'nationalists': {
            'target_focus': 'WRL_cooperate_with_the_nationalists',
            'name': 'Cooperate with Nationalists',
            'desc': 'Warlord aligns with Nationalists.'
        },
        'communists': {
            'target_focus': 'WRL_cooperate_with_the_communists',
            'name': 'Cooperate with Communists',
            'desc': 'Warlord aligns with Communists.'
        }
    }
    },
    'AFG': {
    'rule_name': 'SAH_afg_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'barakzai': {
            'target_focus': 'AFG_the_barakzai_dynasty',
            'name': 'Barakzai Dynasty',
            'desc': 'Afghanistan supports the Barakzai Dynasty.'
        }
    }
    },
    'ARG': {
    'rule_name': 'SAH_arg_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'infamous_decade': {
            'target_focus': 'ARG_the_concordancia_government',
            'name': 'Historical Argentina',
            'desc': 'Provides the historical setup for Argentina.'
        },
        'radical_civic': {
            'target_focus': 'ARG_the_radical_civic_union',
            'name': 'Radical Civic Union',
            'desc': 'Brings the Radical Civic Union back to power.'
        },
        'peronist': {
            'target_focus': 'ARG_the_peronist_movement',
            'name': 'Peronist Movement',
            'desc': 'Sparks the Peronist movement.'
        }
    }
    },
    'AUS': {
    'rule_name': 'SAH_aus_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'fatherland_front': {
            'target_focus': 'AUS_the_fatherland_front',
            'name': 'Historical Austria',
            'desc': 'Austria maintains the Fatherland Front.'
        },
        'austrofascism': {
            'target_focus': 'AUS_austrofascism',
            'name': 'Austrofascism',
            'desc': 'Austria fully embraces Fascism.'
        },
        'social_democrats': {
            'target_focus': 'AUS_the_social_democrats',
            'name': 'Social Democrats',
            'desc': 'Austria aligns with democratic socialism.'
        }
    }
    },
    'BEL': {
    'rule_name': 'SAH_bel_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 1,
    'starts': {
        'catholic_bloc': {
            'target_focus': 'BEL_the_catholic_bloc',
            'name': 'Historical Belgium',
            'desc': 'Belgium continues with the Catholic Bloc.'
        },
        'liberal_party': {
            'target_focus': 'BEL_the_liberal_party',
            'name': 'Liberal Party',
            'desc': 'The Liberal Party takes control.'
        },
        'rexist_party': {
            'target_focus': 'BEL_the_rexist_party',
            'name': 'Rexist Party (Fascist)',
            'desc': 'Degrelle and the Rexists seize power.'
        }
    }
    },
    'BUL': {
    'rule_name': 'SAH_bul_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'tsars_dictatorship': {
            'target_focus': 'BUL_the_tsars_dictatorship',
            'name': 'Historical Tsar',
            'desc': 'The Tsar maintains his royal dictatorship.'
        },
        'zveno': {
            'target_focus': 'BUL_zveno',
            'name': 'Zveno (Fascist)',
            'desc': 'The militarist Zveno takes control.'
        },
        'fatherland_front': {
            'target_focus': 'BUL_the_fatherland_front',
            'name': 'Fatherland Front (Communist)',
            'desc': 'Bulgaria turns Communist.'
        }
    }
    },
    'CHI': {
    'rule_name': 'SAH_chi_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'historical': {
            'target_focus': 'CHI_three_principles_of_the_people',
            'name': 'Historical China',
            'desc': 'China follows the Three Principles.'
        },
        'welfare': {
            'target_focus': 'CHI_welfare',
            'name': 'Welfare State',
            'desc': 'China commits to social welfare.'
        }
    }
    },
    'CHL': {
    'rule_name': 'SAH_chl_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'popular_front': {
            'target_focus': 'CHL_the_popular_front',
            'name': 'Popular Front (History)',
            'desc': 'Chile follows the Popular Front.'
        },
        'nacistas': {
            'target_focus': 'CHL_the_nacistas',
            'name': 'Nacistas (Fascist)',
            'desc': 'The Nacistas assume control.'
        }
    }
    },
    'COG': {
    'rule_name': 'SAH_cog_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'force_publique': {
            'target_focus': 'COG_the_force_publique',
            'name': 'Force Publique',
            'desc': 'Congo relies on the Force Publique.'
        },
        'evolues': {
            'target_focus': 'COG_the_evolues',
            'name': 'The Evolues',
            'desc': 'Congo empowers the Evolues.'
        }
    }
    },
    'CZE': {
    'rule_name': 'SAH_cze_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'political_direction': {
            'target_focus': 'CZE_political_direction',
            'name': 'Historical Czechoslovakia',
            'desc': 'Czechoslovakia maneuvers politics.'
        },
        'fascist_direction': {
            'target_focus': 'CZE_fascist_direction',
            'name': 'Fascist Direction',
            'desc': 'Czechoslovakia turns fascist.'
        },
        'communist_direction': {
            'target_focus': 'CZE_communist_direction',
            'name': 'Communist Direction',
            'desc': 'Czechoslovakia turns communist.'
        }
    }
    },
    'DEN': {
    'rule_name': 'SAH_den_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'social_democrats': {
            'target_focus': 'DEN_the_social_democrats',
            'name': 'Historical Denmark',
            'desc': 'Denmark retains the Social Democrats.'
        },
        'conservative': {
            'target_focus': 'DEN_the_conservative_peoples_party',
            'name': 'Conservative Party',
            'desc': 'The Conservative party rules.'
        }
    }
    },
    'EGY': {
    'rule_name': 'SAH_egy_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'anglo_treaty': {
            'target_focus': 'EGY_the_anglo_egyptian_treaty',
            'name': 'Historical Egypt',
            'desc': 'Egypt proceeds with the Anglo-Egyptian treaty.'
        },
        'wafd_party': {
            'target_focus': 'EGY_the_wafd_party',
            'name': 'Wafd Party',
            'desc': 'Egypt embraces the Wafd Party.'
        }
    }
    },
    'EST': {
    'rule_name': 'SAH_est_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'era_of_silence': {
            'target_focus': 'EST_the_era_of_silence',
            'name': 'Era of Silence',
            'desc': 'Estonia maintains the Era of Silence.'
        },
        'vaps_movement': {
            'target_focus': 'EST_the_vaps_movement',
            'name': 'Vaps Movement',
            'desc': 'The Vaps Movement takes over.'
        }
    }
    },
    'ETH': {
    'rule_name': 'SAH_eth_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'emperor': {
            'target_focus': 'ETH_the_emperor',
            'name': 'The Emperor',
            'desc': 'Ethiopia rallies behind the Emperor.'
        }
    }
    },
    'FIN': {
    'rule_name': 'SAH_fin_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'finnish_model': {
            'target_focus': 'FIN_the_finnish_model',
            'name': 'Historical Finland',
            'desc': 'Finland uses the Finnish Model.'
        },
        'lapua_movement': {
            'target_focus': 'FIN_the_lapua_movement',
            'name': 'Lapua Movement (Fascist)',
            'desc': 'The Lapua Movement succeeds.'
        },
        'red_guards': {
            'target_focus': 'FIN_the_red_guards',
            'name': 'Red Guards (Communist)',
            'desc': 'The Red Guards launch a revolution.'
        }
    }
    },
    'HUN': {
    'rule_name': 'SAH_hun_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'renounce_trianon': {
            'target_focus': 'HUN_renounce_the_treaty_of_trianon',
            'name': 'Historical Hungary',
            'desc': 'Hungary renounces Trianon.'
        },
        'king': {
            'target_focus': 'HUN_a_king_for_our_people',
            'name': 'Monarchist Hungary',
            'desc': 'Hungary invites a King.'
        },
        'communist': {
            'target_focus': 'HUN_the_communist_party',
            'name': 'Communist Hungary',
            'desc': 'Hungary turns Communist.'
        },
        'habsburg': {
            'target_focus': 'HUN_invite_the_habsburg_prince',
            'name': 'Habsburg Prince',
            'desc': 'Hungary restores Austria-Hungary.'
        }
    }
    },
    'IRQ': {
    'rule_name': 'SAH_irq_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'hashemite': {
            'target_focus': 'IRQ_the_hashemite_kingdom',
            'name': 'Hashemite Kingdom',
            'desc': 'Iraq stays a Hashemite Kingdom.'
        },
        'golden_square': {
            'target_focus': 'IRQ_the_golden_square',
            'name': 'Golden Square (Fascist)',
            'desc': 'The Golden Square executes a coup.'
        }
    }
    },
    'LAT': {
    'rule_name': 'SAH_lat_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'ulmainis': {
            'target_focus': 'LAT_the_ulmanis_dictatorship',
            'name': 'Ulmanis Dictatorship',
            'desc': 'Latvia under Ulmanis.'
        },
        'perkonkrusts': {
            'target_focus': 'LAT_the_perkonkrusts',
            'name': 'Perkonkrusts',
            'desc': 'The Perkonkrusts take power.'
        }
    }
    },
    'LIT': {
    'rule_name': 'SAH_lit_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'smetona': {
            'target_focus': 'LIT_the_smetona_dictatorship',
            'name': 'Smetona Dictatorship',
            'desc': 'Lithuania under Smetona.'
        },
        'iron_wolf': {
            'target_focus': 'LIT_the_iron_wolf',
            'name': 'Iron Wolf',
            'desc': 'The Iron Wolf ascends.'
        }
    }
    },
    'MAN': {
    'rule_name': 'SAH_man_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'obedience': {
            'target_focus': 'MAN_obedience',
            'name': 'Obedience',
            'desc': 'Manchukuo remains obedient to Japan.'
        },
        'assertiveness': {
            'target_focus': 'MAN_assertiveness',
            'name': 'Assertiveness',
            'desc': 'Manchukuo asserts its independence.'
        },
        'democratic': {
            'target_focus': 'MAN_the_democratic_party',
            'name': 'Democratic Party',
            'desc': 'Manchu transition to democracy.'
        },
        'communist': {
            'target_focus': 'MAN_the_communist_party',
            'name': 'Communist Party',
            'desc': 'Manchu communist revolution.'
        }
    }
    },
    'NOR': {
    'rule_name': 'SAH_nor_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'nygaardsvold': {
            'target_focus': 'NOR_the_nygaardsvold_cabinet',
            'name': 'Nygaardsvold Cabinet',
            'desc': 'Norway under Nygaardsvold.'
        },
        'quisling': {
            'target_focus': 'NOR_quisling_government',
            'name': 'Quisling Government (Fascist)',
            'desc': 'Quisling seizes control.'
        },
        'communist': {
            'target_focus': 'NOR_the_communist_party',
            'name': 'Communist Party',
            'desc': 'Norway adopts communism.'
        }
    }
    },
    'NZL': {
    'rule_name': 'SAH_nzl_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'labour': {
            'target_focus': 'NZL_the_labour_party',
            'name': 'Labour Party',
            'desc': 'New Zealand under the Labour Party.'
        }
    }
    },
    'PAR': {
    'rule_name': 'SAH_par_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'febrerista': {
            'target_focus': 'PAR_the_febrerista_revolution',
            'name': 'Febrerista Revolution',
            'desc': 'Paraguay proceeds post-revolution.'
        }
    }
    },
    'PER': {
    'rule_name': 'SAH_per_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'pahlavi': {
            'target_focus': 'PER_the_pahlavi_dynasty',
            'name': 'Pahlavi Dynasty',
            'desc': 'Iran empowers the Pahlavi Dynasty.'
        },
        'tudeh': {
            'target_focus': 'PER_the_tudeh_party',
            'name': 'Tudeh Party (Communist)',
            'desc': 'The Tudeh party incites revolution.'
        }
    }
    },
    'PHI': {
    'rule_name': 'SAH_phi_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'commonwealth': {
            'target_focus': 'PHI_the_commonwealth',
            'name': 'The Commonwealth',
            'desc': 'The Philippines remains a Commonwealth.'
        },
        'ganap': {
            'target_focus': 'PHI_the_ganap_party',
            'name': 'Ganap Party (Fascist)',
            'desc': 'The Ganap party asserts control.'
        },
        'hukbalahap': {
            'target_focus': 'PHI_the_hukbalahap',
            'name': 'Hukbalahap (Communist)',
            'desc': 'The Hukbalahap rebel.'
        }
    }
    },
    'POR': {
    'rule_name': 'SAH_por_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'estado_novo': {
            'target_focus': 'POR_the_estado_novo',
            'name': 'Estado Novo',
            'desc': 'Portugal proceeds with the Estado Novo.'
        },
        'popular_front': {
            'target_focus': 'POR_the_popular_front',
            'name': 'Popular Front',
            'desc': 'The Popular Front sweeps the government.'
        }
    }
    },
    'PRC': {
    'rule_name': 'SAH_prc_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'maoism': {
            'target_focus': 'PRC_maoism',
            'name': 'Maoism',
            'desc': 'Communist China under Mao.'
        },
        'orthodox_marxism': {
            'target_focus': 'PRC_orthodox_marxism',
            'name': 'Orthodox Marxism',
            'desc': 'Communist China under Orthodox Marxism.'
        },
        'social_democracy': {
            'target_focus': 'PRC_social_democracy',
            'name': 'Social Democracy',
            'desc': 'A transition towards Social Democracy.'
        }
    }
    },
    'SWI': {
    'rule_name': 'SAH_swi_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'federal_council': {
            'target_focus': 'SWI_the_federal_council',
            'name': 'Federal Council',
            'desc': 'Switzerland under the Federal Council.'
        }
    }
    },
    'URU': {
    'rule_name': 'SAH_uru_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'colorado': {
            'target_focus': 'URU_the_colorado_party',
            'name': 'Colorado Party',
            'desc': 'Uruguay relies on the Colorado Party.'
        }
    }
    },
    'WRL': {
    'rule_name': 'SAH_wrl_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'nationalists': {
            'target_focus': 'WRL_cooperate_with_the_nationalists',
            'name': 'Cooperate with Nationalists',
            'desc': 'Warlord aligns with Nationalists.'
        },
        'communists': {
            'target_focus': 'WRL_cooperate_with_the_communists',
            'name': 'Cooperate with Communists',
            'desc': 'Warlord aligns with Communists.'
        }
    }
    },
    'AFG': {
    'rule_name': 'SAH_afg_scenario_start_rule',
    'group_name': 'SAH_GAME_RULES_GROUP',
    'tier': 2,
    'starts': {
        'barakzai': {
            'target_focus': 'AFG_the_barakzai_dynasty',
            'name': 'Barakzai Dynasty',
            'desc': 'Afghanistan supports the Barakzai Dynasty.'
        }
    }
    },
}

# Rewards that should NOT be granted when auto-completing Day 1 starts
FILTERED_REWARDS = [
    "add_political_power",
    "add_army_experience",
    "add_navy_experience",
    "add_air_experience",
    "add_command_power",
    "custom_effect_tooltip",
    "add_named_threat",
    "start_civil_war",
    "country_event",
    "news_event",
    "declare_war",
    "create_wargoal"
]

def clean_rewards(reward_block: str) -> str:
    """Removes 'fluff' and conflicting event rewards so day 1 scenarios aren't overpowered/buggy."""
    if not reward_block: return ""
    lines = reward_block.split('\n')
    out: list[str] = []
    skip_depth = 0
    
    for line in lines:
        # Are we currently skipping a block?
        if skip_depth > 0:
            skip_depth += line.count('{')
            skip_depth -= line.count('}')
            continue
            
        # If any filtered keyword is in the line, we start skipping
        if any(keyword in line for keyword in FILTERED_REWARDS):
            if '{' in line:
                skip_depth += line.count('{')
                skip_depth -= line.count('}')
            continue
            
        out.append(line)
    return '\n'.join(out)

def read_all_focuses(mod_path: str = ".") -> Dict[str, Dict[str, Any]]:
    focuses: Dict[str, Dict[str, Any]] = {}
    focus_dir = os.path.join(mod_path, "common", "national_focus")
    
    for filename in os.listdir(focus_dir):
        if not filename.endswith('.txt'): continue
        filepath = os.path.join(focus_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()

        # Bracket parser to find focuses safely
        idx = 0
        while True:
            idx = content.find("focus = {", idx)
            if idx == -1: break

            bracket_count = 0
            start_idx = content.find("{", idx)
            end_idx = -1
            for i in range(start_idx, len(content)):
                if content[i] == '{': bracket_count += 1
                elif content[i] == '}':
                    bracket_count -= 1
                    if bracket_count == 0:
                        end_idx = i
                        break
            
            if end_idx != -1:
                block = content[idx:end_idx+1]
                id_match = re.search(r'^\s*id\s*=\s*([a-zA-Z0-9_\.]+)', block, re.MULTILINE)
                if id_match:
                    f_id = id_match.group(1)
                    
                    # Extract prerequisites 
                    # simple match, gets multiple if mutually exclusive or AND'd
                    prereqs = list(set(re.findall(r'focus\s*=\s*([a-zA-Z0-9_\.]+)', block)))
                    if f_id in prereqs: prereqs.remove(f_id)

                    # Extract rewards
                    reward_text = ""
                    r_idx = block.find("completion_reward = {")
                    if r_idx != -1:
                        rb_count = 0
                        r_start = block.find("{", r_idx)
                        for j in range(r_start, len(block)):
                            if block[j] == '{': rb_count += 1
                            elif block[j] == '}':
                                rb_count -= 1
                                if rb_count == 0:
                                    reward_text = block[r_start:j+1]
                                    break

                    focuses[f_id] = {
                        "file": filepath,
                        "prereqs": prereqs,
                        "reward_block": reward_text
                    }
            idx += 9
    return focuses

def get_focus_chain(target: str, all_focuses: Dict[str, Dict[str, Any]]) -> list[str]:
    """Recursively fetch the backward path required to trace this focus."""
    chain: list[str] = []
    visited: set[str] = set()
    
    def dfs(node: str) -> None:
        if node in visited: return
        visited.add(node)
        if node not in all_focuses: return
        
        for prereq in all_focuses[node]['prereqs']:
            dfs(prereq)
        chain.append(node)

    dfs(target)
    return chain

def generate():
    all_focuses = read_all_focuses()
    
    # 1. Output string for SAH_init_events.txt
    event_payload = "\t\tif = { limit = { date > 1938.1.1 }\n\t\t\tSAH_adjust_1939_units = yes\n\t\t\tSAH_purge_1939_ideas = yes\n\t\t}\n\n\t\t# --- AUTO-GENERATED SCENARIO STARTS ---\n"
    
    # 2. Output string for the Game Rules
    rules_payload = "\n# --- AUTO-GENERATED SCENARIO RULES ---\n"
    
    # 3. Track file bypasses needed { "filepath": { "focus_id": "bypass_code" } }
    file_injections: Dict[str, Dict[str, list[str]]] = {}
    
    # 4. Generate Localization Strings for SAH_game_rules_l_english.yml
    localization_payload = "====== 3. PASTE THIS AT THE BOTTOM OF localisation/english/SAH_game_rules_l_english.yml ======\n"

    for country, config in SCENARIOS.items():
        rule_name = config['rule_name']
        group_name = config['group_name']
        
        rules_payload += f"custom_game_rule = {{\n\tname = {rule_name}\n\tgroup = {group_name}\n\tdefault = normal_start\n"
        rules_payload += f"\toption = {{ name = normal_start text = SAH_{rule_name}_normal }}\n"
        
        localization_payload += f" {rule_name}: \"{country} Initial Scenario Start\"\n"
        localization_payload += f" SAH_{rule_name}_normal: \"Normal (Not started)\"\n"
        
        event_payload += f"\t\t{country} = {{\n"

        for opt_key, opt_data in config['starts'].items():
            rules_payload += f"\toption = {{ name = {opt_key} text = SAH_{rule_name}_{opt_key} }}\n"
            localization_payload += f" SAH_{rule_name}_{opt_key}: \"{opt_data['name']}\"\n"
            # Optional: Add description to tooltip if needed somewhere, but usually game rules just use names.
            
            target = opt_data['target_focus']
            chain = get_focus_chain(target, all_focuses)
            print(f"[{country}] {opt_key} requires: {chain}")
            
            # --- EVENTS PAYLOAD ---
            event_payload += f"\t\t\tif = {{\n\t\t\t\tlimit = {{ has_game_rule = {{ rule = {rule_name} option = {opt_key} }} }}\n"
            
            # Inject filtered rewards directly
            for f_id in chain:
                raw_reward = all_focuses[f_id]['reward_block']
                clean = clean_rewards(raw_reward)
                # Strip leading/trailing braces from clean block
                clean = clean.strip()
                if clean.startswith('{'): clean = clean[1:]
                if clean.endswith('}'): clean = clean[:-1]
                
                if clean.strip():
                    event_payload += f"\t\t\t\t# Rewards for {f_id}\n\t\t\t\t{clean.strip()}\n"


            # --- TIER LOGIC ---
            if 'historical' not in opt_key.lower() and 'infamous_decade' not in opt_key.lower() and 'catholic_bloc' not in opt_key.lower() and 'fatherland_front' not in opt_key.lower():
                tier = config.get('tier', 2)
                event_payload += "\t\t\t\t# Rebuilding State Tier logic\n"
                
                # 1936
                event_payload += "\t\t\t\tif = {\n\t\t\t\t\tlimit = { date < 1938.1.1 }\n"
                if tier == 1:
                    event_payload += "\t\t\t\t\tadd_ideas = SAH_devastating_recovery\n"
                elif tier == 2:
                    event_payload += "\t\t\t\t\tadd_ideas = SAH_prolonged_rebuilding\n"
                elif tier == 3:
                    event_payload += "\t\t\t\t\tadd_ideas = SAH_stabilized_regime\n"
                event_payload += "\t\t\t\t}\n"
                
                # 1939 (Degrades by 1)
                event_payload += "\t\t\t\tif = {\n\t\t\t\t\tlimit = { date > 1938.1.1 }\n"
                if tier == 1:
                    event_payload += "\t\t\t\t\tadd_ideas = SAH_prolonged_rebuilding\n"
                elif tier == 2:
                    event_payload += "\t\t\t\t\tadd_ideas = SAH_stabilized_regime\n"
                event_payload += "\t\t\t\t}\n"

            event_payload += "\t\t\t}\n"

            # --- BYPASS PAYLOAD ---
            for f_id in chain:
                filepath = all_focuses[f_id]['file']
                if filepath not in file_injections: file_injections[filepath] = {}
                # Append bypass code rule (allows multiple scenarios to bypass the same focus)
                if f_id not in file_injections[filepath]: file_injections[filepath][f_id] = []
                file_injections[filepath][f_id].append(f"has_game_rule = {{ rule = {rule_name} option = {opt_key} }}")

        rules_payload += "}\n\n"
        event_payload += "\t\t}\n"
        localization_payload += "\n"
    
    # Write summary for user to paste
    with open("scenario_generated_code.txt", "w", encoding="utf-8") as out:
        out.write("====== 1. PASTE THIS INTO common/custom_game_rules/SAH_custom_rules.txt ======\n")
        out.write(rules_payload)
        out.write("\n\n====== 2. PASTE THIS INTO events/SAH_init_events.txt (Inside immediate = {}) ======\n")
        out.write(event_payload)
        out.write("\n\n" + localization_payload)
        
    print("Generated rules, events, and localization to scenario_generated_code.txt!")
    
    # 4. Safely auto-inject bypasses
    # To keep your focus files fully safe, the script writes bypass configs that you can manually implement
    # OR injects them dynamically
    with open("scenario_generated_bypasses.txt", "w", encoding="utf-8") as bp:
        bp.write("====== ADD THESE TO YOUR FOCUS TREES ======\n")
        for filepath, injects in file_injections.items():
            bp.write(f"\n--- File: {os.path.basename(filepath)} ---\n")
            for f_id, conditions in injects.items():
                bp.write(f"Focus: id = {f_id}\n")
                bp.write("Add this block right underneath cost/x/y:\n")
                conds = "\n\t\t\t\t".join(conditions)
                bp.write(f"\t\tbypass = {{\n\t\t\tOR = {{\n\t\t\t\t{conds}\n\t\t\t}}\n\t\t}}\n\n")
    print("Generated bypass instructions to scenario_generated_bypasses.txt")

if __name__ == "__main__":
    generate()
