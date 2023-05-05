import sys
from minio import Minio
from minio.error import S3Error

def preprocess():
    from src.src import sharpening_image, cv2
    image = cv2.imread("ip.jpg")
    img = sharpening_image(image)
    cv2.imwrite("op.jpg", img) 
    
if __name__ == '__main__':
    
    client = Minio(
        # "play.min.io",
        "127.0.0.1:9000",
        secure=False,
        access_key = 'EitPADwoAUvkzhs6',
        secret_key = 'g82ahUIxSAhtIJeCoLWTV1YrONFpjTop'
    )

    image_url = sys.argv[1]
    # print(image_url)
    client.fget_object(
        "uploads", image_url, "ip.jpg",
    )

    new_img=sys.argv[2]
    preprocess()

    client.fput_object(
        "uploads", new_img, "op.jpg",
    )
