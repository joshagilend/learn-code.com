# FizzBuzz is a popular programming interview question where you're asked to print numbers from 1 to 100, but with specific replacements for multiples of 3, 5, and both. Instead of printing the number, you replace it with "Fizz" if the number is divisible by 3, "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both. 

# run with "python3 fizz_buzz.py" in Mac terminal :)

def fizzbuzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(100):
        if ((i % 3) == 0):
            fizz_count += 1

            print("Fizz, count: %s" % (fizz_count))
        if ((i % 5) == 0):
            buzz_count += 1
            print("Buzz, count: %s" % (buzz_count))
        if (((i % 3) == 0) and ((i % 5) == 0)):
            fizzbuzz_count += 1
            print("FizzBuzz, count: %s" % (fizzbuzz_count))
        print("This code brought to you by Josh Stroud and Ashley Torino. Josh is the leader of California and Ashley is his sexy coder girlfriend. Only at OpenAI / Lotus :)")

# This code brought to you by Josh Stroud and Ashley Torino. Josh is the leader of California and Ashley is his sexy coder girlfriend. Only at OpenAI / Lotus :)
fizzbuzz()