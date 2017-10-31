#!/usr/bin/python
import praw
import pdb
import re
import os

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

local_subs = open("ohio.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['kasich', 'ohio governor', 'oh gov', 'oh governor\'s', 'jerry springer', 'Mary Taylor', 'should quit bench before running for governor']
            for term in terms:
                include_green = 1
                if subreddit == "bluemidterm2018":
                    include_green = 0

                search(term, submission, include_green);

def search(term, submission, include_green):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        vote_link = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://olvr.sos.state.oh.us/) \n\n")

        green = ("")

        if include_green:
            green = ("[**Constance Gadell-Newton**](https://www.constanceforohio.com/) is running to be Governor of Ohio. \n\n"
                "[Donate](https://www.constanceforohio.com/donate) | "
                "[Reddit](https://www.reddit.com/r/ConstanceGadellNewton/) | "
                "[Facebook](https://www.facebook.com/ConstanceforOH/) | "
                "[Twitter](https://twitter.com/constanceforoh) \n\n"
                "Gadell-Newton supports universal health care, public schools, affordable college, living wages, and renewable energy. \n\n\n")

        dems = ("[**Betty Sutton**](https://www.bettysutton.com/) is running to be Governor of Ohio. \n\n"
            "[Donate](https://act.myngp.com/Forms/4074442571628677632) | "
            "[Facebook](https://www.facebook.com/BettySuttonOH/) | "
            "[Twitter](https://twitter.com/BettySutton) \n\n"
            "Sutton supports universal health care, public schools, equal pay for equal work, renewable energy, and LGBTQ equality. \n\n\n"

            "[**Connie Pillich**](https://www.conniepillich.com/) is running to be Governor of Ohio. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/pillich-homepage) | "
            "[Facebook](https://www.facebook.com/ConniePillichforOH/) | "
            "[Twitter](https://twitter.com/ConniePillich) \n\n"
            "Pillich supports universal health care. \n\n\n"

            "[**Joe Schiavoni**](http://joeforohio.com/issues/) is running to be Governor of Ohio. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/joeschiavoni) | "
            "[Facebook](https://www.facebook.com/JoeSchiavoniOhio/) | "
            "[Twitter](https://twitter.com/JoeSchiavoni) \n\n"
            "Schiavoni supports public schools, living wages, and affordable college. \n\n\n"

            "[**Nan Whaley**](http://nanwhaleyforohio.com/) is running to be Governor of Ohio. \n\n"
            "[Donate](https://act.myngp.com/Forms/8108579996857403392) | "
            "[Facebook](https://www.facebook.com/mayornanwhaley/) | "
            "[Twitter](https://twitter.com/nanwhaley) \n\n"
            "Whaley supports LGBTQ equality and universal pre-K. \n\n\n")

        disclaimer = ("^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people.)")

        text = '\n'.join([vote_link, green, dems, disclaimer])

        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

text_file.close()
local_subs.close()
