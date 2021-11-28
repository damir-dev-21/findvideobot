from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .calback_data import chanel_callback

menu = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text="Путешествия",
                                        callback_data=chanel_callback.new(category = "Travel",subcategory="")
                                    )
                                ]
                            ])