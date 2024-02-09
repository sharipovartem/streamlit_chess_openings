import requests
from converter.pgn_data import PGNData
import os, shutil
import time

#Getting data from the website
username = 'canijustlose'
chess_website = 'lichess'
def data_request(username: str, chess_website: str) -> None:
    """
    Makes a request to a chess website for user data and saves it to a file.
    
    Args:
    - username: a string representing the username of the user
    - chess_website: a string representing the chess website to make the request to
    """
    # Construct the request link based on the chess website
    req_link = (
        'https://lichess.org/api/games/user/' + str(username)
        if chess_website == "lichess"
        else 'https://api.chess.com/pub/player/' + str(username)
    )
    print(req_link)

    # Make the request to the chess website
    user_data = requests.get(req_link)
    
    # Print response status
    print(user_data.status_code)
    
    # If request is successful, save user data to a file
    if user_data.status_code == 200:
        # Check if directory exists, if not, create it
        if not os.path.exists('players_data'):
            os.makedirs('players_data')
            print("Created directory: players_data")


        # Write user data to a file
        file_path = os.path.join('players_data', f'{username}.pgn')
        with open(file_path, 'w') as f:
            f.write(user_data.text)
            print(f"Saved user data to: {file_path}")
    
    else:
        print("Couldn't fetch data, please check username or website.")

def convert_to_csv(username: str) -> None:
    """
    Converts the PGN data to a CSV format and exports it to a specified directory and file.

    Args:
    username (str): The username for the PGN file.

    Returns:
    None
    """
    # Initialize PGNData object
    pgn_data = PGNData('players_data/' + f'{username}.pgn')

    # Export PGN data to CSV
    pgn_data.export( moves_required=False)
    try:
        shutil.move(f'{username}_game_info.csv', "players_data/")
        os.remove('players_data/' + f'{username}.pgn')
    except shutil.Error as e:
        print(f"Error moving file: {e}")


    # Print success message
    print("File converted successfully.")

def wait_for_file(username: str) -> None:
    """
    Waits for a file to exist in the 'players_data' directory.
    
    Args:
    username (str): The username of the file to wait for.
    
    Returns:
    None
    """
    time_to_wait = 10
    time_counter = 0
    while not os.path.exists('players_data/' + username + ".pgn"):
        print(f"File 'players_data/{username}.pgn' does not exist yet, waiting...")
        time.sleep(1)
        time_counter += 1
        if time_counter > time_to_wait:
            print(f"File 'players_data/{username}.pgn' still does not exist after {time_to_wait} seconds.")
            break


