import pandas as pd

# Establish all csv files for later reference

abilities = pd.read_csv('data/Abilities Data.csv')
pokemon = pd.read_csv('data/Pokemon Data.csv')
moves = pd.read_csv('data/Moves Data.csv')
natures = pd.read_csv('data/Nature Data.csv')
items = pd.read_csv('data/Item Data.csv')
pokeedges = pd.read_csv('data/Poke Edges.csv')
features = pd.read_csv('data/Features Data.csv')
classes = pd.read_csv('data/Class Data.csv')
edges = pd.read_csv('data/Edges Data.csv')
food = pd.read_csv('data/Food Data.csv')
weather = pd.read_csv('data/Weather Data.csv')
capabilities = pd.read_csv('data/Capability Data.csv')
held_items = pd.read_csv('data/Held Items.csv')
status = pd.read_csv('data/Status Data.csv')
db = pd.read_csv('data/Damage Base.csv')
type_effect = pd.read_csv('data/Type Effectiveness.csv')
keyword = pd.read_csv('data/Keyword Data.csv', encoding='Windows-1252')


def get_ability(abil_name: str):
    """Iterates through abilities dataframe and creates a list from which the information is formatted in an f-string
    and returned"""
    ability = []
    for i, row in abilities.iterrows():
        if abil_name == row['Name']:
            ability.append(row['Name'])
            ability.append(row['Frequency'])
            ability.append(row['Effect'])
            ability.append(row['Trigger'])
            ability.append(row['Target'])
    if pd.isna(ability[3]) and pd.isna(ability[4]):
        ability_info = f"```\n{ability[0]}\nFrequency: {ability[1]}\n{ability[2]}```"
    elif pd.isna(ability[3]):
        ability_info = f"```\n{ability[0]}\nTarget: {ability[4]}\nFrequency: {ability[1]}\n{ability[2]}```"
    elif pd.isna(ability[4]):
        ability_info = f"```\n{ability[0]}\nTrigger: {ability[3]}\nFrequency: {ability[1]}\n{ability[2]}```"
    else:
        ability_info = f"```\n{ability[0]}\nTarget: {ability[4]}\nTrigger: {ability[3]}\nFrequency: {ability[1]}\n" \
                       f"{ability[2]}```"
    return ability_info


def get_capability(cap_name: str):
    """Iterates through capabilities dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    capability = []
    for i, row in capabilities.iterrows():
        if cap_name == row['Capability']:
            capability.append(row['Capability'])
            capability.append(row['Description'])
    capability_info = f'```\n{capability[0]}:\n{capability[1]}```'
    return capability_info


def get_class_mechanic(class_name: str):
    """Iterates through classes dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    trainer_class = []
    for i, row in classes.iterrows():
        if class_name == row['Class Name']:
            trainer_class.append(row['Class Name'])
            trainer_class.append(row['Mechanic'])
            trainer_class.append(row['Effect'])
    class_info = f'```\n{trainer_class[0]}:\n{trainer_class[1]}\n{trainer_class[2]}```'
    return class_info


def get_edge(edge_name):
    """Iterates through edges dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    edge = []
    for i, row in edges.iterrows():
        if edge_name == row['Name']:
            edge.append(row['Name'])
            edge.append(row['Prerequisites'])
            edge.append(row['Effect'])
    edge_info = f'```\n{edge[0]}\nPrerequisites: {edge[1]}\n{edge[2]}```'
    return edge_info


def get_feat(feat_name):
    """Iterates through features dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    feat = []
    for i, row in features.iterrows():
        if feat_name == row['Name']:
            feat.append(row['Name'])
            feat.append(row['Tags'])
            feat.append(row['Prerequisites'])
            feat.append(row['Frequency/Action'])
            feat.append(row['Effects'])
    feat_info = f'```\n{feat[0]}\n{feat[1]}\nPrerequisites: {feat[2]}\n{feat[3]}\n{feat[4]}```'
    return feat_info


def get_food(food_name):
    """Iterates through food dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    foods = []
    for i, row in food.iterrows():
        if food_name == row['Food Item']:
            foods.append(row['Food Item'])
            foods.append(row['Digestion Buff'])
    food_info = f'```\n{foods[0]}:\n{foods[1]}```'
    return food_info


def get_held_item(held_name):
    """Iterates through held_items dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    held_item = []
    for i, row in held_items.iterrows():
        if held_name == row['Held Item']:
            held_item.append(row['Held Item'])
            held_item.append(row['Description'])
    held_info = f'```\n{held_item[0]}\n{held_item[1]}```'
    return held_info


