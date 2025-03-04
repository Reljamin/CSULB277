import die

class Player:
    
    def __init__(self):
        self.dice = [die.Die(), die.Die(), die.Die()]
        self.point = 0

    def points(self):
        return self.point
    
    def roll_dice(self):

        for die in self.dice:
            die.roll()
        
        if self.dice[1] < self.dice[0]:
            temp = self.dice[1]
            self.dice[1] = self.dice[0]
            self.dice[0] = temp

        if self.dice[2] < self.dice[1]:
            temp = self.dice[2]
            self.dice[2] = self.dice[1]
            self.dice[1] = temp

        if self.dice[1] < self.dice[0]:
            temp = self.dice[1]
            self.dice[1] = self.dice[0]
            self.dice[0] = temp
    
    def has_pair(self):
        
        if self.dice[0] == self.dice[1]:
            self.point += 1
            return True
        elif self.dice[1] == self.dice[2]:
            self.point += 1
            return True
    
    def has_three_of_a_kind(self):
        if (self.dice[0] == self.dice[1] == self.dice[2]):
            self.point += 3
            return True

    def has_series(self):
        if ((self.dice[2] - self.dice[1] == 1) and (self.dice[1] - self.dice[0] == 1)):
            self.point += 2
            return True

    def __str__(self):
        return "D1=" + str(self.dice[0]) + ", D2=" + str(self.dice[1]) + ", D3=" + str(self.dice[2])
