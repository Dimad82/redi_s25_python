class Counter:
    instance_count = 0

    def __init__(self):
        Counter.instance_count += 1

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

print(f"Instances created: {Counter.instance_count}")