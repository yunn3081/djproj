from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, QuickReply, QuickReplyButton, MessageAction
from musics.models import Music

line_bot_api = LineBotApi(settings.LINE_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                mtext=event.message.text
                message=[]
                if mtext == '熱門音樂排行榜':
                    try:
                        songs, singers = utils()
                        txt = '今天的熱門排行榜：\n\n'
                        count = 1
                        for song, singer in zip(songs, singers):
                            if count == 50:
                                buffer = 'Rank #' + str(count) + '\n歌名: ' + song + '\n歌手: ' + singer
                            else:
                                buffer = 'Rank #' + str(count) + '\n歌名: ' + song + '\n歌手: ' + singer + '\n\n'
                            txt += buffer
                            count += 1

                        message = TextSendMessage(
                            text=txt,
                            quick_reply = QuickReply(
                                items=[
                                    QuickReplyButton(
                                        action = MessageAction(label='熱門音樂排行榜', text='熱門音樂排行榜')
                                    )
                                ]
                            )
                        )
                        line_bot_api.reply_message(event.reply_token, message)
                    except:
                        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Something wrong'))
                #message.append(TextSendMessage(text=mtext))
                # line_bot_api.reply_message(event.reply_token,message)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

def utils():
    song = list(Music.objects.values_list('song',flat=True))[-50:]
    singer = list(Music.objects.values_list('singer',flat=True))[-50:]

    return(song, singer)
