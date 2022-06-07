# ner-api

## Description
An experiment with Named-Entity Recognition in Python using the Flask and FuzzyWuzzy libraries. Flask serves as an API which expects fuzzy entity names, which are compared against a list of valid entity names using FuzzyWuzzy.

## Installing
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

Login the NER API client using bash:

```bash
USERNAME=username \
PASSWORD=password \
LOGIN=$(echo -n "$USERNAME:$PASSWORD" | base64) \
TOKEN=$(curl -H "Authorization:Basic ${LOGIN}" "http://127.0.0.1:5000/login" | jq -r ".token") \
```
Be aware that the [jq](https://stedolan.github.io/jq/download/) library is required to parse the JSON response.

Request a named-entity match using bash.
```bash
curl -X POST "http://127.0.0.1:5000/api/named-entity-recognizer/" \
-H "Content-Type: application/json" \
-d '{"account_name_client":"entity_name"}' \
-H "token: $TOKEN" \
```
You need to pass two headers. The first contains the JSON payload consisting of the requested named-entity. The second consists of the Web Token to authorize the request.

## Acknowledgements
* [Flask](https://flask.palletsprojects.com/)
* [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/)
* [jq](https://stedolan.github.io/jq/download/)