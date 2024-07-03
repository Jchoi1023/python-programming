#CIS41- Jihye Choi
#Read a file and write error log

fileName = input("Enter the file name: ")
countLine = 0
countError = 0

try:
    if fileName == 'ErrorLog.txt':
        with open(fileName, 'r') as infile:
            for line in infile:
                line = line.strip()
                if line:
                    countLine += 1
                    if "error" in line:
                        countError += 1
        with open('reportError.txt', 'w') as outfile:
            print(countLine)
            outfile.write(f'linesCount: {countLine}\n')
            print(countError)
            outfile.write(f'errorLinesCount: {countError}\n')
    else:
        print("Input correct file name!")
except FileNotFoundError:
    print("Error!! There is no file with this name: ", fileName)