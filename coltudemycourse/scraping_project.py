import requests
from bs4 import BeautifulSoup
from random import choice, randint

response = requests.get(f"http://quotes.toscrape.com")
list_quotes = []
while True:
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        div_quotes = soup.select('.quote')      
        for div_quote in div_quotes:
            quote = div_quote.find("span").get_text()
            author = div_quote.select('.author')[0].get_text()
            bio_res = requests.get(
                    f"http://quotes.toscrape.com{div_quote.find('a')['href']}")
            bio_soup = BeautifulSoup(bio_res.text, "html.parser")
            bio = f"Born {bio_soup.select('.author-born-date')[0].get_text()} {bio_soup.select('.author-born-location')[0].get_text()}"
            list_quotes.append({'quote': quote,
                                'author': author,
                                'tip1': f"{bio}",
                                'tip2': f'The author\'s first name starts with {author.split(" ")[0][0]}',
                                'tip3': f'The author\'s last name starts with {author.split(" ")[1][0]}'
                                })
        next_page = soup.select('.next')[0].find('a')['href']
        print(next_page)
        response = requests.get(f"http://quotes.toscrape.com{next_page}")
    except IndexError:
        break

play_again = 'y'
while play_again == 'y':
    ch = choice(list_quotes)
    print(f'Here\'s a quote:\n\n {ch["quote"]}')
    erro = 0
    for i in range(0,4): 
        answer = input(f'Who said this? Guesses remaining {erro}. ')
        if answer == ch["author"]:
            print('You guessed correctly! Congratulations!')
            break   
        elif erro < 3:
            erro += 1       
            print(f'Here\'s a hint: {ch["tip" + str(erro)]}')
        else:
            print(f'Sorry, you\'ve run out of guesses. The answer was {ch["author"]}')
    play_again = input('Would you like to play again (y/n)?: ').lower()
    while play_again != 'n' and play_again != 'y': 
        print('Invalid Option!')
        play_again = input('Would you like to play again (y/n)?: ').lower()

print('Ok! See you next time!')
