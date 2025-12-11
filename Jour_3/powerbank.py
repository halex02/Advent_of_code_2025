class Battery:
    def __init__(self, power=None, powered=False):
        self.power = power
        self.powered = powered
    
    def set_power(self, power):
        self.power = power
    
    def get_power(self):
        return self.power
        
    def print_power(self):
        print("la batterie a une puissance de ", self.get_power(),".")
    
    def switch_battery(self):
        self.powered = not self.powered
    
    def get_battery_status(self):
        return self.powered
    
    def print_battery_status(self):
        if self.powered:
            print("La batterie est allumée.")
        else:
            print("La batterie est éteinte.")
    
class PowerBank:
    def __init__(self):
        self.bank = []
        self.power_produced = 0
    
    def add_battery(self, power):
        self.bank.append(Battery(power))
        
    def remove_battery(self):
        return self.bank.pop()
    
    def switch_battery(self, battery_id):
        self.bank[battery_id].switch_battery()
        return self.bank[battery_id].get_battery_status()
    
    def calculate_power_produced(self):
        power = ""
        for battery in self.bank:
            if battery.get_battery_status() && len(power)<2:
                power = power+str(battery.get_power())
        self.power_produced = int(power)
        return self.power_produced()
        
    def get_power_produced(self):
        return self.power_produced
    
class Solver:
    def __init__(self):
        self.powerbanks_t = []
        self.power_produced = 0
        
    def input_importer():
        with open("input.txt", "r") as f:
            while True:
                line = f.readline()
                if line = "":
                    break
                powerbank = PowerBank()
                for i in line:
                    powerbank.add_battery(int(i))
                self.powerbanks_t.append(powerbank)
    
    def activate_powerbanks():
        for powerbank in self.powerbanks_t:
            powerbank.activate_powerbank()
            powerbank.calculate_power_produced()
            self.power_produced = self.power_produced + powerbank.get_power_produced()
