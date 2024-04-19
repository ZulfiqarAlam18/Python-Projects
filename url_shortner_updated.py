from urlshortener import Shortener

def main():
    shortener = Shortener('Tinyurl')
    while True:
        print("\n1. Shorten URL\n2. Expand URL\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            original_url = input("Enter the URL to shorten: ")
            short_url = shortener.short(original_url)
            print("Shortened URL:", short_url)
        elif choice == '2':
            short_url = input("Enter the short URL to expand: ")
            original_url = shortener.expand(short_url)
            print("Expanded URL:", original_url)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
