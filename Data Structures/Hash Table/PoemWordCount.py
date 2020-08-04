def main():
    wordcount = {}
    with open('poem.txt','r') as f:
        for line in f:
            tokens =  line.split(" ")
            for token in tokens:
                token = token.replace("\n","")
                if token in wordcount:
                    wordcount[token] += 1
                else:
                    wordcount[token] = 1   
    print(wordcount)
                                   
if __name__ == "__main__":
    main()