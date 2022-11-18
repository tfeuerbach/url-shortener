<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tfeuerbach/url_shortener">
    <img src="/ui/assets/images/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">URL Shortener API</h3>

  <p align="center">
    Python based url shortening service.
    <br />
    <a href="http://myshortened.link/docs"><strong>Explore the API here»</strong></a>
    <br />
    <br />
    <a href="https://github.com/tfeuerbach/url_shortener/issues">Report Bug</a>
    ·
    <a href="https://github.com/tfeuerbach/url_shortener/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Download and Use</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

URL Shortenening service built for a CLI tool.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Visit http://myshortened.link to view and test the API.

Command Line tool available at url_shortener/cli.

### Download and Use

1. Clone the repo
   ```sh
   git clone https://github.com/tfeuerbach/url_shortener.git
   ```
2. Install packages (requirements.txt)
   ```sh
   pip install -r requirements.txt
   ```
3. Use CLI tool to interact with the API
   ```sh
   cd cli/
   python clapi.py
   ```

To host your own, edit the config to point to 127.0.0.1:8000.

   ```sh
   uvicorn app.main:app --reload   
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Flexible URL Validation
- [ ] User-Friendly UI

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Thomas Feuerbach - [My LinkedIn](https://linkedin.com/in/tfeuerbach)

Project Link: [https://github.com/tfeuerbach/url_shortener](https://github.com/tfeuerbach/url_shortener)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Resources used for the creation of this application.

* [Real Python](https://realpython.com)
* [FastAPI](https://fastapi.tiangolo.com)
* [Gunicorn](https://gunicorn.org)
* [AWS](https://aws.amazon.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/tfeuerbach/url_shortener.svg?style=for-the-badge
[contributors-url]: https://github.com/tfeuerbach/url_shortener/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tfeuerbach/url_shortener.svg?style=for-the-badge
[forks-url]: https://github.com/tfeuerbach/url_shortener/network/members
[stars-shield]: https://img.shields.io/github/stars/tfeuerbach/url_shortener.svg?style=for-the-badge
[stars-url]: https://github.com/tfeuerbach/url_shortener/stargazers
[issues-shield]: https://img.shields.io/github/issues/tfeuerbach/url_shortener.svg?style=for-the-badge
[issues-url]: https://github.com/tfeuerbach/url_shortener/issues
[license-shield]: https://img.shields.io/github/license/tfeuerbach/url_shortener.svg?style=for-the-badge
[license-url]: https://github.com/tfeuerbach/url_shortener/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tfeuerbach
[Python]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
