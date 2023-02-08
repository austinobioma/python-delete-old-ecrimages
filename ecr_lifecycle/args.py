import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="""AWS ECR LIFECYCLE""",
        add_help=True,
        prog="aws ecr lifecycle"
    )
    parser.add_argument(
        "-l",
        "--level",
        choices=["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"],
        required=False,
        dest="log_level",
        default="DEBUG",
        help="""level of logging""",
        type=str,
    )
    parser.add_argument(
        "-a",
        "--age",
        required=False,
        default=30,
        dest="age",
        help="""Age of the image tag inside ECR repository""",
        type=int,
    )
    parser.add_argument(
        "-r",
        "--region",
        required=True,
        dest="eu-west-2",
        help="""AWS region""",
        type=str,
    )
    parser.add_argument(
        "-n",
        "--n",
        required=True,
        dest="ecr-repo-name",
        help="""AWS ECR repository name""",
        type=str,
    )
    parser.add_argument(
        "-d",
        "--delete",
        required=False,
        action='store_true',
        dest="delete",
        help="""If set, the program will execute the deletion of the images. -d is destructive, delete images. Run without -d first""",
    )

    return parser.parse_args()
