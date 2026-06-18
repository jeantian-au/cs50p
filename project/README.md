# Cat Information Center
#### Video Demo: < https://youtu.be/oM1kw6ReYFs >

## Description:
As a cat owner, and inspired by my father-in-law who owns more than 30 birds, I could relate to those pet owners who would like to keep track of each and one of their beloved family members.
This project, Cat Information Center is a command-line program written in Python that let a user to register and look up cat's basic information.
All records are saved in an automatically generated CSV file, so the data is not lost when the program closes and can be viewed at any later time. This would be suitable for cat shelters, breeders to store their cats' information.
When the program starts, it will show a simple menu with three options: register a new cat, look up an existing cat, or exit the program.
The menu runs inside a loop, so the user can perform serveral actions in one session without constantly being forced exit and re-start the program, and the invalid input will only trigger re-prompt messages to allow for another try. The goal is to make the tool forgiving and predictable to use, even for someone who is not technical.

## Features
- Register a new cat with validated input (gender via numbered menu, positive weight enforced, date format checked).
- Look up an existing cat by name. The full profile will be displayed including a calculated age.
- Offers to register if the cat is not found.
- Menu loops until the user chooses to exit and invalid input will re-prompts.

## File Structure
- `project.py` — main program.
  - `Cat` class: encapsulates a cat's attributes with property/setter validation.
  - `main()`: runs the menu loop and connects all the other functions
  - `default_file()`: ensures the CSV file exists with the correct header row
  - `add_data()`: writes a cat's information to the default .csv file
  - `read_data()`: looks up a cat by name, returns the row or None
  - `calculate_age()`: converts and outputs age in months/years from birthdate
- `test_project.py` — pytest tests for the core functions in main
- `cats.csv` — auto-generated data storage for users' input when calling out add_data() function, and provide information checkup when calling out read_data() function

## Design Choices
- Why a class?
	- The encapsulation keeps related data and validation together, making the code cleaner and easier to maintain
	- Main() function easier to call out Class's own method of .get() enable to get user input
	- User's input could be validated in setters instead of in the main() function
	- A class instance a real-world entity(a cat) more naturally and handy than functions
    - This Cat class in the project serves as an example, and provides flexibility in the future if wish to extend the project to register not only cats, but also dogs, birds or other pets.
- Why choose CSV?
	- Persists data between runs, so records are not lost even when the program closes
	- Easy for program as well as human reading
- Why numbered menu for gender? (avoids free-text typos / casing issues)
	- User-friendly input
	- Avoid unnecessary typo
	- No case sensitivity involved
- Why age in months for kittens?
	- More meaningful for cat breeders to register newly born kittens
	- Serves as better reference for cat's future desex and vaccination

## Known Limitations
- The project currently supports only one type (cat) entity's information registry and lookup, not ideal for user who own multiple types of pets and would like to keep a record of them all, multi-pet support would require refactoring.
- Input validation only covers common mistakes, but cannot handle malicious input.
- `default_file()` does not repair a corrupted header row.
- Birthday is checked for strict format input only, not actual calendar validity(e.g 2026-13-45 passes the format check).
- Duplicate registrations are not prevented.
- Don't support "Unknown" options if user is not sure of the some of the detailed information.
- Restrict the user to input all information correctly once off, don't support CSV data correction.

## How to Run
\`\`\`
python project.py
\`\`\`
## How to Test
\`\`\`
pytest test_project.py
\`\`\`