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

local_subs = open("michigan.dat", "r")
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
            terms = ['rick snyder', 'governor snyder', 'gov snyder', 'gov. snyder', 'michigan governor', 'governor of michigan', 'michigan\'s governor', 'Court testimony exposes governor', 'Michigan OKs limitless campaign spending', 'allow candidates to raise money for super PACs', 'ACLU sues Michigan for violating the 1st and 14th Amendments']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.dmv.org/mi-michigan/voter-registration.php) by July 8, 2018 \n\n"
            "[**Abdul El-Sayed**](https://abdulformichigan.com/issues) is running to be Michigan's Governor. \n\n"
            "[Facebook](https://www.facebook.com/AbdulforMichigan) | "
            "[Twitter](https://twitter.com/AbdulElSayed) | "
            "[Volunteer](https://abdulformichigan.com/get-involved) | "
            "[Donate](https://secure.actblue.com/contribute/page/ab4mi_web) \n\n"
            "El-Sayed supports universal health care, public schools, affordable college, living wages, paid sick leave, renewable energy, and campaign finance reform. \n\n\n"

            "[**Shri Thanedar**](https://www.shri2018.com/) is running to be Michigan's Governor. \n\n"
            "[Facebook](https://www.facebook.com/ShriForMI/) | "
            "[Twitter](https://twitter.com/ShriForMI) | "
            "[Volunteer](https://www.shri2018.com/volunteer/) | "
            "[Donate](https://secure.actblue.com/entity/fundraisers/51212) \n\n"
            "Thanedar supports universal health care, public schools, living wages, paid family leave, protecting Social Security and Medicare, equal pay for equal work, campaign finance reform, LGBTQ equality, community policing, voting rights, redistricting reform, and marijuana decriminalization. \n\n\n"

            "[**Gretchen Whitmer**](https://www.gretchenwhitmer.com/issues/) is running to be Michigan's Governor. \n\n"
            "[Facebook](https://www.facebook.com/GretchenWhitmer) | "
            "[Twitter](https://twitter.com/gretchenwhitmer) | "
            "[Volunteer](https://www.gretchenwhitmer.com/volunteer/) | "
            "[Donate](https://secure.actblue.com/contribute/page/whitmer-spash-page) \n\n"
            "Whitmer supports universal health care, public schools, affordable college, living wages, paid family leave, equal pay for equal work, campaign finance reform, LGBTQ equality, voting rights, and redistricting reform. \n\n\n"

            "[**Bill Cobbs**](https://www.billcobbs.com/issues/) is running to be Michigan's Governor. \n\n"
            "[Facebook](https://www.facebook.com/BillCobbsforGovernor/) | "
            "[Volunteer](https://www.billcobbs.com/volunteer/) | "
            "[Donate](https://secure.actblue.com/contribute/page/billcobbs2018.com) \n\n"
            "Cobbs supports public schools. \n\n\n"

            "Primary Election: August 7, 2018 | General Election: November 6, 2018 \n\n"
            "[Find your polling place](https://webapps.sos.state.mi.us/MVIC/votersearch.aspx) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people.)")

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