import numpy as np
from scipy.stats import chi2

def generate_random_numbers(multiplier, increment, modulus, seed_value, num_random_numbers):
    random_numbers = []
    current_value = seed_value
    for _ in range(num_random_numbers):
        current_value = (multiplier * current_value + increment) % modulus
        random_numbers.append(round(current_value / modulus, 2))
    return random_numbers

def chi_square_test(observed_frequencies, expected_frequencies, significance_level, df):
    chi2_stat = np.sum((observed_frequencies - expected_frequencies)**2 / expected_frequencies)
    critical_value = chi2.ppf(1 - significance_level, df)
    return chi2_stat, critical_value

def print_chi_square_table_stepwise(observed_frequencies, expected_frequencies, significance_level, df):
    print("Step-wise Chi-square Table:")
    print("Step | Interval | Observed(O) | Expected(E) | (O-E) | (O- E)^2/E")
    print("-" * 70)
    for i in range(len(observed_frequencies)):
        interval = f"{i/10:}-{(i+1)/10:}"
        diff_observed_expected = observed_frequencies[i] - expected_frequencies[i]
        chi_square_step = (diff_observed_expected)**2 / expected_frequencies[i]
        print(f" {i+1:<4} | {interval:^9} | {observed_frequencies[i]:^11} | {expected_frequencies[i]:^11} | {diff_observed_expected:^5} | {chi_square_step:^9.4f}")
    print("-" * 70)
    chi2_stat, critical_value = chi_square_test(observed_frequencies, expected_frequencies, significance_level, df)
    print(f"Sample test statistics: {chi2_stat:.4f}")
    print(f"Critical value (alpha={significance_level}, df={df}): {critical_value:.4f}")
    if chi2_stat <= critical_value:
        print("Null hypothesis accepted. The observed frequencies indicate uniformity.")
    else:
        print("Null hypothesis rejected. The observed frequencies do not indicate uniformity.")

for i in range(5):
    print(f"\nSet {i+1}:")
    multiplier = int(input("Enter multiplier (a): "))
    increment = int(input("Enter increment (c): "))
    modulus = int(input("Enter modulus (m): "))
    seed_value = int(input("Enter seed value: "))
    num_random_numbers = 100
    significance_level = 0.05
    df = 9

    random_numbers = generate_random_numbers(multiplier, increment, modulus, seed_value, num_random_numbers)

    observed_frequencies, _ = np.histogram(random_numbers, bins=10, range=(0, 1))
    expected_frequencies = np.full(10, fill_value=num_random_numbers/10)
    print_chi_square_table_stepwise(observed_frequencies, expected_frequencies, significance_level, df)
