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

# Get the top posts from relevant subreddits
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['now ban ar-15s', 'fled the Bahamas with her family during Hurricane Dorian was separated', 'sarasota vot', 'trump at golf club', 'trump doral', 'Floridians overwhelmingly support legalizing', 'millennials in miami', 'corporate giveaway of florida', '2,300 conflicts of interest', 'NZ but nope they wanna put dogs at risk', ' will cost voters ', 'school shootings prevented: 0', 'florida man pulls gun', '2020 initiative to legalize recreational marijuana', 'rally suggests shooting migrants', 'Dwyane Wade is retweeting Beto', 'Trump supporter apologizes on Obama', 'florida board of education', 'Board of Education Chairman is an Evolution Denier', 'Florida just declared a public health emergency', 'California with three suitcases worth of pot', '15,600 deaths', 'Mueller Testimony Implicates Trump in Committing Perjury', 'fl59', 'broward lawmaker', 'southerners are scared of the climate crisis', 'sobs woman who voted for the Leopards', 'alan dershowitz', 'miami\'s trump tower', 'fpl wanted to punish', 'Satanists Has Been Vandalized in the Name of Christianity', 'florida county cannot ban', 'florida migrant detention', 'st petersburg pride', 'planned ice raids', 'ICE shows up at your door', 'facebook moderators break their nda', 'rally in orlando', 'orlando rally', 'orlando wants money upfront', 'Trump Fan Tells MSNBC She Will Vote For Trump', 'dolphins along the gulf coast', 'trayvon martin', 'make america straight again', 'Marijuana Employment Policies', 'This is worse than Watergate', 'equal rights amendment', 'give up your password or go to jail', 'florida ex-felons registered to vote', 'regulate florida', 'florida man threatens to eat cops', '22 million for trumps border wall', '17m to build trump', '16m to build trump', 'trump would beat biden', 'Florida radio stations vow to broadcast Trump', 'lose house because he didn\'t mow his lawn', 'we the people will build the wall', 'bills die in florida', 'i eat ass', 'judge orders florida', 'Florida Man Arrested After Inviting Police Officer to Smoke a Bowl With Him', 'florida will ban', 'republicans are making it harder to vote', 'behead bernie sanders', 'florida man misspell', 'florida and the 2020', 'rallies for florida', 'weed in florida', 'tallahassee yoga shoot', 'florida politic', 'anthony borges', 'democrats win florida', 'cesar sayoc', 'maga bomber', 'magabomber', 'flip florida', 'shalala', 'george zimmerman', 'Palm Beach County Chapter of the Democrat', 'Florida GOP gubernatorial', 'pam bondi', 'ballots in florida', 'gillum', 'parkland teens', 'florida state house', 'melissa howard', 'miami-dade teachers', 'cameron_kasky', 'lee mangold', 'florida republican', 'commissioner of agriculture of florida', 'vern buchanan', 'fl-16', 'jeremy ring', 'mar-a-lago', 'algae bloom threatens Florida', 'fladems', 'Lake Okeechobee Algae Bloom', 'FL-21', 'fl governor', 'aron davis', 'parkland survivor', 'fl-gov', 'nelson campaign', 'scottforflorida', 'orlando massacre', 'orlando mass shooting', 'pulse shooting', 'senator nelson', 'Gary Wayne Lindsey', 'gerrymandering in florida', 'save rural florida', 'school safety commission', 'adam putnam', 'parkland kid', 'bill nelson', 'parkland parents', 'joe negron', 'lauren baer', 'mayor of tallahassee', 'hogg wild', 'scott-nelson', 'fl-6', 'parkland student activist', 'david hogg', 'Emma Gonzales', 'parkland shoot', 'wildlife conservation council', 'florida legislators', 'stoneman douglas students', 'flgov', 'florida state senator', 'fla. senate', 'kelli stargel', 'florida senate', 'florida poll', 'gwen graham', 'fl lawmaker', 'Tampa Bay lawmaker', 'Florida GOP Votes', 'florida lawmaker', 'Florida House', 'debra kaplan', 'Tom Rooney', 'march for our lives', 'Florida high school shooting', 'florida school shooting', 'margaret good', 'Miami congressional campaign', 'Posey for Congress', 'Peters4Congress', 'Florida congressman', 'philip levine', 'sean shaw', 'Proposed Florida amendment', 'vote in Florida', 'victor torres', 'Florida Congressional District 3', 'Florida vot', 'florida legislature', 'Anna Eskamani', 'FL House district 31', 'matt haggman', 'Kelly Smith for Pasco County Commissioner', 'Orlando Lawmakers', 'ron reid', 'florida marijuana', 'bilirakis', 'marijuana in Fl', 'cannabis in florida', 'Florida Cannabis Act',  '^(?!.*klatvala).*latvala.*$' '^(?!.*gov. scott walker).*gov. scott.*$', 'Florida HD-58', 'gaetz', '2018 congressional races in Florida', 'rick scott', 'Florida Democrat', '^(?!.*governor scott).*governor scott.*$', 'florida governor', 'fla. governor', 'governor of florida', 'curbelo', 'brian mast', 'rep mast', 'rep. mast', 'representative mast', 'congressman mast', 'fl-18', 'lehtinen', 'fl-27', 'desantis', 'dennis ross', 'fl-15', 'andrew learned', 'balart', 'fl-25']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Florida 2020 Election \n\n"
            "[Presidential Preference Primary Registration Deadline](https://registertovoteflorida.gov/en/Registration/Eligibility): February 18, 2020 \n\n"
            "[Presidential Preference Primary Election](https://dos.myflorida.com/elections/for-voters/quick-facts-presidential-preference-primary/): March 17, 2020 \n\n"
            "[Primary Registration Deadline](https://registertovoteflorida.gov/en/Registration/Eligibility): July 27, 2020 \n\n"
            "[Primary Election](https://registration.elections.myflorida.com/CheckVoterStatus): August 25, 2020 \n\n"
            "[General Election Registration Deadline](https://registertovoteflorida.gov/en/Registration/Eligibility): October 5, 2020 \n\n"
            "[General Election](https://registration.elections.myflorida.com/CheckVoterStatus): November 3, 2020 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write the post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()