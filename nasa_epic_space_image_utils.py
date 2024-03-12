import argparse
from nasa_foto import fetch_nasa_images
from spacex import fetch_spacex_launch_photos
from epic_image import get_epic_images

def main():
    parser = argparse.ArgumentParser(description='Fetch space images')
    parser.add_argument('--nasa', help='Fetch NASA images', action='store_true')
    parser.add_argument('--spacex', help='Fetch SpaceX launch photos', type=str)
    parser.add_argument('--epic', help='Fetch EPIC images', action='store_true')
    parser.add_argument('--count', help='Number of images to fetch (for NASA and EPIC)', type=int, default=5)
    parser.add_argument('--api_key', help='NASA API key')

    args = parser.parse_args()

    if args.nasa:
        if args.api_key:
            fetch_nasa_images(args.api_key, args.count)
        else:
            print('Please provide the NASA API key using --api_key option.')

    if args.spacex:
        fetch_spacex_launch_photos(args.spacex)

    if args.epic:
        if args.api_key:
            get_epic_images(args.api_key, args.count)
        else:
            print('Please provide the NASA API key using --api_key option.')

if __name__ == "__main__":
    main()
