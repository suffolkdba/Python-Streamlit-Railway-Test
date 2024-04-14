FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port for Streamlit
EXPOSE 8501

CMD [ "python", "./Home.py" ]