import discord
from discord import ui

from client import bot


class Message(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Sim, confirmar!", emoji=discord.PartialEmoji.from_str("<a:870209867221200906:>"),
                       style=discord.ButtonStyle.success)
    async def iniciar(self, interaction: discord.Interaction, button: discord.ui.Button,
                      custom_id='persistent_view:green'):
        await interaction.response.send_modal(InputModal(interaction))

    @discord.ui.button(label="Não, cancelar.", emoji=discord.PartialEmoji.from_str("<a:870209867221200906:>"),
                       style=discord.ButtonStyle.red)
    async def finalizar(self, interaction: discord.Interaction, button: discord.ui.Button,
                        custom_id='persistent_view:red'):
        await interaction.message.delete()


class InputModal(ui.Modal, title="Postagem com Embed"):
    def __init__(self, interaction):
        super().__init__(timeout=None)
        self.interaction = interaction

    custom_title = ui.TextInput(label="Escolha o título:", style=discord.TextStyle.short,
                                required=False)

    normal_text = ui.TextInput(label="Insira o texto comum:", style=discord.TextStyle.short,
                               required=False)

    embed_text = ui.TextInput(label="Insira o texto do embed:", style=discord.TextStyle.paragraph,
                              required=False)

    image_url = ui.TextInput(label="Insira o link da imagem:", style=discord.TextStyle.short,
                             required=False)

    custom_color = ui.TextInput(label="Escolha a cor:", placeholder="Apenas roxo ou rosa",
                                style=discord.TextStyle.short,
                                required=False)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer()

        embed = discord.Embed(
            title=self.custom_title,
            description=self.embed_text,
            color=get_post_color(self.custom_color)
        )

        embed.set_image(url=self.image_url)

        message = await self.interaction.channel.send(content=self.normal_text, embed=embed)

        await message.add_reaction("❤️")
        await message.add_reaction("🔥")
        await message.add_reaction("🚀")

        await self.interaction.message.delete()


def get_post_color(custom_color):
    custom_color = custom_color.value.lower()

    if custom_color == "roxo":
        return discord.Color.dark_purple()
    elif custom_color == "rosa":
        return discord.Color.from_rgb(255, 105, 180)
    else:
        return discord.Color.light_grey()


@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(
        colour=discord.Colour.light_gray(),
        description="Deseja fazer uma postagem com Embed?"
    )
    view = Message()
    await ctx.send(view=view, embed=embed)

    await ctx.message.delete()