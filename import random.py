import random

def generate_random_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def main():
    size = random.randint(5, 20)
    min_value = random.randint(1, 10)
    max_value = random.randint(20, 100)
    
    random_list = generate_random_list(size, min_value, max_value)
    print(f"Generated list: {random_list}")
    
    average = calculate_average(random_list)
    print(f"Average of the list: {average}")

if __name__ == "__main__":
    main()
