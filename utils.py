from datetime import datetime
import yaml
from collections import Counter


def load_config(config_path: str) -> dict:
    try:
        with open(config_path, 'r') as f:
            config_data = yaml.safe_load(f)
    except FileNotFoundError:
        raise Exception(f'Input file not found at {config_path}')
    return config_data

def save_config(config_path:str, data) -> None:
    with open(config_path, 'w') as f:
        yaml.dump(data, f)

class PlanGenerator:
    def __init__(self, config: str) -> None:
        self.config = config
        self.data = load_config(config)
        self.today = datetime.today().strftime("%Y-%m-%d")

    def add_item(self, input):
        self.data[self.today].append(input)
        save_config(self.config, self.data)

    
    def generate(self):
        result = []
        for key in self.data:
            date_obj = datetime.strptime(str(key), "%Y-%m-%d")
            delta = (datetime.today() - date_obj).days -6

            if delta in [1,2,4,7,14]:
                result.extend(self.data[key])
        

        return set(sorted(result))

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def find_combination(nums, target):
    """
    Finds a combination of integers in nums that add up to target.
    Returns a counter of nums that indicates the frequency of each integer in the combination.
    """
    # Initialize a dictionary to keep track of the frequency of each number in the combination
    count = Counter()
    # Sort the input list in non-decreasing order
    nums.sort()
    res = []
    # Use a helper function to recursively search for combinations
    def search_combinations(start_index, remaining_target):
        # Base case: we've found a combination that adds up to the target
        if remaining_target == 0:
            res.append(count)
            return True
        # Recursive case: explore all possible combinations that start with the current number
        for i in range(start_index, len(nums)):
            # Skip over duplicates to avoid duplicates in the output
            if i > start_index and nums[i] == nums[i-1]:
                continue
            # If the current number is too large to fit into the remaining target, stop searching
            if nums[i] > remaining_target:
                break
            # Add the current number to the combination and recursively search for the remaining target
            count[nums[i]] += 1
            if search_combinations(i+1, remaining_target - nums[i]):
                return True
            # Backtrack by removing the current number from the combination
            count[nums[i]] -= 1
        # If we've explored all possible combinations starting at the current index and didn't find a solution, return False
        return False
    # Call the recursive helper function to search for combinations
    search_combinations(0, target)
    # Return the frequency counter of the output combination
    return res

if __name__ == '__main__':
    config_path = 'config.yaml'
    gen = PlanGenerator(config_path)
    result = gen.generate()
    print(result)
    
        


