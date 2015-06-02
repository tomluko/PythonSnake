import glob
#reads, writes level templates to files and from them
# 0 = empty block
# 1 = solid block
# 2 = snakes starting position
class FileIO():
    def readLevel(self, fileName):
        file = open(fileName, "r");
        mapTemplate = []
        for line in file:
            lineList = line.split()
            mapTemplate.append(lineList)
        file.close()
        return mapTemplate

    def writeLevel(self, fileName, mapTemplate):
        file = open(fileName, "w")
        for line in mapTemplate:
            lineStr = " ".join(line)
            file.write(lineStr + "\n")
        file.close()

def getLevels():
    files = glob.glob("*.level")
    filesTuple = tuple(files)
    return filesTuple