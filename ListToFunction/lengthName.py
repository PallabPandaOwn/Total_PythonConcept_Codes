names = ['pallab', 'bidya','Ravi']


def GetLength(names):
    for name in names:
        if len(name) >= 5:
            print('Name :{}'.format(name))

GetLength(names)