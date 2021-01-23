from tqdm import tqdm

#bar = tqdm(total=0)


def Setup(Max):
    global bar
    bar = tqdm(total=Max)


def Bar(step):
    bar.update(step)


def Close():
    bar.close()


"""
example

while True:
        Setup(100)
        count = 0
        while jan != 100:
            Bar(1)
            time.sleep(0.1)
            count += 1
        Close()
        break
"""