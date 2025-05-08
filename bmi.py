def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return bmi, -1  
    elif 18.5 <= bmi <= 25.0:
        return bmi, 0  
    else:
        return bmi, 1   