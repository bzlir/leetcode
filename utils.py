from datetime import datetime
import yaml
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
            delta = (datetime.today() - date_obj).days

            if delta in [1,2,4,7,14]:
                result.extend(self.data[key])
        
        return set(sorted(self.data[key]))
    

if __name__ == '__main__':
    config_path = 'config.yaml'
    gen = PlanGenerator(config_path)
    result = gen.generate()
    print(result)
