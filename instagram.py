import instaloader
import sys
from instaloader import Instaloader

def banner():
    print("""
\033[32m██\033[0m╗ \033[32m██████\033[0m╗      \033[32m██████\033[0m╗ \033[32m███████\033[0m╗\033[32m██\033[0m╗\033[32m███\033[0m╗   \033[32m██\033[0m╗\033[32m████████\033[0m╗
\033[32m██\033[0m║\033[32m██\033[0m╔════╝     \033[32m██\033[0m╔═══\033[32m██\033[0m╗\033[32m██\033[0m╔════╝\033[32m██\033[0m║\033[32m████\033[0m╗  \033[32m██\033[0m║╚══\033[32m██\033[0m╔══╝
\033[32m██\033[0m║\033[32m██\033[0m║  \033[32m███\033[0m╗    \033[32m██\033[0m║   \033[32m██\033[0m║\033[32m███████\033[0m╗\033[32m██\033[0m║\033[32m██\033[0m╔\033[32m██\033[0m╗ \033[32m██\033[0m║   \033[32m██\033[0m║
\033[32m██\033[0m║\033[32m██\033[0m║   \033[32m██\033[0m║    \033[32m██\033[0m║   \033[32m██\033[0m║╚════\033[32m██\033[0m║\033[32m██\033[0m║\033[32m██\033[0m║╚\033[32m██\033[0m╗\033[32m██\033[0m║   \033[32m██\033[0m║
\033[32m██\033[0m║╚\033[32m██████\033[0m╔╝    ╚\033[32m██████\033[0m╔╝\033[32m███████\033[0m║\033[32m██\033[0m║\033[32m██\033[0m║ ╚\033[32m████\033[0m║   \033[32m██\033[0m║
\033[0m╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝\033[0m
\033[41m=[===> Mr. Tom | https://github.com/AmanRembersu <===]=\n\033[0m""")
banner()

x = Instaloader()

try:
    uname = input("\033[36mEnter a username \033[0m: \033[36m")
    if uname == "":
        print("\033[33mUnknown command!")
        sys.exit()

    profile = instaloader.Profile.from_username(x.context, uname)

    print("\033[32mUsername\033[0m :", profile.username)
    print("\033[32mID\033[0m :", profile.userid)
    print("\033[32mFull Name\033[0m :", profile.full_name)
    print("\033[32mBiography\033[0m :", profile.biography)
    print("\033[32mBusiness Category Name\033[0m :", profile.business_category_name)
    print("\033[32mExternal URL\033[0m :", profile.external_url)
    print("\033[32mFollowed by Viewer\033[0m :", profile.followed_by_viewer)
    print("\033[32mFollowees\033[0m :", profile.followees)
    print("\033[32mFollowers\033[0m :", profile.followers)
    print("\033[32mFollows Viewer\033[0m :", profile.follows_viewer)
    print("\033[32mBlocked by Viewer\033[0m :", profile.blocked_by_viewer)
    print("\033[32mHas Blocked Viewer\033[0m :", profile.has_blocked_viewer)
    print("\033[32mHas Highlight Reels\033[0m :", profile.has_highlight_reels)
    print("\033[32mHas Public Story\033[0m :", profile.has_public_story)
    print("\033[32mHas Requested Viewer\033[0m :", profile.has_requested_viewer)
    print("\033[32mRequested by Viewer\033[0m :", profile.requested_by_viewer)
    print("\033[32mHas Viewable Story\033[0m :", profile.has_viewable_story)
    print("\033[32mIGTV\033[0m :", profile.igtvcount)
    print("\033[32mIs Business Account\033[0m :", profile.is_business_account)
    print("\033[32mIs Private Account\033[0m :", profile.is_private)
    print("\033[32mIs Verified\033[0m :", profile.is_verified)
    print("\033[32mMedia Count\033[0m :", profile.mediacount)
    print("\033[32mProfile Picture URL\033[0m :", profile.profile_pic_url)

except KeyboardInterrupt:
    print("\033[33mI understand!")

except EOFError:
    print("\033[33mWhy?")
