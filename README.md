## About The Project
My configurations for running apache airflow and a Carte server locally with docker compose

### Built With
* Docker
* Bash
* Python

## Getting Started

### Prerequisites
* Docker
```sh
sudo apt get docker
```
### Installation

1. Clone the repo
  ```sh
  git clone https://github.com/brianamaral/airflow_pdi_composer.git
  ```
2. Edit the config.xml located at /configs as you like 
  ```xml
<slave_config>
    <slaveserver>
        <name>Master</name>
        <hostname>0.0.0.0</hostname>
        <port>8080</port>
        <username>cluster</username>
        <password>cluster</password>
        <master>Y</master>
    </slaveserver>
</slave_config>
  ```
3. Optionally, you can put some jobs in the /jobs folder and build a volume pointing from there

### Usage
1. Run the command below
```sh
docker-compose up
```
2. Then, just go to https://localhost:8080 for running airflow, and https://localhost:9090 for the Carte server

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

Brian Bomfim Amaral - [Linkedin](https://www.linkedin.com/in/brian-amaral-29013a200/) - brian.amaralt@gmail.com

Project Link: [https://github.com/brianamaral/pdi-docker](https://github.com/brianamaral/airflow_pdi_composer)

