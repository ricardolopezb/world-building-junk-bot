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
    f'```**Here\'s your ATOM draw!**\n'
    f'**A - Arc Card Draw:**\nArc Type: {arc_type}\nArc Timeline: {arc_timeline}\n'
    f'**T - Terrain Card Draw:**\nTerrain: {terrain}\n'
    f'**O - Object Card Draw:**\nObject: {object}\n'
    f'**M - Mood Card Draw:**\nMood: {mood}```'
    )
    # Send the response message to the Discord channel
    await ctx.send (response)
    
    
# Start the bot with your unique token
bot.run(os.environ["BOT_TOKEN"])
