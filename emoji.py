def greet(name,last):
    print("good moening to "+ name+last)

emoji = {
        ":)": "😀",
        ":(": "😥"
    }
def emote(message):
    msg=" "

    word=message.split(" ")
    print(word)
    for i in word:
        msg+=emoji.get(i,i)+" "
    print(msg)
        #word+=emoji.get(i,i)+" "





emote("hi there :)")


