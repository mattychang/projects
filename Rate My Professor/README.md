# RateMyProfessors Scraper
## Author: Matthew Chang

This Python script allows you to search for a professor's rating information on RateMyProfessors.com using Google search.

## Features

- Searches for a professor by university name, first name, and last name.
- Retrieves the professor's rating, department, "would take again" percentage, and difficulty rating.
- Outputs each piece of information on a new line for clarity.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `googlesearch-python` library

## Installation

1. Download the `ratemyprofessor.py` file to your local machine.

2. Open your terminal (or command prompt) and navigate to the directory where the file is located.

3. Install the required libraries:
    ```sh
    pip install requests beautifulsoup4 googlesearch-python
    ```

## Usage

1. Run the script:
    ```sh
    python ratemyprofessor.py
    ```

2. Enter the university name, professor's first name, and professor's last name when prompted.

3. The script will search for the professor on RateMyProfessors.com and output the following information:
    - Name
    - Rating
    - Department
    - "Would Take Again" percentage
    - Difficulty rating

## Example

```sh
$ python ratemyprofessor.py
Enter the university name: Case Western Reserve University
Enter the professor's first name: Nicole
Enter the professor's last name: Crown
Professor Found:
Name: Nicole Crown
Rating: 4.1
Department: Biology department at Case Western Reserve University
Would Take Again: 100%
Difficulty: 2.8
