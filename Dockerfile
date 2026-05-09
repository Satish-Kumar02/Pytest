FROM python:3.12-slim

# Install dependencies
RUN set -e && \
    apt-get update && \
    apt-get install -y wget curl unzip default-jre gnupg && \
    rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN set -e && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN set -e && \
    CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1) && \
    DRIVER_VERSION=$(curl -sSL "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_$CHROME_VERSION" | head -1) && \
    [ -n "$DRIVER_VERSION" ] || exit 1 && \
    wget -q -O /tmp/chromedriver.zip "https://storage.googleapis.com/chrome-for-testing-public/$DRIVER_VERSION/linux64/chromedriver-linux64.zip" && \
    unzip -q /tmp/chromedriver.zip -d /opt && \
    cp /opt/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip /opt/chromedriver-linux64

# Install Allure
RUN set -e && \
    wget -q https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.0/allure-commandline-2.24.0.tgz && \
    tar -zxf allure-commandline-2.24.0.tgz && \
    mv allure-2.24.0 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure && \
    rm allure-commandline-2.24.0.tgz

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["pytest", "-n", "4", "--alluredir=allure-results"]