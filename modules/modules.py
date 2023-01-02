def content():
    return '''
<h1 id="idparser-backend">idParser-Backend</h1>

<img src="https://raw.githubusercontent.com/putuwaw/idparser-frontend/main/public/logo192.png" width="150px;" alt="Logo IdParser"/><br>

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&amp;logo=python&amp;logoColor=blue" alt="Python">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&amp;logo=flask&amp;logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&amp;logo=vercel&amp;logoColor=white" alt="Vercel">
<img src="https://img.shields.io/github/forks/putuwaw/idparser-backend?style=for-the-badge" alt="Forks">
<img src="https://img.shields.io/github/contributors/putuwaw/idparser-backend?style=for-the-badge" alt="Contributors">
<img src="https://img.shields.io/github/stars/putuwaw/idparser-backend?style=for-the-badge" alt="Stars"></p>

<p>Backend Repository for "idParser", Web Based Indonesian Sentence Syntactic Parsing using CYK Algorithm with Table Filling Method.</p>
<p>Frontend: <a href="https://github.com/putuwaw/idparser-frontend">idparser-frontend</a></p>

<h2 id="features-">Features💡</h2>
<p>API Endpoint:</p>
<pre><code><span>POST:</span> /parser
</code></pre><p>Request:</p>
<pre><code>{
<span>"string"</span>: <span>""</span>
}
</code></pre><p>Response:</p>
<pre><code>{
<span>"result"</span>: <span>""</span>,
<span>"graph"</span>: <span>""</span>,
<span>"table"</span>: <span>""</span>,
}
</code></pre>

<h2 id="technology-">Technology 👨‍💻</h2>
<p>idParser-Backend is created using:</p>
<ul>
<li><a href="https://www.python.org/">Python</a> - Python as the main programming language.</li>
<li><a href="https://flask.palletsprojects.com/en/2.2.x/">Flask</a> - Flask is a web framework for Python, based on the Werkzeug toolkit.</li>
<li><a href="https://vercel.com/">Vercel</a> - Vercel is a cloud platform that we use to deploy our apps.</li>
</ul>

<h2 id="structure-">Structure 📂</h2>
<pre><code>idparser-backend
├── .github
├── docs
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
</code></pre>
<ul>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/.github/">.github</a> is a folder that used to place Github related stuff, like CI pipeline.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/docs/">docs</a> contain documentation of this app.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/handlers/">handlers</a> contain handler to handling HTTP request methods.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/modules/">modules</a> contain the main modules of the app.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/tests/">tests</a> contain unit test of the app.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/.gitignore">.gitignore</a> is a file to exclude some folders like venv.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/LICENSE">LICENSE</a> is a file that contains the license used in this app.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/README.md">README.md</a> is the file you are reading now.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/app.py">app.py</a> is the main file of this app.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/requirements.txt">requirements.txt</a> is a file that contains a list of dependencies used in this app.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/set_of_production.txt">set_of_production.txt</a> is a file that contains set of production of the grammar.</li>
<li><a href="https://github.com/putuwaw/idparser-backend/tree/main/vercel.json">vercel.json</a> is a file that contains configuration and override the default behavior of Vercel.</li>
</ul>

<h2 id="requirements-">Requirements 📦</h2>
<ul>
<li>Python 3.10 or later</li>
</ul>

<h2 id="installation-">Installation 🛠️</h2>
<ul>
<li>Clone the repository:<pre><code>git <span>clone</span> <span>https</span>://github.com/putuwaw/idparser-backend.git
</code></pre></li>
<li>Create a virtual environment:<pre><code><span>python -m venv venv</span>
</code></pre></li>
<li>Activate virtual environment:<pre><code><span>source</span> venv<span>/Scripts/</span>activate
</code></pre></li>
<li>Install dependencies:<pre><code>pip <span>install</span> -r requirements.txt
</code></pre></li>
<li>Run app:<pre><code><span>python</span> app.<span>py</span>
</code></pre></li>
<li>Run test:<pre><code><span>pytest</span>
</code></pre></li>
</ul>

<h2 id="contributors-">Contributors ✨</h2>
<p><br></p>
<table align="center">
<tr>
    <td align="center"><a href="https://github.com/putuwaw"><img src="https://avatars.githubusercontent.com/u/90038606?v=4" width="150px;" alt=""/><br><sub><b>Putu Widyantara</b></sub></td> 
    <td align="center"><a href="https://github.com/KEVINMOSESWALELENG"><img src="https://avatars.githubusercontent.com/u/103045275?v=4" width="150px;" alt=""/><br><sub><b>Kevin Moses</b></sub></td> 
    <td align="center"><a href="https://github.com/Antoniusata"><img src="https://avatars.githubusercontent.com/u/103051993?v=4" width="150px;" alt=""/><br><sub><b>Antonius Ata</b></sub></td>
    <td align="center"><a href="https://github.com/YogaLaksana"><img src="https://avatars.githubusercontent.com/u/103047470?v=4" width="150px;" alt=""/><br><sub><b>Yoga Laksana</b></sub></td>
</tr>
</table>
            '''
