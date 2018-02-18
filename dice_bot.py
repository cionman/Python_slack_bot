import re
from slackbot.bot import listen_to, respond_to
from slackbot.dispatcher import Message


# listen_to는 채널에 오가는 모든 대화에 반응
@listen_to("Hello", re.IGNORECASE)
def hello(msg:Message):
    msg.send("World!!")


# respond_to는 @을 이용해서 멘션했을 경우에만 반응
@respond_to("hi", re.IGNORECASE)
def hi(msg:Message):
    msg.reply("Thank you!!")