# == IMPORTATIONS == #

try:
    from cmath import *
    from pylab import *
except Exception as e:
    raise e

# == LOGIC PART == #


class Main:

    def __init__(self, Xmin, Xmax, Ymin, Ymax, N):
        self.Xmin = Xmin
        self.Xmax = Xmax
        self.Ymin = Ymin
        self.Ymax = Ymax
        self.N = N
        self.complex = 0

        self.M_2()

    def M_1(self):
        k = 0
        z = 0 + 0j
        while k <= 100 and abs(z) <= 2:
            z = z ** 2 + self.complex
            k = k + 1

        if abs(z) <= 2:
            m = True
        else:
            m = False

        return m

    def M_2(self):
        for u in range(0, self.N + 1):
            for v in range(0, self.N + 1):
                re = self.Xmin + u * (self.Xmax - self.Xmin) / self.N
                im = self.Ymin + v * (self.Ymax - self.Ymin) / self.N
                self.complex = re + im * 1j

                if self.M_1():
                    plot([re], [im], '.')
        show()
        return

# == START PROGRAM == #

if __name__ == '__main__':
    main = Main(-2, 2, -2, 2, 100)