# Need to rework the csv file a little as items are currently seperated into categories
def get_item(item_name):
    """Iterates through items dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    items_list = []
    for i, row in items.iterrows():
        if item_name == row['Name']:
            items_list.append(row['Name'])
            items_list.append(row['Cost'])
            items_list.append(row['Description'])
    items_list = f'```\n{items_list[0]}\nCost: {items_list[1]}\n{items_list[2]}```'
    return items_list


def get_move(move_name):
    """Iterates through moves dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    move_list = []
    for i, row in moves.iterrows():
        if move_name == row['Name']:
            move_list.append(row['Name'])
            move_list.append(row['Category'])
            move_list.append(row['Type'])
            move_list.append(row['Damage Base'])
            move_list.append(row['Frequency'])
            move_list.append(row['AC'])
            move_list.append(row['Range'])
            move_list.append(row['Effects'])
            move_list.append(row['Contest Stats'])
    move_info = f'```\n{move_list[0]}\nCategory: {move_list[1]}\nType: {move_list[2]}\nDamage Base: {move_list[3]}\n' \
                f'Frequency: {move_list[4]}\nAC: {move_list[5]}\nRange: {move_list[6]}\nEffects: {move_list[7]}\n' \
                f'Contest Stats: {move_list[8]}```'
    return move_info


def get_nature(nature_name):
    """Iterates through natures dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    nature = []
    for i, row in natures.iterrows():
        if nature_name == row['Nature']:
            nature.append(row['Nature'])
            nature.append(row['Raise'])
            nature.append(row['Lower'])
            nature.append(row['Liked Flavor'])
            nature.append(row['Disliked Flavor'])
    nature_info = f'```\n{nature[0]}\nRaise: {nature[1]}\nLower: {nature[2]}\nLiked Flavor: {nature[3]}\n' \
                  f'Disliked Flavor: {nature[4]}```'
    return nature_info


def get_poke_edge(pedge_name: str):
    """Iterates through pokeedges dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    pokeedge = []
    for i, row in pokeedges.iterrows():
        if pedge_name == row['Name']:
            pokeedge.append(row['Name'])
            pokeedge.append(row['Prerequisites'])
            pokeedge.append(row['Cost'])
            pokeedge.append(row['Effect'])
    pokedge_info = f'```\n{pokeedge[0]}\nPrerequisite: {pokeedge[1]}\nCost: {pokeedge[2]}\n{pokeedge[3]}```'
    return pokedge_info


