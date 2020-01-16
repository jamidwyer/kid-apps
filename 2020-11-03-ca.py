# coding: utf-8
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

local_subs = open("california.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.selftext)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = [
                # misc
                'newsom order', \
                'rep. torres', \
                'khanna introduce', \
                'ca-sd-32', \
                'plan to criminalize homelessness', \
                'campaigning in cali', \
                'called giving a damn', \
                'Unconstitutional War With Iran', \
                'california endorsement', 'wine cave', 'house will not vote impeachment', \
                'California\'s Democratic primary', 'h.r.5433', 'waters off california', \
                'free bernie buttons', \
                'california coastal waters', 'warren turned down lucrative job', 'california primary', \
                'congressmen who endorsed trump', 'takes the lead in california', 'housing units this year than San Francisco', 'super tuesday', 'embarcadero homeowners', 'san francisco rally', 'san francisco protest', 'san francisco worker rally', 'california dmv', 'trump hosted zuckerberg', 'tough tailpipe standards', 'dream defenders', 'california staff', 'poll in california', 'tax cut was a scam', 'polling for california', 'triggered book launch', 'aid to california', 'captive labor force', 'climate2020', 'andrew in sf', 'california fire season', 'mark zuckerberg', 'kincade fire', 'CA staffer Susie Shannon', 'treasury secretary', 'mnuchin', '1,500 california fires', 'u.s. out of the paris', 'homeless opera singer', 'housing crisis', 'chanel miller', 'bay area director', 'rally at pershing square', 'court over auto emissions', 'rally in san jose', 'sf climate march', 'revokes california', 'googlers signed a letter', '\'housing for all\' plan', 'gig workers in california', 'san diego border wall', 'rep. katie porter', 'my african american', 'ady barkan', 'bay area supercommuting', 'oakland yang gang', 'oakland planning commission', 'sanders has a movement for that', 'mayor of san diego', 'vaccinate detained migrant families', 'california is banning', 'California will make community colleges', 'rhetoric for mass shootings', 'censor the internet', 'trumpsbodycount', 'cda 230', 'white nationalist killers', 'ronald reagan called africans', 'racist conversation with richard nixon', 'monkeys wearing shoes', 'Reagan called President Nixon to slur Africans', 'reagan using racist language', 'ban on chlorpyrifos', 'tedlieu', 'conditions deteriorated after Amazon takeover', 'peter thiel', 'california quinnipiac', 'third parties access to customers', 'served in the air force and in congress', 'Chevron spills 800,000 gallons', 'tied up and raped by her detective', 'impeachment inquiry is risky', 'reverse transgender military ban', 'haim saban', 'california supports yang', \
                'california poll', 'disney heiress', 'western liberalism', 'brock turner', \
                'la rally', 'san francisco broadband', 'costco shooting', 'los angeles landlords', \
                'Marijuana Employment Policies', 'ice deported veterans', 'nasty nancy', 'wearenhta', \
                'beverly hills climate strike', 'attacks on california', ' ca dem', 'pasadena\'s rally', \
                'monument to migrants', 'california bans', 'oakland to decriminalize', 'san francisco bans', \
                'california high speed rail', 'adachi leak', 'bayarea.jpg', 'bay area is affordable', \
                'east bay dsa', 'ca-24', 'ca-21', 'traitor nunes', 'tight calif. race', 'irvine city council', \
                'California This Election Cycle', 'california neo-nazi', 'trump claims california', \
                'strikers in san francisco', 'california legislat', 'bill in california', 'bay area yimby', \
                'afford a home in Bay Area', 'California\’s wildfires', \
                'California Wildfires', \
                'dsa los angeles', 'nazi rally in berkeley', 'long beach chapter of dsa', \
                'california into three states', 'orange county vote', 'electoral college', \
                'fifth-largest economy', 'san diego rent control', 'ca-ad-58', \
                'maxine waters', 'california dem', \
                'California Pregnancy-Center Rules', 'California disclosure law', \
                'ted lieu', 'asm. santiago', \
                'california law', 'kevin jang', 'kevin hee young jang', 'miguel santiago', 'three californias', \
                'one california or three', 'california into 3 states', 'california\'s democrat', \
                'Democratic tide in Orange County', 'california\'s blue wave', 'pasadena vote', 'ca-04', 'california primar', 'bay area housing', 'dsa-la', 'renters in san francisco', 'oakland mayor', 'ca gov', 'ca04', 'rent in san francisco', 'CALIFORNIA\'S REPUBLICAN VOTER', 'California Assembly', 'uc workers strike', 'pelosi', '5th largest economy', 'california needs rent control', 'candidate for SF mayor', 'ca state senate', 'california voters', 'california senate', 'california considering bill', 'san diego council candidates', 'house intelligence Committee Republicans', 'california bill ', 'repbarbaralee', 'dave min', 'ca48', 'ca25', 'California gun reform', 'California ballot initiative', 'julia peacock', 'ca49', 'nunes campaign', 'steve poizner', 'new office in california', 'gayleforca', 'mike cernovich', 'California Republican', 'gavinnewsom', 'California House Republicans', 'nunes challenger', 'devinnunes', 'Orange County congressional races', 'house intelligence chair', 'Nunes FBI memo', 'nunes\' memo', 'schiff says pence', 'Nunes gave Trump', 'ca-4', 'khanna', 'anthony rendon', 'rep schiff', 'jeff denham', 'ca-10', 'rep. denham', 'rep denham', 'congressman denham', 'representative denham', 'dotty nygard', 'Dem Midterm Wave', 'pro war speech on yemen', 'Dems retake the House', 'jess phoenix', 'ed royce', 'rep. royce', 'congressman royce', 'rep royce', 'ca-39', 'Daniel Wenzek', 'duncan hunter', 'rep. hunter', 'congressman hunter', 'rep hunter', 'ca-50', 'Rackauckas', 'todd spitzer', 'orange county da ', 'orange county d.a.', 'orange county district attorney', 'mimi walters', 'Kia Hamadanchy', 'republicans in orange county', 'devin nunez', 'Orange County Alt-Right', 'devin nunes', 'rep. nunes', 'congressman nunes', 'House Intel chief', 'Nunes Subpoenaed', 'rep nunes', 'darrell issa', 'rep. issa', 'rep issa', 'california gop', 'rohrabacher', 'michael kotick', '@danarohrabacher', 'rohrabracher', 'gop leader mccarthy', 'Transcript of McCarthy', 'pro-assange gop congressman', 'pro-putin california congressman', 'Pro-Russia GOP Rep.', 'Putin\'s congressman', 'rhorabacher', 'steveknight25', 'steve knight', 'rep. knight', 'congressman knight', 'rep knight', 'representative knight', 'ca-25', 'valadao']
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("California 2020 Election \n\n"
            "[Primary Voter Pre-Registration Deadline](http://registertovote.ca.gov/): February 17, 2020  \n\n"
            "[Primary Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): March 3, 2020 \n\n"
            "[General Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): November 3, 2020 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub)

text_file.close()
local_subs.close()