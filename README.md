# Django Major Project

This is my major project built using Django + PostgreSQL.

#Project Overview
A Django-based system to verify authentic products using blockchain technology. Each product is registered on the blockchain, making its authenticity record tamper‑proof.


#Architecture (Simple)
Django Backend ↔ Web3.py ↔ Blockchain
Consumer (QR Scan) → Verification API → Authentic / Fake


## How to run
```bash
git clone <repo>
cd project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

