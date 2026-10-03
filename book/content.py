"""Book content. One dict per concept = one page.

Keys: title, idea, know (code), req, inputs, output, steps (list), code, tips (list), tryit (list of (level, text))
Levels: M = micro, C = combination, R = real requirement
"""

CONCEPTS = [
# ------------------------------------------------------------ BASICS
dict(
 part="BASICS", title="Variables and types",
 idea="A variable is a named box that holds a value. The type of the value decides what you can do with it.",
 know='''
price = 4.5            # float  (decimal)
count = 3              # int    (whole number)
name = "Mug"           # str    (text, needs quotes)
in_stock = True        # bool   (True / False, capital letter)
total = price * count  # right side is calculated, then stored
print(type(price))     # <class 'float'>
print(name, total)     # Mug 13.5
''',
 req="A mug costs $4.50. A customer buys 3. Show the total cost.",
 inputs="price = 4.5, quantity = 3", output="the total cost (a number)",
 steps=["Store the price in a variable.", "Store the quantity in a variable.",
        "Multiply them and store the result.", "Print the result."],
 code='''
price = 4.5
quantity = 3
total_cost = price * quantity
print(total_cost)
''',
 tips=["Name variables after what they hold: `total_cost`, not `x`.",
       "`=` stores a value. `==` compares two values. Never mix them up.",
       "`\"5\"` (text) and `5` (number) are different things. `\"5\" + 1` is an error.",
       "Convert when needed: `int(\"7\")`, `float(\"2.5\")`, `str(10)`."],
 tryit=[("M", "Make variables for your name and age. Print both on one line."),
        ("C", "Store a temperature in Celsius. Compute and print Fahrenheit: c * 9 / 5 + 32."),
        ("R", "A phone costs 300 and tax is 8%. Print the price, the tax amount, and the final price."),
        ("C", "Swap the values of `a = 5` and `b = 9` without losing either value.")],
),
dict(
 part="BASICS", title="Input and output",
 idea="input() asks the user for text. print() shows results. Everything typed in arrives as a string, so convert it before doing math.",
 know='''
name = input("Name: ")              # always a str
age = int(input("Age: "))           # whole number
rate = float(input("Rate: "))       # decimal number

print("Hi", name)                   # Hi Sam
print(f"Hi {name}, you are {age}")  # f-string: variables inside {}
print(f"Pay: {rate * 8:.2f}")       # :.2f = exactly 2 decimals
print("a", "b", sep="-")            # a-b
print("no newline", end="")         # next print continues on same line
''',
 req="Ask for a distance in kilometres. Print it in miles (1 km = 0.621 miles), with 2 decimals.",
 inputs="km, typed by the user (text -> float)", output="a line of text with miles to 2 decimals",
 steps=["Ask for the distance and convert the text to a float.", "miles = km * 0.621",
        "Print a sentence with miles formatted to 2 decimals."],
 code='''
km = float(input("Distance in km: "))
miles = km * 0.621
print(f"{km} km is {miles:.2f} miles")
''',
 tips=["`input()` ALWAYS returns text. `\"10\" + \"5\"` is `\"105\"`, not 15.",
       "Forgot `int()`/`float()`? Expect a `TypeError`.",
       "An f-string needs the `f` BEFORE the opening quote: `f\"...{x}...\"`.",
       "Your prompt should tell the user what to type: `\"Distance in km: \"`."],
 tryit=[("M", "Ask for a name and print: Hello, <name>!"),
        ("M", "Ask for a word and print it 3 times separated by dashes."),
        ("C", "Ask for two numbers. Print their sum and their product on separate lines."),
        ("R", "Ask for hours worked and hourly rate. Print the pay with exactly 2 decimals.")],
),
dict(
 part="BASICS", title="Arithmetic",
 idea="Python does math with operators. Two of them, // and %, solve most 'split into parts' problems.",
 know='''
7 + 2   7 - 2   7 * 2      # 9  5  14
7 / 2                      # 3.5   (always a decimal)
7 // 2                     # 3     (whole-number division)
7 % 2                      # 1     (remainder)
2 ** 5                     # 32    (power)
total += 5                 # same as total = total + 5   (also -= *= /=)
abs(-4)  min(3, 9)  max(3, 9)  round(3.14159, 2)   # 4  3  9  3.14
n % 2 == 0                 # True when n is even
n % 10                     # last digit      n // 10  # all but last digit
''',
 req="Convert 275 minutes into hours and remaining minutes.",
 inputs="total_minutes = 275", output="hours and minutes, e.g. 4 hours 35 minutes",
 steps=["Whole hours = total_minutes // 60.", "Leftover minutes = total_minutes % 60.", "Print both."],
 code='''
total_minutes = 275
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{hours} hours {minutes} minutes")
''',
 tips=["`//` and `%` come as a pair: how many full groups, and what is left over.",
       "Use `/` for averages and prices. Use `//` for counting whole things.",
       "`2 ** 3` is 8. `^` means something else in Python. Do not use it.",
       "Percent: 15% of x is `x * 15 / 100` or `x * 0.15`."],
 tryit=[("M", "Print the last digit of 4527."),
        ("M", "Print whether 38 is even."),
        ("C", "Convert 4000 seconds into hours, minutes and seconds."),
        ("R", "A $86 bill is split between 4 people. Print each share and any leftover cents when working in whole cents.")],
),
dict(
 part="BASICS", title="Comparisons and booleans",
 idea="A comparison asks a yes/no question and answers with True or False. and / or / not combine answers. Conditions are built from these.",
 know='''
==  !=  >  <  >=  <=        # comparisons give True or False
score >= 50                 # at least 50
score > 50                  # more than 50 (50 itself is False)
5 <= x <= 10                # between 5 and 10, both ends included
a and b                     # True only if BOTH are True
a or b                      # True if EITHER is True
not a                       # flips True <-> False
day in ("Sat", "Sun")       # True if day matches one of these
''',
 req="A student passes if the score is at least 50 and attendance is at least 75%. Print True or False.",
 inputs="score, attendance (numbers)", output="True or False",
 steps=["Compare score to 50 using at-least.", "Compare attendance to 75 using at-least.",
        "Join the two checks with `and`.", "Print the result."],
 code='''
score = 62
attendance = 70
passed = score >= 50 and attendance >= 75
print(passed)          # False, attendance is too low
''',
 tips=["Underline the boundary words: \"at least\" is `>=`, \"more than\" is `>`, \"at most\" is `<=`, \"under\" is `<`.",
       "Always test the exact boundary value (50, 75). That is where bugs live.",
       "`x == 5 or 6` is WRONG. Write `x == 5 or x == 6`, or `x in (5, 6)`.",
       "A comparison result can be stored in a variable, like `passed` above."],
 tryit=[("M", "Print whether 18 <= 17 is True or False, then work out why before you run it."),
        ("M", "Is a number divisible by both 3 and 5? Test it with 15, 9, 30."),
        ("C", "Print True if a temperature is between 15 and 25 inclusive."),
        ("R", "A promo applies if the cart total is over $40 OR the customer is a member. Print whether it applies for several cases.")],
),
# ------------------------------------------------------------ DECISIONS
dict(
 part="DECISIONS", title="if / else",
 idea="An if statement runs a block only when a condition is True. else runs when it is not. Indentation (4 spaces) marks what belongs inside.",
 know='''
if temperature > 30:           # condition, then a COLON
    print("Too hot")           # indented = inside the if
else:                          # no condition on else, just a colon
    print("OK")
print("always runs")           # not indented = outside

if is_raining:                 # a bool needs no == True
    print("Take umbrella")
''',
 req="A thermostat alarm: if the temperature is above 30, print Too hot, otherwise print OK.",
 inputs="temperature (number from the user)", output="one line: Too hot, or OK",
 steps=["Read the temperature as a number.", "Is it greater than 30?",
        "If yes, print Too hot.", "Otherwise, print OK."],
 code='''
temperature = float(input("Temperature: "))
if temperature > 30:
    print("Too hot")
else:
    print("OK")
''',
 tips=["Forgot the `:` after `if` / `else`? That is a `SyntaxError`.",
       "Exactly 30 here prints OK, because \"above\" means `>`. Test the boundary every time.",
       "Print EXACTLY the text the requirement asks for, including capital letters.",
       "A common mistake: a function with an if inside is defined but never called. Nothing happens until you call it."],
 tryit=[("M", "Print Pass if a score is 50 or more, otherwise Fail."),
        ("M", "Print Even or Odd for a number the user enters."),
        ("C", "A cinema charges $8 for under 12, $12 otherwise. Ask for age and print the price."),
        ("R", "A bank blocks a withdrawal if the amount is more than the balance. Print Approved or Declined. Test with an amount equal to the balance.")],
),
dict(
 part="DECISIONS", title="elif chains",
 idea="When there are more than two outcomes, chain conditions with elif. Python checks top to bottom and runs ONLY the first True branch.",
 know='''
if usage <= 10:
    level = "Low"
elif usage <= 30:          # only reached if usage > 10
    level = "Medium"
elif usage <= 60:
    level = "High"
else:                      # everything else
    level = "Extreme"
print(level)
''',
 req="A water bill label: up to 10 units is Low, up to 30 is Medium, up to 60 is High, anything above is Extreme.",
 inputs="usage (number)", output="a label: Low, Medium, High or Extreme",
 steps=["Check the smallest range first: usage <= 10.", "Then usage <= 30 (we already know it is above 10).",
        "Then usage <= 60.", "Everything else is Extreme (use else)."],
 code='''
usage = float(input("Units used: "))
if usage <= 10:
    label = "Low"
elif usage <= 30:
    label = "Medium"
elif usage <= 60:
    label = "High"
else:
    label = "Extreme"
print(label)
''',
 tips=["ORDER MATTERS. Go smallest-to-largest with `<=`, or largest-to-smallest with `>=`. Never mix.",
       "Wrong order example: checking `usage <= 60` first would label 5 as High.",
       "Use `else` for \"everything not covered above\" and also to catch bad input.",
       "Separate `if` statements are ALL checked. `elif` stops at the first match."],
 tryit=[("M", "Grade from a score: 90+ A, 80+ B, 70+ C, else F."),
        ("C", "Delivery fee by distance: up to 5 km $3, up to 15 km $6, over 15 km $10."),
        ("C", "Print Negative, Zero or Positive for a number."),
        ("R", "Phone battery: below 10% Critical, below 30% Low, below 80% Good, otherwise Full. Test 9, 10, 29, 30, 79, 80, 100.")],
),
dict(
 part="DECISIONS", title="and / or / not and nested ifs",
 idea="Real rules combine several facts. Join them with and / or / not, or place one if inside another.",
 know='''
if is_member and hour >= 6 and hour < 22:    # all must be true
    print("Welcome")

if day == "Sat" or day == "Sun":             # one is enough
    price = 12

if not is_banned:
    ...

# nested: second question only matters if the first is true
if has_ticket:
    if age >= 12:
        print("Enter")
    else:
        print("Kids area")
else:
    print("Buy a ticket")
''',
 req="A gym admits you if you are a member AND it is open (6:00 up to but not including 22:00). Otherwise print which reason applies.",
 inputs="is_member (bool), hour (int 0-23)", output="Welcome, Not a member, or Closed",
 steps=["If not a member -> Not a member.", "Else if the hour is outside 6..21 -> Closed.",
        "Otherwise -> Welcome."],
 code='''
is_member = True
hour = 22
if not is_member:
    print("Not a member")
elif hour < 6 or hour >= 22:
    print("Closed")
else:
    print("Welcome")
''',
 tips=["Say the rule out loud as a sentence, then translate word for word.",
       "\"Not between 6 and 22\" is `hour < 6 or hour >= 22`. De Morgan: flip the comparisons AND swap and/or.",
       "Deep nesting is hard to read. Prefer early checks for the failing cases.",
       "Python does `5 < x < 10` correctly. It is perfectly valid."],
 tryit=[("M", "Print Discount if age < 12 or age >= 65."),
        ("C", "A ride is allowed if height >= 120 and the person has a ticket. Print the reason when denied."),
        ("C", "Login: correct username AND correct password. Different messages for each failure."),
        ("R", "Shipping is free if the order is over $50 OR the customer is a member; otherwise $7. Express adds $10 whatever else happens.")],
),
dict(
 part="BASICS", title="Strings",
 idea="Text is a sequence of characters. You can index it, slice it, search it and loop over it. It never changes in place.",
 know='''
s = "Hello World"
len(s)                      # 11
s[0]   s[-1]                # 'H'  'd'
s[0:5]   s[:5]   s[6:]      # 'Hello'  'Hello'  'World'
s[::-1]                     # 'dlroW olleH'  (reverse)
s.lower()  s.upper()  s.strip()   # return NEW strings
s.split()                   # ['Hello', 'World']
"-".join(["a", "b"])        # 'a-b'
s.replace("l", "L")   s.count("l")   s.find("W")
"World" in s                # True
s.isdigit()  s.isalpha()  s.isupper()
for ch in s: ...            # one character at a time
''',
 req="A username is valid if it has at least 5 characters and contains only letters and digits.",
 inputs="username (str)", output="True or False",
 steps=["Check len(username) >= 5.", "Check username.isalnum() (letters and digits only).",
        "Both must be true, so combine with and."],
 code='''
username = "sam99"
valid = len(username) >= 5 and username.isalnum()
print(valid)        # True
''',
 tips=["Strings are immutable. `s.upper()` does nothing unless you save it: `s = s.upper()`.",
       "Slices exclude the stop: `s[0:5]` is characters 0..4.",
       "Compare text ignoring case: `a.lower() == b.lower()`.",
       "`\"abc\" * 2` is `\"abcabc\"`, but `\"abc\" + 2` is a TypeError."],
 tryit=[("M", "Print the first and last character of a word."),
        ("M", "Print a word reversed."),
        ("C", "Count the vowels in a sentence."),
        ("R", "Password rule: at least 8 chars, contains a digit, contains an uppercase letter. Print which rules fail.")],
),
dict(
 part="FUNCTIONS", title="Functions and return",
 idea="A function is a named recipe. Parameters are its inputs. return hands back its output. Defining does nothing until you call it.",
 know='''
def calculate_tip(bill, percent):      # parameters = inputs
    tip = bill * percent / 100
    return tip                         # output, function ends here

result = calculate_tip(80, 15)         # CALL it. result is 12.0
print(result)

def greet(name, loud=False):           # default value = optional input
    if loud:
        return name.upper() + "!"
    return "Hi " + name

def min_max(nums):
    return min(nums), max(nums)        # two values back
lo, hi = min_max([4, 9, 1])
''',
 req="Write calculate_total(price, quantity, tax_percent) that returns the final cost including tax, rounded to 2 decimals.",
 inputs="price, quantity, tax_percent", output="a number: the final cost",
 steps=["subtotal = price * quantity.", "tax = subtotal * tax_percent / 100.",
        "Return round(subtotal + tax, 2)."],
 code='''
def calculate_total(price, quantity, tax_percent):
    subtotal = price * quantity
    tax = subtotal * tax_percent / 100
    return round(subtotal + tax, 2)

print(calculate_total(4.5, 3, 8))     # 14.58
''',
 tips=["`return` gives a value back. `print` only shows it. Requirement says return? Use return.",
       "Forgot `return`? The function gives back `None`.",
       "A `def` alone runs nothing. You must CALL it.",
       "Plan the signature first: name, inputs, output. Then write the body."],
 tryit=[("M", "Write `square(n)` that returns n * n."),
        ("M", "Write `is_even(n)` returning True or False."),
        ("C", "Write `average(a, b, c)`. Call it with three different sets."),
        ("R", "Write `final_price(price, is_member)`: members get 10% off. Return the price rounded to 2 decimals.")],
),
# ------------------------------------------------------------ LOOPS
dict(
 part="LOOPS", title="for loops and range",
 idea="A for loop repeats a block once for each item. range() makes a sequence of numbers to loop over.",
 know='''
for x in [4, 8, 15]:           # each item in a list
    print(x)
for ch in "hey":               # each character
    print(ch)

range(5)           # 0 1 2 3 4        (stop is NOT included)
range(1, 6)        # 1 2 3 4 5
range(0, 10, 2)    # 0 2 4 6 8        (step 2)
range(5, 0, -1)    # 5 4 3 2 1        (count down)

for i in range(1, 4):
    print(i)
print("done")                  # outside loop: runs once at the end
''',
 req="Print a countdown from 5 to 1, then print Liftoff.",
 inputs="none (fixed range)", output="5 4 3 2 1 then Liftoff, one per line",
 steps=["Loop i from 5 down to 1.", "Print i each time.", "After the loop, print Liftoff."],
 code='''
for i in range(5, 0, -1):
    print(i)
print("Liftoff")
''',
 tips=["`range(a, b)` stops BEFORE b. For 1..10 write `range(1, 11)`.",
       "Everything indented under the `for` repeats. The first unindented line ends the loop.",
       "Do not change the list while looping over it.",
       "To repeat N times and ignore the number: `for _ in range(N):`."],
 tryit=[("M", "Print the numbers 1 to 10."),
        ("M", "Print only the even numbers from 1 to 20."),
        ("C", "Print the 7 times table up to 7 x 10, formatted like `7 x 3 = 21`."),
        ("R", "Print a table of Celsius 0, 10, 20 ... 100 next to Fahrenheit.")],
),
dict(
 part="LOOPS", title="while loops",
 idea="A while loop repeats as long as its condition is True. YOU must change something inside so it eventually becomes False.",
 know='''
count = 0
while count < 3:               # check first, then run block
    print(count)
    count += 1                 # without this: infinite loop (Ctrl+C stops it)

while True:                    # repeat until I say stop
    answer = input("> ")
    if answer == "quit":
        break                  # leave the loop now
''',
 req="A savings account starts at $500 and grows 10% each year. How many years until it exceeds $1000?",
 inputs="start = 500, growth = 10%, goal = 1000", output="number of years",
 steps=["balance = 500, years = 0.", "While balance is not above 1000: add 10% interest, add one to years.",
        "Print years."],
 code='''
balance = 500
years = 0
while balance <= 1000:
    balance = balance * 1.10
    years += 1
print(years)           # 8
''',
 tips=["Use `for` when you know how many times or what to loop over. Use `while` when you wait for something to happen.",
       "Infinite loop? You forgot to update the variable in the condition.",
       "Check the condition direction: loop WHILE the goal is NOT yet reached.",
       "Validation pattern: ask once, `while` the answer is bad, ask again."],
 tryit=[("M", "Print 1 to 5 using a while loop."),
        ("C", "Keep asking for a number until the user enters one between 1 and 10."),
        ("C", "Halve 1000 repeatedly until it is below 1. Print how many halvings it took."),
        ("R", "ATM PIN check: 3 attempts allowed. Stop on success. Print Locked after 3 failures.")],
),
dict(
 part="LOOPS", title="break and continue",
 idea="break leaves the loop entirely. continue skips the rest of this round and goes to the next one.",
 know='''
for x in nums:
    if x < 0:
        continue          # skip negatives, go to next x
    if x == 99:
        break             # stop everything
    print(x)

for x in nums:
    if x == target:
        print("found")
        break
else:                     # runs only if the loop did NOT break
    print("not found")
''',
 req="Read numbers from the user until they type 0. Ignore negative numbers. Print the sum of the others.",
 inputs="numbers typed one at a time", output="the sum of the non-negative numbers",
 steps=["total = 0.", "Repeat forever: read a number.", "If it is 0, stop (break).",
        "If negative, skip (continue).", "Otherwise add it to total.", "After the loop, print total."],
 code='''
total = 0
while True:
    n = int(input("Number (0 to stop): "))
    if n == 0:
        break
    if n < 0:
        continue
    total += n
print(total)
''',
 tips=["`break` and `continue` only affect the INNERMOST loop.",
       "`continue` in a `while` loop: make sure the update line is not skipped, or you loop forever.",
       "Searching? `break` as soon as you find it, no need to keep looking.",
       "Put the stop check first, so it can never be skipped."],
 tryit=[("M", "Print 1 to 10 but skip 5."),
        ("C", "Print numbers 1 to 100 and stop at the first multiple of 17."),
        ("C", "Loop through a list of prices. Skip anything above 100. Print the rest."),
        ("R", "Process a list of transactions. Stop at the first one marked FRAUD and report its position.")],
),
# ------------------------------------------------------------ PATTERNS
dict(
 part="LOOP PATTERNS", title="Pattern: Sum (accumulator)",
 idea="Start a variable at 0 BEFORE the loop. Add to it on every round. This shape solves 'total', 'sum', 'add up'.",
 know='''
total = 0                  # 1. start BEFORE the loop
for x in nums:             # 2. visit each item
    total += x             # 3. accumulate
print(total)               # 4. use the result AFTER the loop

# same shape, different jobs:
revenue += price * qty       salary_total += salary
distance += leg              points += gained
''',
 req="Given the steps walked each day of a week, print the weekly total.",
 inputs="steps = [4200, 8100, 6500, 3000, 9900, 12000, 7000]", output="total steps",
 steps=["total = 0.", "For each day's steps: add them to total.", "Print total after the loop."],
 code='''
steps = [4200, 8100, 6500, 3000, 9900, 12000, 7000]
total = 0
for day_steps in steps:
    total += day_steps
print(total)        # 50700
''',
 tips=["The most common bug: `total = 0` INSIDE the loop. It resets every round.",
       "`print(total)` inside the loop prints a running total, not the answer.",
       "Totals of floats: round at the END, `round(total, 2)`.",
       "Python has `sum(nums)`, but learn the loop first. You need it for harder problems."],
 tryit=[("M", "Sum the numbers 1 to 100 with a loop."),
        ("C", "Sum only the even numbers in a list."),
        ("C", "Given prices and quantities as two lists, compute the total cost."),
        ("R", "A shopping cart is a list of (item, price) pairs. Print the subtotal, 8% tax, and total.")],
),
dict(
 part="LOOP PATTERNS", title="Pattern: Count",
 idea="Same shape as sum, but you add 1 only when an item meets a rule. This solves 'how many'.",
 know='''
count = 0
for x in nums:
    if x % 2 == 0:         # the rule
        count += 1         # add ONE, not x
print(count)

# the rule can be anything:
if temp > 30:          if name.startswith("A"):      if score < 50:
''',
 req="Given a week of daily temperatures, count how many days were above 30 degrees.",
 inputs="temps = [28, 31, 35, 29, 33, 30, 27]", output="the number of days above 30",
 steps=["count = 0.", "For each temperature:", "If it is above 30, add 1 to count.", "Print count."],
 code='''
temps = [28, 31, 35, 29, 33, 30, 27]
hot_days = 0
for t in temps:
    if t > 30:
        hot_days += 1
print(hot_days)     # 3
''',
 tips=["Count adds 1. Sum adds the value. Do not confuse them.",
       "30 itself is not counted because the rule says above (`>`). Check the boundary.",
       "Counting TWO different kinds? Use two counters.",
       "Percentage = `count / len(items) * 100`. Guard against an empty list."],
 tryit=[("M", "Count how many numbers in a list are negative."),
        ("M", "Count how many words in a list start with a capital letter."),
        ("C", "Count odd numbers AND even numbers in one pass."),
        ("R", "Test scores: count how many passed (>= 50) and print the pass percentage.")],
),
dict(
 part="LOOP PATTERNS", title="Pattern: Max and Min",
 idea="Remember the best value so far. Compare each new item to it. Replace it if the new one is better.",
 know='''
best = nums[0]             # start with the first item (list must not be empty)
for x in nums:
    if x > best:           # use < for minimum
        best = x
print(best)

# need WHERE it was? remember the index too:
best_i = 0
for i in range(len(nums)):
    if nums[i] > nums[best_i]:
        best_i = i
''',
 req="Given test scores, print the highest score and which student (position) got it.",
 inputs="scores = [72, 91, 65, 88]", output="highest score and its position",
 steps=["Assume the first score is the best (position 0).", "Look at each score by position.",
        "If it beats the best, update best and its position.", "Print both."],
 code='''
scores = [72, 91, 65, 88]
best_i = 0
for i in range(len(scores)):
    if scores[i] > scores[best_i]:
        best_i = i
print(scores[best_i], best_i)     # 91 1
''',
 tips=["Do NOT start `best = 0`. If all numbers are negative you get the wrong answer. Start from the first item.",
       "`max(nums)` and `min(nums)` exist, but interviewers want the loop.",
       "Ties: `>` keeps the FIRST maximum. `>=` keeps the LAST. Decide which is wanted.",
       "Second largest: track `best` and `second`, or sort the unique values."],
 tryit=[("M", "Find the smallest number in a list."),
        ("C", "Find the longest word in a list."),
        ("C", "Find the largest and smallest in ONE loop."),
        ("R", "Sensor readings: report the highest reading, the lowest, and the gap between them.")],
),
dict(
 part="LOOP PATTERNS", title="Pattern: Average",
 idea="Average = total / count. You already know how to sum and count. The new skill is guarding against an empty list.",
 know='''
total = 0
for x in nums:
    total += x
if len(nums) > 0:
    average = total / len(nums)
else:
    average = 0                    # or None, or print a message
print(round(average, 2))

# conditional average: only items that qualify
total = 0
count = 0
for x in nums:
    if x >= 0:
        total += x
        count += 1
''',
 req="Print the average of a student's grades, ignoring any grade of -1 (missing).",
 inputs="grades = [80, -1, 90, 70]", output="average of valid grades, 2 decimals",
 steps=["total = 0, count = 0.", "For each grade: if it is not -1, add it and count it.",
        "If count is 0, there is no average. Otherwise total / count.", "Print rounded."],
 code='''
grades = [80, -1, 90, 70]
total = 0
count = 0
for g in grades:
    if g != -1:
        total += g
        count += 1
if count == 0:
    print("No grades")
else:
    print(round(total / count, 2))     # 80.0
''',
 tips=["Dividing by zero crashes (`ZeroDivisionError`). Always ask: can the count be 0?",
       "Use the COUNT of qualifying items, not `len(nums)`, when you skip some.",
       "`/` always gives a decimal. `//` throws away the decimals.",
       "Keep `total` and `count` separate until the very end."],
 tryit=[("M", "Average of 5 numbers typed by the user."),
        ("C", "Average of only the positive numbers in a list."),
        ("C", "Print every value that is above the average."),
        ("R", "Employee salaries: print the average and the number of people paid above average.")],
),
dict(
 part="LOOP PATTERNS", title="Pattern: Filter and Transform",
 idea="Build a NEW list. Filter keeps items that pass a rule. Transform changes every item. Start with an empty list, append inside the loop.",
 know='''
cheap = []                     # 1. empty result list
for p in prices:
    if p < 10:                 # filter: only some items
        cheap.append(p)

with_tax = []
for p in prices:
    with_tax.append(p * 1.08)  # transform: every item changed

# both together: keep cheap items AND discount them
sale = []
for p in prices:
    if p < 10:
        sale.append(p * 0.9)

# shortcut (learn the loop first):
cheap = [p for p in prices if p < 10]
''',
 req="From a list of prices, make a new list of the prices under $10, each with 8% tax added.",
 inputs="prices = [4.5, 12, 9.99, 25, 3]", output="a new list of taxed cheap prices",
 steps=["result = [] (empty).", "For each price: if it is under 10, add price * 1.08 to result.",
        "Print result."],
 code='''
prices = [4.5, 12, 9.99, 25, 3]
result = []
for p in prices:
    if p < 10:
        result.append(round(p * 1.08, 2))
print(result)          # [4.86, 10.79, 3.24]
''',
 tips=["The empty list goes BEFORE the loop. Inside it would reset every round.",
       "`append` changes the list and returns `None`. Never write `lst = lst.append(x)`.",
       "Want to remove items from the original? Build a new list of the ones to KEEP.",
       "Never remove from a list while looping over it. You will skip items."],
 tryit=[("M", "From a list of numbers, build a list of just the even ones."),
        ("M", "Build a list of the squares of 1 to 10."),
        ("C", "From a list of words, build a list of those longer than 4 letters, in uppercase."),
        ("R", "Transactions list: build a list of refunds (negative amounts) shown as positive numbers.")],
),
dict(
 part="LOOP PATTERNS", title="Pattern: Search",
 idea="Does something exist? Where is it? Use a flag (found = False), loop, set it True and break when you find it.",
 know='''
found = False
for x in ids:
    if x == target:
        found = True
        break              # no need to keep looking
print(found)

# where is it?
position = -1              # -1 means not found
for i in range(len(ids)):
    if ids[i] == target:
        position = i
        break

# shortcuts:  target in ids      ids.index(target)  (crashes if missing)
''',
 req="Given a list of employee IDs, print the position of ID 4821, or Not found.",
 inputs="ids = [1003, 4821, 7712], target = 4821", output="position or Not found",
 steps=["position = -1.", "For each index: if ids[i] equals the target, save i and stop.",
        "If position is still -1 print Not found, else print it."],
 code='''
ids = [1003, 4821, 7712]
target = 4821
position = -1
for i in range(len(ids)):
    if ids[i] == target:
        position = i
        break
if position == -1:
    print("Not found")
else:
    print(position)       # 1
''',
 tips=["Never `print(\"Not found\")` inside the loop's else branch. It prints for every non-match.",
       "Initialize the flag BEFORE the loop; change it only on success.",
       "`x in list` is the one-line version. It loops internally, so it is O(n).",
       "Many matches wanted? Do not `break`. Collect them into a list instead."],
 tryit=[("M", "Check whether the number 7 is in a list."),
        ("C", "Print the index of the first negative number, or -1."),
        ("C", "Find the first word longer than 6 letters."),
        ("R", "Given orders as (id, status) pairs, find order 1042 and print its status.")],
),
# ------------------------------------------------------------ LISTS
dict(
 part="LISTS", title="List basics",
 idea="A list holds many values in order. Each has a position (index) that starts at 0. Negative indexes count from the end.",
 know='''
nums = [5, 3, 9, 1]       empty = []
len(nums)                  # 4
nums[0]    nums[2]         # 5   9     first, third
nums[-1]   nums[-2]        # 1   9     last, second to last
nums[1] = 7                # change an item
nums.append(4)             # add to the end
nums.pop()                 # remove and return the last item
nums.remove(9)             # remove first VALUE 9
9 in nums                  # True / False
if not nums: ...           # True when the list is empty
''',
 req="Given a list of three quiz scores, add a fourth, change the first to 100, and print the last score and the number of scores.",
 inputs="scores = [70, 85, 90]", output="the last score, and how many scores",
 steps=["Append the new score.", "Set scores[0] to 100.", "Print scores[-1] and len(scores)."],
 code='''
scores = [70, 85, 90]
scores.append(77)
scores[0] = 100
print(scores[-1], len(scores))     # 77 4
''',
 tips=["Valid indexes are `0` to `len(nums) - 1`. `nums[len(nums)]` is an `IndexError`.",
       "`nums[-1]` is the safe way to get the last item. It fails on an empty list.",
       "`nums.remove(x)` raises an error if x is missing. Check `x in nums` first.",
       "`b = a` does NOT copy a list. Use `b = a.copy()`."],
 tryit=[("M", "Make a list of 5 numbers. Print the first, last, and length."),
        ("M", "Append 10 to a list, then remove the last item."),
        ("C", "Replace every 0 in a list with -1."),
        ("R", "A waiting line: add 3 customers, serve (remove) the first, print who is next.")],
),
dict(
 part="LISTS", title="List methods and sorting",
 idea="Methods change a list or ask it a question. Know which ones change the list and which return something.",
 know='''
nums.append(x)             # add at end           (returns None)
nums.insert(0, x)          # add at position
nums.extend([1, 2])        # add many
nums.pop()   nums.pop(i)   # remove + return
nums.remove(x)             # remove by value
nums.index(x)              # position of x (error if missing)
nums.count(x)              # how many x
nums.sort()                # sort IN PLACE, ascending   (returns None)
nums.sort(reverse=True)    # descending
sorted(nums)               # NEW sorted list, original untouched
nums.reverse()             # in place              nums[::-1]  # reversed copy
nums.copy()   nums.clear()
people.sort(key=lambda p: p[1])    # sort pairs by 2nd field
''',
 req="Print the three highest scores from a list, highest first, without changing the original list.",
 inputs="scores = [72, 91, 65, 88, 79]", output="[91, 88, 79]",
 steps=["Make a sorted copy in descending order (sorted).", "Take the first three with a slice.", "Print."],
 code='''
scores = [72, 91, 65, 88, 79]
top3 = sorted(scores, reverse=True)[:3]
print(top3)           # [91, 88, 79]
print(scores)         # unchanged
''',
 tips=["`nums = nums.sort()` makes `nums` equal to `None`. `sort()` returns nothing.",
       "Need the original later? Use `sorted(nums)`, not `nums.sort()`.",
       "`pop()` is O(1) at the end but `pop(0)` and `insert(0, x)` are O(n).",
       "To sort by a field: `key=`. To sort descending: `reverse=True`."],
 tryit=[("M", "Sort a list ascending, then descending."),
        ("C", "Remove duplicates from a list but keep the first-seen order."),
        ("C", "Find the second largest number in a list."),
        ("R", "Students as (name, score) pairs: print them ranked by score, highest first.")],
),
dict(
 part="LISTS", title="Looping with indexes",
 idea="Three ways to loop a list. Pick by what you need: the value, the position, or both.",
 know='''
for x in nums:                     # just the values
    print(x)
for i in range(len(nums)):         # positions: needed to CHANGE items
    nums[i] = nums[i] * 2
for i, x in enumerate(nums):       # position AND value
    print(i, x)

# compare neighbours: stop one early
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        print("not sorted at", i)

# two lists together
for name, score in zip(names, scores):
    print(name, score)
''',
 req="Given a list of prices, apply a 10% discount in place to every price above 50.",
 inputs="prices = [20, 80, 55, 10]", output="the same list with big prices reduced",
 steps=["Loop over the POSITIONS (we need to modify items).", "If prices[i] > 50, set prices[i] to prices[i] * 0.9.", "Print the list."],
 code='''
prices = [20, 80, 55, 10]
for i in range(len(prices)):
    if prices[i] > 50:
        prices[i] = prices[i] * 0.9
print(prices)         # [20, 72.0, 49.5, 10]
''',
 tips=["Changing `x` in `for x in nums` does NOT change the list. Use the index.",
       "Off-by-one: `range(len(nums) + 1)` crashes with `IndexError`.",
       "Comparing `nums[i + 1]` requires stopping at `len(nums) - 1`.",
       "`enumerate(nums, start=1)` gives numbering that starts at 1."],
 tryit=[("M", "Print each item with its position: `0: apple`."),
        ("C", "Double every item of a list in place."),
        ("C", "Check whether a list is sorted ascending using neighbours."),
        ("R", "Given two lists names and scores, print the name of the person with the top score.")],
),
dict(
 part="LISTS", title="Slicing",
 idea="A slice takes a piece of a list or string: [start:stop:step]. The stop is NOT included. Any part can be left out.",
 know='''
a = [10, 20, 30, 40, 50]
a[1:3]      # [20, 30]        index 1 and 2
a[:2]       # [10, 20]        first two
a[2:]       # [30, 40, 50]    from index 2 on
a[-2:]      # [40, 50]        last two
a[::2]      # [10, 30, 50]    every other
a[::-1]     # [50, 40, 30, 20, 10]  reversed
a[:]        # a full copy
"hello"[1:4]   # 'ell'       works on strings too
''',
 req="Given a list of daily sales, print the first three days, the last two days, and the list reversed.",
 inputs="sales = [120, 90, 150, 80, 200]", output="three printed lists",
 steps=["First three: slice from the start up to 3.", "Last two: slice with -2 and no stop.", "Reversed: step of -1."],
 code='''
sales = [120, 90, 150, 80, 200]
print(sales[:3])      # [120, 90, 150]
print(sales[-2:])     # [80, 200]
print(sales[::-1])    # [200, 80, 150, 90, 120]
''',
 tips=["Slices never crash on out-of-range numbers. They just return less. Indexes DO crash.",
       "`a[1:3]` has `3 - 1 = 2` items. Length = stop - start.",
       "A slice makes a NEW list. Changing it does not change the original.",
       "Palindrome check: `s == s[::-1]`."],
 tryit=[("M", "Print the middle three items of a 5-item list."),
        ("M", "Print every third item of a list."),
        ("C", "Print the first and last 2 characters of a string."),
        ("R", "Rotate a list left by 1: [1,2,3,4] -> [2,3,4,1].")],
),
# ------------------------------------------------------------ DICTS / SETS
dict(
 part="DICTIONARIES", title="Dictionary basics",
 idea="A dictionary stores key -> value pairs. Use it for lookups: 'price OF this item', 'score FOR this name'.",
 know='''
prices = {"small": 10, "medium": 15, "large": 20}
empty = {}                          # empty dict  (NOT set())
prices["large"]                     # 20     KeyError if missing
prices.get("huge")                  # None   safe
prices.get("huge", 0)               # 0      safe with default
prices["xl"] = 25                   # add or overwrite
del prices["xl"]                    # remove
"small" in prices                   # True   checks KEYS
len(prices)
for k in prices: ...                # keys
for k, v in prices.items(): ...     # key and value
list(prices.values())
''',
 req="A cafe menu has prices. Given a drink name, print its price, or Not on menu.",
 inputs="menu dict, drink (str)", output="the price or Not on menu",
 steps=["Build the menu dictionary.", "If the drink is a key in the menu: print menu[drink].", "Otherwise print Not on menu."],
 code='''
menu = {"latte": 4.5, "mocha": 5.0, "tea": 3.0}
drink = input("Drink: ")
if drink in menu:
    print(menu[drink])
else:
    print("Not on menu")
''',
 tips=["Missing key with `[]` crashes (`KeyError`). With `.get(key, default)` it does not.",
       "`{}` is an empty DICT. An empty set is `set()`.",
       "Keys must be unchangeable (str, int, tuple). Lists cannot be keys.",
       "Keys are unique: assigning to an existing key overwrites it."],
 tryit=[("M", "Create a dict of 3 countries and capitals. Print one capital."),
        ("M", "Add a new country, then print how many entries there are."),
        ("C", "Print every key and value on its own line."),
        ("R", "Inventory: given {item: quantity}, sell 2 of an item (only if enough stock), then print the stock.")],
),
dict(
 part="DICTIONARIES", title="Pattern: Frequency count",
 idea="Count how many times each thing appears. The dictionary key is the thing, the value is its count. This is the single most reused interview pattern.",
 know='''
freq = {}
for x in items:
    freq[x] = freq.get(x, 0) + 1        # 0 if first time, then +1

# same thing, written out:
for x in items:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

best = max(freq, key=freq.get)           # most common key
for k, v in freq.items():
    print(k, v)
''',
 req="Count how many times each word appears in a sentence, and print the most common word.",
 inputs="a sentence (str)", output="counts per word, and the most common word",
 steps=["Split the sentence into words.", "freq = {}.", "For each word: freq[word] = freq.get(word, 0) + 1.",
        "Find the key with the largest count and print it."],
 code='''
sentence = "the cat and the hat and the bat"
freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)                       # {'the': 3, 'cat': 1, 'and': 2, ...}
print(max(freq, key=freq.get))    # the
''',
 tips=["Memorize `freq[x] = freq.get(x, 0) + 1`. You will write it hundreds of times.",
       "Counting characters? Loop over the string instead of `split()`.",
       "Counting products, votes, orders, letters. Always the same shape.",
       "All counts equal 1 means no duplicates."],
 tryit=[("M", "Count how many times each letter appears in a word."),
        ("C", "Votes list: print the winner (most votes)."),
        ("C", "Check whether two words are anagrams using counts."),
        ("R", "Orders list of product names: print each product with its count, most popular first.")],
),
dict(
 part="DICTIONARIES", title="Lookup tables and grouping",
 idea="Use a dictionary to replace a long if/elif chain, and to gather items into groups.",
 know='''
# lookup table: rules live in DATA, not in code
BASE = {"small": 10, "medium": 15, "large": 20}
price = BASE[size]                  # BASE.get(size, 0) if size may be invalid

# group items by a key
groups = {}
for name, dept in staff:
    if dept not in groups:
        groups[dept] = []           # first time: make the list
    groups[dept].append(name)

# total by group
totals = {}
for cat, amount in expenses:
    totals[cat] = totals.get(cat, 0) + amount
''',
 req="Expenses are (category, amount) pairs. Print the total spent per category.",
 inputs="expenses = [(\"food\", 12), (\"rent\", 500), (\"food\", 8)]", output="a total for each category",
 steps=["totals = {}.", "For each (category, amount): add the amount to totals[category] (start at 0).",
        "Loop the dict and print each category and total."],
 code='''
expenses = [("food", 12), ("rent", 500), ("food", 8)]
totals = {}
for category, amount in expenses:
    totals[category] = totals.get(category, 0) + amount
for category, total in totals.items():
    print(category, total)       # food 20 / rent 500
''',
 tips=["Unpack pairs in the loop header: `for category, amount in expenses:`.",
       "A dict of lists needs the list created before the first `append`.",
       "Lookup dicts make rules easy to change: edit the data, not the logic.",
       "Dict of dicts: `accounts[\"A1\"][\"balance\"] += 50`."],
 tryit=[("M", "Make a lookup dict for shipping rates by zone and print the rate for a zone."),
        ("C", "Group names by their first letter."),
        ("C", "Total the salary per department."),
        ("R", "Bank: accounts as {id: balance}. Apply a list of (id, amount) transactions. Skip unknown ids and overdrafts.")],
),
dict(
 part="DICTIONARIES", title="Sets and duplicates",
 idea="A set stores unique values and answers 'have I seen this before?' almost instantly. Use it for duplicates, uniqueness and membership.",
 know='''
seen = set()                  # empty set (NOT {})
s = {1, 2, 3}
s.add(4)                      # adding again does nothing
s.remove(4)                   # error if missing
s.discard(4)                  # no error if missing
4 in s                        # fast membership test
set([1, 1, 2])                # {1, 2}   removes duplicates
len(set(nums)) < len(nums)    # True if the list has duplicates
a | b      a & b      a - b   # union  both  only-in-a
# sets have no order and no indexes: s[0] is an error
''',
 req="Given a list of transaction IDs, print each ID that appears more than once (each only once).",
 inputs="ids = [101, 205, 101, 330, 205, 101]", output="[101, 205]",
 steps=["seen = set(), repeated = set().", "For each id: if it is in seen, add it to repeated.", "Otherwise add to seen.", "Print repeated."],
 code='''
ids = [101, 205, 101, 330, 205, 101]
seen = set()
repeated = set()
for x in ids:
    if x in seen:
        repeated.add(x)
    else:
        seen.add(x)
print(repeated)       # {101, 205}
''',
 tips=["Need only 'is it present?' -> set. Need a count -> dict. Need order or indexes -> list.",
       "`in` on a list is O(n). On a set it is O(1). That is a big deal on large inputs.",
       "`list(set(nums))` removes duplicates but loses the order.",
       "Two Sum idea: remember seen values in a set or dict while you loop."],
 tryit=[("M", "Print how many unique numbers a list contains."),
        ("C", "Print True if a list contains any duplicate."),
        ("C", "Given two lists of user IDs, print the IDs that are in both."),
        ("R", "Sign-up check: given existing emails and new emails, print the new ones that are already taken.")],
),
dict(
 part="DICTIONARIES", title="Tuples and unpacking",
 idea="A tuple is a fixed group of values. It is how you return several things from a function and how you loop over pairs.",
 know='''
point = (3, 4)
x, y = point                      # unpack into two variables
point[0]                          # 3   (read only: point[0] = 9 fails)

def min_max(nums):
    return min(nums), max(nums)   # returns a tuple
lo, hi = min_max([4, 9, 1])

pairs = [("Ana", 91), ("Bo", 78)]
for name, score in pairs:         # unpack in the loop header
    print(name, score)
best = max(pairs, key=lambda p: p[1])    # pair with highest score
''',
 req="Write a function that returns both the cheapest and the most expensive price from a list.",
 inputs="prices (list of numbers)", output="two values: lowest, highest",
 steps=["Compute min and max (or loop for both).", "Return them together.", "The caller unpacks into two variables."],
 code='''
def price_range(prices):
    return min(prices), max(prices)

low, high = price_range([4.5, 12, 9.99, 3])
print(low, high)          # 3 12
''',
 tips=["Unpacking needs matching counts: 2 values -> 2 variables.",
       "Tuples can be dict keys (lists cannot): `grid[(row, col)]`.",
       "`a, b = b, a` swaps two variables using tuples.",
       "Need to change it later? Use a list. Fixed record? Tuple."],
 tryit=[("M", "Swap two variables in one line."),
        ("C", "Write `stats(nums)` returning min, max and average."),
        ("C", "Loop over (name, age) pairs and print the oldest."),
        ("R", "Given (item, price, qty) rows, print each line total and the grand total.")],
),
# ------------------------------------------------------------ REQUIREMENTS
dict(
 part="REQUIREMENTS TO CODE", title="Rules to code: add-ons",
 idea="Many requirements are a base price plus optional extras. Base = a choice (if/elif or a dictionary). Extras = separate ifs.",
 know='''
# base: ONE of several  -> if / elif / else  (or a lookup dict)
# extras: ANY combination -> separate ifs, never elif

total = BASE[size]
if extra_cheese:
    total += 1
if bacon:
    total += 2 if size == "small" else 3     # extra depends on size

# quantity
total = total * quantity
''',
 req="A burger is $8 (single), $11 (double) or $14 (triple). Add bacon: +$2 on single, +$3 otherwise. Add cheese: +$1. Compute the total for a given order.",
 inputs="size (str), bacon (bool), cheese (bool)", output="total price (number)",
 steps=["Base price from size.", "If bacon: add $2 for single, $3 for others.", "If cheese: add $1.", "Return the total."],
 code='''
def burger_price(size, bacon, cheese):
    base = {"single": 8, "double": 11, "triple": 14}
    total = base[size]
    if bacon:
        if size == "single":
            total += 2
        else:
            total += 3
    if cheese:
        total += 1
    return total

print(burger_price("double", True, True))   # 15
''',
 tips=["Choice among options = `if/elif`. Optional extras = separate `if`s.",
       "Write each rule as a comment first, then turn each comment into code.",
       "Test a case for each rule alone, then all rules together.",
       "Invalid input (`size = \"mega\"`)? Decide what to do: error message, 0, or `.get()`."],
 tryit=[("C", "Coffee: small 3, medium 4, large 5. Extra shot +1, oat milk +0.5. Compute the price."),
        ("C", "Hotel: nights x rate, +$15 breakfast per night, weekend nights cost 20% more."),
        ("R", "Phone plan: base by plan, +$10 per extra line, +$5 if international."),
        ("R", "Game scoring: 10 per coin, 50 per enemy, x2 multiplier if no damage taken.")],
),
dict(
 part="REQUIREMENTS TO CODE", title="Rules to code: tiers, caps, minimums",
 idea="Most billing rules are tiers (different rates for different ranges), caps (never above) and minimums (never below). min() and max() make them one-liners.",
 know='''
total = min(total, 20)                     # CAP: never above 20
total = max(total, 5)                      # MINIMUM charge of 5

first = min(units, 100) * 0.10             # tier 1: first 100 units
rest = max(units - 100, 0) * 0.15          # tier 2: everything after
bill = first + rest

fee = 5 + 3 * (hours - 1)                  # first hour 5, then 3 each extra
import math
hours = math.ceil(minutes / 60)            # started hours: 61 min -> 2

price = price * (1 - 20 / 100)             # 20% off
price = price * 1.08                       # 8% tax
''',
 req="A parking garage charges $5 for the first hour and $3 for each additional hour. The daily maximum is $20. Compute the charge for a given number of hours.",
 inputs="hours (whole number >= 0)", output="charge in dollars",
 steps=["0 hours -> 0.", "Otherwise: 5 + 3 * (hours - 1).", "Cap with min(fee, 20).", "Return."],
 code='''
def parking_fee(hours):
    if hours <= 0:
        return 0
    fee = 5 + 3 * (hours - 1)
    return min(fee, 20)

print(parking_fee(1), parking_fee(4), parking_fee(9))   # 5 14 20
''',
 tips=["Check the exact boundaries: 0, 1, 2, the hour where the cap starts, far past the cap.",
       "'Each additional hour' means subtract the first one before multiplying.",
       "Order matters: discount THEN tax, or tax THEN discount? Read the requirement.",
       "'Partial hours count as full' -> `math.ceil`."],
 tryit=[("C", "Electricity: first 100 units $0.10, next 100 $0.15, above that $0.20. Compute the bill."),
        ("C", "Taxi: $3 base + $1.20 per km, minimum fare $8."),
        ("R", "Shipping: free over $50, otherwise by weight: up to 1 kg $4, up to 5 kg $8, above $12."),
        ("R", "Premium 20% off, regular 10% off, orders under $20 no discount, then add 8% tax.")],
),
# ------------------------------------------------------------ SKILLS
dict(
 part="TEST AND DEBUG", title="Testing your code",
 idea="Never trust code you have not run on cases where you know the answer. Test the boundaries, not just the typical case.",
 know='''
print(parking_fee(1))        # expect 5
print(parking_fee(10))       # expect 20

assert parking_fee(1) == 5            # silent if correct, crashes if wrong
assert parking_fee(10) == 20, "cap failed"

cases = [(0, 0), (1, 5), (2, 8), (6, 20), (50, 20)]   # (input, expected)
for hours, expected in cases:
    got = parking_fee(hours)
    print("OK " if got == expected else "BAD", hours, expected, got)
''',
 req="Test a function is_valid_age(age) that should accept 0 to 120 inclusive.",
 inputs="age (int)", output="True / False",
 steps=["List normal values.", "List BOUNDARIES: -1, 0, 1, 119, 120, 121.", "Add weird: huge number.", "Write expected answers BEFORE running."],
 code='''
def is_valid_age(age):
    return 0 <= age <= 120

cases = [(-1, False), (0, True), (1, True), (120, True), (121, False)]
for age, expected in cases:
    print(age, is_valid_age(age) == expected)
''',
 tips=["Decide expected answers BEFORE you run. Otherwise you will believe the output.",
       "Five kinds: normal, boundary, empty/zero, single item, invalid.",
       "Float math: compare `round(x, 2) == 5.0`, not `x == 5.0`.",
       "A passing test only proves those cases. Look for what you did not test."],
 tryit=[("M", "Write 5 test cases for a function that returns the maximum of a list."),
        ("C", "Test a grade function around every grade boundary."),
        ("C", "Write asserts for `average(nums)` including an empty list."),
        ("R", "Take one of your earlier solutions and try to break it with weird input.")],
),
dict(
 part="TEST AND DEBUG", title="Reading errors",
 idea="Read the error from the BOTTOM line up. The last line tells you WHAT, the line number tells you WHERE.",
 know='''
Traceback (most recent call last):
  File "ex.py", line 9, in <module>      <- WHERE (line 9)
    print(nums[5])
IndexError: list index out of range       <- WHAT (read this first)

SyntaxError        missing : or ) or quote, = instead of ==
IndentationError   uneven spaces
NameError          typo, or variable used before it exists
TypeError          wrong type: "a" + 5, forgot int(input())
ValueError         int("abc"), list.remove(missing)
IndexError         index past the end (off by one) or empty list
KeyError           dict key missing -> use .get()
ZeroDivisionError  dividing by 0 (empty average?)
AttributeError     method does not exist, or the variable is None
''',
 req="This crashes. Find the bug without running it:  nums = [1, 2, 3, 4]   then   for i in range(len(nums) + 1): print(nums[i])",
 inputs="a list of 4 numbers", output="should print all four numbers",
 steps=["What are the valid indexes? 0, 1, 2, 3.", "What does range(len(nums) + 1) produce? 0 to 4.",
        "Index 4 does not exist -> IndexError.", "Fix: remove the + 1."],
 code='''
nums = [1, 2, 3, 4]
for i in range(len(nums)):      # was: len(nums) + 1
    print(nums[i])
''',
 tips=["A `SyntaxError` may really be on the line ABOVE the one reported.",
       "No error but wrong answer? That is a LOGIC bug. Print values to find it.",
       "No output at all? You probably never called your function.",
       "`print(type(x))` solves most `TypeError`s in seconds."],
 tryit=[("M", "What error does `int(\"hello\")` raise? Predict first, then run it."),
        ("M", "Fix: `if x = 5:`"),
        ("C", "Why does `total = 0` INSIDE a loop give wrong sums?"),
        ("R", "Take a function you wrote and deliberately cause each error type once, to recognize them.")],
),
dict(
 part="TEST AND DEBUG", title="Common logic bugs",
 idea="Most wrong answers come from the same dozen mistakes. Learn their shapes so you can spot them on sight.",
 know='''
Off-by-one         range(len(nums)+1)       range(1, n) when you meant n+1
Wrong boundary     > where >= was needed    ("at least" vs "more than")
Wrong variable     added price instead of total
Forgot return      function result is None
Early return       return inside the loop on the first round
Reset in loop      total = 0 inside the for
print vs return    prints but gives back None
Alias not copy     b = a changes a too -> b = a.copy()
Strings immutable  s.upper() alone changes nothing
Type confusion     input() is text: "10" < "9" is True
Integer division   // where / was needed
Mutating a list    removing while looping over it
''',
 req="This returns the wrong answer for [3, 5, 8]. Find the bug:  def total(nums): for x in nums: t = 0; t += x; return t",
 inputs="nums = [3, 5, 8]", output="expected 16, actual 8",
 steps=["Trace by hand: round 1 t=0 then t=3. Round 2 t is RESET to 0 then 5.", "Spot the problem: initialization inside the loop.",
        "Also return should be after the loop."],
 code='''
def total(nums):
    t = 0               # before the loop
    for x in nums:
        t += x
    return t            # after the loop (outside the for)
''',
 tips=["Debug method: smallest failing input -> predict each line -> print values -> first line where reality differs is the bug.",
       "Fix ONE thing at a time, then rerun.",
       "Read your code aloud as the computer would, not as you intended.",
       "Log every bug you make in `ERROR_LOG.md`. Patterns will show up fast."],
 tryit=[("M", "Why does `nums = nums.append(5)` break the list?"),
        ("C", "Why does `for x in nums: nums.remove(x)` skip items?"),
        ("C", "Why is `0.1 + 0.2 == 0.3` False? How do you compare floats safely?"),
        ("R", "Write a buggy function on purpose, then trace it by hand to find the bug.")],
),
dict(
 part="INTERVIEW", title="Big-O basics",
 idea="Big-O describes how the work grows as the input size n grows. Interviewers always ask for time and space complexity.",
 know='''
O(1)        constant   index, dict get/set, set add/in, append, pop()
O(log n)    log        halving each step (binary search)
O(n)        linear     one loop over the data, sum, max, "x in list"
O(n log n)             sorting
O(n^2)      quadratic  a loop inside a loop over the same data

list: x in lst is O(n)      set / dict: x in s is O(1) on average
Space: extra memory you create. A new list/dict sized by the input = O(n).
       A handful of variables = O(1).
''',
 req="Find whether a list has duplicates. Compare two solutions and state their complexity.",
 inputs="nums (list of n numbers)", output="True or False",
 steps=["Slow: compare every pair -> loop inside a loop -> O(n^2) time, O(1) space.",
        "Fast: remember seen values in a set -> one loop -> O(n) time, O(n) space.",
        "State the trade-off: extra memory buys speed."],
 code='''
def has_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:       # O(1)
            return True
        seen.add(x)         # O(1)
    return False
# time O(n), space O(n)
''',
 tips=["Count loops: one loop is usually O(n). A loop in a loop is O(n^2).",
       "Replacing `x in list` inside a loop with a set check turns O(n^2) into O(n).",
       "Drop constants: 3n and n are both O(n).",
       "Always say BOTH time and space."],
 tryit=[("M", "What is the time complexity of finding the max of a list?"),
        ("C", "What is the complexity of looking up a key in a dict? A value in a list?"),
        ("C", "State the time and space of your frequency-count solution."),
        ("R", "Take any earlier solution with a nested loop. Can you remove one loop with a set or dict?")],
),
dict(
 part="INTERVIEW", title="Interview protocol",
 idea="When the interviewer says 'write the code', never go silent. Follow the same script every time. Talk through it. A simple correct solution beats an unfinished clever one.",
 know='''
 1  Repeat the problem in your own words.                         (20 s)
 2  Ask: types? negative? empty? duplicates? invalid input?      (30 s)
 3  State INPUTS and OUTPUT. Give one example with numbers.     (20 s)
 4  Explain your plan in plain English.                          (30 s)
 5  Write pseudocode as comments.                                (1 min)
 6  Turn each comment into code. Talk while typing.
 7  Trace by hand with the example. Test an edge case.          (1-2 min)
 8  State time and space complexity.
 9  Mention an improvement or an alternative.
''',
 req="Interviewer: \"Given a list of order totals, return the total of orders over $20, with a 10% discount applied to those orders.\"",
 inputs="order_totals (list of numbers)", output="one number",
 steps=["Say: I will loop through orders, pick the ones over 20, discount them, and add them up.",
        "Ask: can the list be empty? (then return 0)", "Comments first, then code.", "Test: [], [10], [25, 30], [20]."],
 code='''
def discounted_total(order_totals):
    total = 0                           # empty list -> 0
    for amount in order_totals:
        if amount > 20:                 # strictly over 20
            total += amount * 0.9
    return round(total, 2)

print(discounted_total([25, 30, 10, 20]))   # 49.5
''',
 tips=["Freeze? Say \"let me do an example by hand\". Then write your steps as numbered lines.",
       "Start with the brute-force solution. Improve it afterwards.",
       "Name things well. It shows clarity.",
       "Say what you are testing and why before you run."],
 tryit=[("R", "Pick any exercise and answer steps 1 to 4 out loud before writing code."),
        ("R", "Do a mock: write the blank-file template below from memory."),
        ("R", "Time yourself: requirement to working code in 10 minutes."),
        ("R", "Explain your solution to a rubber duck, including complexity.")],
),
]

