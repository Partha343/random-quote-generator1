import csv

quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "Everything you’ve ever wanted is on the other side of fear. – George Addair",
    "Dream big and dare to fail. – Norman Vaughan",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Act as if what you do makes a difference. It does. – William James",
    "Never bend your head. Always hold it high. Look the world straight in the eye. – Helen Keller",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "Try to be a rainbow in someone else's cloud. – Maya Angelou",
    "You do not find the happy life. You make it. – Camilla Eyring Kimball",
    "The most wasted of days is one without laughter. – E.E. Cummings",
    "You must do the things you think you cannot do. – Eleanor Roosevelt",
    "In a gentle way, you can shake the world. – Mahatma Gandhi",
    "Let us make our future now, and let us make our dreams tomorrow’s reality. – Malala Yousafzai",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Everything you can imagine is real. – Pablo Picasso",
    "Whatever you are, be a good one. – Abraham Lincoln",
    "Turn your wounds into wisdom. – Oprah Winfrey",
    "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
    "If opportunity doesn't knock, build a door. – Milton Berle",
    "I am not a product of my circumstances. I am a product of my decisions. – Stephen R. Covey",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Start where you are. Use what you have. Do what you can. – Arthur Ashe",
    "Don’t wait. The time will never be just right. – Napoleon Hill",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "Be yourself; everyone else is already taken. – Oscar Wilde",
    "Be the change that you wish to see in the world. – Mahatma Gandhi",
    "No act of kindness, no matter how small, is ever wasted. – Aesop",
    "Limit your ‘always’ and your ‘nevers.’ – Amy Poehler",
    "Light tomorrow with today. – Elizabeth Barrett Browning",
    "Nothing is impossible. The word itself says ‘I’m possible!’ – Audrey Hepburn",
    "You are enough just as you are. – Meghan Markle",
    "Stay foolish to stay sane. – Maxime Lagacé",
    "Try again. Fail again. Fail better. – Samuel Beckett",
    "Be so good they can’t ignore you. – Steve Martin",
    "Fall seven times, stand up eight. – Japanese Proverb",
    "Action is the foundational key to all success. – Pablo Picasso",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Great things never come from comfort zones.",
    "Push yourself, because no one else is going to do it for you.",
    "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
    "The key to success is to focus on goals, not obstacles.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work, the luckier you get. – Gary Player",
    "If you want it, work for it.",
    "Don't stop when you're tired. Stop when you're done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t wait for opportunity. Create it.",
    "Sometimes later becomes never. Do it now.",
    "Success is what comes after you stop making excuses.",
    "Work hard in silence, let your success be the noise.",
    "Don’t limit your challenges. Challenge your limits.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "It always seems impossible until it's done.",
    "Opportunities don't happen. You create them.",
    "Doubt kills more dreams than failure ever will.",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Do what you feel in your heart to be right – for you’ll be criticized anyway.",
    "Magic is believing in yourself. If you can do that, you can make anything happen.",
    "The secret of getting ahead is getting started.",
    "Your passion is waiting for your courage to catch up.",
    "Don’t wish it were easier. Wish you were better.",
    "You are capable of amazing things.",
    "Start each day with a positive thought.",
    "You don’t need to see the whole staircase, just take the first step.",
    "Success is not for the lazy.",
    "If you can dream it, you can do it.",
    "Chase your dreams until you catch them… and then dream, catch, and dream again!",
    "Success is the sum of small efforts, repeated day in and day out.",
    "What we fear doing most is usually what we most need to do.",
    "Don’t count the days, make the days count. – Muhammad Ali",
    "Life is short. Do stuff that matters.",
    "Keep going. Everything you need will come to you at the perfect time.",
    "If you're going through hell, keep going. – Winston Churchill",
    "Believe in yourself and all that you are.",
    "Take the risk or lose the chance.",
    "Don't tell people your plans. Show them your results.",
    "Prove them wrong.",
    "Difficult roads often lead to beautiful destinations.",
    "You didn’t come this far to only come this far.",
    "Stay positive, work hard, make it happen.",
    "Work until you no longer have to introduce yourself.",
    "Discipline is doing what needs to be done, even if you don’t want to do it.",
    "You are stronger than you think."
]

# Write to CSV
with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['quote'])  # header
    for q in quotes:
        writer.writerow([q])

print("✅ quotes.csv with 100 quotes has been created.")
