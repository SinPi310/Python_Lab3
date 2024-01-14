from datasets import load_dataset

import pandas as pd
import matplotlib.pyplot as plt


def required_data():
    dataset = load_dataset("imodels/credit-card")
    return dataset

dataset = required_data()
df = pd.DataFrame(dataset['train'])


def find_duplicates():

    duplicates = df[df.duplicated(keep=False)]
    return duplicates


def correlation():

    correlation = df['age'].corr(df['limit_bal'])
    return correlation


def sum_of_transaction():

    bill_columns = [f'bill_amt{i}' for i in range(1, 7)]
    df['sum_of_transactions'] = df[bill_columns].sum(axis=1)

    return df


def ten_oldest_clients():

    df = sum_of_transaction()

    top_10_oldest = df.nlargest(10, 'age')

    selected_columns = ['limit_bal', 'age'] + [f'education:{i}' for i in range(7)] + ['sum_of_transactions']


    top_10_oldest = top_10_oldest[selected_columns]
    print(top_10_oldest)


def draw_hists():

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].hist(df['limit_bal'], bins=20, color='blue', edgecolor='black')
    axes[0].set_title('Histogram Limitu Kredytu')
    axes[0].set_xlabel('Limit Kredytu')
    axes[0].set_ylabel('Liczba Klientów')

    axes[1].hist(df['age'], bins=20, color='red', edgecolor='black')
    axes[1].set_title('Histogram Wieku')
    axes[1].set_xlabel('Wiek')
    axes[1].set_ylabel('Liczba Klientów')

    axes[2].scatter(df['age'], df['limit_bal'], color='green', alpha=0.5)
    axes[2].set_title('Zależność Limitu Kredytu od Wieku')
    axes[2].set_xlabel('Wiek')
    axes[2].set_ylabel('Limit Kredytu')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    #print(find_duplicates())
    correlation_of_age_and_credit_balance = correlation()
    print(correlation_of_age_and_credit_balance)
    #sum_of_transaction()
    ten_oldest_clients()
    #draw_hists()
