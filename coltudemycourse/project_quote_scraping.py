import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep

def scrape_quotes():
    response = requests.get(f"http://quotes.toscrape.com")
    list_quotes = []
    while True:
        try:
            soup = BeautifulSoup(response.text, "html.parser")
            div_quotes = soup.select('.quote')      
            for div_quote in div_quotes:
                quote = div_quote.find("span").get_text()
                author = div_quote.select('.author')[0].get_text()
                list_quotes.append({'quote': quote,
                                    'author': author,
                                    'bio-link': div_quote.find('a')['href'],
                                    })
            next_page = soup.select('.next')[0].find('a')['href']
            #sleep(2)
            response = requests.get(f"http://quotes.toscrape.com{next_page}")
        except IndexError:
            return list_quotes

def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print('Here\'s a quote:')
    print(quote['quote'])
    guess = ''
    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
        guess = input(f'Who said this? Guesses remaining {remaining_guesses}.\n')
        if guess.lower() == quote['author'].lower():
            print('You guessed correctly! Congratulations!')
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            bio_res = requests.get(f"http://quotes.toscrape.com{quote['bio-link']}")
            bio_soup = BeautifulSoup(bio_res.text, "html.parser")
            birth_date = bio_soup.select('.author-born-date')[0].get_text()
            birth_place = bio_soup.select('.author-born-location')[0].get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            print(f"Here's a hint: The author's last name starts with {quote['author'].split(' ')[1][0]}")
        else:
            print(f"Sorry, you've run out of guesses. The answer was {quote['author']}")
    
    play_again = ' '
    while play_again not in ('y', 'yes', 'n', 'no'):
        play_again = input('Would you like to play again (y/n)?: ').lower()
    if play_again in ('y', 'yes'):
        return start_game(quotes)
    else:
        print('Ok! See you next time!')

quotes = scrape_quotes()
start_game(quotes)