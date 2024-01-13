import pandas as pd
from functools import wraps
import os
import pickle

def cache_result(file_path):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    result = pickle.load(file)
                print(f'Wynik wczytany z pamięci podręcznej: {result}')
            else:
                result = func(*args, **kwargs)
                print(f'Wynik obliczony: {result}')

                with open(file_path, 'wb') as file:
                    pickle.dump(result, file)
                    print(f'Wynik zapisany do pamięci podręcznej: {result}')
            return result  # Zwracaj wynik funkcji

        return wrapper

    return decorator

from datasets import load_dataset

def required_data():
    dataset = load_dataset("imodels/credit-card")
    return dataset

dataset = required_data()
df = pd.DataFrame(dataset['train'])

@cache_result(file_path='ten_oldest_clients_cache.pkl')
def ten_oldest_clients():
    top_10_oldest = df.nlargest(10, 'age')
    selected_columns = ['limit_bal', 'age'] + [f'education:{i}' for i in range(7)]
    top_10_oldest = top_10_oldest[selected_columns]
    print(top_10_oldest)
    return top_10_oldest  # Zwracaj wynik funkcji

if __name__ == '__main__':
    ten_oldest_clients_result = ten_oldest_clients()
