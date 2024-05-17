import argparse
import requests
import json

def fetch_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching JSON data:", e)
        return None

def format_json(json_data, start=None, end=None):
    if json_data is not None:
        if start is None and end is None:
            formatted_json = json.dumps(json_data, indent=4)
        else:
            formatted_json = json.dumps(json_data[start:end], indent=4)
        print(formatted_json)

def main():
    parser = argparse.ArgumentParser(description="Fetch and format JSON data from a URL")
    parser.add_argument("-u", "--url", help="URL containing JSON data", required=True)
    args = parser.parse_args()

    # Fetch JSON data from the provided URL
    json_data = fetch_json_data(args.url)

    # Print the length of the full JSON data
    if json_data is not None:
        print("Length of full JSON data:", len(json_data))

        # Prompt the user for a range of lines
        

        # Ask if the user wants to print all lines
        choice = input("Do you want to print all lines? (Y/N): ").lower()
        if choice in ['n', 'no']:
            start = int(input("Enter the start index of the range (0-indexed): "))
            end = int(input("Enter the end index of the range (0-indexed): "))
            format_json(json_data, start, end)
        elif choice in ['y', 'yes']:
            format_json(json_data)
        else:
            print("Invalid choice. Please enter Y or N.")

if __name__ == "__main__":
    main()
