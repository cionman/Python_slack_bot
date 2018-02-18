import random
import re
from slackbot.bot import listen_to, respond_to
from slackbot.dispatcher import Message


# listen_to는 채널에 오가는 모든 대화에 반응
@listen_to("roll (\d*)d(\d+)", re.IGNORECASE)
def hello(msg:Message, number_of_die: str, side_of_die: str):

    # 'roll 던지는횟수d숫자면체' 로
    # '던지는횟수'를 number_of_die
    # '숫자면체'를 side_of_die
    # '
    roll_result = [random.randrange(1,int(side_of_die), 1)
                   for i in range(int(number_of_die))]
    roll_sum = sum(roll_result)

    msg.send(str(roll_result))
    msg.send(str(roll_sum))

# respond_to는 @을 이용해서 멘션했을 경우에만 반응
@respond_to("hi", re.IGNORECASE)
def hi(msg:Message):
    msg.reply("Thank you!!")