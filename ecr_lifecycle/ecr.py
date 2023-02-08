from ecr_lifecycle.logger import Logger
from datetime import datetime, timedelta

images_to_delete = []


class ECR:
    def __init__(self, log_level) -> None:
        self.log = Logger(log_level)

    # def days_old(self, date) -> int:
    #     current_time = datetime.now().strftime('%Y/%m/%d')
    #     format_current_time = datetime.strptime(current_time, "%Y/%m/%d")
    #     print(format_current_time)
    #     print(date)
    #     delta = format_current_time - date
    #     return delta.days

    def get_images(self, images, age):
        for image in images['imageDetails']:
            image_digest = image['imageDigest']

            if self.get_image_days(image['imagePushedAt']) > age:
                images_to_delete.append(image_digest)
            else:
                self.log.debug(
                    f"{image_digest} will not be delete since is not older than {age} days ago")
        self.log.info(f"Images to delete: {len(images_to_delete)}")
        return images_to_delete

    @staticmethod
    def get_image_days(image_date):
        current_format_date = datetime.now().strftime('%Y/%m/%d')
        image_format_date = image_date.strftime('%Y/%m/%d')

        date_image_formatted = datetime.strptime(image_format_date, "%Y/%m/%d")
        current_date_formatted = datetime.strptime(current_format_date, "%Y/%m/%d")

        days_image_old = current_date_formatted - date_image_formatted

        return days_image_old.days

    def delete_images(self, client, repository_name, delete, digest):
        if not delete:
            self.log.info(f"Dry run: deleting {digest}")
            return

        try:
            self.log.info(f"Image {digest} deleted")
            client.batch_delete_image(
                repositoryName=repository_name,
                imageIds=[
                    {
                        'imageDigest': digest,
                    },
                ]
            )
        except Exception as e:
            self.log.warn(f"{e}")
