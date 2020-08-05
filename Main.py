import exercise1
import exercise2


def main():
    M = [
         [1,0,1,0,1,1,0,0,1],
         [1,1,1,1,0,1,1,1,1],
         [0,1,1,1,0,1,0,0,1],
         [0,1,1,0,1,1,1,0,0],
         [1,0,1,1,0,1,1,0,1],
         [1,1,0,1,0,0,1,0,1],
         [0,1,1,1,1,1,1,1,1],
         [1,1,0,1,0,1,0,0,1],
         [0,0,0,1,1,1,0,0,1]
        ]
    for arr in M:
        print(arr)
    print(exercise1.bigCross1(M, 9))
    print(exercise2.bigCross2(M, 9))

if __name__ == '__main__':
    main()