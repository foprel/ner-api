# ner-api

## Description
An experiment with Named-Entity Recognition in Python using the Flask and FuzzyWuzzy libraries. Flask serves as an API which expects fuzzy entity names, which are compared against a list of valid entity names using FuzzyWuzzy.

## Installing
```python
git clone https://github.com/foprel/ner-api.git
cd ner-api
```

## Usage
Set NER-API environment variables:
```
SECRET_KEY=your_secret_key
USERNAME=your_username
PASSWORD=your_password
IP_RANGES=your_ip_ranges
```

Start NER-API:
```python
flask run
```

Login to NER-API :
```bash
USERNAME=frank \
PASSWORD=1234 \
LOGIN=$(echo -n "$USERNAME:$PASSWORD" | base64) \
TOKEN=$(curl -H "Authorization:Basic ${LOGIN}" "http://127.0.0.1:5000/login" | jq -r ".token") \
```

Request entity match:
```bash
curl -X POST "http://127.0.0.1:5000/api/named-entity-recognizer/" \
-H "Content-Type: application/json" \
-d '{"account_name_client":"entity_name"}' \
-H "token: $TOKEN" \
```

## Acknowledgements
* [Flask](https://flask.palletsprojects.com/)
* [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/)