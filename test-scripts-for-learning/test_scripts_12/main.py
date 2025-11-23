# test_scripts_12 

import csv

def main():

    names = []
    salaries = []

    # Overwrite the contents of output.csv with just the header line (so if running this script subsequent times, clears out old data)
    file_name = "output.csv"
    with open(file_name, 'w') as file:
        file.write("name,salary\n")

    with open("input.csv") as file:
        # DictReader knows first line is header, takes rest of lines as dictionaries (for input.csv format of dictionary is {"name" : "person's name", "hours_worked" : "##"} (## some 2 digit number))
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            # Uncomment these two lines to see how referencing the row works
            # print(row['name'])
            # print(row['hours_worked'])
            names.append(row['name'])
            salary = int(row['hours_worked']) * 15
            salaries.append(salary)

    # You could probably also write the above to an array of dictionaries and iterate/set row that way, but whatever
    for i in range (3): # 0,1,2
        row = f"{names[i]},{salaries[i]}"
        print(row)

        # a is 'append mode' as in append to the file contents, don't overwrite them
        with open(file_name, "a") as file:
            file.write(f"{row}\n")

if __name__ == "__main__":
    main()