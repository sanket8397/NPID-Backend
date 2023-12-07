<h1><img src = "Image/logoreadme.jpg">  NPID:National Police Incident Database  </h1>



Aim: A user-friendly web application that serves as a central hub for collecting, verifying, and visualizing data related to police-involved incidents across the United States. The app provides essential details such as location, involved parties, and descriptions. The app places a strong focus on data accuracy and validation, ensuring the reliability of the information. It also features an interactive mapping system, powerful data analysis tools, and transparency ratings for participating law enforcement agencies. NPID aims to promote transparency, accountability, and data-driven decision-making in law enforcement while providing valuable insights into policing practices.

Setup instructions:
- Download the backend zip folder from the master branch of this GitHub repository
- unzip the downloaded folder and open it in any editor like VS code
- Installing all the requirements using the command - pip install -r requirements.txt
- Running Flask server using command - python3 app.py --fuseki_url "http://localhost:3030/ds/query"