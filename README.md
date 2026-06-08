# Hello World Flask Application

A minimal Flask web application that responds with "Hello World" at the root endpoint.

## Running locally

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Testing

```bash
pip install pytest
pytest
```

## Docker

```bash
docker build -t hello-flask .
docker run -p 5000:5000 hello-flask
```
