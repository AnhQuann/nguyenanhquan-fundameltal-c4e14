from mlab import mlab_connect
from models.champ import Champ
from random import choice

mlab_connect()

champ_name = [
    # A
    "Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "Aurelion Sol", "Azir",
    # B
    "Bard", "Blitzcrank", "Brand", "Braum",
    # C
    "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki",
    # D
    "Darius", "Diana", "Dr. Mundo", "Draven",
    # E
    "Ekko", "Elise", "Evelynn", "Ezreal",
    # F
    "Fiddlesticks", "Fiora", "Fizz",
    # G
    "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves",
    # H
    "Hecarim", "Heimerdinger",
    # I
    "Illaoi", "Irelia", "Ivern",
    # J
    "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx",
    # K
    "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'zix", "Kindred", "Kled", "Kog'Maw",
    # L
    "LeBlanc", "Lee Sin", "Leona", "Lissandra", "Lucian", "Lulu", "Lux",
    # M
    "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana",
    # N
    "Nami", "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu",
    # O
    "Olaf", "Orianna", "Ornn",
    # P
    "Pantheon", "Poppy",
    # Q
    "Quinn",
    # R
    "Rakan", "Rammus", "Rek'Sai", "Renekton", "Rengar", "Riven", "Rumble", "Ryze",
    # S
    "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Syndra",
    # T
    "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
    # U
    "Udyr", "Urgot",
    # V
    "Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir", "Volibear",
    # W
    "Warwick", "Wukong",
    # X
    "Xayah", "Xerath", "Xin Zhao",
    # Y
    "Yasuo", "Yorick",
    # Z
    "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"
]

champ_role = ["Assassin", "Maskman", "Mage", "Support", "Tank", "Fighter"]

for i in champ_name:
    champ = Champ(
        image = i + ".png",
        name = i,
        role = choice(champ_role)
    )
    champ.save()
