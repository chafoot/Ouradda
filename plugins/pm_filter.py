# Credit @LazyDeveloper.

# Please Don't remove credit.

# Born to make history @LazyDeveloper !

# Thank you LazyDeveloper for helping us in this Journey

# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰

# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 

# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍

# with Love @LazyDeveloperr 💘

# Subscribe YT @LazyDeveloperr - to learn more about this for free...



import asyncio

import re

import ast

import math

import pytz

from datetime import datetime, timedelta, date, time

lock = asyncio.Lock()

from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty

from Script import script

from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, \

    make_inactive

from info import *

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ForceReply, Message

from pyrogram import Client, filters, enums

from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid

from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings

from database.users_chats_db import db

from database.ia_filterdb import Media, get_file_details, get_search_results,get_search_results_badAss_LazyDeveloperr

from database.lazy_utils import progress_for_pyrogram, convert, humanbytes

from hachoir.metadata import extractMetadata

from hachoir.parser import createParser

import os 

from Script import script

import humanize

from PIL import Image

import time

from utils import get_shortlink

from database.filters_mdb import (

    del_all,

    find_filter,

    get_filters,

)

from util.human_readable import humanbytes

from plugins.settings.settings import OpenSettings

from plugins.dl_button import ddl_call_back

from plugins.yt_lazy_dl_btn import youtube_dl_call_back

from urllib.parse import quote_plus

from util.file_properties import get_name, get_hash, get_media_file_size

import logging

logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)



req_channel = REQ_CHANNEL

BUTTONS = {}

SPELL_CHECK = {}

# 

BUTTON = {}

FRESH = {}

BUTTONS0 = {}

BUTTONS1 = {}

BUTTONS2 = {}



# @Client.on_message(filters.group & filters.text & filters.incoming)

# async def give_filter(client, message):

#     try:

#         chatIDx = message.chat.id

#         lazy_chatIDx = await db.get_chat(int(chatIDx))

#         if lazy_chatIDx['is_lazy_verified']:

#             k = await manual_filters(client, message)

#     except Exception as e:

#         logger.error(f"Chat not verifeid : {e}") 



#     if k == False:

#         try:

#             chatID = message.chat.id

#             lazy_chatID = await db.get_chat(int(chatID))

#             if lazy_chatID['is_lazy_verified']:

#                 await auto_filter(client, message)

#         except Exception as e:

#             logger.error(f"Chat Not verified : {e}") 



@Client.on_message(filters.group & filters.text & filters.incoming)

async def give_filter(client, message):

    k = await manual_filters(client, message)

    if k == False:

        await auto_filter(client, message)



@Client.on_callback_query(filters.regex('rename'))

async def rename(bot,update):

	user_id = update.message.chat.id

	date = update.message.date

	await update.message.delete()

	await update.message.reply_text("»»——— 𝙋𝙡𝙚𝙖𝙨𝙚 𝙚𝙣𝙩𝙚𝙧 𝙣𝙚𝙬 𝙛𝙞𝙡𝙚 𝙣𝙖𝙢𝙚...",	

	reply_to_message_id=update.message.reply_to_message.id,  

	reply_markup=ForceReply(True))  

    

# Born to make history @LazyDeveloper !

@Client.on_callback_query(filters.regex("upload"))

