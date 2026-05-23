import re

filepath = r'C:\Users\Administrator\smartpetguide\src\pages\guides\[slug].astro'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

mapping = {
    'Capacity: How Big Should Your Feeder Be?': 'How Big Should Your Automatic Feeder Be?',
    'Camera vs No Camera': 'Should You Get an Automatic Feeder With a Built-in Camera?',
    'App Reliability': 'How Important Is App Reliability for a Smart Feeder?',
    'Power Backup': 'Do You Need Battery Backup for Your Automatic Feeder?',
    'Food Type Compatibility': 'What Type of Food Works in an Automatic Feeder?',

    'How Self-Cleaning Litter Boxes Work': 'How Do Self-Cleaning Litter Boxes Actually Work?',
    'Sifting vs. Rotating: Which Mechanism Is Better?': 'Which Litter Box Cleaning Mechanism Is Better: Sifting or Rotating?',
    'How Many Cats Do You Have?': 'How Many Cats Will Use the Automatic Litter Box?',
    'Space Requirements': 'How Much Space Does a Self-Cleaning Litter Box Need?',
    'Odor Control Features': 'What Odor Control Features Should You Look For?',
    'Ongoing Costs': 'How Much Do Self-Cleaning Litter Boxes Cost to Maintain?',

    'Filtration: The Most Important Feature': 'Why Is Filtration the Most Important Feature in a Cat Fountain?',
    'Material: Stainless Steel vs Plastic vs Ceramic': 'Which Cat Fountain Material Is Best: Steel, Plastic, or Ceramic?',
    'Capacity: Match It to Your Pet Household': 'What Size Cat Water Fountain Do You Need?',
    'Smart vs Simple: Do You Need an App?': 'Do You Need a Smart Cat Fountain With an App?',
    'Noise and Pump Quality': 'How Quiet Should a Cat Water Fountain Be?',

    'Treat Tossing vs Monitoring Only': 'Should You Get a Treat-Tossing Pet Camera or Just Monitoring?',
    'Pan/Tilt vs Fixed Wide-Angle': 'Which Is Better: Pan/Tilt or Fixed Wide-Angle Pet Camera?',
    'Subscription Costs: The Hidden Expense': 'How Much Do Pet Camera Subscriptions Really Cost?',
    'Night Vision and Video Quality': 'What Video Quality and Night Vision Do You Need in a Pet Camera?',
    'Smart Home Integration': 'Do You Need Smart Home Integration for Your Pet Camera?',

    'Subscription vs No Subscription: The Biggest Decision': 'Should You Pay a Monthly Fee for a GPS Dog Tracker?',
    'Range: How Far Can It Track?': 'How Far Can a GPS Dog Tracker Track Your Pet?',
    'Battery Life: Days vs Weeks': 'How Long Do GPS Dog Tracker Batteries Actually Last?',
    "Collar Compatibility & Size": 'Will a GPS Tracker Fit Your Dog\'s Collar?',
    'Water Resistance': 'Do GPS Dog Trackers Need to Be Waterproof?',

    'The Three-Device Travel Stack': 'What Devices Do You Need to Monitor Your Pet While Traveling?',
    'Camera Placement Strategy': "Where Should You Place Pet Cameras When You're Away?",
    "Feeder Redundancy — Don't Trust One Device": 'Why Should You Have a Backup Feeder When Traveling?',
    'Power and Internet Backup': 'How Do You Keep Pet Devices Running During Power Outages?',
    'What If Something Goes Wrong?': "What Should You Do If Your Pet Devices Fail While You're Away?",

    'The Multi-Pet Feeding Problem': "How Do You Stop One Pet From Eating Another's Food?",
    'Litter Box Math for Multiple Cats': 'How Many Litter Boxes Do You Need for Multiple Cats?',
    'Water Stations for Multiple Pets': 'How Many Water Fountains Do Multi-Pet Homes Need?',
    'Managing Different Dietary Needs': 'How Do You Feed Pets With Different Diets in the Same Home?',
    'Monitoring Individual Pet Health': 'How Can Smart Devices Track Individual Pet Health?',

    'The Time Savings Are Real': 'How Much Time Do Self-Cleaning Litter Boxes Actually Save?',
    'The True 3-Year Cost': 'What Is the True 3-Year Cost of a Self-Cleaning Litter Box?',
    'Odor Control: The Killer Feature': 'How Well Do Automatic Litter Boxes Control Odor?',
    'Who Should NOT Buy an Automatic Litter Box': 'Who Should NOT Buy a Self-Cleaning Litter Box?',
    'Budget Picks That Make Sense': 'What Are the Best Budget Self-Cleaning Litter Boxes?',

    'The Portion Control Problem': 'Why Is Portion Control the #1 Cause of Pet Obesity?',
    'Meal Splitting: Why Frequency Matters': 'How Many Meals Per Day Should Your Pet Eat?',
    'The Data: Weight Loss Results': 'Can Automatic Feeders Actually Help Pets Lose Weight?',
    'Feeders That Excel at Portion Control': 'Which Automatic Feeders Have the Best Portion Control?',
    'The Exercise Companion': 'Is an Automatic Feeder Enough for Pet Weight Loss?',

    'The $100 Rule: What to Prioritize': 'What Should You Prioritize in a $100 Pet Tech Budget?',
    'The Budget Feeder: DOGNESS Mini ($99 → Often on sale)': 'What Is the Best Budget Automatic Feeder Under $100?',
    'The Budget Fountain: Pioneer Pet Raindrop ($39)': 'What Is the Best Budget Cat Water Fountain?',
    'The Budget Camera: Repurpose an Old Phone + AlfredCamera App (Free)': 'Can You Use an Old Phone as a Pet Camera?',
    "What You're Missing at $100": 'What Do You Sacrifice With a $100 Pet Tech Budget?',

    'The $250-400 Sweet Spot': 'What Is the Best Mid-Range Pet Tech Setup Under $400?',
    'The Camera Feeder: Petlibro Granary ($139)': 'Is the Petlibro Granary the Best Camera Feeder for the Price?',
    'The Smart Fountain: PETKIT Eversweet Solo 2 ($59)': 'Is the PETKIT Eversweet the Best Smart Fountain Under $60?',
    'The Pet Camera: xpai 4K ($43) or eufy ($129)': 'Which Budget Pet Camera Offers Better Value: xpai 4K or eufy?',
    'Total Cost': 'How Much Does a Complete Mid-Range Pet Tech Setup Cost?',

    'The Premium Philosophy': 'Is a Premium Pet Tech Setup Worth the Investment?',
    'The Ultimate Litter Box: Litter-Robot 4 ($699)': 'Is the Litter-Robot 4 the Best Automatic Litter Box?',
    'The Camera Feeder: Petlibro Granary ($139)': 'Why Is the Petlibro Granary Still the Best Premium Feeder Pick?',
    'The Interactive Camera: Furbo 360 ($179)': 'Is the Furbo 360 the Best Interactive Dog Camera?',
    'The GPS Tracker: Aorkuler ($229) or Tractive ($79)': 'Which Premium GPS Tracker Is Better: Aorkuler or Tractive?',

    'Why Stainless Steel Matters for Cat Health': 'Why Does Stainless Steel Matter for Your Cat\'s Health?',
    'Stainless Steel vs Ceramic vs Plastic': 'Which Is the Best Material for a Cat Water Fountain?',
    'Pump vs Pumpless: Which Design?': 'Should You Choose a Pump or Pumpless Cat Fountain?',
    'Sizing: How Big Should Your Fountain Be?': 'What Size Cat Water Fountain Do You Need?',
    'Cleaning & Maintenance': 'How Often Should You Clean a Stainless Steel Cat Fountain?',
    'Our Top Picks': 'What Are the Best Stainless Steel Cat Fountains in 2026?',
}

count = 0
for old, new in mapping.items():
    old_pattern = f'heading: "{old}"'
    new_pattern = f'heading: "{new}"'
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern)
        count += 1

print(f'Updated {count} headings out of {len(mapping)}')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
