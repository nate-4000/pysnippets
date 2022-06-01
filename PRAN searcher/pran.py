import random
e = None
def snrr(seed=int):
    random.seed(seed)
    return random.random()
def rn():
    return random.random()
if __name__ == "__main__":
    while bool(1):
        random.seed(int(input()))
        print(random.random())
