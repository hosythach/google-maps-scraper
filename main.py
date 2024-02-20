from src import Gmaps

def read_file_to_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Remove newline characters from the end of each line
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

# Example usage:
file_path = 'inputs.txt'  # Replace 'example.txt' with the path to your text file
lines = read_file_to_list(file_path)
print(lines)

queries =  read_file_to_list(file_path)
# Gmaps.Cities.Vietnam
Gmaps.places(queries, lang=Gmaps.Lang.Vietnamese, convert_to_english=False, geo_coordinates="Vietnam", sort = Gmaps.SORT_BY_RATING_DESCENDING)