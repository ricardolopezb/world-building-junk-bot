import discord
import random
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Create a new bot instance with the specified command prefix
bot = commands.Bot(command_prefix='!', intents=intents)
# Event listener for when the bot has finished logging in
@bot.event
async def on_ready() :
    print(f'Logged in as {bot.user.name}')
    
# Command to draw a card
@bot.command(name='draw')
async def draw_card(ctx) :
    # Predefined lists of items to choose
    arc_types = [
        'Collapse',
        'Discipline',
        'Grow',
        'Transform'
    ]
    
    arc_timelines = [
        'A few years',
        'A decade',
        'A generation',
        'Two generations',
        'A century',
        'A millennium'
    ]
    
    terrains = [
        'Agriculture',
        'The Brain',
        'Childhood',
        'Citizenship',
        'Class',
        'Climate',
        'Cloning',
        'Communications',
        'Court', 
        'Disease',
        'Drones',
        'The Economy', 
        'Education',
        'Entertainment', 
        'Environment',
        'Equality', 
        'Family',
        'Fashion',
        'Flight',
        'Forests',
        'Genetics',
        'Gender',
        'Governance',
        'Health',
        'Hobbies',
        'Home',
        'Identity',
        'Insects',
        'Intellectual Property',
        'Journalism',
        'Justice',
        'Learning',
        'Memory',
        'Oceans',
        'Oil',
        'Mining', 
        'The Moon',
        'Music',
        'Old Age',
        'Pets',
        'Power',
        'Religion',
        'Robots',
        'Sex',
        'Shopping',
        'Space',
        'Sports',
        'Theatre',
        'Travel', 
        'War',
        'Water',
        'Wealth',
        'Women',
        'Work',
        'Zombies',
        'The Zoo',
        'Wildcard - Topic or location of your choice'
    ]

    
    objects = [
        'Advertisement', 
        'Artwork', 
        'Beverage',
        'Book',
        'Bottle',
        'Clothing',
        'Box', 'Brochure', 'Building',
        'Candy',
        'Corporation',
        'Device',
        'Document',
        'Event',
        'Festival',
        'Flag',
        'Game',
        'Gift',
        'Headline',
        'Implant',
        'Instrument',
        'Jewellery',
        'Kit',
        'Law',
        'Logo',
        'Lotion',
        'Machine', 'Magazine',
        'Cover',
        'Map',
        'Mask',
        'Monument',
        'Passport',
        'Pill',
        'Plant',
        'Postcard',
        'Poster',
        'Product',
        'Prosthetic',
        'Public service announcement',
        'Relic',
        'Ritual',
        'Show',
        'Slogan',
        'Snack',
        'Song',
        'Souvenir',
        'Statue',
        'Sticker', 'Symbol',
        'Tattoo',
        'Tool',
        'Toy',
        'Vehicle', 'Video',
        'T-Shirt',
        'Weapon',
        'Wildcard - Artifact of your choice'
    ]

    moods = [
        'Admiration', 
        'Alienation',
        'Amusement',
        'Anger',
        'Anxiety',
        'Awkwardness',
        'Calm', 'Charm', 'Cheer',
        'Contentment',
        'Curiosity',
        'Decadence', 'Delight',
        'Dignity', 'Disgust', 'Dread',
        'Embarrassment',
        'Excitement', 'Exhilaration',
        'Fascination',
        'Fervor',
        'Frustration',
        'Gratitude',
        'Happiness',
        'Hilarity',
        'Hope',
        'Longing',
        'Malaise',
        'Melancholy',
        'Melodrama',
        'Nostalgia', 'Optimism', 'Outrage',
        'Pathos',
        'Pleasure',
        'Pride',
        'Rationality',
        'Relief',
        'Resentment',
        'Respect',
        'Sadness',
        'Satisfaction', 'Serenity',
        'Shame',
        'Shock',
        'Sorrow', 'Surprise', 'Unease', 'Warmth', 'Weirdness',
        'Wellbeing',
        'Wonder',
        'Worry',
        'Zen'
    ]

    # Randomly select one item from each list
    arc_type = random.choice(arc_types)
    arc_timeline = random.choice(arc_timelines)
    terrain = random.choice(terrains)
    object = random.choice(objects)
    mood = random.choice(moods)
    # Format the response message
    response = (
    f'\n**Here\'s your ATOM draw!**\n\n'
    f'**A - Arc Card Draw:**\n> Arc Type: {arc_type}\n> Arc Timeline: {arc_timeline}\n\n'
    f'**T - Terrain Card Draw:**\n> Terrain: {terrain}\n\n'
    f'**O - Object Card Draw:**\n> Object: {object}\n\n'
    f'**M - Mood Card Draw:**\n> Mood: {mood}'
    )
    # Send the response message to the Discord channel
    await ctx.send (response)
    
@bot.command(name='info')
async def info(ctx) :
    help_message = (
    '''
:globe_with_meridians:  **The Thing From The Future / ATOM is an imagination game.** \nThe object of the game is to use the cards to generate the most interesting, funny or thought-provoking ideas for artifacts from the future. There are over 3.7 million possible prompts in the deck. 

:black_joker: **Use _!draw_ to shuffle the deck and get a unique set of cards.**


**There are 4 cards deployed in every shuffle** :small_blue_diamond: :small_blue_diamond: :small_blue_diamond: :small_blue_diamond: 

> **A - ARC** outlines the type of future world that the “thing” comes from, and how far away it is from today. _There are four types of Arc, each an umbrella for countless possible scenarios:_
> _------- Growth - a future in which “progress” has continued_
> _------- Collapse – a future in which society as we know it has come apart_
> _------- Discipline - a future in which order is deliberately coordinated or imposed_
> _------- Transformation – a future in which a profound historical evolution has occurred_
> 
> **T - TERRAIN** is the thematic context or location where this object could be found in that future.
> 
> **O - OBJECT** is the focus for your imagination: a specific cultural artifact that reveals something about how this future is different from today.
> 
> **M - MOOD** suggests how it might feel to experience this thing from the future.


*A game by Stuart Candy and Jeff Watson*
2015 CC-BY-NC-SA | situationlab.org | @sitlab
Discord implementation by JUNK Consortium - Universidad Austral, Argentina (2024)
    ''')
    await ctx.send(help_message)
    
# Start the bot with your unique token
bot.run(os.environ["BOT_TOKEN"])
