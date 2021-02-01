txt = open("text.txt", "r")

codex = []

codex = txt.read()


def main(codex):

    wordcount = dict()
    words = codex.split()

    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    return[wordcount]


print (main(codex))






txt.close()

