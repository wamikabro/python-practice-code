a = 5

aIsNegativeOrPositive = "Negative" if a < 0 else "Positive"
print(f"The number {a} is {aIsNegativeOrPositive}.")


a = 0

# multiple conditions
aIsNegativePositiveOrZero = "Negative" if a < 0 else "Positive" if a > 0 else "Zero"
print(f"The number {a} is {aIsNegativePositiveOrZero}.")

a = 3

aIsNegativePositiveDeep = ("NegNeg" if a < -2 else "Negative") if a < 0 else (("PosPos" if a > 2 else "Positive") if a > 0 else "Zero")
print(f"The number {a} is {aIsNegativePositiveDeep}.")