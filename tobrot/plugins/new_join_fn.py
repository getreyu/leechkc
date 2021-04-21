#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import logging

import pyrogram
from tobrot import AUTH_CHANNEL, LOGGER


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(chat_id=message.chat.id, delete=True)
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    # channel_id = str(AUTH_CHANNEL)[4:]
    # message_id = 99
    # display the /help

    await message.reply_text(
        """⭕️No Rules Lah 🤪
        ⭕️Perintah command yang Tersedia
        
/ savethumbnail: Mengganti thumbnail yang di upload di telegram menjadi custom.

/ clearthumbnail: Menghapus thumbnail custom.
 
/ log: Ini akan mengirimi Anda file txt dari log.

/ ytdl: Perintah ini harus digunakan sebagai balasan ke tautan yang didukung.

/ pytdl: Perintah ini akan mendownload video dari link playlist youtube dan akan diunggah ke telegram.

/ leech: Perintah ini harus digunakan sebagai balasan ke tautan magnetis, tautan torrent, atau tautan langsung. [Perintah ini akan SPAM obrolan dan mengirim unduhan file terpisah, jika ada lebih dari satu file, dalam torrent yang ditentukan]

/ leechzip: Perintah ini harus digunakan sebagai balasan ke tautan magnetis, tautan torrent, atau tautan langsung. [Perintah ini akan membuat file .tar.gz dari direktori output, dan mengirim file dalam obrolan, dibagi menjadi BAGIAN masing-masing 1024MiB, karena keterbatasan Telegram]

/ leechunzip: Ini akan membuka file dan mengunggah ke telegram.

/ renewme: Ini akan menghapus sisa unduhan yang tidak terhapus setelah mengunggah file atau setelah / membatalkan perintah.

/ rename: Untuk mengganti nama file telegram.

Hanya bekerja dengan tautan langsung dan tautan youtube untuk saat iniSeperti Anda dapat menambahkan nama khusus sebagai awalan dari nama file asli. Seperti jika nama file Anda adalah gk.txt yang diunggah akan menjadi apa yang Anda tambahkan di CUSTOM_FILE_NAME + gk.txt

Hanya berfungsi dengan tautan langsung / tautan youtube. Tanpa magnet atau torrent.

Dan juga menambahkan nama kustom seperti ...

Anda harus memberikan tautan sebagai www.download.me/gk.txt | new.txt

file akan diunggah sebagai new.txt.

Cara Penggunaan?
kirim salah satu dari perintah yang tersedia, sebagai balasan ke tautan / magnet / torrent yang valid. 👊""",
        disable_web_page_preview=True,
    )
