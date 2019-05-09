import random, math, numpy as np
def pow(x, y):
    return math.pow(x,y)
class tubesMosi():
    dots = []
    fBar, a, b = 0, 0, 0
    banyakTitik = 0
    vf = 0
    vfbar = 0
    batasAmbang = {'bawah':0, 'atas':0}
    fxifbar = 0.0
    def __init__(self,banyakTitik, a, b):
        self.a = a
        self.b = b
        # for i in range(banyakTitik):
        #     self.dots.append(random.uniform(a, b))
        file = open('dataUniform.csv','r')
        datas = file.readlines()
        for i in datas:
            self.dots.append(float(i))
    
    def defineFX(self):
        for i in range(len(self.dots)):
            x = self.dots[i]
            self.dots[i] = pow(x,3) + 3*pow(x,2) + 3*x + 1
            # self.dots[i] = round(x + 1,6)
        
    def defineFbar(self):
        for i in self.dots:
            self.fBar += i
        self.fBar /= len(self.dots)

    def substitutionFbarF(self):
        j = 0
        for i in self.dots:
            if j == 0:
                self.fxifbar = i-self.fBar
            x = math.pow(i-self.fBar, 2)
            self.dots[j] = x
            j += 1

    def defineVF(self):
        for i in self.dots:
            self.vf += i
        self.vf = self.vf * 1/ (len(self.dots) - 1)
    
    def defineVFbar(self):
        self.vfbar = self.vf / len(self.dots)

    def defineTreshold(self):
        self.batasAmbang['bawah'] = (self.b - self.a) * (self.fBar - 1.6448536 * self.vfbar)
        self.batasAmbang['atas'] = (self.b - self.a) * (self.fBar + 1.6448536 * self.vfbar)

    def run(self):
        self.defineFX()
        self.defineFbar()
        self.substitutionFbarF()
        self.defineVF()
        self.defineVFbar()
        self.defineTreshold()

    


if __name__ == "__main__":
    mosi = tubesMosi(200, 2, 4)
    mosi.run()
    print('Bawah: ',mosi.batasAmbang['bawah'],' Atas: ',mosi.batasAmbang['atas'])
