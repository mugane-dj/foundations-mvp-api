# Online Complaint Registration and Management System (OCRM)
![Sign-up page](https://iili.io/HLS7IoB.png)
## Introduction
The project aims at helping with handling complaints from residents through incorporating a web application approach. The system's client interface was built using NextJS while the backend was built using Django Rest Framework. Here's the link to the [deployed site](https://complaints.davidmuia.com/) and the [blog article](https://mugane.hashnode.dev/a-breakdown-of-an-mvp-built-for-the-alx-se-programme-foundation) that goes deeper about the project.

### Authors
[Sally Nzungula](https://www.linkedin.com/in/sally-nzungula-295466236/)

[Samuel Mugane](https://www.linkedin.com/in/smugane25/)

## Installation
1. Clone repository
```
git clone https://github.com/mugane-dj/foundations-mvp-api.git
```
2. Navigate to server directory and install dependencies
```
cd core
pip3 install -r requirements.txt
```
3. Configure server environment variables
```
cp .env.example .env
```
4. Navigate to client directory and install client dependencies using npm or yarn
```
cd client
npm install
```
5. Configure client environment variables
```
cp .env.example .env
```
## Usage
To use the web app, follow these steps
1. Run the core server in development mode
```
python3 core/manage.py runserver
```
2. Run the client in development mode
```
cd client
npm run dev
```
This will start the development server and make the application accessible at http://localhost:3000.

3. Open your web browser and visit http://localhost:3000 to access the web application.

4. Explore the different features and functionalities of the application.

## Contributing
Interested in contributing to the ORCM project? Thanks so much for your interest! We are always looking for improvements to the project and contributions from open-source developers are greatly appreciated.

## Licensing
The ORCM web app is a free and open-source software licensed under the GNU General Public License v3.0.
