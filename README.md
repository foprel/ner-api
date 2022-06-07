# ner-api

## Description
An experiment with Named-Entity Recognition in Python using the Flask and FuzzyWuzzy libraries. Flask serves as an API which expects fuzzy entity names, which are compared against a list of valid entity names using FuzzyWuzzy.

## Installing
```python
git clone https://github.com/foprel/ner-api.git
cd ner-api
```

## Usage
Set environment variables:
```
export SECRET_KEY=your_secret_key
export USER_NAME=your_user_name
export PASSWORD=your_password
export IP_RANGES=your_ip_ranges
```

Start NER-API:
```python
flask run
```

Login to NER-API :
```bash
USERNAME=<YOUR_USERNAME>
PASSWORD=<YOUR_PASSWORD>
LOGIN=$(echo "${USERNAME}:${PASSWORD}" | base64)

curl -H "Authorization:Basic ${LOGIN}"
```

Request entity match:
```bash
Xyz
```

## Acknowledgements
* [Flask](https://flask.palletsprojects.com/)
* [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/)