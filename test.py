#Подключение необходимых библиотек
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim   

#Создание пространства и подпространства для анимации 
fig, ax = plt.subplots(figsize=(10,10))              

#Создание анимируемого объкта
anim_object, = plt.plot([], [], color='orange',ms = 100, label='Star')

#Пределы изменения переменной x и y
ax.set_xlim(-25, 25)  
ax.set_ylim(-25, 25)

#Функция создания и анимации звезды
def star_move(angle_vel=None, time=None):
    """Функция делает анимацию вращающейся звезды.
       На вход подаются:
       angle_vel, time - необходимые для анимации параметры
    """    
    alpha = np.linspace(0, 4 * np.pi, 100)
    t = angle_vel * (np.pi / 180) * time
    
    x = 12 * np.cos(alpha) + 8 * np.cos(1.5 * alpha)
    y = 12 * np.sin(alpha) - 8 * np.sin(1.5 * alpha)
    
    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + x * np.sin(t)
    
    return X, Y

#Функция, добавляющая дополнительную звезду
#def star(angle_vel=None, time=None):
#    t = angle_vel * (np.pi / 180) * time    
#    x = -(12 * np.cos(t) + 8 * np.cos(1.5 * t))
#    y = -(12 * np.sin(t) - 8 * np.sin(1.5 * t))
#    return x, y

#Функция анимации
def animate(i):
    anim_object.set_data(star_move(angle_vel = 1, time = i))
    ax.set_title('time, day{}'.format(i))

#Дополнительная звезда
#sub = star(angle_vel = 1080,time = np.arange(0, 2 * np.pi, 0.01))
#plt.plot(sub[0],sub[1], color = 'orange')
    
#Создание анимации
animation_7_dop_1 = anim.FuncAnimation(fig,animate,frames=400,interval=0.1)

#Сохранение анимации
animation_7_dop_1.save('animation_7_dop_1.gif')