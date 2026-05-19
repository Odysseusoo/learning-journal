def convert(emoticon):
    emoticon = emoticon.replace(":)","🙂")
    emoticon = emoticon.replace(":(","🙁")
    return emoticon


def main ():
    text = input("Enter emoticon: ")
    print (convert(text))

main()
