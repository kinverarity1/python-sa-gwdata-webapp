# python-sa-gwdata-webapp

Web app interface to the Python package [python-sa-gwdata](https://github.com/kinverarity1/python-sa-gwdata) for groundwater data in South Australia.

Very much just a concept at this stage FYI.

## Usage

```
pip install -r requirements.txt
uvicorn app:app --reload --log-config log-config.yaml --host 0.0.0.0 --port 8080
```

## Example deployment

[http://ec2-13-238-11-223.ap-southeast-2.compute.amazonaws.com/app/well/253378](http://ec2-13-238-11-223.ap-southeast-2.compute.amazonaws.com/app/well/253378)

HTTPS does not work. Loading this on my phone auto-selects HTTPS on the above link incorrectly, so you might need to edit the URL manually.
