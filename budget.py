class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []
        self.wsum = 0
    
    # String Ausgabe definieren
    def __str__(self):
        string = ""
        next_string = ""
        first_string = self.name.center(30, "*") + "\n"
        last_string = f"Total: {self.balance}".ljust(10)
        for item in self.ledger:
            text = item["description"]
            price = "{:.2f}".format(item["amount"])
            next_string += f"{text[:23]}".ljust(23) + f"{price}".rjust(7) + "\n"
        string = first_string + next_string + last_string
        return string
          
    def deposit(self, amount, description = ''):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})
        return self.ledger
        
        
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount) == True:
            self.wsum += amount
            amount = -1 * amount
            self.balance += amount
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False
        
    def transfer(self, amount, DestinationCategory):
        if self.check_funds(amount) == True:
            self.withdraw(amount, ("Transfer to " + DestinationCategory.name)) 
            DestinationCategory.deposit( amount, ("Transfer from " + self.name))
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def get_name(self):
        return self.name
    
    def get_ledger(self):
        return self.ledger
    
    def get_withdraw_sum(self):
        wert = int(self.wsum)
        return wert
    
    
def names_spend_chart(categories):
    name_string = ""
    for cat in categories:
        name_string += (cat.get_name() + " ")
    return name_string    
    
def withdraw_categorie(cat):
    withdraw_sum = 0
    for item in cat.ledger:
        if item["amount"] < 0:
            withdraw_sum += item["amount"]
    return withdraw_sum

def create_spend_chart(categories):
    # Werte für Ausgabe ermitteln
    withdraw_sum_entry = 0
    withdraw_sum_all = 0
    budget_spend_all_names = []
    budget_spend_all_sum = []
    
    for item in range(len(categories)):
        name = (categories[item].get_name())
        withdraw_sum_entry = (categories[item].get_withdraw_sum())
        budget_spend_all_names.append(name)
        budget_spend_all_sum.append(withdraw_sum_entry)
        withdraw_sum_all += withdraw_sum_entry
    
    
    # grafische Worte für Prozente berechnen
    ysign = []
    for wert in budget_spend_all_sum:
        #prozent = ((round(wert / withdraw_sum_all , 1)) * 100)
        prozent = (( wert / withdraw_sum_all ) * 100)
        # Anzahl o
        ocount = (int(prozent / 10)) + 1
        ysign.append(("".ljust((ocount),"o")).rjust(11))
    
    # Wortlänge für Beschriftung
    xlength = 0
    for name in range(len(budget_spend_all_names)):
        if len(budget_spend_all_names[name]) >  xlength:
            xlength = len(budget_spend_all_names[name])
    
    # Text für Beschriftung normieren
    xnames = []
    for name in range(len(budget_spend_all_names)):
        xnames.append(budget_spend_all_names[name].ljust(xlength))
    
    # Tabelle anzeigen
    # Breite definieren
    length = 3 * len(categories)
    
    
    # Reihen mit % Angaben
    print("Percentage spent by category")
    y = 100
    count1 = 0
    while count1 < 11:
        line = (str(y).rjust(3) + "|")
        for sign in range(len(ysign)):
            line += (ysign[sign][count1].center(3))
        print(line)
        count1 += 1
        y -= 10
        
    while y > (-1):
        print(str(y).rjust(3) + "|")
        y -= 10
        
    print("    ".ljust((length + 5),"-"))
    
    # Besschriftung
    count = 0
    while count < xlength:
        line = ("    ")
        for cat in range(len(xnames)):
            line += (xnames[cat][count].center(3))
        print(line)
        count+= 1
    