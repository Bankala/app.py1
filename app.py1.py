class Team:
     company = "wipro"

     def __init__(self, name, emp_id):
          self.name = name
          self.emp_id = emp_id

     def set_salary(self, salary):
          self.salary = salary

     def show_details(self):
          print("salary:", self.salary)
          print("emp_id:", self.emp_id)

     def manager(self):
          print(f"{self.name} approved leaves for shiva")

     def developer(self):
          print(f"{self.code} python programming")


manager = Team("shiva", 2512546)
manager.set_salary(20000)
manager.show_details()
manager.manager()

developer = Team("shiva", 2512546)
developer.code = "python"
developer.developer()

                
     

          
          
     