import boto3
from typing import List
from django.conf import settings
from extensions.utils import create_random_code


# todo: complete the bucket name
class Bucket:
    """ CDN bucket manager

    init method creates connection.
    """

    def __init__(self):
        my_session = boto3.session.Session()
        self.conn = my_session.client(
            service_name=settings.AWS_SERVICE_NAME,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )

    def get_object_url(self, key: str, expiration=3600) -> str:
        """Get URL to share an S3 object
            :param key: string
            :param expiration: Time in seconds for the URL to remain valid
            :return: URL as string.
            """
        url = self.conn.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                'Key': key
            },
            ExpiresIn=expiration
        )
        return url

    def put_object(self, file, category: str) -> str:
        """Adds an object to an S3 bucket
        :param file: File to upload
        :param category: Category of file to upload
        """
        random_str = create_random_code(10)
        key = f"{category}/" + file.name
        li = key.split('.')
        li[0] += random_str
        key = '.'.join(li)
        self.conn.put_object(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME,
            Key=key,
            Body=file
        )
        return self.get_object_url(key)

    def delete_objects(self, keys: List) -> None:
        """Delete multiple objects from an S3 bucket
        :param keys: List
        """
        self.conn.delete_objects(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME,
            Delete={
                'Objects': [
                    {'Key': key} for key in keys
                ]
            }
        )


bucket = Bucket()
