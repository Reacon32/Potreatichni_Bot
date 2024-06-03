from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline1():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://structure.mil.ru/structure/forces/ground.htm')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inline2():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://structure.mil.ru/structure/forces/air/history.htm')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inline3():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://structure.mil.ru/structure/forces/navy.htm')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inline4():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://structure.mil.ru/structure/forces/airborne.htm')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inline5():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://structure.mil.ru/structure/forces/strategic_rocket.htm')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inline6():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://structure.mil.ru/structure/forces/vks.htm')
    keyboard_inline.add(but_inline)
    return keyboard_inline