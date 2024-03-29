from __future__ import annotations

import logging
import os
import json

config_text = "hello world" 

index_text = {
 "user":{
    "email": "example@example.com",
    "name": "test user"
 },
 "assistant":{
    "name": "test assistant",
    "jobs": "test jobs",
    "description": "test description",
    "model": {
        "model name": "test model",
        "model id": "test model id",
        "parameters": {}
    },
    "memoryConfig":"algorithms memory",

 }
}

log = logging.getLogger(__name__)

def new(output_dir: str) -> None:
    asis_dir = os.path.join(output_dir, 'asis_')  # Carpeta principal "asis"
    assistant_dir = os.path.join(asis_dir, 'assistant')
    scripts_dir = os.path.join(assistant_dir, 'scripts')
    seeds_dir = os.path.join(asis_dir, 'seeds')  # Carpeta para las semillas
    
    config_path = os.path.join(asis_dir, 'index.py')
    seed_path = os.path.join(seeds_dir, 'public_seed.json')

    if os.path.exists(config_path):
        log.info('Project already exists.')
        return

    if not os.path.exists(output_dir):
        log.info(f'Creating project directory: {output_dir}')
        os.mkdir(output_dir)
        
    if not os.path.exists(asis_dir):
        log.info(f'Creating "asis" directory: {asis_dir}')
        os.mkdir(asis_dir)    
        
    if not os.path.exists(assistant_dir):  
        os.mkdir(assistant_dir)

    if not os.path.exists(scripts_dir):  
        os.mkdir(scripts_dir)

    log.info(f'Writing config file: {config_path}')
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(config_text)

    if os.path.exists(seed_path):
        return

    log.info(f'Writing initial seed: {seed_path}')
    if not os.path.exists(seeds_dir):
        os.mkdir(seeds_dir)
        
    with open(seed_path, 'w', encoding='utf-8') as f:
        json.dump(index_text, f)  # Convertir el diccionario a JSON antes de escribirlo

# basic config logging
logging.basicConfig(level=logging.INFO)

# example
new('./')

