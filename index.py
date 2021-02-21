import random,requests,string,discord,asyncio,time,datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.ext.commands import Bot
from discord.ext import commands


# Random Str Func
def get_random_string(length):return (''.join(random.choice(string.ascii_lowercase) for i in range(length))+'_Mr28')
# Click Download Button
def clickBu(url):    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
    driver.get(url)
    driver.find_element_by_id('percentageText').click()
    time.sleep(2)
    driver.close()
# short Url
def shortUrl(url):
    id = get_random_string(8)
    requests.post('https://v.ht/processreq.php', data = {'txt_url': url,'txt_name': id})
    return "https://v.ht/"+id
# Start Bot
class Mr28Bot(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Type $onii_chan'))
        print('Connected to bot: {}'.format(client.user.name))
        print('Bot ID: {}'.format(client.user.id))
    async def on_message(self, message):
        if message.content.startswith('$mp4') | message.content.startswith('$mp3'):
            if ('https://www.youtube.com/watch?v' in message.content)&(len(message.content) > 37):
                f = message.content.partition(' ')[0].replace('$', '')
                downloadLink = ("https://loader.to/api/button/?f="+f+"&url="+message.content.replace('$mp4', '').replace('$mp3', '')).replace(" ","")
                print(message.content.replace('$mp4', '').replace('$mp3', ''))
                clickBu(downloadLink)
                embedVar = discord.Embed(description="please wait 5s ...😁", color=0x5396D2)
                await message.channel.send(embed=embedVar)
                time.sleep(5)
                embedVar = discord.Embed(title="Download Mp3 & Mp4 From YouTube :purple_heart: ", color=0x5200A3)
                embedVar.add_field(name="Download Link :", value=shortUrl(downloadLink), inline=False)
                await message.channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(description="invalid youtube video 😥❌", color=0xFF0000)
                await message.channel.send(embed=embedVar)
        if message.content.startswith('$onii_chan'):
            embedVar = discord.Embed(title="Download Mp3 & Mp4 From YouTube :purple_heart: ", description="Type $mp3 Youtube Link : to download 'Mp3' Sound \nType $mp4 Youtube Link : to download Mp4 Video\n Type #onii_chan To help.\n\nProgrammed By ＳＡＩＦ 剣 \n Contact : \nGitHub : JUSTSAIF\nINSTA : @qq_iq", color=0xFFFF00)
            await message.channel.send(embed=embedVar)
        else:
            pass
client = Mr28Bot()
client.run('NzQyMzY3NzgxMzk1MTAzNzQ2.XzFF3w.dQzxswGG7X6lt-nkXNWBI0rhSFI')