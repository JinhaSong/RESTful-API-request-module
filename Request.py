import requests
import json

def send_request(video_path, module_url, extract_fps=1):
    json_video = open(video_path, 'rb')
    json_files = {'video': json_video}

    json_data = dict({
        'analysis_type': 'video',
        'video_text': '',
        'extract_fps': extract_fps
    })
    result_response = requests.post(url=module_url, data=json_data, files=json_files)
    result = json.loads(result_response.content)

    json_video.close()

    return result

def save_result2json(result, result_path):
    try :
        with open(result_path, 'w') as result_file:
            json.dump(result, result_file, indent='\t')
        return True
    except:
        return False