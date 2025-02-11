# San Valentino Project

Un'applicazione web per calcolare i giorni trascorsi da una data specifica.

## Struttura del Progetto 


SAN_VALENTINO/
├── fe/ # Frontend directory
│ ├── frontend/ # React application
│ │ ├── node_modules/
│ │ ├── public/
│ │ ├── src/
│ │ ├── package.json
│ │ └── package-lock.json
│ └── README.md
│
└── san_valentino/ # Backend directory

├── san_valentino/ # Django project settings
│ ├── pycache/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── webapp/ # Django application
│ ├── pycache/
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── db.sqlite3
└── manage.py



## Funzionalità Attuali

### Backend (Django)
- API endpoint per calcolare i giorni trascorsi da una data specifica
- Endpoint: `/calculate-days/`
- Metodo: POST
- Payload esempio:


json
{
"date": "2024-02-14",
"description": "San Valentino"
}


### Frontend (React)
- In fase di sviluppo

## Tecnologie Utilizzate

### Backend
- Django 5.0
- Python 3.11+
- SQLite3
- Django REST Framework

### Frontend
- React 18
- Node.js 20+
- npm 10+

## Prerequisiti
- Python 3.11 o superiore
- Node.js 20 o superiore
- npm 10 o superiore

## Installazione

### Backend
1. Clona il repository

bash
git clone <repository-url>
cd san_valentino

2. Crea un ambiente virtuale

bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

3. Installa le dipendenze

bash
pip install -r requirements.txt


4. Esegui le migrazioni

bash
python manage.py migrate


### Frontend
1. Naviga nella directory frontend

bash
cd fe/frontend

2. Installa le dipendenze

bash
npm install     

## Come Avviare il Progetto

### Backend
bash
cd san_valentino
python manage.py runserver

### Frontend
bash
cd fe/frontend
npm start


Il server backend sarà disponibile su `http://localhost:8000`
Il frontend sarà disponibile su `http://localhost:3000`

## API Endpoints

### Calcolo Giorni
- **URL**: `/calculate-days/`
- **Metodo**: POST
- **Headers**:
  - Content-Type: application/json
- **Payload**:
  ```json
  {
      "date": "YYYY-MM-DD",
      "description": "Descrizione opzionale"
  }
  ```
- **Risposta di Successo**:
  ```json
  {
      "days_passed": 42,
      "start_date": "2024-02-14",
      "description": "San Valentino"
  }
  ```
- **Codici di Risposta**:
  - 200: Successo
  - 400: Errore nei dati inviati
  - 405: Metodo non permesso

## Testing
### Backend
bash
python manage.py test webapp


### Frontend
bash
cd fe/frontend
npm test



## Contribuire
1. Fai il fork del repository
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Committa i tuoi cambiamenti (`git commit -m 'Add some AmazingFeature'`)
4. Pusha al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## Licenza
Questo progetto è sotto licenza MIT - vedi il file LICENSE.md per i dettagli

## Autori
- Nome Autore - [GitHub Profile]()

## Riconoscimenti
- Django Documentation
- React Documentation
- Altri riconoscimenti...