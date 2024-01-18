import csv

records = []
headings = []


def display_menu():
    print("""
    Please select one of the following options:
    [1] Display the names of all passengers
    [2] Display the number of passengers that survived
    [3] Display the number of passengers per gender
    [4] Display the number of passengers per age group
    [5] Display survivors by age group


    """)
    return int(input(""))


def display_passenger_names():
    print("The name of the passengers are: ")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = sum(1 for record in records if int(record[1]==1))
    print(f"{num_survived} passengers survived")
    for record in records:
        if num_survived == int(record[1]):
            num_survived += 1
        print(f"{num_survived} passengers survived where {num_survived}")

def display_passenger_per_gender():
    females =sum(1 for record in records if record[4].lower() == "female")
    males = sum(1 for record in records if record[4].lower() == "male")
    print(f"females: {females}, males: {males}")

def disply_passenger_per_age_group():
    children = adults = elderly = 0
    for record in records:
        age = record[5]
        if age:
            age = float(age)
            if age < 18:
                children +=1
            elif age <65:
                adults +=1
            else:
                elderly += 1
    print(f"children: {children}, adults: {adults }, elderly: {elderly}")


def load_data(file_path):

    global records, headings
    print("Loading data ...")
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)
    print("Done ")


def survivors_by_age_group():
    children = adult = elderly = 0
    children_survived = adult_survived = elderly_survived = 0
    survived = 0
    for record in records:
        age = record[5]
        survived = int(record[1])
        if age:
            age = float(age)
            if age < 18:
                children += 1
                children_survived += survived
            elif age < 65:
                adult +=1
                adult_survived += survived
            elif age > 65:
                elderly +=1
                elderly_survived += survived
    print(f"Children : {children_survived}/{children} Adults {adult_survived}/{adult} Elderly: {elderly_survived}/{elderly}")


def run():
    file_path = "titanic.csv"
    load_data(file_path)
    print(f"successfully loaded {len(records)} records")
    selected_option =  display_menu()
    print(f"You have selected option {selected_option}")
    if selected_option == 1:
        display_passenger_names()

    elif selected_option == 2:
        display_num_survivors()

    elif selected_option == 3:
        display_passenger_per_gender()

    elif selected_option == 4:
        disply_passenger_per_age_group()
    elif selected_option == 5:
        survivors_by_age_group()


    else:
        print("Error!")


run()
display_menu()
