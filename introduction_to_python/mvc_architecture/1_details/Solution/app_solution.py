import view_solution as view
import model_solution as model

name = input(view.capture_name())
age = input(view.capture_age())
model.store(name,age)
info = view.display(name, age)
print(info)