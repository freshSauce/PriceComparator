<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />

  <h3 align="center">Price Comparator Bot</h3>

  <p align="center">
    Need to know the best price for your PC Parts? Use this bot!
    <br />
    <a href="https://github.com/freshSauce/PriceComparator"><strong>Give the project a star!</strong></a>
    <br />
    <br />
    <a href="https://t.me/PCPartsComparatorMX_bot">View Demo</a>
    ·
    <a href="https://github.com/freshSauce/PriceComparator/issues">Report Bug</a>
    ·
    <a href="https://github.com/freshSauce/PriceComparator/issues">Request Feature</a>
  </p>


<!-- ABOUT THE PROJECT -->
## About The Project

[![First message][product-screenshot]](https://t.me/PCPartsComparatorMX_bot)

I made this bot with the purpose of helping out the gamers to get the best prices for their PC's.
The bot is currently on a Beta phase as it still shows some errors that need to get fixed.

### Modules used

* [Flask](https://pypi.org/project/Flask/)
* [Requests](https://pypi.org/project/requests/)
* [BeatifulSoup4](https://pypi.org/project/beautifulsoup4/)



<!-- GETTING STARTED -->
## Getting Started

Let's get to it! 

### Bot Setup

#### Setting up the webhook

To setup te bot's webook you need where to launch the app (Flask) to receive the incoming updates via webhook.
If you already have your host make sure to set your bot's webhook to the host:

```
https://api.telegram.org/bot<YOUR_BOT_API_KEY>/setWebhook?url=<YOUR_URL>
```

#### Setting up our code

We need to make some changes in our code:

```python

TGLink = 'https://api.telegram.org/bot<YOUR_BOT_API_KEY>/sendMessage'

```
Replace <**YOUR_BOT_API_KEY**> with your bot's api key.



<!-- USAGE EXAMPLES -->
## Usage

To use the bot you only need to know two commands (both do the same):

```
/compare <item's_name> and !compare <item's_name>
```

<!-- CONTRIBUTING -->
## Contributing

Wanna contribute to the project? Great! Please follow the next steps in order to submit any feature or bug-fix :) You can also send me your ideas to my [Telegram](tg://user?id=560110547), any submit is **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Telegram: - [@freshSauce](tg://user?id=560110547)

Project Link: [https://github.com/freshSauce/PriceComparator](https://github.com/freshSauce/PriceComparator)







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/freshSauce/PriceComparator.svg?style=for-the-badge
[contributors-url]: https://github.com/freshSauce/PriceComparator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/freshSauce/PriceComparator.svg?style=for-the-badge
[forks-url]: https://github.com/freshSauce/PriceComparator/network/members
[stars-shield]: https://img.shields.io/github/stars/freshSauce/PriceComparator.svg?style=for-the-badge
[stars-url]: https://github.com/freshSauce/PriceComparator/stargazers
[issues-shield]: https://img.shields.io/github/issues/freshSauce/PriceComparator.svg?style=for-the-badge
[issues-url]: https://github.com/freshSauce/PriceComparator/issues
[license-shield]: https://img.shields.io/github/license/freshSauce/PriceComparator.svg?style=for-the-badge
[license-url]: https://github.com/freshSauce/PriceComparator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-@freshSauce-black?style=for-the-badge&logo=telegram&colorB=0af
[linkedin-url]: tg://user?id=560110547
[product-screenshot]: images/main.png
