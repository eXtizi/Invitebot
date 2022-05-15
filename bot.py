from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


invite_logger = -695370268
esanaChat = -1001764307883
esanaChannel = -1001608186877
session='1AZWarzUBu4oDsHpTyrNHXGaUKcWT9putRU9X0h83ypraGblDHuC8_unMlFudHCCK0MEdUqph2MN3eRoiuHq8kuwETzBJrixXUZ2aKzMSuc7jzPdixfwnQnRXixO7PUcv7a58dm3X_'
session1='CjxclhSZMTQ5XtNMPkIv5YSHizNDWg46Mz7CokXlDa9-lAtJcQ2Jn8lYUdHwGAXeFCD3aCGwN1rhQ1l4FiNOxr_gXOqOExZGAg0nYY8CUvzU_0tTv_GOIlR2ayNkK6Q1Psqz1nBxJ_Aha9uVu_b0Woa_'
session2='rxsz2hQRPQO_L56B7-TjlTnO4vDZ3u0bn1kvw2inCJVwpaQA7cnQhedBSbDVJE='

api_id = 8004294
api_hash = '5091fcf2a3948b6bc7c5f39dec044a63'

app = Client(session+session1+session2,api_id,api_hash)

@app.on_message(filters.command('invite') & filters.chat(esanaChat))
def my_handler(client, message):
    r=app.search_messages(invite_logger, query='('+str(message.from_user.id), limit=5)
    if len(r)==0:
        link = app.create_chat_invite_link(esanaChannel)
        m=message.reply("User: {0} ( {2} )\nYour invite link : {1}\n\nShare as you can to get free netflix.".format(message.from_user.mention(message.from_user.first_name) ,link.invite_link ,message.from_user.id) , disable_web_page_preview = True)
        m.forward(invite_logger)
    else:
        message.reply(r[-1]['text'],  disable_web_page_preview = True)

app.run()
