import random

class CouponCollector:
    @staticmethod
    def generate_random_number(N):
        # Generate a random number between 1 and N
        return random.randint(1, N)

    @staticmethod
    def collect_coupons(N):
        collected_coupons = set()  # Set to store unique coupons
        total_random_numbers = 0   # Counter for the total number of random numbers generated

        while len(collected_coupons) < N:
            new_coupon = CouponCollector.generate_random_number(N)
            total_random_numbers += 1
            collected_coupons.add(new_coupon)

        return total_random_numbers

# Main code
N = int(input("Enter the number of distinct coupons: "))

total_random_numbers = CouponCollector.collect_coupons(N)

print(f"Total random numbers needed to collect all {N} distinct coupons: {total_random_numbers}")
