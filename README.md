# Job Scraper

This is a Python script that scrapes job listings from a specific website, filters them by date and a skill that the user specifies, and saves the details of the jobs that do not require that skill to text files.

## How to Use

1. Clone this repository to your local machine.
2. Install the necessary modules by running the command `pip install -r requirements.txt` in your terminal.
3. Open `job_scraper.py` and specify the skill you don't have by entering it at the prompt.
4. Run the script by typing `python job_scraper.py` in your terminal.
5. The script will check for new job listings every 10 minutes and save the details of relevant jobs to text files in the `posts` directory.

## Dependencies

This script uses the following modules:
- BeautifulSoup
- requests

## Contributing

If you have any suggestions for how to improve this script, please feel free to submit a pull request!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