async def doc(bot, update):

    try:

        type = update.data.split("_")[1]

        new_name = update.message.text

        new_filename = new_name.split(":-")[1]

        file = update.message.reply_to_message

        file_path = f"downloads/{new_filename}"

        ms = await update.message.edit("\n༻☬ད 𝘽𝙪𝙞𝙡𝙙𝙞𝙣𝙜 𝙇𝙖𝙯𝙮 𝙈𝙚𝙩𝙖𝘿𝙖𝙩𝙖...")

        c_time = time.time()

        try:

            path = await bot.download_media(

                    message=file,

                    progress=progress_for_pyrogram,

                    progress_args=("**\n  ღ♡ ꜰɪʟᴇ ᴜɴᴅᴇʀ ᴄᴏɴꜱᴛʀᴜᴄᴛɪᴏɴ... ♡♪**", ms, c_time))

        except Exception as e:

            await ms.edit(e)

            return 

        splitpath = path.split("/downloads/")

        dow_file_name = splitpath[1]

        old_file_name =f"downloads/{dow_file_name}"

        os.rename(old_file_name, file_path)

        duration = 0

        try:

            metadata = extractMetadata(createParser(file_path))

            if metadata.has("duration"):

               duration = metadata.get('duration').seconds

        except:

            pass

        user_id = int(update.message.chat.id) 

        ph_path = None 

        media = getattr(file, file.media.value)

        filesize = humanize.naturalsize(media.file_size) 

        c_caption = await db.get_caption(update.message.chat.id)

        c_thumb = await db.get_thumbnail(update.message.chat.id)

        if c_caption:

             try:

                 caption = c_caption.format(filename=new_filename, filesize=humanize.naturalsize(media.file_size), duration=convert(duration))

             except Exception as e:

                 await ms.edit(text=f"Your caption Error unexpected keyword ●> ({e})")

                 return 

        else:

            caption = f"**{new_filename}** \n\n⚡️Data costs: `{filesize}`"

        if (media.thumbs or c_thumb):

            if c_thumb:

               ph_path = await bot.download_media(c_thumb) 

            else:

               ph_path = await bot.download_media(media.thumbs[0].file_id)

            Image.open(ph_path).convert("RGB").save(ph_path)

            img = Image.open(ph_path)

            img.resize((320, 320))

            img.save(ph_path, "JPEG")

        await ms.edit("三 𝘗𝘳𝘦𝘱𝘢𝘳𝘪𝘯𝘨 𝘵𝘰 𝘳𝘦𝘤𝘦𝘪𝘷𝘦 𝘓𝘢𝘻𝘺 𝘧𝘪𝘭𝘦...︻デ═一")

        c_time = time.time() 

        try:

           if type == "document":

              await bot.send_document(

	            update.message.chat.id,

                       document=file_path,

                       thumb=ph_path, 

                       caption=caption, 

                       progress=progress_for_pyrogram,

                       progress_args=( "**⎝⎝✧ ʀᴇᴄɪᴇᴠɪɴɢ ꜰɪʟᴇ ꜰʀᴏᴍ ʟᴀᴢʏ ꜱᴇʀᴠᴇʀ ✧⎠⎠**",  ms, c_time))

           elif type == "video": 

               await bot.send_video(

	            update.message.chat.id,

	            video=file_path,

	            caption=caption,

	            thumb=ph_path,

	            duration=duration,

	            progress=progress_for_pyrogram,

	            progress_args=( "**⎝⎝✧ ʀᴇᴄɪᴇᴠɪɴɢ ꜰɪʟᴇ ꜰʀᴏᴍ ʟᴀᴢʏ ꜱᴇʀᴠᴇʀ ✧⎠⎠**",  ms, c_time))

           elif type == "audio": 

               await bot.send_audio(

	            update.message.chat.id,

	            audio=file_path,

	            caption=caption,

	            thumb=ph_path,

	            duration=duration,

	            progress=progress_for_pyrogram,

	            progress_args=( "**⎝⎝✧ ʀᴇᴄɪᴇᴠɪɴɢ ꜰɪʟᴇ ꜰʀᴏᴍ ʟᴀᴢʏ ꜱᴇʀᴠᴇʀ ✧⎠⎠**",  ms, c_time   )) 

        except Exception as e: 

            await ms.edit(f" Erro {e}") 

            os.remove(file_path)

            if ph_path:

              os.remove(ph_path)

            return 

        await ms.delete() 

        os.remove(file_path) 

        if ph_path:

           os.remove(ph_path) 

    except Exception as e:

        logger.error(f"error 2 : {e}")



