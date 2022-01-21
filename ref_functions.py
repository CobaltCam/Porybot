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


def get_ability(abil_name):
    """Finds series that matches user input and formats data into a dictionary, checking for missing data and adjusting
     output accordingly. Returns f-string using dictionary indexes"""
    ability_dict = abilities[abilities['Name'] == abil_name].to_dict(orient='list')
    if pd.isna(ability_dict['Trigger'][0]) and pd.isna(ability_dict['Target'][0]):
        return f"```\n{ability_dict['Name'][0]}\nFrequency: {ability_dict['Frequency'][0]}\n" \
               f"{ability_dict['Effect'][0]}```"
    elif pd.isna(ability_dict['Trigger'][0]):
        return f"```\n{ability_dict['Name'][0]}\nTarget: {ability_dict['Target'][0]}\nFrequency:" \
               f" {ability_dict['Frequency'][0]}\n{ability_dict['Effect'][0]}```"
    elif pd.isna(ability_dict['Target'][0]):
        return f"```\n{ability_dict['Name'][0]}\nTrigger: {ability_dict['Trigger'][0]}\nFrequency:" \
               f" {ability_dict['Frequency'][0]}\n{ability_dict['Effect'][0]}```"
    else:
        return f"```\n{ability_dict['Name'][0]}\nTarget: {ability_dict['Target'][0]}\n" \
               f"Trigger: {ability_dict['Trigger'][0]}\nFrequency:{ability_dict['Frequency'][0]}\n" \
               f"{ability_dict['Effect'][0]}```"


def get_capability(cap_name: str):
    """Finds series that matches user input and formats data into a dictionary"""
    cap_dict = capabilities[capabilities['Capability'] == cap_name].to_dict(orient='list')
    return f'```\n{cap_dict["Capability"][0]}\n{cap_dict["Description"][0]}```'


def get_class_mechanic(class_name: str):
    classes_dict = classes[classes['Class Name'] == class_name].to_dict(orient='list')
    return f'```\n{classes_dict["Class Name"][0]}\n{classes_dict["Mechanic"][0]}: {classes_dict["Effect"][0]}```'


def get_edge(edge_name: str):
    edge_dict = edges[edges['Name'] == edge_name].to_dict(orient='list')
    return f'```\n{edge_dict["Name"][0]}\nPrerequisites: {edge_dict["Prerequisites"][0]}\nEffect:' \
           f' {edge_dict["Effect"][0]}```'


def get_feat(feat_name: str):
    feat_dict = features[features['Name'] == feat_name].to_dict(orient='list')
    if pd.isna(feat_dict["Tags"][0]):
        return f'```\n{feat_dict["Name"][0]}\nPrerequisites: {feat_dict["Prerequisites"][0]}\n' \
               f'Frequency/Action: {feat_dict["Frequency/Action"][0]}\n{feat_dict["Effect"][0]}```'
    else:
        return f'```\n{feat_dict["Name"][0]}\n{feat_dict["Tags"][0]}\nPrerequisites: {feat_dict["Prerequisites"][0]}\n' \
               f'Frequency/Action: {feat_dict["Frequency/Action"][0]}\n{feat_dict["Effects"][0]}```'


def get_food(food_name: str):
    food_dict = food[food['Food Item'] == food_name].to_dict(orient='list')
    return f'```\n{food_dict["Food Name"][0]}\n{food_dict["Digestion Buff"][0]}```'


def get_held_item(held_name):
    held_item_dict = held_items[held_items['Held Items'] == held_name].to_dict(orient='list')
    return f'```\n{held_item_dict["Held Item"][0]}\n{held_item_dict["Description"][0]}```'


def get_item(item_name):
    item_dict = items[items['Name'] == item_name].to_dict(orient='list')
    return f'```\n{item_dict["Name"]}\nCost: {item_dict["Cost"][0]}\n{item_dict["Description"][0]}```'


def get_move(move_name):
    move_dict = moves[moves['Name'] == move_name].to_dict(orient='list')
    return f'```\n{move_dict["Name"][0]}\nCategory: {move_dict["Category"][0]}\nType: {move_dict["Type"][0]}\n' \
           f'DB: {move_dict["Damage Base"][0]}\nFrequency: {move_dict["Frequency"][0]}\nAC: {move_dict["AC"][0]}' \
           f'\nRange: {move_dict["Range"][0]}\nEffects: {move_dict["Effects"][0]}```'


def get_nature(nature_name):
    nature_dict = natures[natures['Nature'] == nature_name].to_dict(orient='list')
    return f'```\n{nature_dict["Nature"]}\nRaise: {nature_dict["Raise"][0]}\nLower: {nature_dict["Lower"][0]}' \
           f'\nLikes: {nature_dict["Liked Flavor"][0]}\nDislikes {nature_dict["Disliked Flavor"]}```'


