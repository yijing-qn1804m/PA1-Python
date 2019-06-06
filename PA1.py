class CalUtils:

    def __init__(self):
        self.names = []
        self.heights = []
        self.totalStudentHeight = 0
        self.totalStudentCount = 0

    def appendlist(self):
        with open("listOfStudentHeight.txt", "r") as file:
            for n in file:
                file = n.split("\t")
                name = file[0]
                height = float(file[1])
                self.names.append(name)
                self.heights.append(height)
            self.totalStudentHeight = (sum(self.heights))
            self.totalStudentCount = (len(self.names))

    def calAvgHeight(self):
        a.appendlist()
        avg = (round(self.totalStudentHeight / self.totalStudentCount,2))
        print("Student average height is", avg, "m for", self.totalStudentCount, "Student")

    def new_student(self):
        question = (input("Do you have any additional student?(YES/NO):").upper())
        if question == "NO":
            print('Nothing to be added to list')

        elif question == 'YES':
            new_name = (input("Enter new student name:").upper())
            new_height = (input("Enter student height (in meters):"))
            try:
                i = float(new_height)
                with open("listOfStudentHeight.txt", 'a') as file:
                    file.write(f"\n{new_name}\t{new_height}")
                    self.names.clear()
                    self.heights.clear()
                    self.totalStudentHeight = 0
                    self.totalStudentCount = 0
                a.calAvgHeight()
            except (ValueError, TypeError):
                print('\nPlease enter a numeric height')
            print()
            exit()
        else:
            print("Please Enter Yes or No only")

a = CalUtils()
a.calAvgHeight()
a.new_student()
