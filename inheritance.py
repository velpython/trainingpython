# praticing inheritance

class ProgramLanguage:
  def __init__(self, name):
    self.name = name
    self.private = 'i am founded '

class Python(ProgramLanguage):
    def __init__(self, variable):
        self.variable = variable
        print("i am avialble") 

print(Python(ProgramLanguage))