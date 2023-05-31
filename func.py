from linebot import LineBotApi
from linebot.models import *
import requests
# 必須放上自己的Channel Access Token(在Line Developers的Messaging API裡)
line_bot_api = LineBotApi('qu84Pp81PIJp+Ue+8Pb9aOVM2OH3z+Wc1A84diY05Ivq8/sprT01RD/kPFVG4QokoyQrkZwEiulFoDSOA2xoqAG8rPY4RHNgzFLACVAjyIZAqgP5oUyjSlGE//aZWq/Eu62H7VBKT/5jey+x47/cBwdB04t89/1O/w1cDnyilFU=')

def sendQuicklyReply(event):#Quick Reply Message
    try:
        message = TextSendMessage(
            text='來點什麼？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label='我想來點正餐', text='正餐!')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='來個下午茶！', text='下午茶!')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='來點飲料！', text='飲料!')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='不吃了！', text='不吃了!')
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def meal(event):#Carousel Template Message
    #可以用line提供的flex message simulator進行編輯，並輸出成json格式，用下面方式貼上(記得要檢查json有些地方會寫true，要改成True，不然會出錯) 
    try:
        message = FlexSendMessage(
            alt_text="選擇餐廳",
            contents=
        {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://img.onl/q7h3zE",
                "size": "full",
                "aspectMode": "fit",
                "aspectRatio": "320:213",
                "backgroundColor": "#9D9D9D"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "開川飯食堂",
                    "weight": "bold",
                    "size": "sm",
                    "wrap": True
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                    },
                    {
                        "type": "text",
                        "text": "4.2",
                        "size": "xs",
                        "color": "#8c8c8c",
                        "margin": "md",
                        "flex": 0
                    }
                    ]
                }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "菜單連結",
                    "uri": "https://farm8.staticflickr.com/7812/39984702263_f231b5b31e_o.jpg"
                    },
                    "position": "relative",
                    "height": "sm",
                    "style": "link",
                    "gravity": "center"
                }
                ]
            }
            },
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://img.onl/RtTMVs",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "麥當勞",
                    "weight": "bold",
                    "size": "sm",
                    "align": "start"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                    },
                    {
                        "type": "text",
                        "text": "3.8",
                        "size": "sm",
                        "color": "#8c8c8c",
                        "margin": "md",
                        "flex": 0
                    }
                    ]
                }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "菜單連結",
                    "uri": "https://cdn2.ettoday.net/images/3525/d3525813.jpg"
                    },
                    "gravity": "bottom",
                    "offsetTop": "none",
                    "offsetBottom": "none",
                    "height": "sm"
                }
                ]
            }
            },
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://pic.pimg.tw/bravejim/1605972544-2932113965-g_wn.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "綠光庭園",
                    "weight": "bold",
                    "size": "sm"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                    },
                    {
                        "type": "text",
                        "text": "3.8",
                        "size": "sm",
                        "color": "#8c8c8c",
                        "margin": "md",
                        "flex": 0
                    }
                    ]
                }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "先不要拜託",
                    "text": "先不要拜託!"
                    },
                    "gravity": "bottom",
                    "offsetTop": "none",
                    "offsetBottom": "none",
                    "height": "sm"
                }
                ]
            }
            }
        ]
        }
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def snack(event):
    try:
        message = FlexSendMessage(
            alt_text="選擇下午茶",
            contents=
        {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213",
                "action": {
                "type": "uri",
                "label": "action",
                "uri": "http://linecorp.com/"
                },
                "url": "https://img.onl/tb3t9x"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "木白甜點咖啡店",
                    "weight": "bold",
                    "size": "sm",
                    "wrap": True
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "text",
                        "text": "4.4",
                        "size": "xs",
                        "color": "#8c8c8c",
                        "margin": "md",
                        "flex": 0
                    }
                    ],
                    "position": "relative",
                    "spacing": "none"
                }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "菜單連結",
                    "uri": "https://acarpblog.com/wp-content/uploads/2017/08/%E8%8F%9C%E5%96%AE1.jpg"
                    },
                    "position": "relative",
                    "margin": "none",
                    "style": "link",
                    "gravity": "bottom",
                    "offsetTop": "lg"
                }
                ],
                "action": {
                "type": "uri",
                "label": "action",
                "uri": "http://linecorp.com/"
                },
                "offsetTop": "none",
                "margin": "none",
                "spacing": "none",
                "offsetBottom": "none"
            }
            },
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip11.jpg",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Jumane Cafe' 佐曼咖啡館",
                    "weight": "bold",
                    "size": "sm",
                    "wrap": True
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                    },
                    {
                        "type": "text",
                        "text": "4.2",
                        "size": "sm",
                        "color": "#8c8c8c",
                        "margin": "md",
                        "flex": 0
                    }
                    ]
                }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "菜單連結",
                    "uri": "https://pic.pimg.tw/vilo92/1369088223-2240808140.jpg"
                    },
                    "gravity": "bottom",
                    "offsetTop": "lg"
                }
                ]
            }
            },
            {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213",
                "url": "https://img.onl/c9pyNX"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Hoto Cafe",
                    "weight": "bold",
                    "size": "sm"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "icon",
                        "size": "xs",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                        "type": "text",
                        "text": "4.5",
                        "size": "sm",
                        "color": "#8c8c8c",
                        "margin": "md",
                        "flex": 0
                    }
                    ]
                }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "菜單連結",
                    "uri": "https://pic.pimg.tw/vivianchiu/1501948159-1574194933.jpg"
                    },
                    "gravity": "bottom",
                    "offsetTop": "lg"
                }
                ]
            }
            }
        ]
        }
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def drink(event):
    try:
        message = FlexSendMessage(
            alt_text="選擇飲料",
            contents=
            {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213",
                    "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "http://linecorp.com/"
                    },
                    "url": "https://img.onl/DU386M"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "50嵐",
                        "weight": "bold",
                        "size": "sm",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "3.6",
                            "size": "xs",
                            "color": "#8c8c8c",
                            "margin": "md",
                            "flex": 0
                        }
                        ],
                        "position": "relative",
                        "spacing": "none"
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "菜單連結",
                        "uri": "https://img.onl/GWr20F"
                        },
                        "position": "relative",
                        "margin": "none",
                        "style": "link",
                        "gravity": "bottom",
                        "offsetTop": "lg"
                    }
                    ],
                    "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "http://linecorp.com/"
                    },
                    "offsetTop": "none",
                    "margin": "none",
                    "spacing": "none",
                    "offsetBottom": "none"
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://img.onl/Tsrm6S",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "可不可熟成紅茶",
                        "weight": "bold",
                        "size": "sm",
                        "wrap": True
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "4.0",
                            "size": "sm",
                            "color": "#8c8c8c",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "菜單連結",
                        "uri": "https://img.onl/ve6dr0"
                        },
                        "gravity": "bottom",
                        "offsetTop": "lg"
                    }
                    ]
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "320:213",
                    "url": "https://img.onl/xA3YuZ"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "麻古茶坊",
                        "weight": "bold",
                        "size": "sm"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xs",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        },
                        {
                            "type": "text",
                            "text": "4.5",
                            "size": "sm",
                            "color": "#8c8c8c",
                            "margin": "md",
                            "flex": 0
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "paddingAll": "13px"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "uri",
                        "label": "菜單連結",
                        "uri": "https://img.onl/8rVsYu"
                        },
                        "gravity": "bottom",
                        "offsetTop": "lg"
                    }
                    ]
                }
                }
            ]
            }
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def nothing(event):
    try:
        message = TextSendMessage(
            text='好喔掰掰！'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def HowIsTheWeather(event):
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請傳送目前位置：'))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def sendWeather(event):
    try:
        lat = event.message.latitude
        lon = event.message.longitude
        response = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid=35aada274f86531e1d1e959566f33736&units=metric&lang=zh_tw&lat={lat}&lon={lon}')
        data = response.json()
        weather = data['weather']
        for item in weather:
            print(item)
            weather_description = item['description']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'今日天氣：{weather_description}\n'
                                                                           f'最高溫：{temp_max}度\n'
                                                                           f'最低溫：{temp_min}度'))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def exchangeRate(event):
    try:
        response = requests.get('https://tw.rter.info/capi.php')
        currency = response.json()
        usdToTwd = currency['USDTWD']['Exrate']
        message = TextSendMessage(
            text=f"美元 USD 對台幣 TWD: \n1 : {usdToTwd}"
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def sendImage(event):
    try:
        image_message = ImageSendMessage(
            original_content_url='https://img.onl/6Q0as6',
            preview_image_url='https://img.onl/6Q0as6'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))

def sendVideo(event):
    try:
        video_message = VideoSendMessage(
            original_content_url='https://i.imgur.com/1BnZGQC.mp4',
            preview_image_url='https://i.imgur.com/wpM584d.jpg'
        )
        line_bot_api.reply_message(event.reply_token, video_message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='錯誤！'))