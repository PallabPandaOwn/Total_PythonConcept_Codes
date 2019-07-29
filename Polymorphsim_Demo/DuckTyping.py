class MyEditor:
    def execute(self):
        print('My Editor')


class Pycharm:
    def execute(self):
        print('Pycharm')


class Editor:
    def __init__(self, ide):
        ide.execute()


p = Pycharm()
my = MyEditor()

M = Editor(my)
