# voila: voila --port=$PORT --no-browser --Voila.ip=0.0.0.0 --Voila.base_url=/dashboard dashboard.ipynb
web: gunicorn main:app
web: sh setup.sh && streamlit run dashboard.py --server.port $PORT --server.address 0.0.0.0