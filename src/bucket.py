# import boto3
# from django.conf import settings
#
#
# # todo: complete the bucket name
# class Bucket:
#     """ CDN bucket manager
#
#     init method creates connection.
#     """
#
#     def __init__(self):
#         self.s3_resource = boto3.client(
#             settings.AWS_SERVICE_NAME,
#             endpoint_url=settings.AWS_S3_ENDPOINT_URL,
#             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
#         )
#
#     def get_objects(self):
#         response = self.s3_resource.head_bucket(Bucket="iranable-storages")
#         return response
#
#
# bucket = Bucket()
