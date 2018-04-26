# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
# 粒子（鸟）
class particle:
    def __init__(self):
        self.pos = 0  # 粒子当前位置
        self.pos2 = 0
        self.pos3 = 2.5
        self.speed = 0
        self.pbest = 0  # 粒子历史最好位置
        self.pbest2 = 0
        self.pbest3 = 0


class PSO:
    def __init__(self):
        self.w = 0.5  # 惯性因子
        self.c1 = 1  # 自我认知学习因子
        self.c2 = 1  # 社会认知学习因子
        self.gbest = 0  # 种群当前最好位置
        self.gbest2 = 0  # 种群当前最好位置
        self.gbest3 = 0
        self.N = 20  # 种群中粒子数量
        self.POP = []  # 种群
        self.iter_N = 1000  # 迭代次数

    # 适应度值计算函数
    #def fitness(self, x):
    #    return x + 10 * np.sin(5 * x) + 7 * np.cos(4 * x)
    def fitness(self, wi, qi, t):
        return (5563.6-qi)*qi-0.5*wi*wi - 17*(1.525*qi-wi)-t*(9.525*qi-wi)



    # 找到全局最优解
    def g_best(self, pop):
        for bird in pop:
            if bird.fitness > self.fitness(self.gbest,self.gbest2,self.gbest3):
                self.gbest = bird.pos
                self.gbest2 = bird.pos2
                self.gbest3 = bird.pos3

    # 初始化种群
    def initPopulation(self, pop, N):
        for i in range(N):
            bird = particle()
            bird.pos = np.random.uniform(0, 100000)
            bird.pos2 = np.random.uniform(0, 100000)

            # //////////////////////////////////////////////////////////////////////
            bird.pos3 = np.random.uniform(0, 5)
            bird.fitness = self.fitness(bird.pos, bird.pos2, bird.pos3)
            bird.pbest = bird.fitness
            pop.append(bird)

        # 找到种群中的最优位置
        self.g_best(pop)

    # 更新速度和位置
    def update(self, pop):
        for bird in pop:
            # 速度更新
            speed = self.w * bird.speed + self.c1 * np.random.random() * (
                bird.pbest - bird.pos) + self.c2 * np.random.random() * (
                self.gbest - bird.pos)

            # 位置更新
            pos = bird.pos + speed
            pos2 = bird.pos2 + speed
            pos3 = bird.pos3 + speed


            if 0 < pos < 100000 and 0 < pos2 < 100000 and pos < 9.525*pos2 and 0<= pos3 <=5: # 必须在搜索空间内
                bird.pos = pos
                bird.pos2 = pos2
                bird.pos3 = pos3
                bird.speed = speed
                # 更新适应度
                bird.fitness = self.fitness(bird.pos, bird.pos2, bird.pos3)

                # 是否需要更新本粒子历史最好位置
                if bird.fitness > self.fitness(bird.pbest,bird.pbest2, bird.pbest3):
                    bird.pbest = bird.pos
                    bird.pbest2 = bird.pos2
                    bird.pbest3 = bird.pos3

    # 最终执行
    def implement(self):
        # 初始化种群
        self.initPopulation(self.POP, self.N)

        # 迭代
        for i in range(self.iter_N):
            # 更新速度和位置
            self.update(self.POP)
            # 更新种群中最好位置
            self.g_best(self.POP)


pso = PSO()
pso.implement()

for ind in pso.POP:
    print(ind.pos," ", ind.pos2, " ", ind.pos3, " ", ind.fitness)


#def func(x):
#    return x + 10 * np.sin(5 * x) + 7 * np.cos(4 * x)
# def func(wi, qi):
#     return -0.5*qi*qi-0.5*wi*wi+3664.77425*qi+213.63*wi
#
# x = np.linspace(0, 100000, 10000)
# y = np.linspace(0, 100000, 10000)
# z = func(x, y)
#
# scatter_x = np.array([ind.pos for ind in pso.POP])
# scatter_y = np.array([ind.fitness for ind in pso.POP])
# plt.plot(x, z)
# plt.plot(y, z)
# plt.scatter(scatter_x, scatter_y, c='r')
# plt.show()