def get_status(status_name: str):
    """Iterates through status dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    status_list = []
    for i, row in status.iterrows():
        if status_name == row['Status']:
            status_list.append(row['Status'])
            status_list.append(row['Affliction Type'])
            status_list.append(row['Effect'])
    status_info = f'```\n{status_list[0]}\nAffliction Type: {status_list[1]}\n{status_list[2]}```'
    return status_info


def get_weather(weather_name: str):
    """Iterates through weather dataframe and creates a list from which the information is formatted in an f-string
        and returned"""
    weather_list = []
    for i, row in weather.iterrows():
        if weather_name == row['Weather']:
            weather_list.append(row['Weather'])
            weather_list.append(row['Effect'])
    weather_info = f'```\n{weather_list[0]}\n{weather_list[1]}```'
    return weather_info


def pokemon_info(poke_name):
    """Iterates through pokemon dataframe and creates a list from which the information is formatted in an f-string
    chekcing for missing data at list index 2 and leaving that value out of the f-string if it is found then returned
    """
    poke_list = []
    for i, row in pokemon.iterrows():
        if poke_name == row['Pokemon']:
            poke_list.append(row['Pokemon'])
            poke_list.append(row['Type 1'])
            poke_list.append(row['Type 2'])
            poke_list.append(row['HP'])
            poke_list.append(row['Attack'])
            poke_list.append(row['Defense'])
            poke_list.append(row['Special Attack'])
            poke_list.append(row['Special Defense'])
            poke_list.append(row['Speed'])

    if pd.isna(poke_list[2]):
        basic_info = f'```\n{poke_list[0]}\nType: {poke_list[1]}\nHP: {poke_list[3]}\nAttack: {poke_list[4]}' \
                     f'\nDefense: {poke_list[5]}\nSpecial Attack: {poke_list[6]}\nSpecial Defense: {poke_list[7]}' \
                     f'\nSpeed:{poke_list[8]}```'
    else:
        basic_info = f'```\n{poke_list[0]}\nType: {poke_list[1]}/{poke_list[2]}\nHP: {poke_list[3]}\n' \
                     f'Attack: {poke_list[4]}\nDefense: {poke_list[5]}\nSpecial Attack: {poke_list[6]}\n' \
                     f'Special Defense: {poke_list[7]}\nSpeed:' \
                     f'{poke_list[8]}```'
    return basic_info


def pokemon_capabilities(poke_name):
    """Iterates through pokemon dataframe and creates a list from which the information is formatted in an f-string
    chekcing for missing data at list index 2 and leaving that value out of the f-string if it is found, any missing
    data is replaced with - character"""
    pokecap_list = []
    for i, row in pokemon.iterrows():
        if poke_name == row['Pokemon']:
            pokecap_list.append([row['Pokemon']])
            pokecap_list.append(row['Type 1'])
            pokecap_list.append(row['Type 2'])
            pokecap_list.append(row['Overland'])
            pokecap_list.append(row['Sky'])
            pokecap_list.append(row['Swim'])
            pokecap_list.append(row['Levitate'])
            pokecap_list.append(row['Burrow'])
            pokecap_list.append(row['H Jump'])
            pokecap_list.append(row['L Jump'])
            pokecap_list.append(row['Power'])
            pokecap_list.append(row['Naturewalk'])
            pokecap_list.append(row['Capability 1'])
            pokecap_list.append(row['Capability 2'])
            pokecap_list.append(row['Capability 3'])
            pokecap_list.append(row['Capability 4'])
            pokecap_list.append(row['Capability 5'])
            pokecap_list.append(row['Capability 6'])
            pokecap_list.append(row['Capability 7'])
            pokecap_list.append(row['Capability 8'])
            pokecap_list.append(row['Capability 9'])
            pokecap_list.append(row['Weight'])

    for i in pokecap_list:
        if pd.isna(i):
            '-'
    if pd.isna(pokecap_list[2]):
        pokecap_info = f'```\n{pokecap_list[0]}\nType: {pokecap_list[1]}\nOverland: {pokecap_list[3]}\n' \
                       f'Sky: {pokecap_list[4]}\nSwim: {pokecap_list[5]}\nLevitate: {pokecap_list[6]}\n' \
                       f'Burrow: {pokecap_list[7]}\nHigh Jump: {pokecap_list[8]}\nLong Jump: {pokecap_list[9]}\n' \
                       f'Power: {pokecap_list[10]}\nNaturewalk: {pokecap_list[11]}\nCapabilities: {pokecap_list[12]},' \
                       f' {pokecap_list[13]}, {pokecap_list[14]}, {pokecap_list[15]}, {pokecap_list[16]}, ' \
                       f'{pokecap_list[17]}, {pokecap_list[18]}, {pokecap_list[19]}```'
    else:
        pokecap_info = f'```\n{pokecap_list[0]}\nType: {pokecap_list[1]}/{pokecap_list[2]}\nOverland:' \
                       f' {pokecap_list[3]}\nSky: {pokecap_list[4]}\nSwim: {pokecap_list[5]}\nLevitate:' \
                       f' {pokecap_list[6]}\n Burrow: {pokecap_list[7]}\nHigh Jump: {pokecap_list[8]}\nLong Jump:' \
                       f' {pokecap_list[9]}\nPower: {pokecap_list[10]}\nNaturewalk: {pokecap_list[11]}\nCapabilities: ' \
                       f'{pokecap_list[12]},{pokecap_list[13]}, {pokecap_list[14]}, {pokecap_list[15]}, ' \
                       f'{pokecap_list[16]}, {pokecap_list[17]}, {pokecap_list[18]}, {pokecap_list[19]}```'
    return pokecap_info


def damage_base(db_num: int):
    """Iterates through db dataframe and creates a list from which the information is formatted in an f-string
        returning the formatted string"""
    db_list = []
    for i, row in db.iterrows():
        if db_num == row['Damage Base']:
            db_list.append(row['Damage Base'])
            db_list.append(row['Rolled Damage'])
            db_list.append(row['Set Damage'])
    db_info = f'```\nDamage Base: {db_list[0]}\nRolled Damage: {db_list[1]}\nSet Damage: {db_list[2]}```'
    return db_info


def get_type_effect(pkmn_type: str):
    """Iterates through pokemon dataframe and creates a list from which the information is formatted in an f-string
        checking for missing data at list index 3 and leaving that value out of the f-string if it is found. returns
        formatted f-string"""
    type_list = []
    for i, row in type_effect.iterrows():
        if pkmn_type == row['Type']:
            type_list.append(row['Type'])
            type_list.append(row['Vulnerable'])
            type_list.append(row['Resistant'])
            type_list.append(row['Immune'])
    if pd.isna(type_list[3]):
        type_info = f'```\n{type_list[0]}\nVulnerable: {type_list[1]}\nResistant: {type_list[2]}```'
    else:
        type_info = f'```\n{type_list[0]}\nVulnerable: {type_list[1]}\nResistant: {type_list[2]}\n' \
                    f'Immune: {type_list[3]}```'
    return type_info


def get_keyword(keyword_name: str):
    keyword_list = []
    for i, row in keyword.iterrows():
        if keyword_name == row['Keyword']:
            keyword_list.append(row['Keyword'])
            keyword_list.append(row['Description'])
    keyword_info = f'```\n{keyword_list[0]}\n{keyword_list[1]}```'
    return keyword_info
