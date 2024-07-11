from vkbottle.bot import Bot
from vkbottle import GroupEventType
from gpt import answer_to_question
from config import config

bot = Bot(token=config.VK_TOKEN)


@bot.on.raw_event(GroupEventType.WALL_REPLY_NEW)
async def on_comment_add(event: GroupEventType.WALL_REPLY_NEW):
    if event['object']['from_id'] != config.GROUP_ID:
        if config.TRIGGER in event['object']['text']:
            await bot.api.wall.create_comment(
                owner_id=event['object']['owner_id'],
                user_id=event['object']['from_id'],
                reply_to_comment=event['object']['id'],
                message=config.MSG_TEXT,
                random_id=0,
                post_id=event['object']['post_id']
            )
        else:
            comment = await answer_to_question(event['object']['text'])
            await bot.api.wall.create_comment(
                                        owner_id=event['object']['owner_id'],
                                        user_id=event['object']['from_id'],
                                        reply_to_comment=event['object']['id'],
                                        message=f"{comment}",
                                        random_id=0,
                                        post_id=event['object']['post_id']
                                        )

bot.run_forever()