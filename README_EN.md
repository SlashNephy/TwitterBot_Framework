# PyChroner  
[![Python](https://img.shields.io/badge/Python-3.6-blue.svg?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT%20License-blue.svg?style=flat-square)]()

> Python + Chronus(Cron) = PyChroner  

Basic Concept: **You can build your own Bot in only little programming knowledge.**  
日本語版 Readmeは[こちら](https://github.com/NephyProject/TwitterBotFramework/blob/master/README.md)です。  

Info: **「TwitterBotFramework」 is renamed to 「PyChroner」.**
Currently **we're changing specifications and functions** actively, Before update please **check change point**.  
- [What's changed from TwitterBotFramework](https://github.com/NephyProject/PyChroner/wiki/changelog#v3)
- [Plugin migration guide from TwitterBotFramework](https://github.com/NephyProject/PyChroner/wiki/plugin_migration_fromTBFW)

## Features
### Easily
Even who not good at programming, you can build various Bot with using PyChroner.  
Currently we are supporting only Twitter as standard, but we planned support various services in future. Do not worry.  

### Usefully
PyChroner has logging feature. For this reason, you can easily check the load situation of plugin and the occurrence of an exception.  
And, there is API of dump the internal situation(e.g. Thread) as JSON.  
If you think found bug, attaching log at issue will help us.  

### As you want
You can add feature easily with using PyChroner's plugin system.  
To create plugin, please read 「[How to make plugin](https://github.com/NephyProject/PyChroner/wiki/plugin_getting_started)」in Wiki.  

### Many
PyChroner can load plugins as far as specs allow.  
Plugins are will run at each different thread, plugin will not interfere to other plugins.  

### Freely
This project published under MIT LICENSE, you can use freely while you follow the LICENSE.  
For example, fork this PyChroner and add the feature, you can publish on Github with same MIT LICENSE.  

---

## How to install (Redhat)
PyChroner will run on Python **3.6**+

### 1. Clone Repository
```bash
git clone https://github.com/NephyProject/PyChroner.git
```

### 2. Install the using libraries
```bash
cd PyChroner
sudo pip3 install watchdog psutil gevent flask timeout-decorator
```

### 3. Create `config.json`
Copy `sample.config.json` and edit it.
```bash
cp sample.config.json
```
#### configの内容
|Option name|Description|Needed?|Default value|
|:-----------:|:------------:|:-----------:|:------------:|
|services|Account authentication information of various services used in Bot.|Yes|-|
|logLevel|Setting of logging level.|Yes|info|
|slack|Various settings to notify Slack.|No|-|
|secret|Various informations to used in plugin.|No|-|

For setting various services account in `services`, please reference Wiki.  
- [Setting Twitter Account](https://github.com/NephyProject/PyChroner/wiki/config_services_twitter)  

### 4. Run
```bash
python3 main.py
```
In first time launch, it will create `plugins` directory. To run plugin, put plugin in to the directory.
When error occurs, it will dump datasets to file in `logs`, please reference that.

---

## Copyright and License 
Copyright © 2017 Nephy Project Team All Rights Reserved.  
This product released under [The MIT License](/LICENSE).  
