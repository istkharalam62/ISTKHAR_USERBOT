@app_pyrogram.on_message(
    filters.command("banall") & filters.group
)
async def banall_command(client, message: Message):
    print("Getting members from {}".format(message.chat.id))
    async for i in app_pyrogram.get_chat_members(message.chat.id):
        try:
            await app_pyrogram.ban_chat_member(chat_id=message.chat.id, user_id=i.user.id)
            print("Kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("Failed to kick {}: {}".format(i.user.id, e))
    print("Process completed")
