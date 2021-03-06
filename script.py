from modules.scraper import scrape
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--places', 
    type=str, 
    required=True, 
    help="List of places near which you want to make a search")
    
    parser.add_argument('--query', 
    type=str, 
    required=True,
    help="Beginning of the search query. Places will be appended to this query")

    parser.add_argument('--pages',
    type=int,
    required=False,
    help="Number of pages of results to scrape on each query")

    parser.add_argument('--scrape-website', 
    action="store_true",
    required=False,
    help="The scraper will work way slower if it scrapes websites too. This flag is here so the websites are optional")

    parser.add_argument('--skip-duplicate-addresses',
    action="store_true",
    required=False,
    help="Flag that indicates whether to skip results that have matching addresses")

    args = parser.parse_args()
    scrape(args)


