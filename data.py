import pandas as pd 


def get_data():

    df = pd.read_csv('values.csv')
    
    print(df['food'].tolist())
    food            = df['food'].tolist()
    carbohydrates   = df['carbohydrates'].tolist()
    protein         = df['protein'].tolist()
    fat             = df['fat'].tolist()
   
    south_food = {
        'food'           : food,
        'carbohydrates'  : carbohydrates,
        'protein'        : protein,
        'fat'            : fat
        
    }

    print(south_food)
    return south_food


def add_row(food, carbohydrates,protein,fat ):
    df = pd.read_csv('values.csv') 
    new_food = {
        'food'           : food,
        'carbohydrates'  : carbohydrates,
        'protein'        : protein,
        'fat'            : fat
        
    }
    print(df)
    df = df.append(new_row, ignore_index=True)
    print(df)
    df.to_csv('values.csv')


if __name__ == "__main__":
    get_data()