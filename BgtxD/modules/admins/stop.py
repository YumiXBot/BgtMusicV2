

from pyrogram import filters
from pyrogram.types import Message
from BgtxD.config import BANNED_USERS
from BgtxD.power import get_command
from BgtxD import app
from BgtxD.centre.call import BIKASH
from BgtxD.utility.database import set_loop
from BgtxD.utility.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await BIKASH.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )