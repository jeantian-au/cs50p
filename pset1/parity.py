def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Is Even")
    else:
        print("Is odd")

def is_even(n):
    # 最简洁的方式
    return n % 2 == 0

    # 最符合自然语言的方式
    # return True if n % 2 == 0 else False

    # 最清楚的方式：
    #if n % 2 == 0:
    #    return True
    #else:
    #    return False


