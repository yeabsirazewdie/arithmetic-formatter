from pytest import main
from arithmetic_arranger import arithmetic_arranger



# Example usage with results shown

problems_with_results = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arranged_problems_with_results = arithmetic_arranger(problems_with_results, True)
print(arranged_problems_with_results)


# Run unit tests automatically
main(['-vv'])
