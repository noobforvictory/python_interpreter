
import array


def parse(program: str):
    start = 0
    end = 0
    arr = []
    for i in range(1,len(program)):
        if not program[i].isnumeric():
            end = i-1
            if start == end:
                arr.append(program[start])
            else:
                arr.append(program[start: end+1])
            start = i+1
            arr.append(program[i])
    arr.append(program[-1])
    print(arr)

   



def main():
    parse("8+10/2*2-1")


if __name__ == "__main__":
    main()
