import discord


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.auther == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('hello')

client.run(NzA0ODU2MTg0NDczMTI0OTA0.XqjOeQ.-tTVsX90uAsbJJhE-p333asu2nM)