#!/usr/bin/python
# coding: utf-8

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

text_file = open("standardsubs.dat", "r")
subs = text_file.read().split('\n')

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['al-sen', '@mooresenate', 'roy moore', 'Moore Fundraising Appeals', 'Moore to step down', 'moore/jones', 'Moore for Senate', 'MOORE And jones', 'Conservatives appeasing right-wing crackpots rather than deflating them', 'The end of the conservative Republican', 'The Republican purge has only just begun', 'love to be able to look my grandkids in the eye, but if I do', 'What the Trump Abyss Looks Like', 'How Trump Has Reshaped the GOP', 'The fate of America is at stake', 'Has Strange or Shelby actually bothered to excuse why they', 'Steve Bannon Is Kicking Our Ass', 'Bends Toward Trump, Critics Either Give In or Give Up', 'Dems lead 50-35 on generic ballot', 'Conservatives are appeasing right-wing crackpots', 'As GOP Senators Bail, Republicans Are Learning What A Trump Party Looks Like', 'one of these put up alongside 565', 'what steve Bannon told the California Republican Party', 'Moore as income to IRS', 'Injuring The Gop In Alabama', 'Koch donors and Bannon take aim', 'as Republican feud rages', 'I can\'t support the GOP if it doesn', 'Kasich Hints That He May Need To Leave The GOP', 'Steve Bannon renews call for war', 'Chill in the air as McConnell', 'Bannon after interview declaring war on GOP', 'GOP Landslide 2018', 'Nobody can run and hide', 'Steve Bannon\'s Republican insurgency', 'conservative donors may still punish Republicans in 2018', 'Unraveling Could Lead to a Major Democratic Wave', 'The unraveling of Donald J. Trump', 'Corker Is Just the Beginning of Trump', 'Steve Bannon thinks DJT has a 30', 'I Hate Everyone in the White House!', 'some of the stuff in here is pretty horrifying', 'Why Republicans Are Starting to Worry About the Trump Presidency', 'could cost them the Senate', 'Bob Corker and the Disgrace of Republican Silence', 'war against Mitch McConnell', 'path to Senate majority in 2018', 'decision to pick Mike Pence as vice president', 'son arrested for criminal trespassing', 'Democrats look to wreak havoc in GOP primaries', 'Bannon Plans to Back Challengers to Most GOP Senators', 'Trump vs. the Senate', 'support for Jones in Senate race', 'alabama senate race', ' al senate race', 'alabama senate election', 'Alabama\'s GOP Senate Frontrunner', 'alabama\'s gop senate race', '@lutherstrange', 'ray moore', 'Deep South Dems', 'Ala. Senate hopeful Moore', 'reds and yellows', 'Alabama Senate frontrunner', 'alabama senate showdown', 'alabama senate poll', 'sen. strange', 'senator strange', 'special election in alabama', 'alabama special election', 'Alabama Senate candidate', 'Senate Seat in Alabama', 'Alabama Senate: Special Election', 'trump voters in alabama', 'alabama sen. candidate']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register to Vote &#9733;&#9733;&#9733;](https://www.alabamainteractive.org/sos/voter_registration/voterRegistrationWelcome.action) by Monday, November 27, 2017 \n\n"
            "General Election: December 12, 2017 \n\n"
            "[Find your polling place](https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do) \n\n"

            "[**Doug Jones**](http://dougjonesforsenate.com/) is running to represent Alabama in the U.S. Senate. \n\n "
            "[Facebook](https://www.facebook.com/dougjonessenate) | "
            "[Twitter](https://twitter.com/gdouglasjones) | "
            "[Volunteer](https://dougjones.bsd.net/page/s/volunteer) | "
            "[Donate](https://secure.actblue.com/donate/homepage-donate) \n\n "

            "Jones supports universal health care, public schools, living wages, protecting Medicare, equal pay for equal work, renewable energy, and LGBTQ equality.  \n\n "

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")
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