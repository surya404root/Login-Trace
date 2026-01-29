import requests
from config.settings import ENGINE

HEAD={"User-Agent":ENGINE["user_agent"]}

def post(url,data):
    try:
        r=requests.post(url,data=data,headers=HEAD,timeout=ENGINE["timeout"])
        return r.text.lower()
    except: return ""

def instagram(e): return "sent" in post("https://www.instagram.com/accounts/account_recovery_send_ajax/",{"email_or_username":e})
def github(e): return "sent" in post("https://github.com/password_reset",{"email":e})
def gitlab(e): return "sent" in post("https://gitlab.com/users/password",{"user[email]":e})
def reddit(e): return "sent" in post("https://www.reddit.com/password",{"email":e})
def pinterest(e): return "email" in post("https://www.pinterest.com/password/reset/",{"email":e})
def tumblr(e): return "sent" in post("https://www.tumblr.com/forgot_password",{"email":e})
def medium(e): return "email" in post("https://medium.com/m/reset-password",{"email":e})
def quora(e): return "sent" in post("https://www.quora.com/forgot_password",{"email":e})
def spotify(e): return "success" in post("https://www.spotify.com/api/password-reset/v1/request/",{"email":e})
def vimeo(e): return "email" in post("https://vimeo.com/forgot_password",{"email":e})
def wordpress(e): return "check your email" in post("https://wordpress.com/wp-login.php?action=lostpassword",{"user_login":e})
def flickr(e): return "email" in post("https://identity.flickr.com/forgot-password",{"email":e})
def devto(e): return "sent" in post("https://dev.to/users/password",{"email":e})
def codepen(e): return "email" in post("https://codepen.io/password/reset",{"email":e})
def hackerrank(e): return "sent" in post("https://www.hackerrank.com/auth/forgot_password",{"email":e})
def kaggle(e): return "email" in post("https://www.kaggle.com/account/forgot",{"email":e})
def pastebin(e): return "sent" in post("https://pastebin.com/password_reset.php",{"email":e})
def bitbucket(e): return "email" in post("https://bitbucket.org/account/password/reset/",{"email":e})
def stackoverflow(e): return "sent" in post("https://stackoverflow.com/users/account-recovery",{"email":e})

# Popular social
def tiktok(e): return "email" in post("https://www.tiktok.com/legal/report/feedback",{"email":e})
def snapchat(e): return "email" in post("https://accounts.snapchat.com/accounts/password_reset_request",{"email":e})
def discord(e): return "sent" in post("https://discord.com/api/v9/auth/forgot",{"login":e})
def twitch(e): return "email" in post("https://www.twitch.tv/password-reset",{"email":e})
def telegram(e): return False   # no public endpoint
def twitter(e): return False    # blocked by X
def linkedin(e): return False   # blocked
def facebook(e): return False   # blocked
def whatsapp(e): return False   # blocked

# Indian / common platforms
def flipkart(e): return "email" in post("https://www.flipkart.com/account/login",{"username":e})
def amazon(e): return "email" in post("https://www.amazon.in/ap/forgotpassword",{"email":e})
def paytm(e): return False
def phonepe(e): return False
def zomato(e): return "email" in post("https://www.zomato.com/forgot-password",{"email":e})
def swiggy(e): return "email" in post("https://www.swiggy.com/forgot-password",{"email":e})

# Developer & tech
def docker(e): return "email" in post("https://hub.docker.com/v2/users/password/reset/",{"email":e})
def npm(e): return "email" in post("https://www.npmjs.com/forgot",{"email":e})
def heroku(e): return "email" in post("https://id.heroku.com/password",{"email":e})
def atlassian(e): return "email" in post("https://id.atlassian.com/login/resetpassword",{"email":e})

PLATFORMS = {
"Instagram":instagram,
"GitHub":github,
"GitLab":gitlab,
"Reddit":reddit,
"Pinterest":pinterest,
"Tumblr":tumblr,
"Medium":medium,
"Quora":quora,
"Spotify":spotify,
"Vimeo":vimeo,
"WordPress":wordpress,
"Flickr":flickr,
"Dev.to":devto,
"CodePen":codepen,
"HackerRank":hackerrank,
"Kaggle":kaggle,
"Pastebin":pastebin,
"Bitbucket":bitbucket,
"StackOverflow":stackoverflow,

"TikTok":tiktok,
"Snapchat":snapchat,
"Discord":discord,
"Twitch":twitch,
"Telegram":telegram,
"Twitter(X)":twitter,
"LinkedIn":linkedin,
"Facebook":facebook,
"WhatsApp":whatsapp,

"Flipkart":flipkart,
"Amazon":amazon,
"Paytm":paytm,
"PhonePe":phonepe,
"Zomato":zomato,
"Swiggy":swiggy,

"DockerHub":docker,
"NPM":npm,
"Heroku":heroku,
"Atlassian":atlassian
}
