from d20 import *
import pandas as pd

db = pd.read_csv("data/Damage Base.csv")


def manual_roll(dice):
    return roll(dice)


def rolled_damage(damage: int):
    db_dict = db[db["Damage Base"] == damage].to_dict(orient='list')
    return roll(db_dict["Rolled Damage"][0])
