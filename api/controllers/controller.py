import datetime
import logging
import yaml

from flask import request

from connexion import NoContent

# our memory-only pet storage
PETS = {}


ALLOWED_EXTENSIONS = set(['yml', 'yaml'])


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload(file=None) -> str:
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file provided.', 404
        file = request.files['file']
        if file.filename == '':
            return 'No selected file.', 404
        if file and allowed_file(file.filename):
            data = yaml.load(file)
            print(data['dogs']['name'])
            return file.filename


def get_pets(limit, animal_type=None):
    return [pet for pet in PETS.values()
            if not animal_type or pet['animal_type'] == animal_type][:limit]


def get_pet(pet_id):
    pet = PETS.get(pet_id)
    return pet or ('Not found', 404)


def put_pet(pet_id, pet):
    exists = pet_id in PETS
    pet['id'] = pet_id
    if exists:
        logging.info('Updating pet %s..', pet_id)
        PETS[pet_id].update(pet)
    else:
        logging.info('Creating pet %s..', pet_id)
        pet['created'] = datetime.datetime.utcnow()
        PETS[pet_id] = pet
    return NoContent, (200 if exists else 201)


def delete_pet(pet_id):
    if pet_id in PETS:
        logging.info('Deleting pet %s..', pet_id)
        del PETS[pet_id]
        return NoContent, 204
    else:
        return NoContent, 404
