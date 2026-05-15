# 1. Base image — official Python, slim variant (smaller size)
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy only dependency files first (speeds up rebuilds via layer cache)
COPY pyproject.toml .

# 4. Install pip build tools, then install your project dependencies
RUN pip install --upgrade pip && \
    pip install hatchling && \
    pip install .

# 5. Copy the rest of your application code
COPY . .

# 6. Expose the port FastAPI will run on
EXPOSE 8000

# 7. Start the app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]