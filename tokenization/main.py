import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
text = "hey there! my name is devansh"
tokens = enc.encode(text)
print("Tokens" ,tokens)

decoded = enc.decode([48467, 1354, 0, 922, 1308, 382, 3947, 616, 71])
print("Decoded" ,decoded)
