import discord
import schedule
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
        client.loop.create_task(self.my_background_task())

##Background Task
    async def my_background_task(self):
        await client.wait_until_ready()
        schedule.every().hour.at(":20").do(self.job)
        while not client.is_closed():
            schedule.run_pending()
            await asyncio.sleep(1)

##Send Message / Get Channel
    async def job_async(self):
        channel = client.get_channel(1125166718730371102)
        await channel.send("||<@&1125166904949096458>||\n > **It's 4:20 somewhere, CHEERS!** <:weed:1051662934339760189>")
        
    def job(self):
        client.loop.create_task(self.job_async())

intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run('KEY HERE')
