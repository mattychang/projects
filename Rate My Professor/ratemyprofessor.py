import requests
from bs4 import BeautifulSoup
from googlesearch import search

def search_professor(university_name, first_name, last_name):
    query = f"{university_name} {first_name} {last_name} site:ratemyprofessors.com"
    
    search_results = search(query, num_results=10)
    
    professor_link = None
    for url in search_results:
        if "ratemyprofessors.com" in url:
            professor_link = url
            break
    
    if professor_link:
        professor_info = get_professor_info(professor_link)
        if professor_info:
            print("Professor Found:")
            print(f"Name: {professor_info['name']}")
            print(f"Rating: {professor_info['rating']}")
            print(f"Department: {professor_info['department']}")
            print(f"Would Take Again: {professor_info['would_take_again']}")
            print(f"Difficulty: {professor_info['difficulty']}")
        else:
            print("Error fetching the professor's detailed information.")
    else:
        print("Professor not found or there was an error in fetching the information.")

def get_professor_info(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        name = soup.find('div', class_='NameTitle__Name-dowf0z-0').text.strip()
        
        rating_element = soup.find('div', class_='RatingValue__Numerator-qw8sqy-2')
        rating = rating_element.text.strip() if rating_element else 'N/A'

        department_element = soup.find('div', class_='NameTitle__Title-dowf0z-1').text.strip()
        department = department_element if department_element else 'N/A'
        
        feedback_elements = soup.find_all('div', class_='FeedbackItem__FeedbackNumber-uof32n-1')
        would_take_again = feedback_elements[0].text.strip() if feedback_elements else 'N/A'
        difficulty = feedback_elements[1].text.strip() if len(feedback_elements) > 1 else 'N/A'
        
        return {
            'name': name,
            'rating': rating,
            'department': department,
            'would_take_again': would_take_again,
            'difficulty': difficulty
        }
    except Exception as e:
        return None

if __name__ == "__main__":
    university_name = input("Enter the university name: ")
    first_name = input("Enter the professor's first name: ")
    last_name = input("Enter the professor's last name: ")
    
    search_professor(university_name, first_name, last_name)
