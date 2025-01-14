def text_to_ascii_art(text):
    ascii_art_dict = {
        'A': ["    /\\    ", "   /  \\   ", "  / /\\ \\  ", " / ____ \\ ", "/_/    \\_\\"],
        'B': [" ____  ", "| __ ) ", "|  _ \\ ", "| |_) |", "|____/ "],
        'C': ["  ____ ", " / ___|", "| |    ", "| |___ ", " \\____|"],
        'D': [" ____  ", "|  _ \\ ", "| | | |", "| |_| |", "|____/ "],
        'E': [" _____ ", "| ____|", "|  _|  ", "| |___ ", "|_____|"],
        'F': [" _____ ", "|  ___|", "| |_   ", "|  _|  ", "|_|    "],
        'G': ["  ____ ", " / ___|", "| |  _ ", "| |_| |", " \\____|"],
        'H': [" _   _ ", "| | | |", "| |_| |", "|  _  |", "|_| |_|"],
        'I': [" ___ ", "|_ _|", " | | ", " | | ", "|___|"],
        'J': ["     _ ", "    | |", " _  | |", "| |_| |", " \\___/ "],
        'K': [" _  __", "| |/ /", "| ' / ", "| . \\ ", "|_|\\_\\"],
        'L': [" _     ", "| |    ", "| |    ", "| |___ ", "|_____|"],
        'M': [" __  __ ", "|  \\/  |", "| |\\/| |", "| |  | |", "|_|  |_|"],
        'N': [" _   _ ", "| \\ | |", "|  \\| |", "| |\\  |", "|_| \\_|"],
        'O': ["  ___  ", " / _ \\ ", "| | | |", "| |_| |", " \\___/ "],
        'P': [" ____  ", "|  _ \\ ", "| |_) |", "|  __/ ", "|_|    "],
        'Q': ["  ___  ", " / _ \\ ", "| | | |", "| |_| |", " \\__\\_\\"],
        'R': [" ____  ", "|  _ \\ ", "| |_) |", "|  _ < ", "|_| \\_\\"],
        'S': [" ____  ", "/ ___| ", "\\___ \\ ", " ___) |", "|____/ "],
        'T': [" _____ ", "|_   _|", "  | |  ", "  | |  ", "  |_|  "],
        'U': [" _   _ ", "| | | |", "| | | |", "| |_| |", " \\___/ "],
        'V': ["__     __", "\\ \\   / /", " \\ \\ / / ", "  \\ V /  ", "   \\_/   "],
        'W': ["__        __", "\\ \\      / /", " \\ \\ /\\ / / ", "  \\ V  V /  ", "   \\_/\\_/   "],
        'X': ["__  __", "\\ \\/ /", " \\  / ", " /  \\ ", "/_/\\_\\"],
        'Y': ["__   __", "\\ \\ / /", " \\ V / ", "  | |  ", "  |_|  "],
        'Z': [" _____", "|__  /", "  / / ", " / /_ ", "/____|"],
    }
    
    # Convert text to uppercase
    text = text.upper()
    
    # Split text into individual characters
    chars = [char for char in text]
    
    # Generate ASCII art
    art_lines = [""] * 5
    for char in chars:
        if char in ascii_art_dict:
            for i in range(5):
                art_lines[i] += ascii_art_dict[char][i] + "  "
        else:
            for i in range(5):
                art_lines[i] += "     "  # Add spaces for unknown characters
    
    # Print ASCII art
    for line in art_lines:
        print(line)

# Example usage
text_to_ascii_art("HELLO WORLD")

