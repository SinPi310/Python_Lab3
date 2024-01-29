import pandas as pd
from functools import wraps
import os
import pickle

def cache_result(file_path):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result_data = None

            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    result_data = pickle.load(file)

            if result_data and result_data.get('args') == args:
                result = result_data.get('result')
                print(f'Wynik wczytany z pamięci podręcznej: {result}')
            else:
                result = func(*args, **kwargs)
                print(f'Wynik obliczony: {result}')

                with open(file_path, 'wb') as file:
                    new_data = {'args': args, 'result': result}
                    pickle.dump(new_data, file)
                    print(f'Nowe dane zapisane do pamięci podręcznej: {new_data}')

            return result

        return wrapper

    return decorator

from datasets import load_dataset

def required_data():
    dataset = load_dataset("imodels/credit-card")
    return dataset

dataset = required_data()
df = pd.DataFrame(dataset['train'])

@cache_result(file_path='ten_oldest_clients_cache.pkl')
def ten_oldest_clients(x):
    top_10_oldest = df.nlargest(x, 'age')
    selected_columns = ['limit_bal', 'age'] + [f'education:{i}' for i in range(7)]
    top_10_oldest = top_10_oldest[selected_columns]
    print(top_10_oldest)
    return top_10_oldest

if __name__ == '__main__':
    ##ten_oldest_clients_result = ten_oldest_clients(10)

    df = pd.DataFrame(required_data()['train'])  # Wczytywanie zaktualizowane dane
    ten_oldest_clients_result_new = ten_oldest_clients(3)
    ##ten_oldest_clients_result_new = ten_oldest_clients(6)
