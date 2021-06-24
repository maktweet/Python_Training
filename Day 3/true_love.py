your_name = input("Whats is your name? :").lower()
their_name = input("What is their name? :").lower()
true_count = 0
love_count = 0
t=0
r=0
u=0
e=0
l=0
o=0
v=0
e=0

true_count += your_name.count("t")
true_count += your_name.count("r")
true_count += your_name.count("u")
true_count += your_name.count("e")
love_count += your_name.count("l")
love_count += your_name.count("o")
love_count += your_name.count("v")
love_count += your_name.count("e")

true_count += their_name.count("t")
true_count += their_name.count("r")
true_count += their_name.count("u")
true_count += their_name.count("e")
love_count += their_name.count("l")
love_count += their_name.count("o")
love_count += their_name.count("v")
love_count += their_name.count("e")
love_score = str(true_count) + str(love_count)

if(int(love_score) <10 or int(love_score)>90):
    print(f"Your score is **{love_score}**, you go together like coke and mentos.")
elif (int(love_score) >= 40 and int(love_score) <= 50):
    print(f"Your score is **{love_score}**, you are alright together.")
else:
    print(f"Your score is **{love_score}**.")