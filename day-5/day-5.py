def main():
    after_rules: dict[int, list[int]] = {}
    before_rules: dict[int, list[int]] = {}
    updates: list[list[int]] = []

    with open('rules.txt', 'r') as file:
        for line in file:
            nums = line.strip().split('|')
            after_rules.setdefault(int(nums[0]), []).append(int(nums[1]))
            before_rules.setdefault(int(nums[1]), []).append(int(nums[0]))

    with open('updates.txt', 'r') as file:
        for line in file:
            update = [int(num) for num in line.strip().split(",")]
            updates.append(update)

    sol: int = rules_checker(after_rules, before_rules, updates)
    print(sol)

    sol2: int = rules_checker_v2(after_rules, before_rules, updates)
    print(sol2)

def rules_checker(after_rules, before_rules, updates):
    sol: int = 0
    
    for update in updates:
        if good_rule(after_rules, before_rules, update):
            sol += update[len(update) // 2]
    
    return sol
        
            
def good_rule(after_rules, before_rules, update):
    for i in range(len(update) - 1):
            for j in range(0,i):
                if update[j] not in before_rules[update[i]]:
                    return False
            for j in range(i+1, len(update)):
                if update[j] not in after_rules[update[i]]:
                    return False
    return True

def sort_update(after_rules, update):

    def comes_before(page1, page2):
        return page1 in after_rules and page2 in after_rules[page1]

    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if comes_before(update[j], update[i]): 
                update[i], update[j] = update[j], update[i]
    
    return update

def rules_checker_v2(after_rules, before_rules, updates):
    sol: int = 0
    
    for update in updates:
        if not good_rule(after_rules, before_rules, update):
            sorted_pages = sort_update(after_rules, update)
            sol += sorted_pages[len(sorted_pages) // 2]
    
    return sol

if __name__ == '__main__':
    main()