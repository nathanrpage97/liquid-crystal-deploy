# Liquid Crystal Deploy

A Balena deployment repository for the liquid-crystal app.

## Services

- app: An nginx server that hosts the main webpage. It also acts as a proxy to redirect notebook and server traffic to the correct container and host

- jupyter: A jupyter notebook service installed with the liquid-crystal driver. Allow for remote python access to control the display

- server: A REST api server to control the liquid cystal display

## Structure

Each of the containers uses multistage builds and runs on an alipne linux distro. This allows the conatiners to be as small as possible.
