contents = [{"type": "bubble", "size": "micro", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "gravity": "center", "text": "1"}, {"type": "button", "style": "primary", "action": {"type": "postback", "label": "123", "data": "{\"user_id\": \"1\", \"exchange_type\": \"buy\", \"order_price\": \"123\"}"}}]}}, {"type": "bubble", "size": "micro", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "gravity": "center", "text": "2"}, {"type": "button", "style": "primary", "action": {"type": "postback", "label": "20.3", "data": "{\"user_id\": \"2\", \"exchange_type\": \"buy\", \"order_price\": \"20.3\"}"}}]}}, {"type": "bubble", "size": "micro", "body": {"type": "box", "layout": "vertical", "contents": [{"type": "text", "gravity": "center", "text": "3"}, {"type": "button", "style": "primary", "action": {"type": "postback", "label": "2.7", "data": "{\"user_id\": \"3\", \"exchange_type\": \"buy\", \"order_price\": \"2.7\"}"}}]}}, {"type": "bubble", "size": "micro", "body": {"type": "box", "layout": "vertical", "spacing": "sm", "contents": [{"type": "button", "flex": 1, "gravity": "center", "action": {"type": "postback", "label": "See more sell_list", "data": "{\"coin\": \"sell_list\", \"page\": \"3\"}"}}]}}]
flex_message = FlexSendMessage(
    alt_text='carousel_list',
    contents={"type": "carousel", "contents": contents}
)
line_bot_api.reply_message(event.reply_token, flex_message)
##########
wallet_menu_flex = json.load(open("/home/jedaya9253/mysite/wallet_menu_flex.json", 'r', encoding='utf8'))
flex_message = FlexSendMessage(
    alt_text='錢包選單',
    contents=wallet_menu_flex
)
line_bot_api.reply_message(event.reply_token, flex_message)
