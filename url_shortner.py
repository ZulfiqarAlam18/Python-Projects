import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, original_url, base_url="http://short.url/"):
        hash_object = hashlib.md5(original_url.encode())
        short_url = hash_object.hexdigest()[:6]  # Using the first 6 characters of the hash as the short URL
        self.url_map[short_url] = original_url
        return base_url + short_url

    def expand_url(self, short_url):
        short_url = short_url.split("/")[-1]  # Extracting the short code from the URL
        original_url = self.url_map.get(short_url)
        if original_url:
            return original_url
        else:
            return "URL not found."

def main():
    shortener = URLShortener()
    while True:
        print("\n1. Shorten URL\n2. Expand URL\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            original_url = input("Enter the URL to shorten: ")
            short_url = shortener.shorten_url(original_url)
            print("Shortened URL:", short_url)
        elif choice == '2':
            short_url = input("Enter the short URL to expand: ")
            original_url = shortener.expand_url(short_url)
            print("Expanded URL:", original_url)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
