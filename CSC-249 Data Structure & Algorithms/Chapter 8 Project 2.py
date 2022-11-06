def capitalizeSentences(sentence):
    lst = sentence.split(". ")

    capitalizedText = ""

    for line in lst:
        capitalizedText += line[0].upper() + line[1:] + ". "

    capitalizedText = capitalizedText[:-2]

    return capitalizedText

sentenceToCapitalize = input("Enter sentence to be capitalized:")
print(capitalizeSentences(sentenceToCapitalize))