## w3af REST API

Docker image for w3af's REST API, nginx, supervisord.
[![Circle CI](https://circleci.com/gh/andresriancho/w3af-api-docker.svg?style=svg)](https://circleci.com/gh/andresriancho/w3af-api-docker)

## Benefits

Most users can just use `./w3af_api` from [the main w3af repository](https://github.com/andresriancho/w3af)
but advanced users might need to have an environment that can handle more traffic,
auto-restarts the service if it's down, etc.
 
## Running this image

```bash
sudo docker run -v ~/.w3af:/root/.w3af \
                -v ~/w3af-shared:/root/w3af-shared \
                -p 5000:5000 \
                -p 9001:9001 \
                andresriancho/w3af-api-docker
```

## Services

 * The w3af REST API binds at port `5000`
 * Supervisor daemon binds at port `9001`
 
## TODO

 * [TLS configuration for nginx](https://github.com/andresriancho/w3af-api-docker/issues/1)
