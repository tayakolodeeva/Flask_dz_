import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-url")
    return parser


urls = [
    "https://i.7fon.org/1000/e13116481.jpg",
    "https://i.7fon.org/320/e13198335.jpg",
    "https://i.7fon.org/320/e12856667.jpg",
    "https://samplelib.com/lib/preview/jpeg/sample-clouds-400x300.jpg",
    "https://samplelib.com/lib/preview/jpeg/sample-red-400x300.jpg",
    "https://samplelib.com/lib/preview/jpeg/sample-birch-400x300.jpg"
]

if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    urls.append(namespace.url)