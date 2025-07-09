FROM python:alpine3.22

WORKDIR /app

# Use apk for package management on Alpine Linux
RUN apk update && rm -rf /var/cache/apk/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

# Install the 'shadow' package which provides 'adduser', then create the user
RUN apk add --no-cache shadow && \
    adduser -D -h /home/app app && \
    chown -R app:app /app

EXPOSE 8000

USER app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]