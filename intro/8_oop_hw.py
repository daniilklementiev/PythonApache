import json

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"[{self.numerator}/{self.denominator}]"

    def __add__(self, other):
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Fraction(new_numerator, common_denominator).reduce()

    def __sub__(self, other):
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        return Fraction(new_numerator, common_denominator).reduce()

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator).reduce()

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator).reduce()

    def to_json(self):
        return json.dumps({"numerator": self.numerator, "denominator": self.denominator})

    @classmethod
    def from_json(cls, json_str):
        try:
            data = json.loads(json_str)
            if "numerator" in data and "denominator" in data:
                return cls(data["numerator"], data["denominator"])
            else:
                raise ValueError("Invalid JSON format. Missing numerator or denominator.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {str(e)}")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.to_json())

    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, "r") as file:
                json_str = file.read()
            return cls.from_json(json_str)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")
        except ValueError as e:
            raise ValueError(f"Error loading fraction from file: {str(e)}")

    def reduce(self):
        # Функція для знаходження найменшого спільного множника
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Знаходимо НСМ
        common_divisor = gcd(self.numerator, self.denominator)

        # Скорочуємо дріб
        self.numerator //= common_divisor
        self.denominator //= common_divisor

        return self

# Приклад використання класу Fraction
f1 = Fraction(2, 3)
print(f"Fraction 1: {f1}")

f2 = Fraction(1, 4)
print(f"Fraction 2: {f2}")

# Додавання
result = f1 + f2
print(f"Addition: {result}")

# Віднімання
result = f1 - f2
print(f"Subtraction: {result}")

# Множення
result = f1 * f2
print(f"Multiplication: {result}")

# Ділення
result = f1 / f2
print(f"Division: {result}")
