# Youtube: sbeve_specialist
# Originally tested and built on: onlinegdb.com/online_python_compiler, PyDroid 3
# Licensed under the GitHub MIT License.
# All borrowed features: Delta calculations, Sigma calculations, the charcount function, and the Caesar Cipher.
import math
import time
global xpos
global ypos
xpos = 0
ypos = 0
fib_sequence = []

def average(avg_array):
    asum = sum(avg_array)
    result = asum / len(avg_array)
    print(round(result, 5))

def add(num1, num2):
    result = num1 + num2
    print(round(result, 5))

def subtract(num1, num2):
    result = num1 - num2
    print(round(result, 5))

def divide(num1, num2):
    result = num1 / num2
    print(round(result, 5))

def multiply(num1, num2):
    print(round(num1 * num2, 5))

def absval(number):
    print(abs(round(number)))

def tangent(tangent_array):
    print(round(math.tan(tangent_array), 5))

def cosine(cosine_array):
    print(round(math.cos(cosine_array), 5))

def floor(floor_array):
    print(int(floor_array))

def ceiling(ceiling_array):
    print(round(math.ceil(ceiling_array), 5))

def changexpos(newxpos):
    global xpos
    xpos = newxpos
    print(f"X: {xpos}")
    print(f"Y: {ypos}")

def changeypos(newypos):
    global ypos
    ypos = newypos
    print(f"X: {xpos}")
    print(f"Y: {ypos}")

def easter_egg():
    print("easter egg! thanks for looking through the source code of pmm.py!")

def quack():
    print("quack.")

def charcount(spaces, sentence):
    if spaces == False:
        print(len(sentence.replace(" ", "")))
    else:
        print(len(sentence))

def sine(sine):
    print(round(math.sin(sine), 5))

def asin(arcsine):
    arcsine = math.asin(arcsine)
    print(round(arcsine, 5))

def atan(atan):
    print(round(math.atan(atan), 5))

def acos(acos):
    print(round(math.acos(acos), 5))

def sigma(start, end):
    result = sum(i ** 2 for i in range(start, end + 1))
    print(round(result, 5))

def deltaxpos(xpos2):
    delta = xpos - xpos2
    print(f"Change in X: {delta}")

def deltaypos(ypos2):
    delta = ypos - ypos2
    print(f"Change in Y: {delta}")

def helpme():
    print("""Available functions: average(),absval(),acos(),add(),alphabeticalorder(),asin(),atan(),bold(),caesarcipherdecode(),caesarcipherencode(),ceiling(),changexpos(),changeypos(),charcount(),cosine(),deltaxpos(),deltaypos(),divide(),exponent(),factorial(),fibonacci(),floor(),helpme(),italicize(),italicizebold(),multiply(),party(),reverse(),sigma(),sine(),slowprint(),squareroot(),subtract(),tangent(),underline(),update_fib() """)

def squareroot(sr):
    print(round(math.sqrt(sr), 5))

def exponent(base, exponent):
    # Smart men touch their chins
    result = base ** exponent
    print(round(result, 5))

def factorial(factor):
    print(math.factorial(factor))

def fibonacci(number):
    def fib_gen():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    fib = fib_gen()
    for _ in range(number):
        print(next(fib), end=" ")
    print()

def alphabeticalorder(text):
    sortedtext = sorted(text)
    sortedtext = str(sortedtext)
    sortedtext = sortedtext.replace("[", "")
    sortedtext = sortedtext.replace("]", "")
    sortedtext = sortedtext.replace("'", "")
    sortedtext = sortedtext.replace(",", "")
    print(sortedtext)

def reverse(text):
    reversed_text = text[::-1]
    print(reversed_text)

# As I write this code, I have a bearded dragon on my chest which I must warm with my palm.
def italicize(text):
    print(f"\x1B[3m{text}\x1B[0m")

def bold(text):
    print(f"\033[1m{text}\033[0m")

def italicizebold(text):
    print(f"\033[1;3m{text}\033[0m")

def underline(text):
    print(f"\x1B[4m{text}\x1B[0m")

#The dragon is gone.
def caesarcipherencode(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    print(result)

def caesarcipherdecode(text, shift):
    caesarcipherencode(text, -shift)

def slowprint(text, delay=0.05):
    for char in text:
        time.sleep(delay)
        print(char, end='', flush=True)
    print()

def party():
    while True:
        time.sleep(0.5)
        print("PARTY TIME!")

def update_fib():
    while True:
        cool = fibonacci(10)
        fib_sequence.append(f"{cool}")

# To build something great, all you need is willpower, and a little bit of cocaine.
