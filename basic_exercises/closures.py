def show_message(message):
    message = message.title()
    
    def func():
        print(message)
    
    return func

result = show_message("hi!!!!!!!! world!!!!!!!!!!!")
result()

