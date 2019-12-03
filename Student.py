class Student:
    # initialize function with attributes
    def __init__(self, name, major, gpa, is_on_probation):
        #here assigns the values to the object when the initialize function is called
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    #can define a function w/in a student file that all students can then access
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False