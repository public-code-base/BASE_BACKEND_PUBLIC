import __init__
import os
import json
import time
import base64
import settings.settings as settings
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from logs.logger import logs_dev, logs_sys

"""
Purpose: This files holds all of the read/write functionalities to file
"""

class JsonFunc:
    @staticmethod
    def get_json(payload_file_path):
        """
        Description: Opens the json file and grab the payload
        Purpose: Simply opens the json file
        Quick Links: test_get_json
        """
        try:
            if os.path.exists(payload_file_path):
                payload_file = open(payload_file_path, "r")
                data = payload_file.read()
                payload_file.close()
                return json.loads(data)
        except Exception as e:
            logs_sys.error(f"Unable to analyze the file {payload_file_path}. Error: {e}")
    
    @staticmethod
    def get_json_value(payload_file_path, path_of_payload, ignore_logs=False):
        """
        Description: It is meant to retrive the value of the json file at a specific path. The last
            key in the path is the value being retrieved.
        Purpose: A more consistent way of navigating through json files
        """
        value_retrieved = None
        # 1) Grab the payload from file
        main_payload = JsonFunc.get_json_without_io(payload_file_path)
        error_message = None
        # 2) Check if the path to payload is of string type
        if type(path_of_payload) == str:
            #3) Remove "/" from front and back (i.e. /1/2/3/4/ => 1/2/3/4, then list it => [1,2,3,4])
            path_of_payload = path_of_payload.lstrip("/").rstrip("/").split("/")
            #4) Create a pointer to the payload so we can make adjustments to main_payload
            data = main_payload
            #5) Loop through [1,2,3,4]
            for each_field in path_of_payload[:-1]:
                #6) Check if 1 is in the payload[each_field][each_field][...etc]
                if each_field in data:
                    #7) If it is, go one level deep so payload[each_field] => payload[each_field][each_field]
                    data = data[each_field]
                else:
                    error_message = f"Field '{each_field}' does not exists, please check the payload path again."
                    break
            if path_of_payload[-1] in data:
                value_retrieved = data[path_of_payload[-1]]
            else:
                error_message = f"Field '{path_of_payload[-1]}' does not exists, please check the payload path again."
        else:
            error_message = "The path_of_payload needs to be of type(str)"
        
        if error_message != None:
            if ignore_logs == False:
                logs_sys.error(error_message)

        return value_retrieved

    
    @staticmethod
    def update_json_file(payload_file_path, adjusted_payload):
        """
        Description: Updates json file. Takes in file path and the new payload
        Purpose: Seperate the opening and updating the json functions seperately for
            better modularity
        Quick Links: test_update_json_file, test_update_json_file_2
        """
        if os.path.isfile(payload_file_path):
            json_file = open(payload_file_path, "w+")
            
            try:
                json_file.write(json.dumps(adjusted_payload))
                return "success"
            except Exception as e:
                logs_sys.error(f"Unable to write update to file {payload_file_path}. Error: Invalid JSON format")
                
            json_file.close()
        else:
            logs_sys.error(f"Unable to analyze the file {payload_file_path}. Error: Unable to locate file")
        time.sleep(0.05)
        return None

    @staticmethod
    def write_json_file(file_path, data):
        if not isinstance(data, dict):
            logs_sys.error("Error: Invalid input. Data must be of type 'dict'.")
            return None

        if os.path.exists(file_path):
            logs_sys.error(f"Error: File {file_path} already exists. Please use the 'update_json_file' function to update the file.")
        else:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            logs_sys.info(f"Successfully created file {file_path}")
    
    @staticmethod
    def delete_json_file(file_path):
        if os.path.exists(file_path):
            file_extension = os.path.splitext(file_path)[1]
            if file_extension.lower() == '.json':
                os.remove(file_path)
                logs_sys.info(f"Successfully deleted file {file_path}")
            else:
                logs_sys.error(f"Error: {file_path} is not a JSON file.")
        else:
            logs_sys.error(f"Error: {file_path} not found.")

    @staticmethod
    def update_json_file_with_specific_fields(payload_file_path, path_of_payload, adjusted_value_or_payload):
        """
        Description: The JSON File already exists. The structure already exists.
        Purpose: The purpose of this is writing to specific path under and already existing json
        Example: update_json_file_with_specific_fields("./abc/abc.json, payload['exchange']['money'], adjusted_payload)
            So in this example, the adjusted payload will be stored under exchange>money.
            For the 'exchange/money/" it does not matter if you put a slash in the front or back. It will strip it away.
        Future: Will Add (Append to List)
        Quick Links: test_update_json_file_with_specific_fields
        """
        return_message = "failed"
        # 1) Grab the payload from file
        main_payload = JsonFunc.get_json_without_io(payload_file_path)
        error_message = None
        # 2) Check if the path to payload is of string type
        if type(path_of_payload) == str:
            #3) Remove "/" from front and back (i.e. /1/2/3/4/ => 1/2/3/4, then list it => [1,2,3,4])
            path_of_payload = path_of_payload.lstrip("/").rstrip("/").split("/")
            #4) Create a pointer to the payload so we can make adjustments to main_payload
            data = main_payload
            #5) Loop through [1,2,3,4]
            for each_field in path_of_payload[:-1]:
                #6) Check if 1 is in the payload[each_field][each_field][...etc]
                if each_field in data:
                    #7) If it is, go one level deep so payload[each_field] => payload[each_field][each_field]
                    data = data[each_field]
                else:
                    error_message = f"Field '{each_field}' does not exists, please check the payload path again."
                    break
            #8) Assign the new value to the last level. (i.e. payload[1][2][3][4] = 28)
            data[path_of_payload[-1]] = adjusted_value_or_payload
            
        else:
            error_message = "The path_of_payload needs to be of type(str)"
        
        if error_message != None:
            logs_sys.error(error_message)
        else:
            #9) Grab the entire payload and write it to json
            JsonFunc.update_json_file_without_io(payload_file_path,main_payload)
            return_message = "success"
        
        time.sleep(0.05)
        return return_message
    
    @staticmethod
    def get_json_without_io(payload_file_path):
        """
        Description: Opens the json file and grab the payload
        Purpose: Simply opens the json file
        Quick Links: test_get_json
        """
        try:
            if os.path.exists(payload_file_path):
                payload_file = open(payload_file_path, "r")
                data = payload_file.read()
                payload_file.close()
                return json.loads(data)
        except Exception as e:
            logs_sys.error(f"Unable to analyze the file {payload_file_path}. Error: {e}")
    

        
    
    @staticmethod
    def update_json_file_without_io(payload_file_path, adjusted_payload):
        """
        Description: Updates json file. Takes in file path and the new payload
        Purpose: Seperate the opening and updating the json functions seperately for
            better modularity
        Quick Links: test_update_json_file, test_update_json_file_2
        """
        if os.path.isfile(payload_file_path):
            json_file = open(payload_file_path, "w+")
            
            try:
                json_file.write(json.dumps(adjusted_payload))
                return "success"
            except Exception as e:
                logs_sys.error(f"Unable to write update to file {payload_file_path}. Error: Invalid JSON format")
                
            json_file.close()
        else:
            logs_sys.error(f"Unable to analyze the file {payload_file_path}. Error: Unable to locate file")
        return None

    @staticmethod
    def by_payload_get_json_value(payload, path_of_payload, ignore_logs=False):
        value_retrieved = None
        error_message = None
        # 2) Check if the path to payload is of string type
        if type(path_of_payload) == str:
            #3) Remove "/" from front and back (i.e. /1/2/3/4/ => 1/2/3/4, then list it => [1,2,3,4])
            path_of_payload = path_of_payload.lstrip("/").rstrip("/").split("/")
            #4) Create a pointer to the payload so we can make adjustments to main_payload
            data = payload
            #5) Loop through [1,2,3,4]
            for each_field in path_of_payload[:-1]:
                #6) Check if 1 is in the payload[each_field][each_field][...etc]
                if each_field in data:
                    #7) If it is, go one level deep so payload[each_field] => payload[each_field][each_field]
                    data = data[each_field]
                else:
                    error_message = f"Field '{each_field}' does not exists, please check the payload path again."
                    break
            if path_of_payload[-1] in data:
                value_retrieved = data[path_of_payload[-1]]
            else:
                error_message = f"Field '{path_of_payload[-1]}' does not exists, please check the payload path again."
        else:
            error_message = "The path_of_payload needs to be of type(str)"
        
        if error_message != None:
            if ignore_logs == False:
                logs_sys.error(error_message)

        return value_retrieved


    @staticmethod
    def by_payload_update_json_with_specific_fields(payload, path_of_payload, adjusted_value_or_payload):
        """
        Description: The JSON File already exists. The structure already exists.
        Purpose: The purpose of this is writing to specific path under and already existing json
        Example: update_json_file_with_specific_fields("./abc/abc.json, payload['exchange']['money'], adjusted_payload)
            So in this example, the adjusted payload will be stored under exchange>money.
            For the 'exchange/money/" it does not matter if you put a slash in the front or back. It will strip it away.
        Future: Will Add (Append to List)
        Quick Links: test_update_json_file_with_specific_fields
        """
        # 1) Grab the payload from file
        error_message = None
        # 2) Check if the path to payload is of string type
        if type(path_of_payload) == str:
            #3) Remove "/" from front and back (i.e. /1/2/3/4/ => 1/2/3/4, then list it => [1,2,3,4])
            path_of_payload = path_of_payload.lstrip("/").rstrip("/").split("/")
            #4) Create a pointer to the payload so we can make adjustments to main_payload
            data = payload
            #5) Loop through [1,2,3,4]
            for each_field in path_of_payload[:-1]:
                #6) Check if 1 is in the payload[each_field][each_field][...etc]
                if each_field in data:
                    #7) If it is, go one level deep so payload[each_field] => payload[each_field][each_field]
                    data = data[each_field]
                else:
                    error_message = f"Field '{each_field}' does not exists, please check the payload path again."
                    break
            #8) Assign the new value to the last level. (i.e. payload[1][2][3][4] = 28)
            data[path_of_payload[-1]] = adjusted_value_or_payload
            
        else:
            error_message = "The path_of_payload needs to be of type(str)"
        
        if error_message != None:
            logs_sys.error(error_message)
        
        return payload
    
    @staticmethod
    def encrypt_json(json_data, AES_KEY=None):
        """
        This function takes a python dictionary as input and returns a base64 encoded string 
        which is the encrypted JSON data. It loads the AES key from the file specified 
        in settings.AES_KEY_FILE.
        """

        # Load the AES key
        key = base64.b64decode(settings.AES_KEY)
        if AES_KEY is not None: key = base64.b64decode(AES_KEY)

        # Convert the data into a JSON string
        data_str = json.dumps(json_data).encode()

        # Create a random IV
        iv = get_random_bytes(AES.block_size)

        # Create a cipher object using the random IV
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

        # Pad the input data and then encrypt it
        encrypted = cipher.encrypt(pad(data_str, AES.block_size))

        # Concatenate the IV and the encrypted data
        encrypted_iv_and_data = base64.b64encode(iv + encrypted).decode()
        
        return encrypted_iv_and_data

    @staticmethod
    def decrypt_json(encrypted_json_string, AES_KEY=None):
        """
        This function takes a base64 encoded encrypted string as input and returns a Python dictionary.
        It loads the AES key from the file specified in settings.AES_KEY_FILE for decryption.
        """
        # Load the AES key
        key = base64.b64decode(settings.AES_KEY)
        if AES_KEY is not None: key = base64.b64decode(AES_KEY)
            
        # Convert the encrypted data from a base64 encoded string
        encrypted_iv_and_data = base64.b64decode(encrypted_json_string)

        # Extract the IV from the beginning of the encrypted data
        iv = encrypted_iv_and_data[:AES.block_size]
        encrypted = encrypted_iv_and_data[AES.block_size:]
        
        # Create a cipher object using the IV
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

        # Decrypt the data
        original_message = unpad(cipher.decrypt(encrypted), AES.block_size)

        # Convert the data back into a Python dictionary
        json_data = json.loads(original_message.decode())

        return json_data