def get_poke_edge(pedge_name: str):
    pokeedge_dict = pokeedges[pokeedges["Name"] == pedge_name].to_dict(orient='list')
    return f'```\n{pokeedge_dict["Name"][0]}\nPrerequisites: {pokeedge_dict["Prerequisites"][0]}' \
           f'\nCost {pokeedge_dict["Cost"][0]}\n{pokeedge_dict["Effect"][0]}```'


def get_status(status_name: str):
    status_dict = status[status['Status'] == status_name].to_dict(orient='list')
    return f'```\n{status_dict["Status"][0]}\nAffliction Type: {status_dict["Affliction Type"][0]}\n' \
           f'{status_dict["Effect"][0]}```'


def get_weather(weather_name: str):
    weather_dict = weather[weather["Weather"] == weather_name].to_dict(orient='list')
    return f'```\n{weather_dict["Weather"][0]}\n{weather_dict["Effect"][0]}```'


def pokemon_info(poke_name: str):
    bs_dict = pokemon[pokemon['Pokemon'] == poke_name].to_dict(orient='list')
    if pd.isna(bs_dict["Type 2"]):
        return f'```\n{bs_dict["Pokemon"][0]}\n{bs_dict["Type 1"][0]}\nHP: {bs_dict["HP"][0]}\n' \
               f'Attack: {bs_dict["Attack"][0]}\nDefense: {bs_dict["Defense"][0]}\nSpecial Attack ' \
               f'{bs_dict["Special Attack"][0]}\nSpecial Defense {bs_dict["Special Defense"][0]}\n' \
               f'Speed: {bs_dict["Speed"][0]}```'
    else:
        return f'```\n{bs_dict["Pokemon"][0]}\n{bs_dict["Type 1"][0]}/{bs_dict["Type 2"][0]}\n' \
               f'HP: {bs_dict["HP"][0]}\nAttack: {bs_dict["Attack"][0]}\nDefense: {bs_dict["Defense"][0]}' \
               f'\nSpecial Attack {bs_dict["Special Attack"][0]}\nSpecial Defense {bs_dict["Special Defense"][0]}\n' \
               f'Speed: {bs_dict["Speed"][0]}```'


def pokemon_capabilities(poke_name):
    pokecap_dict = pokemon[pokemon['Pokemon'] == poke_name].to_dict(orient='list')

    for i in pokecap_dict:
        if pd.isna(pokecap_dict[i][0]):
            pokecap_dict[i][0] = "-"

    return f'```\n{pokecap_dict["Pokemon"][0]}\nOverland: {pokecap_dict["Overland"][0]}\nSky: ' \
           f'{pokecap_dict["Sky"][0]}\nSwim: {pokecap_dict["Swim"][0]}\nLevitate: {pokecap_dict["Levitate"][0]}' \
           f'\nBurrow: {pokecap_dict["Burrow"][0]}\nHigh Jump: {pokecap_dict["H Jump"][0]}\nLong Jump: ' \
           f'{pokecap_dict["L Jump"][0]}\nPower: {pokecap_dict["Power"][0]}\nNaturwalk: ' \
           f'{pokecap_dict["Naturewalk"][0]}\n{pokecap_dict["Capability 1"][0]}\n{pokecap_dict["Capability 2"][0]}' \
           f'\n{pokecap_dict["Capability 3"][0]}\n{pokecap_dict["Capability 4"][0]}\n{pokecap_dict["Capability 5"][0]}' \
           f'\n{pokecap_dict["Capability 6"][0]}\n{pokecap_dict["Capability 7"][0]}\n' \
           f'{pokecap_dict["Capability 8"][0]}\n{pokecap_dict["Capability 9"][0]}```'



def damage_base(db_num: int):
    db_dict = db[db['Damage Base'] == db_num].to_dict(orient='list')
    return f'```\nDamage Base: {db_dict["Damage Base"][0]}\nRolled Damage: {db_dict["Rolled Damage"][0]}\nSet Damage:' \
           f'{db_dict["Set Damage"][0]}```'


def get_type_effect(pkmn_type: str):
    type_effect_dict = type_effect[type_effect["Type"] == pkmn_type].to_dict(orient='list')
    if pd.isna(type_effect_dict["Immune"][0]):
        type_effect_dict["Immune"][0] = "-"

    return f'```\nType: {type_effect_dict["Type"][0]}\nVulnerable: {type_effect_dict["Vulnerable"][0]}\n' \
           f'Resistant: {type_effect_dict["Resistant"][0]}\nImmune: {type_effect_dict["Immune"][0]}```'


def get_keyword(keyword_name: str):
    keyword_dict = keyword[keyword['Keyword'] == keyword_name].to_dict(orient='list')
    return f'```\n{keyword_dict["Keyword"][0]}\n{keyword_dict["Description"][0]}```'
