def Chatbot():
    print("Welcome To My Chatbot!")
    while True:
        user=input("you: ").lower()
        if user=="hello":
         print("Bot:Hi!")
        elif user=="hi":
           print("Bot:Hello!How can I help you?")
        elif user=="how are you?":
           print("Bot:I am fine.Thanks.What about you?")
        elif user=="bye":
           print("Bot:Goodbye!")
           break
        else:
           print("Bot:Sorry,I don't understand.") 

Chatbot()                     