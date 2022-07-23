def hello():
    name = ""
    name = input("\nWhat is your name: ")
    if len(name) == 0:
        print("[ No input ]")
        print(" Okay stranger, Congrats to you anyways on creating your first module :)")
    elif len(name) > 0:
        if name[0].islower():
            name = name.capitalize()
        print("\n[ Hey {}, Congratulations on creating your first module :) ]".format(name))


def me():
    adj = ""
    adj = input("\nDescribe yourself in one word: ")
    if len(adj) == 0:
        print("[ If there is one word to describe you, You are amazing! ]")
    else:
        print("\n[ Of course You are {}! ]".format(adj))