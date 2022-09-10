
class Sequences:
    def __init__(self, string):
        self.sequence=string
        self.metric_Satisfied=False
    def get_String(self):
        return self.sequence
    def get_metric_Satisfied(self):
        return self.metric_Satisfied
    def change_metric_Satisfied(self,boolean):
        self.metric_Satisfied=boolean
    def get_Character(self,index):
        return self.sequence[index]
    def get_Length(self):
        return len(self.sequence)
