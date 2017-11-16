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

local_subs = open("alabama.dat", "r")
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
            terms = ['al-sen', '@mooresenate', 'doug jones', 'moore in alabama', 'democrat jones', 'Moore trails Jones', 'Jones beating Moore', 'moore accuser', 'moore lawyer', 'asking Strange to resign', 'rising Dem odds in Alabama', 'moore mud', 'Bannon to stick with Moore', 'If The Democrat Won In Alabama', 'Black Voters Could Help Democrats Replicate Virginia', 'Disloyalty to Moore', 'explain allegations or else he must exit race', 'Hannity breaks with Moore', 'RNC cuts off Moore', 'Democrats Need To Win In Alabama To Take The Senate', 'days as majority leader', 'no reason to doubt these young women', 'Mo Brooks sticking by Moore', 'grossly unfit for office', 'opportunity in the South after Virginia rout', 'Bold Predictions for Democrats in 2018', 'predatory behavior at mall', 'write-in campaign against Moore', 'i believe the women', 'Moore accusations', 'Moore at 55%, Jones at 45%', 'evangelicals more likely to vote for Moore after allegations', 'jones takes the lead', 'Jones Down 48-46', 'The Swine of Conservatism', 'Hannity after Moore coverage', 'dangerous to have as a senator a man who places God', 'Roy dated high school girls', 'Former Moore colleague', 'Fox News And Steve Bannon Invited To Go Fuck Themselves', 'Key Takeaways From Steve Bannon', 'moore is unfit for office', 'judge moore', 'senate race in alabama', 'Moore Fundraising Appeals', 'moore to drop out', 'Moore to step down', 'moore/jones', 'Moore for Senate', 'MOORE And jones', 'Conservatives appeasing right-wing crackpots rather than deflating them', 'The end of the conservative Republican', 'The Republican purge has only just begun', 'love to be able to look my grandkids in the eye, but if I do', 'What the Trump Abyss Looks Like', 'How Trump Has Reshaped the GOP', 'The fate of America is at stake', 'Has Strange or Shelby actually bothered to excuse why they', 'Steve Bannon Is Kicking Our Ass', 'Bends Toward Trump, Critics Either Give In or Give Up', 'Dems lead 50-35 on generic ballot', 'Conservatives are appeasing right-wing crackpots', 'As GOP Senators Bail, Republicans Are Learning What A Trump Party Looks Like', 'one of these put up alongside 565', 'what steve Bannon told the California Republican Party', 'Moore as income to IRS', 'Injuring The Gop In Alabama', 'Koch donors and Bannon take aim', 'as Republican feud rages', 'I can\'t support the GOP if it doesn', 'Kasich Hints That He May Need To Leave The GOP', 'Steve Bannon renews call for war', 'Chill in the air as McConnell', 'Bannon after interview declaring war on GOP', 'GOP Landslide 2018', 'Nobody can run and hide', 'Steve Bannon\'s Republican insurgency', 'conservative donors may still punish Republicans in 2018', 'Unraveling Could Lead to a Major Democratic Wave', 'The unraveling of Donald J. Trump', 'Corker Is Just the Beginning of Trump', 'Steve Bannon thinks DJT has a 30', 'I Hate Everyone in the White House!', 'some of the stuff in here is pretty horrifying', 'Why Republicans Are Starting to Worry About the Trump Presidency', 'could cost them the Senate', 'Bob Corker and the Disgrace of Republican Silence', 'war against Mitch McConnell', 'path to Senate majority in 2018', 'decision to pick Mike Pence as vice president', 'son arrested for criminal trespassing', 'Democrats look to wreak havoc in GOP primaries', 'Bannon Plans to Back Challengers to Most GOP Senators', 'alabama senate race', ' al senate race', 'alabama senate election', 'Alabama\'s GOP Senate Frontrunner', 'alabama\'s gop senate race', '@lutherstrange', 'ray moore', 'Deep South Dems', 'Ala. Senate hopeful Moore', 'reds and yellows', 'alabama senate poll', 'sen. strange', 'senator strange', 'special election in alabama', 'alabama special election', 'Alabama Senate candidate', 'Senate Seat in Alabama', 'Alabama Senate: Special Election', 'trump voters in alabama', 'alabama sen. candidate']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Alabama Senate Special Election 2017 \n\n"
            "[Voter Registration Deadline](https://www.alabamainteractive.org/sos/voter_registration/voterRegistrationWelcome.action): November 27, 2017 \n\n"
            "[General Election](https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do): December 12, 2017 \n\n")
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