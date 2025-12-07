# NANNY CARE

## By solution makers

## Table of Content

+ [Description](#description)
+ [Requirements](#requirements)
+ [Installation](#installation)
+ [Running Project](#running-project)
+ [Running Tests](#running-tests)
+ [Technologies Used](#technologies-used)
+ [Licence](#licence)

## Description

An application where parents/guardians can easily get nannies to take care of their kids.

## Design

- This project is created following this figma mock design. <a href="https://www.figma.com/file/wWIOHgD2GFwMi85vZZPqyJ/Nanny-Care?node-id=0%3A1">Design</a>


[![nanny-care.png](https://i.postimg.cc/pL1SqTmG/nanny-care.png)](https://postimg.cc/gx840Gq8)

[![nanny-care2.png](https://i.postimg.cc/7hxXx8CJ/nanny-care2.png)](https://postimg.cc/ph6KZSJP)

## Requirements

A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

-Python version 3.8
    -Django
    -Pip
    -virtualenv

## Installation

Open Terminal {Ctrl+Alt+T} on ubuntu
git clone `https://github.com/John-Njau/Nanny-Care.git`
cd
code . or atom . based on prefered text editor

## Running Project

On terminal where you have opened the cloned project
`sudo pip3 install virtualenv`

To install virtual enviroment
 `virtualenv venv`

To create virtual enviroment
`source venv/bin/activate`

To activate virtual enviroment
`pip install -r requirements.txt`

To install requirements
Setup your database User, Password, Host, Port and Database Name.
`make makemigrations`

To create migrations
`make migrate`

To migrate database  
`make` - to start the server

## Running Tests

To run test for the project
`$ make test`

## Technologies Used

python3.8

django

HTML

css

Javascript

Cloudninary (for hosting images)

Heroku (for hosting the project)

## Licence

MIT License

Copyright (c) [2022] [Mary Atieno,John Njau,Abigael Wachira,Kate Vanili,Abdi Ali]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
Nanny-Care-development
├─ app
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ management
│  │  ├─ commands
│  │  │  ├─ populate_dummy.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_nanny_company.py
│  │  ├─ 0003_alter_company_image_alter_nanny_profile_pic_and_more.py
│  │  ├─ 0004_company_slug.py
│  │  ├─ 0005_booking.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ signals.py
│  ├─ static
│  │  ├─ css
│  │  │  └─ style.css
│  │  ├─ images
│  │  │  ├─ nannies1.jpg
│  │  │  ├─ nannies2.jpg
│  │  │  ├─ nannies3.jpg
│  │  │  ├─ nannies4.jpg
│  │  │  ├─ nannies5.jpg
│  │  │  ├─ nannies6.jpg
│  │  │  ├─ nannies7.jpg
│  │  │  ├─ social.png
│  │  │  └─ womkid.jpg
│  │  └─ js
│  │     └─ script.js
│  ├─ templates
│  │  ├─ base.html
│  │  ├─ book
│  │  │  └─ booking.html
│  │  ├─ companydetails
│  │  │  ├─ base.html
│  │  │  ├─ company_confirm_delete.html
│  │  │  ├─ company_confirm_delete_fragment.html
│  │  │  ├─ company_detail.html
│  │  │  ├─ company_form.html
│  │  │  ├─ company_form_fragment.html
│  │  │  └─ company_list.html
│  │  ├─ footer.html
│  │  ├─ gallery-section.html
│  │  ├─ gallery.html
│  │  ├─ home.html
│  │  ├─ index.html
│  │  ├─ nannydetails
│  │  │  ├─ base.html
│  │  │  ├─ nannydetails.html
│  │  │  └─ product-search.html
│  │  ├─ navbar.html
│  │  ├─ profile
│  │  │  └─ profile.html
│  │  └─ registration
│  │     ├─ base.html
│  │     ├─ login.html
│  │     └─ registration_form.html
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ images
│  ├─ Akan2.png
│  ├─ Akan2_zW1u2RC.png
│  ├─ baby.jpg
│  ├─ BIG_Idea1_2.webp
│  ├─ books.jfif
│  ├─ brownleather.webp
│  ├─ delivery1.png
│  ├─ IMG-20220212-WA0004.jpg
│  ├─ nannies1.jpg
│  ├─ nannies1_RwhLq5p.jpg
│  ├─ nannies1_TxE5XPd.jpg
│  ├─ nannies2.jpg
│  ├─ nannies3.jpg
│  ├─ tech.jpg
│  └─ womkid.jpg
├─ Makefile
├─ manage.py
├─ media
│  └─ profilepic
│     ├─ Akan_home.png
│     └─ girl-2961959__340.webp
├─ nanny_care
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ Procfile
├─ profilepic
│  ├─ Apple-Store-logo.webp
│  ├─ Bachelor-Party.png
│  ├─ Bachelor-Party_bVGAWIF.png
│  ├─ Diani.webp
│  ├─ eopard-animals.webp
│  ├─ eopard-animals_2zDLKvC.webp
│  ├─ eopard-animals_6ViWZrz.webp
│  ├─ fashion1.jpg
│  ├─ fashion2.jpg
│  ├─ girl-2961959__340.webp
│  ├─ girl-2961959__340_06Cd3PB.webp
│  ├─ girl-2961959__340_SL31PaB.webp
│  ├─ girl-2961959__340_t7KPbIa.webp
│  ├─ hiome.png
│  ├─ maria-lin-kim-8RaUEd8zD-U-unsplash.jpg
│  ├─ nanny4.jpg
│  ├─ nanny4_BpmMesP.jpg
│  └─ the_j_blog_black.png
├─ README.md
├─ requirements.txt
├─ runtime.txt
├─ static
│  ├─ app
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ forms.py
│  │  ├─ management
│  │  │  ├─ commands
│  │  │  │  ├─ populate_dummy.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_nanny_company.py
│  │  │  ├─ 0003_alter_company_image_alter_nanny_profile_pic_and_more.py
│  │  │  ├─ 0004_company_slug.py
│  │  │  ├─ 0005_booking.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ signals.py
│  │  ├─ static
│  │  │  ├─ css
│  │  │  │  └─ style.css
│  │  │  ├─ images
│  │  │  │  ├─ nannies1.jpg
│  │  │  │  ├─ nannies2.jpg
│  │  │  │  ├─ nannies3.jpg
│  │  │  │  ├─ nannies4.jpg
│  │  │  │  ├─ nannies5.jpg
│  │  │  │  ├─ nannies6.jpg
│  │  │  │  ├─ nannies7.jpg
│  │  │  │  ├─ social.png
│  │  │  │  └─ womkid.jpg
│  │  │  └─ js
│  │  │     └─ script.js
│  │  ├─ templates
│  │  │  ├─ base.html
│  │  │  ├─ book
│  │  │  │  └─ booking.html
│  │  │  ├─ companydetails
│  │  │  │  ├─ base.html
│  │  │  │  ├─ company_confirm_delete.html
│  │  │  │  ├─ company_confirm_delete_fragment.html
│  │  │  │  ├─ company_detail.html
│  │  │  │  ├─ company_form.html
│  │  │  │  ├─ company_form_fragment.html
│  │  │  │  └─ company_list.html
│  │  │  ├─ footer.html
│  │  │  ├─ gallery-section.html
│  │  │  ├─ gallery.html
│  │  │  ├─ home.html
│  │  │  ├─ index.html
│  │  │  ├─ nannydetails
│  │  │  │  ├─ base.html
│  │  │  │  ├─ nannydetails.html
│  │  │  │  └─ product-search.html
│  │  │  ├─ navbar.html
│  │  │  ├─ profile
│  │  │  │  └─ profile.html
│  │  │  └─ registration
│  │  │     ├─ base.html
│  │  │     ├─ login.html
│  │  │     └─ registration_form.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ css
│  │  ├─ home.css
│  │  ├─ index.css
│  │  ├─ nannydetails.css
│  │  ├─ style.css
│  │  └─ styles.css
│  ├─ images
│  │  ├─ Akan2.png
│  │  ├─ Akan2_zW1u2RC.png
│  │  ├─ baby.jpg
│  │  ├─ BIG_Idea1_2.webp
│  │  ├─ books.jfif
│  │  ├─ brownleather.webp
│  │  ├─ delivery1.png
│  │  ├─ IMG-20220212-WA0004.jpg
│  │  ├─ nannies1.jpg
│  │  ├─ nannies1_RwhLq5p.jpg
│  │  ├─ nannies1_TxE5XPd.jpg
│  │  ├─ nannies2.jpg
│  │  ├─ nannies3.jpg
│  │  ├─ tech.jpg
│  │  └─ womkid.jpg
│  ├─ img
│  │  ├─ nanny1.webp
│  │  ├─ nanny2.jpeg
│  │  ├─ nanny3.jpg
│  │  ├─ nanny4.jpg
│  │  └─ nc.jpg
│  ├─ js
│  │  ├─ app.js
│  │  └─ index.js
│  ├─ media
│  │  └─ profilepic
│  │     ├─ Akan_home.png
│  │     └─ girl-2961959__340.webp
│  ├─ nanny_care
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  ├─ wsgi.py
│  │  └─ __init__.py
│  └─ profilepic
│     ├─ Apple-Store-logo.webp
│     ├─ Bachelor-Party.png
│     ├─ Bachelor-Party_bVGAWIF.png
│     ├─ Diani.webp
│     ├─ eopard-animals.webp
│     ├─ eopard-animals_2zDLKvC.webp
│     ├─ eopard-animals_6ViWZrz.webp
│     ├─ fashion1.jpg
│     ├─ fashion2.jpg
│     ├─ girl-2961959__340.webp
│     ├─ girl-2961959__340_06Cd3PB.webp
│     ├─ girl-2961959__340_SL31PaB.webp
│     ├─ girl-2961959__340_t7KPbIa.webp
│     ├─ hiome.png
│     ├─ maria-lin-kim-8RaUEd8zD-U-unsplash.jpg
│     ├─ nanny4.jpg
│     ├─ nanny4_BpmMesP.jpg
│     └─ the_j_blog_black.png
└─ staticfiles

```

## Deploying to Render

This repository is ready to deploy to Render (https://render.com). Follow these steps:

1. Push your code to GitHub (if not already):

```bash
git add -A
git commit -m "Prepare for Render deployment"
git push origin main
```

2. Create a new Web Service on Render and connect your GitHub repo.

3. In the Render service settings set these Environment variables:

- `SECRET_KEY` — a secure random string (do NOT use the dev default in production)
- `MODE` — set to `prod`
- `DEBUG` — set to `False`
- `ALLOWED_HOSTS` — e.g. `your-app.onrender.com`
- `DATABASE_URL` — if you attach a managed Postgres instance or external DB
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` — if using Cloudinary

4. Build & Start commands (Render UI or `render.yaml`):

- Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- Start command: `gunicorn nanny_care.wsgi`

5. Add a managed Postgres database via Render (optional but recommended). When you attach a Postgres database, Render will set `DATABASE_URL` automatically.

6. Deploy and monitor the build logs. After deployment, visit the Render URL to verify the site.

Notes:

- This project uses `whitenoise` for static files in production and will run `collectstatic` during build.
- Ensure `SECRET_KEY` is kept secret and never committed.
- Remove any hard-coded secrets from source — this repo now reads Cloudinary values from env.

I also added a `render.yaml` template in the repo to help declare the service. You can edit it and push it, or configure the service via the Render dashboard.