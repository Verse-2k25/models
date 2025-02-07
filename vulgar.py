from better_profanity import profanity

profanity.load_censor_words()  
message = "This is a shit bad message!"
censored_message = profanity.censor(message)
print(censored_message)  
