import pandas as pd


def get_data():

    df = pd.read_csv('values.csv')

    print(df['food'].tolist())
    food = df['food'].tolist()
    carbohydrates = df['carbohydrates'].tolist()
    protein = df['protein'].tolist()
    fat = df['fat'].tolist()

    south_food = {
        'food': food,
        'carbohydrates': carbohydrates,
        'protein': protein,
        'fat': fat

    }

    print(south_food)
    return south_food


if __name__ == "__main__":
    get_data()
