from itertools import combinations

def find_sum_in_list(numbers, target):
    results = []
    for x in range(len(numbers)):
        results.extend(
            [   
                combo for combo in combinations(numbers ,x)  
                    if sum(combo) <= target
            ]   
        )   

    print (results)

if __name__ == "__main__":
    find_sum_in_list([2,5,6,8], 17)