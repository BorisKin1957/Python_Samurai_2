
def get_alarm(n, alarm):
    return n * (alarm + '\n')

n, string = 124, 'Почему меня никто не предупредил, что на работе нельзя фыркать как лошадка в ухо начальнику?'

print(get_alarm(n, string))