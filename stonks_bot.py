import discord
import os

import finnhub_client

print("Enter Discord Bot API Token:", end='')
DISCORD_BOT_TOKEN = input()



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    async def on_message(self, message):
        
        mchannel = message.channel
        
        print('Message from {0.author}'.format(message))
        if (message.content and message.content[0] == '$'):
            if not (message.content[1].isdigit()):
                if (' ' in message.content):
                    SPLIT = message.content.split(' ')
                    print(SPLIT)
                    acronym = SPLIT[0][1:].upper()
                    time_period = SPLIT[-1]
                
                    try:
                        res = finnhub_client.get_stock_candles(acronym, time_period)
                        finnhub_client.plot_stock_data(res)
                        await mchannel.send(file=discord.File('fig1.png'))
                    except Exception as e:
                        print(e)

                else:
                    acronym = message.content[1:].upper()
                    print(acronym)
                    try:
                        curr_price, delta, percent_change = finnhub_client.get_quote(acronym)
                        if (delta[0] == '+'):
                            await mchannel.send('```diff\n+{0}: {1}\n{2} / {3}```'.format(acronym, 
                                                                               curr_price,
                                                                               delta,
                                                                               percent_change))
                        else:
                            await mchannel.send('```diff\n-{0}: {1}\n{2} / {3}```'.format(acronym,
                                                                                curr_price,
                                                                                delta,
                                                                                percent_change))
                    except Exception as e:
                        print(e)

client = MyClient()
client.run(DISCORD_BOT_TOKEN)
