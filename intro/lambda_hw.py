
data = [2, 4, 6, 8, 10]

def strategy(data, lambdas):
    results = []
    for item in lambdas:
        results.append(item(data))
        print("%s: %s" % (item.__name__, item(data)))
    
    return min(results)

def main() -> None:
    lambdas = [
        lambda input: sum(input) / len(input),                # arithmetic mean
        lambda input: len(input) / sum(1 / i for i in input), # harmonic mean
        lambda input: 1 / len(input) * sum(i for i in input)  # geometric mean
    ]
    result = strategy(data, lambdas)
    print(result)

if __name__ == "__main__":
    main()