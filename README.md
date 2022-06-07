# ner-api

## Description
An experiment with Named-Entity Recognition in Python using the Flask and FuzzyWuzzy libraries. Flask serves as an API which expects fuzzy entity names, which are compared against a list of valid entity names using FuzzyWuzzy.

## Installation
```python
git clone https://github.com/foprel/ner-api.git
cd ner-api
```

## Usage
Set the server-side environment variables for the NER API.
```
SECRET_KEY=your_secret_key
USERNAME=your_username
PASSWORD=your_password
IP_RANGES=your_ip_ranges
```

Start the NER API server using Flask:
```python
flask run
```

Login the NER API client using bash. Be aware that the [jq](https://stedolan.github.io/jq/download/) library is required to parse the JSON response.
```bash
USERNAME=username \
PASSWORD=password \
LOGIN=$(echo -n "$USERNAME:$PASSWORD" | base64) \
TOKEN=$(curl -H "Authorization:Basic ${LOGIN}" "http://127.0.0.1:5000/login" | jq -r ".token") \
```

Request a named-entity match using bash. You will need to pass two HTTP headers. The first contains the JSON payload containing the requested named-entity. The second contains the Web Token obtained in the previous setp to authorize the request.
```bash
curl -X POST "http://127.0.0.1:5000/api/named-entity-recognizer/" \
-H "Content-Type: application/json" \
-d '{"account_name_client":"entity_name"}' \
-H "token: $TOKEN" \
```

## Acknowledgements
* [Flask](https://flask.palletsprojects.com/)
* [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/)
* [jq](https://stedolan.github.io/jq/download/)