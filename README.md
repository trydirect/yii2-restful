[![Build Status](https://travis-ci.com/trydirect/yii2-restful.svg?branch=master)](https://travis-ci.com/trydirect/yii2-restful)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/yii2-restful.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/yii2-restful.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/yii2-restful.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/yii2-restful.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/try-direct/community)
# Yii 2 Restful API template for developers
This repo helps Yii2 developers to start their new projects quickly using docker-compose.

**Stack includes**: 
 * PHP-fpm 7.2 (on Ubuntu 18.04 docker image)
   * Yii2 v2.0.20
   * Xdebug 2.6.1 
   * Supervisord
 * MySQL 5.7
 * Nginx
 * Apidoc
 

## Installation
Clone project into your work directory:
```sh
$ git clone https://github.com/trydirect/yii2-restful.git
```
Bring up docker services:
```sh
$ cd yii2-restful
$ docker-compose up -d
```

## Let's check the deployment result in browser
 
| **Url** | **App** |
| --- | --- |
| http://localhost       | Yii2 apidoc page       |
| http://localhost/api/v1/hello | "Hello" endpoint |
| http://localhost:5601  | Kibana                  |
| http://localhost:9200  | Elasticsearch           |


## Run Tests

```
$ python tests.py 
```

## Todo 
Next, to implement
* Redis as cache engine

Logging

* Elasticsearch 5.4.3
* Kibana 5.4.3
* Logstash 5.4.0 

Security
 * Integrate Hashicorp Consul (configs)
 * Integrate Hashicorp Vault (credentials)

## Links
- https://www.yiiframework.com/doc/guide/2.0/en/rest-quick-start
- https://github.com/yiisoft/yii2-apidoc


## Contributing


1. Fork it (<https://github.com/trydirect/yii2-restful/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


## Support Development

Send your PR's, ideas or 

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2BH8ED2AUU2RL) 
