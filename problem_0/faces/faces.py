def main():
    #Read tex with emoticons
    sentence = input("Sentence with emoticons:")

    #Outup converted text
    print(convert(sentence))

def convert(sentence):
    sentence = sentence.replace(":)", "\N{slightly smiling face}")
    sentence = sentence.replace(":(", "\N{slightly frowning face}")

    return sentence

main()
