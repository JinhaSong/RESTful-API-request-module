import argparse
import os

import Logging
from Request import send_request, save_result2json


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RESTful-API Request Module')
    parser.add_argument("--url", dest='url', help='URL of module', type=str, required=True)
    parser.add_argument("--video_path", dest='video_path', help='request path to send as request', type=str)
    parser.add_argument("--json_path", dest='json_path', help='resul jsont path to save', type=str)
    args = parser.parse_known_args()[0]

    url = str(args.url)
    video_path = str(args.video_path)
    json_path = str(args.json_path)

    try :
        print(Logging.i("start request(video path: {})".format(video_path)))
        result = send_request(video_path, module_url=url)
        print(Logging.i("end request(video path: {})".format(video_path)))

        ret = save_result2json(result, result_path=json_path)
        if ret :
            print(Logging.i("it is successfully save result json file(json path: {})".format(json_path)))
        else :
            print(Logging.e("it is failed to save result json file(json path: {})".format(json_path)))
    except :
        print(Logging.e("RESTful API request is failed(video path: {})".format(video_path)))
