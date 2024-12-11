async def notingroup(userid):
    check_member = await main.tbot.get_chat_member(-1002125422822, userid)
    if check_member.status not in ["member", "creator", "administrator", "owner"]:
        return True
    else:
        return False