# Born to make history @LazyDeveloper !

@Client.on_callback_query(filters.regex(r"^next"))

async def next_page(bot, query):

    ident, req, key, offset = query.data.split("_")

    print(f"REQ => {req}")

    if int(req) not in [query.from_user.id, 0]:

        return await query.answer(

                        f"⚠️ ʜᴇʟʟᴏ{query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,\nʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",

                        show_alert=True,

                    )

    try:

        offset = int(offset)

    except:

        offset = 0

    search = BUTTONS.get(key)

    chat_id = query.message.chat.id

    if not search:

        await query.answer("You are using one of my old messages, please send the request again.", show_alert=True)

        return



    files, n_offset, total = await get_search_results_badAss_LazyDeveloperr(chat_id, search, offset=offset, filter=True)

    try:

        n_offset = int(n_offset)

    except:

        n_offset = 0



    if not files:

        return

    temp.GETALL[key] = files

    temp.SHORT[query.from_user.id] = query.message.chat.id

    settings = await get_settings(query.message.chat.id)

        # if query.from_user.id in download_counts and download_counts[query.from_user.id]['date'] == current_date:

        #     if download_counts[query.from_user.id]['count'] >= DOWNLOAD_LIMIT:

        #         # set URL_MODE to False to disable the URL shortener button

        #         URL_MODE = False

        #     else:

        #         # increment the download count for the user

        #         download_counts[query.from_user.id]['count'] += 1

        # else:

        #     # create a new entry for the user in the download counts dictionary

        #     download_counts[query.from_user.id] = {'date': current_date, 'count': 1}d

    if settings['button']:

            if URL_MODE is True:

                if query.from_user.id in ADMINS:

                    btn = [

                        [

                            InlineKeyboardButton(

                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'

                            ),

                        ]

                        for file in files

                    ]

                elif query.from_user.id in MY_USERS:

                    btn = [

                        [

                            InlineKeyboardButton(

                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'

                            ),

                        ]

                        for file in files

                    ]

                elif query.from_user.id in LZURL_PRIME_USERS:

                    btn = [

                        [

                            InlineKeyboardButton(

                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'

                            ),

                        ]

                        for file in files

                        ]

                elif query.message.chat.id is not None and query.message.chat.id in LAZY_GROUPS:

                    btn = [

                    [

                        InlineKeyboardButton(

                            text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'

                        ),

                    ]

                    for file in files

                    ]

                else:

                    btn = [

                        [

                            InlineKeyboardButton(

                                text=f"[{get_size(file.file_size)}] {file.file_name}", 

                                url=await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}")

                            ),

                        ]

                        for file in files

                    ]

            else:

                if query.from_user.id in ADMINS:

                    btn = [

                        [

                            InlineKeyboardButton(

                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'

                            ),

                        ]

                        for file in files

                    ]

                elif query.from_user.id in MY_USERS:

                    btn = [

                        [

                            InlineKeyboardButton(

                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'

                            ),

                        ]

                        for file in files

                    ]

                else:    

                    btn = [

                        [

                            InlineKeyboardButton(

                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'

                            ),

                        ]

                        for file in files

                    ]



    else:

        if URL_MODE is True:

            if query.from_user.id in ADMINS:

                btn = [

                    [

                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),

                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),

                    ]

                    for file in files

                ]

            elif query.from_user.id in MY_USERS:

                btn = [

                    [

                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),

                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),

                    ]

                    for file in files

                ]

            elif query.from_user.id in LZURL_PRIME_USERS:

                btn = [

                    [

                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),

                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),

                    ]

                    for file in files

                ]

            elif query.message.chat.id is not None and query.message.chat.id in LAZY_GROUPS:

                btn = [

                    [

                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),

                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),

                    ]

                    for file in files

                ]

            else:

                btn = [

                    [

                        InlineKeyboardButton(text=f"{file.file_name}",url=await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}")),

                        InlineKeyboardButton(text=f"[{get_size(file.file_size)}]", url=await get_shortlink(f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}")),

                    ]

                    for file in files

                ]

        else:

            if query.form_user.id in ADMINS:

                btn = [

                    [

                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),

                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),

                    ]

                    for file in files

                ]

            elif query.form_user.id in MY_USERS:

                btn = [

                    [

                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),

                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),

                    ]

                    for file in files

                ]

            else:

                btn = [

                    [

                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),

                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),

                    ]

                    for file in files

                ]



    btn.insert(0,

        [ 

        InlineKeyboardButton("  𝐅𝐈𝐋𝐓𝐄𝐑 𝐋𝐀𝐍𝐆𝐔𝐀𝐆𝐄 ʕʘ̅͜ʘ̅ʔ", callback_data=f"languages#{key}"),

        ] 

    )

    btn.insert(0,

        [ 

	    InlineKeyboardButton(text="⚡ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ⚡", url='https://t.me/ouraddaa/9'),

        ] 

    )



    if 0 < offset <= 10:

        off_set = 0

    elif offset == 0:

        off_set = None

    else:

        off_set = offset - 10

    if n_offset == 0:

        btn.append(

            [InlineKeyboardButton("⏪ BACK", callback_data=f"next_{req}_{key}_{off_set}"),

             InlineKeyboardButton(f"📃 Pages {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}",

                                  callback_data="pages")]

        )

    elif off_set is None:

        btn.append(

            [InlineKeyboardButton(f"🗓 {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),

             InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{req}_{key}_{n_offset}")])

    else:

        btn.append(

            [

                InlineKeyboardButton("⏪ BACK", callback_data=f"next_{req}_{key}_{off_set}"),

                InlineKeyboardButton(f"🗓 {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),

                InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{req}_{key}_{n_offset}")

            ],

        )

    try:

        await query.edit_message_reply_markup(

            reply_markup=InlineKeyboardMarkup(btn)

        )

    except MessageNotModified:

        pass

    await query.answer()



# Born to make history @LazyDeveloper !

@Client.on_callback_query(filters.regex(r"^spolling"))

async def advantage_spoll_choker(bot, query):

    _, user, movie_ = query.data.split('#')

    if int(user) != 0 and query.from_user.id != int(user):

        return await query.answer("This Message is not for you dear. Don't worry you can send new one !", show_alert=True)

    if movie_ == "close_spellcheck":

        return await query.message.delete()

    movies = SPELL_CHECK.get(query.message.reply_to_message.id)

    if not movies:

        return await query.answer("You are clicking on an old button which is expired.", show_alert=True)

    movie = movies[(int(movie_))]

    chat_id = query.message.chat.id



    await query.answer('Checking for Movie in database...')

    k = await manual_filters(bot, query.message, text=movie)

    if k == False:

        files, offset, total_results = await get_search_results_badAss_LazyDeveloperr(chat_id, movie, offset=0, filter=True)

        if files:

            k = (movie, files, offset, total_results)

            await auto_filter(bot, query, k)

        else:

            k = await query.message.edit('😒 currently unavailable ! we are really sorry for inconvenience !\n Have patience ! our great admins will upload it as soon as possible !')

            await asyncio.sleep(10)

            await k.delete()





# Born to make history @LazyDeveloeprr 🍁

@Client.on_callback_query(filters.regex(r"^languages#"))

async def languages_cb_handler(client: Client, query: CallbackQuery):

    try:

        if int(query.from_user.id) not in [query.message.reply_to_message.from_user.id, 0]:

            return await query.answer(

                f"⚠️ ʜᴇʟʟᴏ{query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,\nʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",

                show_alert=True,

            )

    except:

        pass

    _, key = query.data.split("#")

    # if BUTTONS.get(key+"1")!
