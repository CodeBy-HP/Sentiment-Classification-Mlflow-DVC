FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for better caching
COPY fastapi_app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader stopwords wordnet

# Copy application code
COPY fastapi_app/ /app/
COPY models/vectorizer.pkl /app/models/vectorizer.pkl

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Health check using urllib (built-in)
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]