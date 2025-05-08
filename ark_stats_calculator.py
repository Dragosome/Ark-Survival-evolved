# @Version : 1.0
# @Author  : Drago
# @File    : ark_stats_calculator.py
# @Time    : 2025/5/7 18:28

class Dino:
    wild_level = 1
    # crafting_skill 默认为0
    total_level = 1 + 255 * 7

    def __init__(self, health_b, health_iw, health_id,
                 stamina_b, stamina_iw, stamina_id,
                 oxygen_b, oxygen_iw, oxygen_id,
                 food_b, food_iw, food_id,
                 weight_b, weight_iw, weight_id,
                 melee_b, melee_iw, melee_id,
                 speed_b, speed_iw, speed_id,
                 health_ta, health_tm,
                 melee_ta, melee_tm):
        self.health_b = health_b
        self.health_iw = health_iw
        self.health_id = health_id
        self.stamina_b = stamina_b
        self.stamina_iw = stamina_iw
        self.stamina_id = stamina_id
        self.oxygen_b = oxygen_b
        self.oxygen_iw = oxygen_iw
        self.oxygen_id = oxygen_id
        self.food_b = food_b
        self.food_iw = food_iw
        self.food_id = food_id
        self.weight_b = weight_b
        self.weight_iw = weight_iw
        self.weight_id = weight_id
        self.melee_b = melee_b
        self.melee_iw = melee_iw
        self.melee_id = melee_id
        self.speed_b = speed_b
        self.speed_iw = speed_iw
        self.speed_id = speed_id
        self.health_ta = health_ta
        self.health_tm = health_tm
        self.melee_ta = melee_ta
        self.melee_tm = melee_tm

    def calculator(self, attribute, b, iw, id, ib=1, ta=0, tm=0):
        max_level = 255
        max_stat = 0
        best_level = 0

        for lw in range(0, max_level + 1):
            # V = (B × (1 + Lw × Iw × IwM) × TBHM × (1 + IB × 0.2 × IBM) + Ta × TaM) ×
            # (1 + TE × Tm × TmM) × (1 + Ld × Id × IdM)
            # ((基础属性 + 野生等级 * 野生增加) * (1 + 留痕 * 0.2) + 加法加成) *
            # (1 + 乘法加成) * (1 + (总等级 - 野生等级) * 驯养增加)
            v = (((b + lw * iw) * (1 + ib * 0.2) + ta) *
                 (1 + tm) * (1 + (max_level - lw) * id))
            if v > max_stat:
                max_stat = v
                best_level = lw

        self.wild_level += best_level
        print(f"{attribute} 的最佳等级是 {best_level}，驯服升级是 {255 - best_level}，"
              f"对应数值为 {max_stat:.2f}")

    def print_level(self):
        print("=" * 40)
        self.wild_level = 1
        self.calculator("health", self.health_b,
                        self.health_iw, self.health_id, 1,
                        self.health_ta, self.health_tm)
        self.calculator("stamina", self.stamina_b,
                        self.stamina_iw, self.stamina_id, 0)
        self.calculator("oxygen", self.oxygen_b,
                        self.oxygen_iw, self.oxygen_id, 0)
        self.calculator("food", self.food_b,
                        self.food_iw, self.food_id)
        self.calculator("weight", self.weight_b,
                        self.weight_iw, self.weight_id)
        self.calculator("melee", self.melee_b,
                        self.melee_iw, self.melee_id, 1,
                        self.melee_ta, self.melee_tm)
        self.calculator("speed", self.speed_b,
                        self.speed_iw, self.speed_id)
        print(f"野生等级为 {self.wild_level}，驯养升级为 {1786 - self.wild_level}")


giganotosaurus = Dino(80000, 40, 0.0004,
                      400, 0.2, 0.01,
                      150, 0.375, 0.025,
                      4000, 10, 0.025,
                      700, 7, 0.01,
                      1, 0.05, 0.02,
                      1, 0, 0.0031,
                      -63000, 0, -0.8, 0)
giganotosaurus.print_level()

spino = Dino(700, 140, 0.11475,
             350, 35, 0.1,
             650, 65, 0.1,
             2600, 260, 0.1,
             350, 7, 0.04,
             1, 0.05, 0.04,
             1, 0, 0.01,
             0.25, 0, 0.25, 0.4)
spino.print_level()

rex = Dino(1100, 220, 0.11475,
           420, 42, 0.1,
           150, 15, 0.1,
           3000, 300, 0.1,
           500, 10, 0.04,
           1, 0.05, 0.04,
           1, 0, 0.01,
           0.25, 0, 0.25, 0.4)
rex.print_level()
