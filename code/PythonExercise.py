import math
import getpass

if __name__ == "__main__":
    # # exercise of course 1
    # x = input("Please input a number(x), then we will show you a result: ")
    # num = int(x)
    #
    # if num == 10:
    #     result = math.pow(num + 1, 2)
    # elif num > 10:
    #     result = math.sqrt(num - 1)
    # else:
    #     result = math.pow(num, 10)
    #
    # print(int(result))

    # exercise of course 2: calculate 1 + 2 + 3 + ... + 100
    # result = 0
    # for i in range(1, 101):
    #     result += i
    # print(result)

    # exercise of course 3: print the right number of star
    # numOfStar = input("Please input the number of the star that you'd like to: ")
    #
    # # 正序
    # for i in range(1, int(numOfStar) + 1):
    #     for j in range(i):
    #         print("*", end="")
    #     print("\r")
    #
    # # 倒序
    # for i in range(0, int(numOfStar)):
    #     for j in range(int(numOfStar) - i):
    #         print("*", end="")
    #     print("\r")
    #
    # # exercise of course 4: calculate 1 + 3 + 5 + ... + 2n-1
    # numOfN = input("Please input the number of N: ")
    # target = 2 * int(numOfN) - 1
    #
    # addend = 1
    # sum = 0
    # while addend <= target:
    #     sum += addend
    #     addend += 2
    #
    # print("The result of 1 + 3 + 5 + ... + ", target, ": ",sum)

    # exercise of course 5: usrname and password
    # while True:
    #     username = input("Please input your username: ")
    #     password = getpass.getpass("Please input your password: ")
    #
    #     if username != "Shelly" or password != "123456":
    #         print("Invaild username or password, Please try again!")
    #     else:
    #         print("Hello, Shelly")
    #         break

    password = getpass.g
    print(password)
