# Import python modules.
# Import internal modules.
import api_stock_exchange as stk
import api_news as news
import send_sms as snd
# Constants.
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STK_VARIANCE = 0.03  # About 3% variance.


def create_sms_message(in_stk_variance: float, in_tesla_news_list: list) -> str:
    out_sms_message = ''
    if in_stk_variance < 0:
        out_sms_message += f'TSLA: 🔻{round(abs(in_stk_variance * 100), 1)}%\n'
    else:
        out_sms_message += f'TSLA: 🔺{round(abs(in_stk_variance * 100), 1)}%\n'
    # Headline 1.
    out_sms_message += f"Headline: {in_tesla_news_list[0]['title']}\n"
    out_sms_message += f"Brief: {in_tesla_news_list[0]['description']}\n"
    # Headline 2.
    out_sms_message += f"Headline: {in_tesla_news_list[1]['title']}\n"
    out_sms_message += f"Brief: {in_tesla_news_list[1]['description']}\n"
    return out_sms_message


def stock_exchange():
    # STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    tesla_stock_obj = stk.StockExchange('TSLA')
    tesla_stock_dict = tesla_stock_obj.get_last_2_days()
    # See data example in json_data_samples.json
    stk_value_d_1, stk_value_d_2 = (float(item['4. close']) for item in tesla_stock_dict.values())
    stk_variance = (stk_value_d_2 / stk_value_d_1) - 1
    if abs(stk_variance) > STK_VARIANCE:
        # STEP 2: Use https://newsapi.org
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
        tesla_news_obj = news.News('Tesla')
        tesla_news_list = tesla_news_obj.get_last_headlines(3)
        # Create message.
        sms_message_to_send = create_sms_message(stk_variance, tesla_news_list)
        # STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and
        # description to your phone number.
        sms_sender = snd.TwilioSMS()
        sms_sender.send_sms(sms_message_to_send)
    return

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == '__main__':
    stock_exchange()
