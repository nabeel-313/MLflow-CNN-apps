#Update this to download the data and unzip
#Step are given in CCN_example.ipynb file
import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
import random


STAGE = "get data" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path, params_path):
    ## read config files
    config = read_yaml(config_path)
    URL = config["data"]["source_data_url"]
    local_dir = config["data"]["local_dir"] #data
    create_directories([local_dir])
    
    data_file = config["data"]["data_file"] #data.zip
    
    data_file = config["data"]["data_file"]
    data_file_path = os.path.join(local_dir, data_file)
    logging.info("Downloading started")
    
    if os.path.isfile(data_file_path):
        #filename, headers = req.urlretrieve(URL, data_file_path)
        logging.info(f"filename: create with info: ")
    else:
        logging.info(f"filename: create with info: already presnet")
    
    params = read_yaml(params_path)
    pass


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e