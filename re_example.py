import re
# re=isthe regular expression library

"""Check if the string starts with "Hello"."""

pattern =r"^Hello"
text ="Hello ,world!We are Feeling Happy today.Hello,you are listening ?"
# match =re.match(pattern,text)

match =re.findall(pattern,text)
# print(f"found : {bool(match)}")
print(f"found : {(match)}")