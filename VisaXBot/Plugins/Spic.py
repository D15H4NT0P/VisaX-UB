# credits - MOST OP PERSON IN TG - @LEGENDX08377 - LEGEND X 🔥❤️

from . import *

@bot.on(visa_cmd(pattern="spic"))
async def oho(event):
  if not event.is_reply:
    return await event.edit('Reply to a self distructing pic !.!.!')
  k = await event.get_reply_message()
  pic = await k.download_media()
  await bot.send_file(event.chat_id, pic, caption=f"""
  Oʜᴏ! Lᴏʟ 😂, Dᴇsᴛʀᴜᴄᴛɪᴏɴ Mᴏᴅᴇ Pɪᴄ Dᴇsᴛʀᴏʏᴇᴅ!\n\nPɪᴄ Dᴇsᴛʀᴏʏᴇᴅ Bʏ\n\n[✰ ւᴇɢᴇɴᴅѧʀ𝞬 𝘃ɪ𝒔ѧ-𝙭 ʙο𝞽 ✰](t.me/Visa_Update) 
  """)                                                            
  await event.delete()
  
CmdHelp("Self Destruction").add_command(
  "spic", "This Command Can Capture The Self Destruction Picturr"
).add_info(
  "Capture 🤫 Pic."
).add_warning(
  "✅ Harmless Module."
).add()
