# idParser-Backend

<img src="https://github.com/putuwaw/idparser-frontend/blob/main/public/logo192.png" width="150px;" alt="Logo IdParser"/>

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
![Forks](https://img.shields.io/github/forks/putuwaw/idparser-backend?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/putuwaw/idparser-backend?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/putuwaw/idparser-backend?style=for-the-badge)

Backend Repository for "idParser", Web Based Indonesian Sentence Syntactic Parsing using CYK Algorithm with Table Filling Method.

Frontend: [idparser-frontend](https://github.com/putuwaw/idparser-frontend)

## Features💡
API Endpoint:
```
POST: /parser
```
Request:
```
{
  "string": ""
}
```
Response:
```
{
  "result": "",
  "graph": "",
  "table": "",
}
```
## Technology 👨‍💻
idParser-Backend is created using:
- [Python](https://www.python.org/) - Python as the main programming language.
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Flask is a web framework for Python, based on the Werkzeug toolkit.
- [Vercel](https://vercel.com/) - Vercel is a cloud platform that we use to deploy our apps.

## Structure 📂
```
idparser-backend
├── .github
├── handlers
├── modules
├── tests
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── requirements.txt
├── set_of_production.txt
└── vercel.json
```
- [.github](.github/) is a folder that used to place Github related stuff, like CI pipeline.
- [handlers](handlers/) contain handler to handling HTTP request methods.
- [modules](modules/) contain the main modules of the app.
- [tests](tests/) contain unit test of the app.
- [.gitignore](.gitignore) is a file to exclude some folders like venv.
- [LICENSE](LICENSE) is a file that contains the license used in this app.
- [README.md](README.md) is the file you are reading now.
- [app.py](app.py) is the main file of this app.
- [requirements.txt](requirements.txt) is a file that contains a list of dependencies used in this app.
- [set_of_production.txt](set_of_production.txt) is a file that contains set of production of the grammar.
- [vercel.json](vercel.json) is a file that contains configuration and override the default behavior of Vercel.

## Installation 🛠️
- Clone the repository:
```
git clone https://github.com/putuwaw/idparser-backend.git
```
- Create a virtual environment:
```
python -m venv venv
```
- Activate virtual environment:
```
source venv/Scripts/activate
```
- Install dependencies:
```
pip install -r requirements.txt
```
- Run app:
```
python app.py
```
- Run test:
```
pytest
```
