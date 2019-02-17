#!/usr/bin/python
# Read file
def getNameOfInputFile():
  raw_val = input("Please enter the name of the input file: ")
  return raw_val

# Read the input file and generate a dictionary of words and the lines they occur in
# form of a dict.
def getWordReferenceDict(fileName):
    try:
        file = open(fileName, "r", buffering=5)
        line_no = 0
        words_dict = {}
        for line in file:
           line_no += 1
           words = line.strip().lower().split(" ")
           for w in words:
               if(w in words_dict.keys()):
                   words_dict.get(w).append(line_no)
               else:
                   words_dict[w] = [line_no]
        file.close()
        return words_dict
    except Exception as e:
        print("Error writing the out file" + str(e))

# Write the output (in form of dict) to the give output file.
def writeOutput(outFileName, words_dict):
    try:
        # Get all occurrences:
        oFile = open(outFileName, "w")
        for w in sorted(words_dict.iterkeys()):
            oFile.write(w + ' ' + ",".join(str(x) for x in words_dict[w]) + '\n')

        oFile.close()
    except Exception as e:
        print("Error writing the out file" + str(e))

fileName = getNameOfInputFile()
print("You have selected file", fileName)
outFileName = fileName.split('.')[0] + '-index.txt'

print("Output filename is ", outFileName)
writeOutput(outFileName, getWordReferenceDict(fileName))
