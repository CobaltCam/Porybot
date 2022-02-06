class HitPointTracker:
    def __init__(self):
        self.hit_points = {}
        self.num = 1

    def encounter_start(self):
        self.hit_points.clear()
        return "```You have cleared the hit point counters. To add a combatant please use the command $add to add" \
               "combatants```"

    def add_combatant(self, name: str, hitpoints: int):
        new_name = name + str(self.num)
        self.num += 1
        self.hit_points.update({new_name: hitpoints})
        return f"```{new_name} was added to combat```"

    def check_combatant(self, combatant: str):
        return f"```{combatant}: {self.hit_points[combatant]}```"

    def remove_combatant(self, combatant: str):
        self.hit_points.pop(combatant)
        return f"```{combatant} has been removed from combat```"

    def update_hitpoints(self, combatant: str, update: int):
        new_hitpoints = self.hit_points[combatant] + update
        self.hit_points[combatant] = new_hitpoints
        if new_hitpoints <= 0:
            self.hit_points.pop(combatant)
            return f"{combatant} dead, removed from combat"
        else:
            return f"```Hitpoints: {self.hit_points[combatant]}```"

    def list_hitpoints(self):
        return f"```{self.hit_points}```"
