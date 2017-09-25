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

local_subs = open("florida.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['jose felix diaz', 'taddeo', 'he-man', 'special Florida Senate election ballot', 'schlaerth', 'artiles', 'including FOUR likely pickups', 'Sept 26! Early voting has began', 'florida state senate district 40']
            for term in terms:
                include_green = 1
                if subreddit == "bluemidterm2018":
                    include_green = 0

                search(term, submission, include_green);

def search(term, submission, include_green):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        vote_info = ("[&#9733;&#9733;&#9733; VOTE September 26, 2017 &#9733;&#9733;&#9733;](https://registration.elections.myflorida.com/CheckVoterStatus) \n\n")

        green = ("")

        if include_green:
            green = ("[**Christian \"He-Man\" Schlaerth**](http://vote4heman.com/Policies.html) is running to represent Florida State Senate District 40. \n\n"
            "[Facebook](https://www.facebook.com/Vote4HeMan/) | "
            "[Twitter](https://twitter.com/Vote4HeMan) | "
            "[Volunteer](http://vote4heman.com/volunteer.html) | "
            "[Donate](http://vote4heman.com/donate.html) \n\n "
            "Schlaerth supports universal health care, campaign finance reform, and decriminalizing marijuana. \n\n\n ")

        dems = ("[**Annette Taddeo**](https://www.annettetaddeo.com/) is running to represent Florida State Senate District 40. \n\n"
        "[Facebook](https://www.facebook.com/annette.taddeo/) | "
        "[Twitter](https://twitter.com/Annette_Taddeo) | "
        "[Volunteer](https://www.annettetaddeo.com/get-involved/) | "
        "[Donate](https://secure.actblue.com/donate/annettetaddeows) \n\n "
        "Taddeo supports public schools. \n\n\n ")

        map = ("[Map of Florida State Senate District 40](https://www.annettetaddeo.com/wp-content/uploads/2017/09/sd40_Lettersize-1.png) \n\n")

        disclaimer = ("^(I'm a bot and I'm learning. Let me know how I can do better.)")

        text = '\n'.join([vote_info, green, dems, map, disclaimer])

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