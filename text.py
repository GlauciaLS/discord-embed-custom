from client import bot


@bot.command(pass_context=True)
async def text(ctx):
    message_split = ctx.message.content.split("!text ")
    await ctx.send(content=message_split[1])

    await ctx.message.delete()
