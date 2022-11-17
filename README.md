# README

## Build Docker

```console
docker build -t mac_address . 
```

## Run Docker Image
```console
docker run mac_address {api_key} {mac_address}
```
for example: `docker run mac_address jo23h4o2h34jkjhfksjk3j 44:38:39:ff:ef:57`

## Security
One of the most vulnerable in accessing public API is the API key. In the production environment, normally I would save the API Key on AWS Secret Manager or GitHub instead of passing it as a parameter