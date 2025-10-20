## HTTP/GRPC instance detection
### To run server
```
git clone https://github.com/mcnckc/efdl-week7.git
cd efdl-week7
docker compose up
```
### Tests
To run tests, in other terminal run `pytest tests.py`

### Demo request
run
```
curl -XPOST http://localhost:8080/predict -H "Content-Type: application/json" -d '{"url": "http://images.cocodataset.org/val2017/000000001268.jpg"}'
```
or from project directory
```
curl -XPOST http://localhost:8080/predict -H "Content-Type: application/json" -d @simple_request.json
```
