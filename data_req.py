import requests


username = 'canijustlose'
chess_website = 'lichess'
def data_request(username, chess_website):
    if chess_website == "lichess":
        req_link = 'https://lichess.org/api/games/user/' + str(username)
        print(req_link)
    else:
        req_link = 'https://api.chess.com/pub/player/' + str(username)
        print(req_link)

    user_data = requests.get(req_link)
    
    print(user_data.status_code)  # print response status
    
    if user_data.status_code == 200:      
        with open(f'{username}.pgn', 'w') as f:
            f.write(user_data.text)
        
        return print("File saved successfully.")
    
    else:
        return print("Couldn't fetch data, please check username or website.")
data_request(username, chess_website)