class Category:
    
    def __init__(self,budgetname):
        self.budget = budgetname
        self.ledger = []
        self.funds = 0
        self.negativebalance = 0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            self.funds -= amount
            self.negativebalance += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.funds

    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else:
            return True

    def transfer(self, amount, category):
        self.withdraw(amount, f"Transfer to {category.budget}")
        if self.check_funds(amount) == True:
            category.deposit(amount, f"Transfer from {self.budget}")
            return True
        else:
            return False

    def __str__(self):
        totalstars = 30 - len(self.budget)
        if totalstars%2 == 0:
            lstars = int(totalstars/2)
            rstars = int(totalstars/2)
        elif totalstars%2 != 0:
            lstars = int(totalstars/2)
            rstars = int(totalstars/2) + 1
        leftstars = "*" * lstars
        rightstars = "*" * rstars

        display = ""
        for entry in self.ledger:
            desc = entry["description"]
            am = entry["amount"]
            if isinstance(am,int):
                am = str(am) + ".00"
                
            if len(desc) <= 23:
                wspaces = " " * (30 - len(desc) - len(str(am)))
                display += f"{desc}{wspaces}{am}\n"
            else:
                dif = len(desc) - 23
                wspaces = " " * (7 - len(str(am)))
                display += f"{desc[:-(dif)]}{wspaces}{am}\n"
            
        finaldisplay = f"{leftstars}{self.budget}{rightstars}\n" + display + f"Total: {self.get_balance()}"
        return finaldisplay

def create_spend_chart(categories):
    
    totalspent = 0
    for category in categories:
        totalspent += category.negativebalance

    grid = []
    percentages = []
    for category in categories:
        #create a list for each element in "categories" with empty strings in the first 0-10 elements
        column = [" "," "," "," "," "," "," "," "," "," "," "]
        #add the capitalized-category-name as individual letters at the end of the corresponding "column" list
        name = category.budget
        splittedname = list(name)
        column.extend(splittedname)
        #append column lists to "grid" list
        grid.append(column)
        #percentage calculation of the category
        percentage = int(((category.negativebalance * 100)/ totalspent) / 10)
        percentages.append(percentage)
        #print(percentages)
        
    #replace empty strings with "o" according to percentage
    for j in range(0, len(grid)): 
        for i in range(0,(percentages[j]+1)): #+1 because range doesnt include end
            grid[j][i] = "o"
                
    #print(grid)
    #preparing percentage display
    graph = ""
    for j in range (10,-1, -1):
        row = " "
        for i in range (0, len(categories)):
            element = grid[i][j] + "  "
            row += element
        pernum = j*10
        margin = " " * (3 - len(str(pernum)))
        graph += "\n" + margin + str(pernum) + "|" + row
            
    dashes = ("---" * len(categories) ) + "-"

    #preparing words display
    names = []
    for category in categories:
        name = category.budget
        names.append(name)

    longestword = max(names, key=len) 
    lenlongestword = len(longestword)

    letters = ""
    for j in range(11,lenlongestword + 11):
        line = " "
        for i in range(0, len(categories)):
            try:
                element = grid[i][j] + "  "
                line += element
            except:
                line += "   "
        letters += "\n    " + line 
    

    display = "Percentage spent by category" + graph +"\n    " + dashes + letters

    #original = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "

    #print(original)
    print(display)
    
    #return display

#TEST
business = Category("Business") #expected 0%
business.deposit(900, "deposit")
business.withdraw(10.99, "paper")

food = Category("Food") #expected 70%
food.deposit(900, "deposit")
food.withdraw(105.55, "pizza")

entretainment = Category("Entretainment") #expected 20%
entretainment.deposit(900, "deposit")
entretainment.withdraw(33.40, "cinema")

create_spend_chart([business, food, entretainment])

print(business)
print(food)
print(entretainment)