# blank file template page content
TEMPLATE = '''
def solve(data):
    # 1. handle empty / edge case
    if not data:
        return 0
    # 2. set up variables (total, count, best, result list / dict / set)
    result = 0
    # 3. loop
    for item in data:
        # 4. decide
        if item > 0:
            result += item
    # 5. return
    return result

# 6. test: normal, boundary, empty
print(solve([1, -2, 3]))     # expect 4
print(solve([]))             # expect 0
'''

QUIZ = [
 ("Last element of a list nums?", "nums[-1]"),
 ("Index of the value 9?", "nums.index(9)"),
 ("Loop through the values?", "for x in nums:"),
 ("Loop through the indexes?", "for i in range(len(nums)):"),
 ("Index and value together?", "for i, x in enumerate(nums):"),
 ("Add an item to the end?", "nums.append(x)"),
 ("Remove the last item?", "nums.pop()"),
 ("Remove the first 5?", "nums.remove(5)"),
 ("Is 5 in the list?", "5 in nums"),
 ("Create an empty dict?", "d = {}"),
 ("Safe dict get, default 0?", "d.get(key, 0)"),
 ("Count frequencies?", "freq[x] = freq.get(x, 0) + 1"),
 ("Create an empty set?", "s = set()"),
 ("Add to a set?", "s.add(x)"),
 ("Sort ascending in place?", "nums.sort()"),
 ("Sorted descending copy?", "sorted(nums, reverse=True)"),
 ("Reverse a string?", "s[::-1]"),
 ("Define a function?", "def name(params):"),
 ("Give a value back?", "return value"),
 ("Swap two variables?", "a, b = b, a"),
 ("Is n even?", "n % 2 == 0"),
 ("Text input to whole number?", "int(input(...))"),
 ("Print 2 decimals?", "print(f'{x:.2f}')"),
 ("Loop 1 to 10 inclusive?", "for i in range(1, 11):"),
 ("Loop 10 down to 1?", "for i in range(10, 0, -1):"),
 ("Largest / total / count?", "max(n)  sum(n)  len(n)"),
 ("Key in dict?", "key in d"),
 ("Loop dict key + value?", "for k, v in d.items():"),
 ("First 3 items?", "nums[:3]"),
 ("Every second item?", "nums[::2]"),
 ("Split a sentence into words?", "s.split()"),
 ("Join words with spaces?", "' '.join(words)"),
 ("Cap a total at 20?", "total = min(total, 20)"),
 ("17 divided by 5: whole and remainder?", "17 // 5 = 3,  17 % 5 = 2"),
 ("Remove duplicates?", "list(set(nums))"),
 ("Copy a list?", "nums.copy()  or  nums[:]"),
 ("Loop forever with an exit?", "while True: ... break"),
 ("Check a key exists, then use it?", "if k in d: d[k]"),
 ("Does the list have duplicates?", "len(set(n)) != len(n)"),
 ("Most common key in freq?", "max(freq, key=freq.get)"),
]
