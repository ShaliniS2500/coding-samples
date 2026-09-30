class Hello:
    def do(self):
        for i in range(5):
            print("Hello ", i+1)

class Hi:
    def do(self):
        for i in range(5):
            print("Hi ", i+1)

if __name__ == '__main__':

    t1 = Hello()
    t2 = Hi()

    t1.do()