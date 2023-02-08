"""ecr-lifecycle command line.
Usage:
------
    $ ecr-lifecycle -r aws_region -n repository_name -a age -l debug_level -c (-c is destructive, delete images)
Available options are:
    ......TO DO
Contact:
--------
- https://github.com/austinobioma
Version:
--------
- ecr-lifecycle v0.0.1
"""

import boto3
import time
from args import parse_args
from ecr import ECR
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import as_completed
from ecr_lifecycle.logger import Logger


def main() -> None:
    """
        Start ecr-lifecycle client
    """
    start = time.perf_counter()
    args = parse_args()
    log = Logger(log_level=args.log_level)

    client = boto3.client('ecr', region_name=args.aws_region)
    images = client.describe_images(
        repositoryName=args.repository_name,
        maxResults=1000,
    )

    ecr = ECR(log_level=args.log_level)
    images_to_delete = ecr.get_images(images, args.age)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(
            ecr.delete_images, client, args.repository_name, args.delete, digest) for digest in images_to_delete]
        for future in as_completed(futures):
            if future.result() is not None:
                log.info(f"{future.result()}")

    finish = time.perf_counter()

    log.info(f"Finished in {round(finish - start, 2)} second(s).")


if __name__ == "__main__":
    main()
