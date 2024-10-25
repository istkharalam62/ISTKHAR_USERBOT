from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Define your pyrogram client instance
app_pyrogram = Client("my_bot")

@app_pyrogram.on_message(
    filters.command("banall") & filters.group
)
async def banall_command(client, message: Message):
    print(f"Getting members from {message.chat.id}")
    async for member in client.get_chat_members(message.chat.id):
        try:
            await client.ban_chat_member(chat_id=message.chat.id, user_id=member.user.id)
            print(f"Kicked {member.user.id} from {message.chat.id}")
        except Exception as e:
            print(f"Failed to kick {member.user.id}: {e}")
    print("Process completed")

# Instead of app_pyrogram.run(), use start() and idle() without blocking the event loop
async def main():
    await app_pyrogram.start()
    await app_pyrogram.idle()

# Check if the event loop is already running
if __name__ == "__main__":
    try:
        asyncio.run(main())  # Will run the main function with the event loop
    except RuntimeError as e:
        print(f"Error: {e}")
