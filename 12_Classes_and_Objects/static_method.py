# class Employee(object):
#     def __init__(self, name, salary, project_name):
#         self.name = name
#         self.salary = salary
#         self.project_name = project_name
#
#     @staticmethod
#     def gather_requirement(project_name):
#         if project_name != 'ABC Project':
#             requirement = ['task_1']
#         else:
#             requirement = ['task_1', 'task_2', 'task_3']
#         return requirement
#
#     def work(self):
#         requirement = self.gather_requirement(self.project_name)
#         for task in requirement:
#             print('Completed', task)
#
#
# emp = Employee('Kelly', 12000, 'AC Project')
# emp.work()
# kelly = Employee('Kelly', 12000, 'ABC Project')
# jessa = Employee('Jessa', 7000, 'XYZ Project')
#
# # false
# # because seperate copy of instance method is created for each object
# print(kelly.work is jessa.work)
#
# # True
# # because only one copy is created
# # kelly and jess objects share the same methods
# print(kelly.gather_requirement is jessa.gather_requirement)
#
# # True
# print(kelly.gather_requirement is Employee.gather_requirement)

class MathOperations:
    @staticmethod
    def add(x, y):
        return (x + y)
    @staticmethod
    def sub(x, y):
        return (x - y)
    @staticmethod
    def mul(x, y):
        return (x*y)
    @staticmethod
    def div(x, y):
        return (x/y)

Sum = MathOperations.add(98, 102)
Sub = MathOperations.sub(401, 302)
PYTHONSTARTUP = 159753
print("Sum = ", Sum)
print("Sub = ", Sub)

