# Create a new Python script that prompts a user to enter in a potential
#  Tweet and then print out whether the tweet is short enough to work
# (under 140 chars) or too long to post.

# prompt the user to enter any tweet
print("*" * 40)
tweet_prompt = input("Type your tweet ")

# check  the length of the tweet
length_tweet = len(tweet_prompt)

# arithmetic to check how much your tweet has exceed the 140 char mark
exceeded_tweet = length_tweet - 140

# conditionals on the length of the tweets
if length_tweet <= 140:
    print("That'll work")
else:
    print(f"\n Your tweet is {exceeded_tweet} characters too long")
