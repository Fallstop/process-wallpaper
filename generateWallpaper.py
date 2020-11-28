import re
from PIL import Image
from wordcloud import WordCloud
import json
import os

commandList = []

with open("top.out", "r") as topFile:
    topOutput = topFile.read().split("\n")[7:]

    for line in topOutput[:-1]:
        line = re.sub(r'\s+', ' ', line).strip()
        fields = line.split(" ")

        try:
            if fields[11].count("/") > 0:
                command = fields[11].split("/")[0]
            else:
                command = fields[11]

            cpu = float(fields[8].replace(",", "."))
            mem = float(fields[9].replace(",", "."))

            if command != "top":
                commandList.append((command, cpu, mem))
        except:
            pass

commandDict = {}

for command, cpu, mem in commandList:
    if command in commandDict:
        commandDict[command][0] += cpu
        commandDict[command][1] += mem
    else:
        commandDict[command] = [cpu + 1, mem + 1]

resourceDict = {}

for command, [cpu, mem] in commandDict.items():
    resourceDict[command] = (cpu ** 2 + mem ** 2) ** 0.5

configJSON = json.loads(open("config.json", "r").read())

width, height = None, None
try:
    width, height = ((os.popen("xrandr | grep '*'").read()).split()[0]).split("x")
    width = int(width)*configJSON['resolution']["downScaler"]
    height = int(height)*configJSON['resolution']["downScaler"]
except:
    pass

if not width or not height:
    width = configJSON['resolution']['width']*configJSON['resolution']["downScaler"]
    height = configJSON['resolution']['height']*configJSON['resolution']["downScaler"]

wc = WordCloud(
    background_color="rgba(255, 255, 255, 0)",
    mode="RGBA",
    width=width - 2 * int(configJSON["wordcloud"]["margin"]),
    height=height - 2 * int(configJSON["wordcloud"]["margin"])
).generate_from_frequencies(resourceDict)

wc.to_file('wc.png')

wordcloud = Image.open("wc.png")
wallpaper = Image.new('RGBA', (width, height), configJSON["wordcloud"]["background"])
wallpaper.paste(
    Image.open("backgroundImage.png").resize((width, height))
) 
wallpaper.paste(
    wordcloud,
    (
        configJSON["wordcloud"]["margin"],
        configJSON["wordcloud"]["margin"]
    ),
    mask=wordcloud
)

wallpaperScaled = wallpaper.resize((configJSON['resolution']['width'],configJSON['resolution']['height']),resample=Image.ANTIALIAS) 

wallpaperScaled.save("wallpaper.png")
